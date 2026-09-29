#!/usr/bin/env python3
"""SFX — o kit de som do showreel, sintetizado (determinístico, sem licença).

Neste estilo o som é metade do soco: todo chicote tem whoosh, todo chip tem
clique, o caça-níquel tem tique, o drop e o soco final têm impacto. Sintetizar
em vez de baixar dá duas coisas: o PICO de cada som cai no quadro exato do
evento visual (a função sabe onde fica o próprio pico), e nada depende de
biblioteca de terceiros.

Uso:
    sfx.py kit PASTA                      # gera um .wav de cada som, para ouvir
    sfx.py mix --cues cues.json --dur 15 --saida trilha.wav [--musica bed.wav]
                                           [--musica-ganho -3] [--lufs -14]

cues.json = lista de {"som": "whoosh", "t": 2.95, "ganho": -6, "args": {...}}
  t = instante do PICO do som (o quadro do evento visual), em segundos.
  sons: whoosh, swish, impacto, subdrop, clique, tique, cacaniquel, pop, riser,
        ding, reverso, digitar
"""
import argparse, json, subprocess, sys
import numpy as np
from scipy.signal import butter, sosfilt, stft, istft, fftconvolve

SR = 48000
RNG_SEED = 7


def rng(seed=0):
    return np.random.default_rng(RNG_SEED + seed)


def db(x):
    return 10 ** (x / 20)


def bp(x, lo, hi, order=4):
    sos = butter(order, [lo / (SR / 2), min(hi / (SR / 2), 0.999)], btype="band", output="sos")
    return sosfilt(sos, x)


def lp(x, f, order=4):
    return sosfilt(butter(order, min(f / (SR / 2), 0.999), btype="low", output="sos"), x)


def hp(x, f, order=4):
    return sosfilt(butter(order, f / (SR / 2), btype="high", output="sos"), x)


def sweep_noise(dur, f0, f1, q=0.35, seed=0):
    """Ruído filtrado por um passa-banda que varre f0→f1 (domínio STFT)."""
    n = int(dur * SR)
    x = rng(seed).standard_normal(n)
    nper = 1024
    f, t, Z = stft(x, fs=SR, nperseg=nper, noverlap=nper * 3 // 4)
    fc = np.geomspace(max(f0, 20), max(f1, 20), Z.shape[1])
    bw = fc * q
    G = np.exp(-0.5 * ((f[:, None] - fc[None, :]) / bw[None, :]) ** 2)
    _, y = istft(Z * G, fs=SR, nperseg=nper, noverlap=nper * 3 // 4)
    y = y[:n]
    return y / (np.abs(y).max() + 1e-9)


def reverb(x, secs=0.9, lp_f=5000, mix=0.25, seed=3):
    n = int(secs * SR)
    ir = rng(seed).standard_normal(n) * np.exp(-np.linspace(0, 7, n))
    ir = lp(ir, lp_f)
    ir /= np.abs(ir).sum() ** 0.5 * 8
    wet = fftconvolve(x, ir)
    out = np.zeros(len(x) + n)
    out[: len(x)] += x * (1 - mix)
    out[: len(wet)] += wet[: len(out)] * mix * 6
    return out


def estereo(x, pan0=0.0, pan1=0.0):
    """pan -1 (esq) .. +1 (dir), varrendo ao longo do som."""
    p = np.linspace(pan0, pan1, len(x))
    a = (p + 1) * np.pi / 4
    return np.stack([x * np.cos(a), x * np.sin(a)], axis=1)


# ---------------------------------------------------------------- sons
# Cada som devolve (sinal estéreo, índice do pico em amostras).

def whoosh(dur=0.42, f0=250, f1=5200, pico=0.72, pan=(-0.6, 0.6), seed=0):
    """Chicote/zoom-through. O pico (a passagem) fica em `pico` da duração."""
    n = int(dur * SR)
    y = sweep_noise(dur, f0, f1, q=0.45, seed=seed)
    tt = np.linspace(0, 1, n)
    env = np.where(tt < pico, (tt / pico) ** 2.6, np.exp(-(tt - pico) / (1 - pico) * 4.5))
    y = y * env
    ar = sweep_noise(dur, f1 * 0.8, f1 * 1.4, q=0.2, seed=seed + 1) * env ** 2 * 0.25
    y = hp(y + ar, 80)
    return estereo(y / (np.abs(y).max() + 1e-9), *pan), int(pico * n)


def swish(dur=0.16, seed=1):
    """Whoosh curto: chip entrando, card passando."""
    s, p = whoosh(dur=dur, f0=900, f1=7000, pico=0.55, pan=(-0.2, 0.2), seed=seed)
    return s * 0.8, p


def impacto(dur=1.6, f_ini=120, f_fim=42, seed=2):
    """Soco/drop: sub com queda de altura + transiente de ruído + cauda."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = f_fim + (f_ini - f_fim) * np.exp(-t / 0.045)
    ph = 2 * np.pi * np.cumsum(f) / SR
    sub = np.sin(ph) * np.exp(-t / 0.42)
    click = lp(rng(seed).standard_normal(n), 3500) * np.exp(-t / 0.012) * 0.9
    body = bp(rng(seed + 1).standard_normal(n), 120, 900) * np.exp(-t / 0.09) * 0.5
    y = sub * 1.0 + click + body
    y = np.tanh(y * 1.6)
    y = reverb(y, secs=1.1, lp_f=3000, mix=0.18)[:n]
    y /= np.abs(y).max() + 1e-9
    return estereo(y), int(0.004 * SR)


def subdrop(dur=1.2):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = 34 + 46 * np.exp(-t / 0.35)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.minimum(1, t / 0.01) * np.exp(-t / 0.55)
    return estereo(y / (np.abs(y).max() + 1e-9)), int(0.01 * SR)


def clique(freq=3100, dur=0.05, seed=4):
    """Clique de UI (apertar chip/botão): transiente + blip curto."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    tr = hp(rng(seed).standard_normal(n), 2500) * np.exp(-t / 0.0015)
    bl = np.sin(2 * np.pi * freq * t) * np.exp(-t / 0.008) * 0.6
    low = np.sin(2 * np.pi * 180 * t) * np.exp(-t / 0.01) * 0.5
    y = tr + bl + low
    return estereo(y / (np.abs(y).max() + 1e-9)), int(0.001 * SR)


def tique(freq=2400):
    s, p = clique(freq=freq, dur=0.03, seed=5)
    return s * 0.55, p


def cacaniquel(dur=0.6, n_tiques=9, desacel=2.2):
    """Tiques desacelerando — o texto rolando no chip. Pico = o último (a trava)."""
    n = int(dur * SR)
    y = np.zeros((n + int(0.05 * SR), 2))
    u = np.linspace(0, 1, n_tiques) ** desacel
    for i, x in enumerate(u):
        s, _ = tique(2200 + 90 * (i % 3))
        k = int(x * n)
        y[k:k + len(s)] += s * (0.55 + 0.45 * i / n_tiques)
    last, _ = clique(freq=3400)
    y[n - 1:n - 1 + len(last)] += last[: len(y) - (n - 1)] * 0.9
    return y / (np.abs(y).max() + 1e-9), n - 1


def pop(f0=880, f1=300, dur=0.09):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t / 0.018)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.03)
    return estereo(y / (np.abs(y).max() + 1e-9)), int(0.002 * SR)


