#!/usr/bin/env python3
"""Aceite — o teste de movimento do motion-por-referencia, com metas ESCALADAS pela duração.

O pericia-movimento.py deriva metas absolutas da referência (ex.: "≥5 picos").
Isso é certo quando os dois filmes têm a mesma duração; um reel de 15s contra
um showreel de 55s precisa das metas proporcionais, senão reprova por ser curto
(picos, cortes) ou aprova por ser curto (quase-parada). Aqui:

  amplitude    >= 0,70 × referência          (não depende da duração)
  quase-parada >= max(0,25, ref − 0,10)      (idem)
  picos        >= max(2, 0,70 × ref × dur_nosso/dur_ref)
  cortes duros >= max(1, 0,40 × ref × dur_nosso/dur_ref)
  [--trilha]   >= 70% dos cortes a ≤2 q de batida/onset da trilha

Uso:
    aceite.py NOSSO.mp4 --contra REF.mp4 [--trilha trilha.wav] [--fps 30]
Sai 1 se reprovar.
"""
import argparse, importlib.util, math, sys
from pathlib import Path

PERICIA = Path.home() / ".claude/skills/motion-por-referencia/scripts/pericia-movimento.py"
BATIDA = Path(__file__).with_name("batida.py")


def carrega(path, nome):
    if not path.exists():
        sys.exit(f"erro: não achei {path}\n  o teste de aceite usa o pericia-movimento.py da skill motion-por-referencia:\n"
                 "  git clone https://github.com/Felpborges/motion-por-referencia.git ~/.claude/skills/motion-por-referencia")
    spec = importlib.util.spec_from_file_location(nome, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("nosso"); ap.add_argument("--contra", required=True)
    ap.add_argument("--trilha", default=None); ap.add_argument("--fps", type=float, default=30.0)
    ap.add_argument("--bpm", type=float, default=None); ap.add_argument("--t0", type=float, default=None)
    a = ap.parse_args()

    pm = carrega(PERICIA, "pericia")
    n = pm.medir(a.nosso); r = pm.medir(a.contra)
    pm.imprime(n)
    esc = n["duracao"] / r["duracao"]
    metas = {
        "amplitude": round(r["amplitude"] * 0.70, 1),
        "parada": round(max(0.25, r["fracao_parada"] - 0.10), 2),
        "picos": max(2, math.floor(len(r["picos"]) * 0.70 * esc)),
        "cortes": max(1, math.floor(len(r["cortes_duros"]) * 0.40 * esc)),
    }
    linhas = [
        ("amplitude", f"{n['amplitude']:.1f}x", f"{r['amplitude']:.1f}x", f">= {metas['amplitude']}x",
         n["amplitude"] >= metas["amplitude"]),
        ("quase-parada", f"{n['fracao_parada']*100:.0f}%", f"{r['fracao_parada']*100:.0f}%",
         f">= {metas['parada']*100:.0f}%", n["fracao_parada"] >= metas["parada"]),
        ("picos", str(len(n["picos"])), str(len(r["picos"])), f">= {metas['picos']}",
         len(n["picos"]) >= metas["picos"]),
        ("cortes duros", str(len(n["cortes_duros"])), str(len(r["cortes_duros"])), f">= {metas['cortes']}",
         len(n["cortes_duros"]) >= metas["cortes"]),
    ]
    if a.trilha:
        bt = carrega(BATIDA, "batida")
        import numpy as np

        def alinhamento(audio, cortes, fps, bpm=None, t0=None):
            """Fração de cortes a ≤2 q de uma batida (fase pelo bumbo) ou de um onset forte."""
            y = bt.carrega(audio)
            t, env, low = bt.envelope(y)
            fe = bt.SR / bt.HOP
            b = 60 / (bpm or bt.andamento(env, fe))
            f0 = t0 if t0 is not None else bt.fase(low, fe, b)
            grade = np.concatenate([np.arange(f0, len(y) / bt.SR, b),
                                    bt.find_peaks(env, height=1.5, distance=int(0.10 * fe))[0] / fe])
            ok = sum(1 for c in cortes if np.min(np.abs(grade - c)) <= 2 / fps + 1e-6)
            return ok / len(cortes) if cortes else 0.0

        frac = alinhamento(a.trilha, n["cortes_duros"], a.fps, a.bpm, a.t0)
        # a referência medida com o MESMO método, no áudio dela (se tiver)
        try:
            ref_frac = alinhamento(a.contra, r["cortes_duros"], r["fps"])
            ref_txt = f"{ref_frac*100:.0f}%"
        except Exception:
            ref_txt = "—"
        linhas.append(("cortes na batida", f"{frac*100:.0f}%", ref_txt, ">= 70%", frac >= 0.70))

    print("\n" + "=" * 70 + "\n  TESTE DE ACEITE (metas escaladas: nosso %.1fs / ref %.1fs = %.2f)\n" % (
        n["duracao"], r["duracao"], esc) + "=" * 70)
    print("  %-17s %-9s %-11s %-10s" % ("", "nosso", "referência", "meta"))
    falhas = []
    for nome, x, y_, m, ok in linhas:
        print("  %-17s %-9s %-11s %-10s %s" % (nome, x, y_, m, "PASSA" if ok else "FALHA"))
        if not ok:
            falhas.append(nome)
    if falhas:
        print("\n  REPROVADO em: " + ", ".join(falhas))
        print("  Conserto típico: eleja UM beat para socar (corte duro, entrada mais curta,")
        print("  objeto maior) e aprofunde as paradas dos vizinhos. Não acelere tudo.")
        sys.exit(1)
    print("\n  APROVADO — a assinatura de movimento bate com a referência.")


if __name__ == "__main__":
    main()
