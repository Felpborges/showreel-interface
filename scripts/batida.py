#!/usr/bin/env python3
"""Batida — mede a trilha e devolve a GRADE em que o filme vai ser montado.

Existe porque, neste estilo, a música vem antes da animação: os socos pousam
na batida (≤2 quadros) e o drop recebe a maior mudança de enquadramento. Chute
"no olho" erra por 3–6 quadros, e isso é exatamente a diferença entre um corte
que bate e um que tropeça.

Só numpy/scipy + ffmpeg (sem librosa).

Uso:
    batida.py TRILHA                         # BPM, fase, compassos, onsets, drop
    batida.py TRILHA --fps 30 --json g.json  # grava a grade (s e quadros)
    batida.py TRILHA --bpm 128               # força o andamento (só acha a fase)
    batida.py TRILHA --video RENDER.mp4      # confere os cortes do render contra a trilha
"""
import argparse, json, re, subprocess, sys
import numpy as np
from scipy.signal import find_peaks, stft

SR = 22050
HOP = 256


def carrega(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR),
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).copy()


def envelope(y):
    """Fluxo espectral (log) — a curva de 'ataques' da trilha, e a mesma só nos graves."""
    f, t, Z = stft(y, fs=SR, nperseg=2048, noverlap=2048 - HOP, boundary=None, padded=False)
    S = np.log1p(200 * np.abs(Z))
    d = np.maximum(0, np.diff(S, axis=1))
    flux = np.concatenate([[0], d.sum(axis=0)])
    low = np.concatenate([[0], d[f < 160].sum(axis=0)])
    tt = np.concatenate([[t[0]], t[1:]]) if len(t) == len(flux) else np.arange(len(flux)) * HOP / SR
    norm = lambda x: (x - np.median(x)) / (x.std() + 1e-9)
    return tt, norm(flux), norm(low)


def andamento(env, fps_env, lo=70, hi=190):
    """Autocorrelação + pente: pega o período que melhor soma o envelope em múltiplos."""
    e = np.maximum(env, 0)
    ac = np.correlate(e, e, mode="full")[len(e) - 1:]
    lags = np.arange(len(ac))
    cand = []
    for bpm in np.arange(lo, hi + 0.01, 0.25):
        L = fps_env * 60 / bpm
        i = int(round(L))
        if i + 1 >= len(ac):
            continue
        # interpolação + harmônicos (1x, 2x, 4x o período) — resolve erro de oitava
        s = sum(np.interp(k * L, lags, ac) / k for k in (1, 2, 4))
        cand.append((s, bpm))
    cand.sort(reverse=True)
    best = cand[0][1]
    # preferência suave pela faixa 100–160 (onde mora música de reel)
    for s, bpm in cand[:6]:
        if 100 <= bpm <= 160 and s >= 0.92 * cand[0][0]:
            best = bpm
            break
    return best


def fase(env, fps_env, periodo_s):
    """Deslocamento da primeira batida que maximiza a soma do envelope na grade."""
    P = periodo_s * fps_env
    melhor, off_best = -1e9, 0.0
    for off in np.arange(0, P, 0.25):
        idx = np.arange(off, len(env) - 1, P)
        s = np.interp(idx, np.arange(len(env)), env).sum()
        if s > melhor:
            melhor, off_best = s, off
    return off_best / fps_env


def cortes_video(video, limiar=0.18):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", video, "-filter:v",
                          "select='gt(scene,%s)',metadata=print:file=-" % limiar, "-f", "null", "-"],
                         capture_output=True, text=True).stdout
    ts = [float(m) for m in re.findall(r"pts_time:([\d.]+)", out)]
    ag = []
    for t in ts:
        if not ag or t - ag[-1] > 0.25:
            ag.append(t)
    return ag