def riser(dur=1.6, seed=6):
    """Subida antes do drop. Termina seca no drop: o pico é o fim."""
    n = int(dur * SR)
    t = np.linspace(0, 1, n)
    y = sweep_noise(dur, 400, 9000, q=0.3, seed=seed) * t ** 2.2
    f = 110 * 2 ** (t * 2)
    saw = ((np.cumsum(f) / SR) % 1.0) * 2 - 1
    y = y + lp(saw, 3000) * t ** 3 * 0.35
    y = hp(y, 150)
    return estereo(y / (np.abs(y).max() + 1e-9), -0.3, 0.3), n - 1


def ding(f0=1568.0, dur=1.3):
    """Sino de notificação (duas notas, parciais de sino). Genérico, não é o som de nenhuma marca."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    y = np.zeros(n)
    for (start, fr, g) in ((0.0, f0 * 0.75, 0.7), (0.085, f0, 1.0)):
        k = int(start * SR)
        tt = t[: n - k]
        s = sum(a * np.sin(2 * np.pi * fr * m * tt) * np.exp(-tt / (0.55 / m ** 0.7))
                for m, a in ((1, 1.0), (2.76, 0.28), (5.4, 0.12), (8.93, 0.05)))
        y[k:] += s * g * np.minimum(1, tt / 0.002)
    y = reverb(y, secs=0.8, lp_f=7000, mix=0.2)[:n]
    return estereo(y / (np.abs(y).max() + 1e-9)), int(0.085 * SR)


def reverso(dur=0.9, seed=8):
    """Sopro reverso (crescendo que termina no evento)."""
    n = int(dur * SR)
    y = hp(rng(seed).standard_normal(n), 2000) * np.exp(-np.linspace(0, 6, n))
    y = reverb(y, secs=0.6, lp_f=9000, mix=0.5)[:n][::-1]
    return estereo(y / (np.abs(y).max() + 1e-9)), n - 1


def digitar(n_teclas=8, intervalo=0.075, seed=9):
    """Teclas digitando (hook na barra de busca). Pico = primeira tecla."""
    L = int((n_teclas * intervalo + 0.08) * SR)
    y = np.zeros((L, 2))
    r = rng(seed)
    for i in range(n_teclas):
        s, _ = clique(freq=1800 + r.integers(0, 900), dur=0.035, seed=seed + i)
        k = int(i * intervalo * SR + r.integers(0, int(0.012 * SR)))
        y[k:k + len(s)] += s * (0.35 + 0.15 * r.random())
    return y / (np.abs(y).max() + 1e-9), 0


SONS = {"whoosh": whoosh, "swish": swish, "impacto": impacto, "subdrop": subdrop,
        "clique": clique, "tique": tique, "cacaniquel": cacaniquel, "pop": pop,
        "riser": riser, "ding": ding, "reverso": reverso, "digitar": digitar}


# ---------------------------------------------------------------- mix

def le_audio(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "2", "-ar", str(SR),
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)


def grava(path, x, lufs=None):
    x = np.clip(x, -1, 1).astype(np.float32)
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-"]
    if lufs is not None:
        cmd += ["-af", f"loudnorm=I={lufs}:TP=-1.0:LRA=11"]
    cmd += ["-ar", str(SR), "-c:a", "pcm_s24le", path]
    subprocess.run(cmd, input=x.tobytes(), check=True)


def mix(a):
    cues = json.load(open(a.cues))
    N = int(a.dur * SR)
    bus = np.zeros((N + SR * 3, 2))
    duck = np.ones(N + SR * 3)
    for c in cues:
        if c["som"] == "abafar":
            continue
        f = SONS[c["som"]]
        s, pico = f(**c.get("args", {}))
        k = int(round(c["t"] * SR)) - pico
        g = db(c.get("ganho", 0))
        i0, j0 = max(0, k), max(0, -k)
        m = min(len(s) - j0, len(bus) - i0)
        if m > 0:
            bus[i0:i0 + m] += s[j0:j0 + m] * g
        if c["som"] in ("impacto", "subdrop") and a.musica:
            # abaixa a música ~4 dB por 250 ms sob o soco (sidechain simples)
            kk = max(0, int(round(c["t"] * SR)))
            L = int(0.35 * SR)
            env = 1 - db(-4) * 0 - (1 - db(-4)) * np.exp(-np.linspace(0, 5, L))
            duck[kk:kk + L] = np.minimum(duck[kk:kk + L], env[: len(duck[kk:kk + L])])
    out = bus[:N]
    if a.musica:
        m = le_audio(a.musica)[:N]
        if len(m) < N:
            m = np.vstack([m, np.zeros((N - len(m), 2))])
        # "abafar": passa-baixa + ganho num trecho da música (a pausa cômica), com rampas de 40 ms
        for c in json.load(open(a.cues)):
            if c.get("som") != "abafar":
                continue
            i0, i1 = int(c["t"] * SR), min(N, int(c["ate"] * SR))
            sos = butter(4, c.get("freq", 500) / (SR / 2), btype="low", output="sos")
            from scipy.signal import sosfiltfilt
            seg = sosfiltfilt(sos, m[i0:i1], axis=0) * db(c.get("ganho", -6))
            r = min(int(0.04 * SR), (i1 - i0) // 2)
            w = np.ones(i1 - i0)
            w[:r] = np.linspace(0, 1, r)
            w[-r:] = np.linspace(1, 0, r)
            m[i0:i1] = m[i0:i1] * (1 - w[:, None]) + seg * w[:, None]
        fade = int(a.fade * SR)
        if fade > 0:
            m[-fade:] *= np.linspace(1, 0, fade)[:, None] ** 1.5
        m *= db(a.musica_ganho) * duck[:N, None]
        out = out + m
    # limitador suave
    pk = np.abs(out).max()
    if pk > 0.95:
        out = np.tanh(out / pk * 1.2) / np.tanh(1.2) * 0.95
    grava(a.saida, out, a.lufs)
    print(f"mix -> {a.saida} ({a.dur:.2f}s, {len(cues)} cues{', com música' if a.musica else ''})")


def kit(a):
    import os
    os.makedirs(a.pasta, exist_ok=True)
    for nome, f in SONS.items():
        s, p = f()
        grava(os.path.join(a.pasta, nome + ".wav"), s * 0.8)
        print(f"{nome:12s} {len(s)/SR:5.2f}s  pico em {p/SR*1000:6.1f} ms")


def main():
    ap = argparse.ArgumentParser(description="Kit de som do showreel.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    k = sub.add_parser("kit"); k.add_argument("pasta")
    m = sub.add_parser("mix")
    m.add_argument("--cues", required=True); m.add_argument("--dur", type=float, required=True)
    m.add_argument("--saida", required=True); m.add_argument("--musica", default=None)
    m.add_argument("--musica-ganho", dest="musica_ganho", type=float, default=-3.0)
    m.add_argument("--fade", type=float, default=0.0, help="fade-out da música no fim (s)")
    m.add_argument("--lufs", type=float, default=-14.0)
    a = ap.parse_args()
    {"kit": kit, "mix": mix}[a.cmd](a)


if __name__ == "__main__":
    main()
