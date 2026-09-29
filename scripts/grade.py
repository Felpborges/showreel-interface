#!/usr/bin/env python3
"""Grade de quadros com carimbo de tempo (substitui ffmpeg drawtext, ausente aqui).
uso: grid.py VIDEO SAIDA.png --ini 0 --fim 14 --fps 4 --cols 8 --w 320
"""
import argparse, cv2, numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("video"); ap.add_argument("saida")
ap.add_argument("--ini", type=float, default=0); ap.add_argument("--fim", type=float, default=None)
ap.add_argument("--fps", type=float, default=4); ap.add_argument("--cols", type=int, default=8)
ap.add_argument("--w", type=int, default=320)
a = ap.parse_args()

cap = cv2.VideoCapture(a.video)
vfps = cap.get(cv2.CAP_PROP_FPS); n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
dur = n / vfps
fim = a.fim if a.fim is not None else dur
ts = np.arange(a.ini, min(fim, dur - 1e-3), 1.0 / a.fps)
tiles = []
for t in ts:
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(round(t * vfps)))
    ok, fr = cap.read()
    if not ok: continue
    h = int(fr.shape[0] * a.w / fr.shape[1])
    fr = cv2.resize(fr, (a.w, h), interpolation=cv2.INTER_AREA)
    f = int(round(t * vfps))
    lab = f"{t:05.2f}s f{f}"
    cv2.rectangle(fr, (0, 0), (len(lab) * 9 + 6, 18), (0, 0, 0), -1)
    cv2.putText(fr, lab, (3, 13), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (0, 255, 255), 1, cv2.LINE_AA)
    tiles.append(fr)
if not tiles: raise SystemExit("sem quadros")
th, tw = tiles[0].shape[:2]
rows = (len(tiles) + a.cols - 1) // a.cols
sheet = np.zeros((rows * th, a.cols * tw, 3), np.uint8)
for i, t in enumerate(tiles):
    r, c = divmod(i, a.cols)
    sheet[r * th:(r + 1) * th, c * tw:(c + 1) * tw] = t
cv2.imwrite(a.saida, sheet)
print(a.saida, len(tiles), "quadros", sheet.shape[1], "x", sheet.shape[0])
