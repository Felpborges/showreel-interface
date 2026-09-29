#!/bin/bash
# Fotografa UM frame no harness em vários instantes e monta uma folha de contato.
# uso: _dev/shoot.sh 01-busca 0F0F0F 0.2 1.3 1.8 1.95
# (servidor: python3 -m http.server 8765 --bind 127.0.0.1 na raiz do projeto)
cd "$(dirname "$0")/.." || exit 1
FRAME=$1; BG=$2; shift 2
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
mkdir -p _check
curl -s -o /dev/null http://127.0.0.1:8765/ || (python3 -m http.server 8765 --bind 127.0.0.1 >/dev/null 2>&1 &) ; sleep 0.6
OUTS=()
for T in "$@"; do
  O="_check/${FRAME}-t${T}.png"
  "$CH" --headless=new --disable-gpu --hide-scrollbars --window-size=1920,1080 --virtual-time-budget=5000 \
    --screenshot="$O" "http://127.0.0.1:8765/_dev/harness.html?frame=${FRAME}&t=${T}&bg=${BG}" >/dev/null 2>&1
  OUTS+=("$O")
done
python3 - "$FRAME" "${OUTS[@]}" <<'EOF'
import sys, cv2, numpy as np
frame, outs = sys.argv[1], sys.argv[2:]
ims = []
for o in outs:
    im = cv2.imread(o)
    if im is None: continue
    im = cv2.resize(im, (960, 540), interpolation=cv2.INTER_AREA)
    cv2.rectangle(im, (0, 0), (260, 30), (0, 0, 0), -1)
    cv2.putText(im, o.split("-t")[-1][:-4] + "s", (8, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    ims.append(im)
cols = 2
while len(ims) % cols: ims.append(np.zeros_like(ims[0]))
rows = [np.hstack(ims[i:i + cols]) for i in range(0, len(ims), cols)]
cv2.imwrite(f"_check/{frame}-folha.jpg", np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 85])
print(f"_check/{frame}-folha.jpg", len(outs), "instantes")
EOF