def main():
    ap = argparse.ArgumentParser(description="Grade de batidas de uma trilha.")
    ap.add_argument("trilha")
    ap.add_argument("--fps", type=float, default=30.0)
    ap.add_argument("--bpm", type=float, default=None, help="força o andamento")
    ap.add_argument("--t0", type=float, default=None, help="força a 1ª batida (s) — use quando a trilha foi alinhada à mão")
    ap.add_argument("--compasso", type=int, default=4, help="tempos por compasso")
    ap.add_argument("--json", default=None)
    ap.add_argument("--video", default=None, help="render para conferir cortes x trilha")
    a = ap.parse_args()

    y = carrega(a.trilha)
    dur = len(y) / SR
    t, env, low = envelope(y)
    fps_env = SR / HOP
    bpm = a.bpm or andamento(env, fps_env)
    b = 60.0 / bpm
    t0 = a.t0 if a.t0 is not None else fase(low, fps_env, b)
    batidas = np.arange(t0, dur, b)

    # tempo 1 do compasso: a fase (entre as N possíveis) com mais grave nas batidas
    scores = []
    for k in range(a.compasso):
        idx = (batidas[k::a.compasso] * fps_env).astype(int)
        idx = idx[idx < len(low)]
        scores.append(low[idx].sum() if len(idx) else -1e9)
    k1 = int(np.argmax(scores))
    tempo1 = batidas[k1::a.compasso]

    # onsets fortes
    pk, _ = find_peaks(env, height=1.5, distance=int(0.10 * fps_env))
    onsets = pk / fps_env

    # volume por batida e o drop (maior subida de RMS sustentada por 1 compasso)
    win = int(b * SR)
    rms = np.array([np.sqrt(np.mean(y[i:i + win] ** 2)) for i in range(0, len(y) - win, win)])
    drop = None
    if len(rms) > a.compasso * 2:
        sus = np.convolve(rms, np.ones(a.compasso) / a.compasso, mode="valid")
        antes = np.concatenate([[sus[0]] * a.compasso, sus[:-a.compasso]])
        salto = sus - antes
        i = int(np.argmax(salto))
        drop = i * b

    q = lambda s: int(round(s * a.fps))
    print(f"\n  {a.trilha}")
    print(f"  duração {dur:.2f}s | andamento {bpm:.2f} BPM | 1 tempo = {b:.4f}s = {b*a.fps:.2f} q @{a.fps:g}fps"
          f" | 1 compasso = {b*a.compasso:.3f}s")
    print(f"  primeira batida {t0:.3f}s | tempo 1 do compasso começa em {tempo1[0]:.3f}s (fase {k1})")
    if drop is not None:
        dq = min(tempo1, key=lambda x: abs(x - drop))
        print(f"  drop (maior subida sustentada de volume) ≈ {drop:.2f}s → tempo 1 mais próximo {dq:.3f}s (q{q(dq)})")
    print(f"  onsets fortes: {len(onsets)}")
    print("\n  compasso  tempo1(s)  quadro   | batidas do compasso (s)")
    for i, t1 in enumerate(tempo1):
        bs = [t1 + j * b for j in range(a.compasso) if t1 + j * b < dur]
        print(f"  {i+1:>7}  {t1:9.3f}  {q(t1):>6}   | " + "  ".join(f"{x:.3f}" for x in bs))

    out = {"trilha": a.trilha, "duracao": dur, "bpm": bpm, "tempo_s": b, "fps": a.fps,
           "compasso": a.compasso, "primeira_batida": t0, "tempo1": [float(x) for x in tempo1],
           "batidas": [float(x) for x in batidas], "onsets": [float(x) for x in onsets],
           "drop": drop, "rms_por_tempo": [float(x) for x in rms]}

    if a.video:
        cs = cortes_video(a.video)
        grade = np.concatenate([onsets, batidas])
        tol = 2.0 / a.fps
        perto = [float(np.min(np.abs(grade - c))) for c in cs] if len(grade) else []
        ok = sum(1 for d in perto if d <= tol + 1e-6)
        print(f"\n  CORTES DO RENDER: {len(cs)} | a ≤2 q de batida/onset: {ok} ({(ok/len(cs)*100 if cs else 0):.0f}%)")
        for c, d in zip(cs, perto):
            print(f"    {c:6.3f}s (q{q(c)})  → {d*1000:5.0f} ms  {'ok' if d <= tol + 1e-6 else 'FORA'}")
        out["cortes_video"] = cs
        out["cortes_alinhados"] = ok

    if a.json:
        with open(a.json, "w") as fh:
            json.dump(out, fh, indent=1)
        print(f"\n  JSON -> {a.json}")


if __name__ == "__main__":
    main()
