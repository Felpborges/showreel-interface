# Ritmo e áudio — a grade vem antes do primeiro tween

## 1 · A trilha

**Gerar (padrão):** Higgsfield `sonilo_music` (modelo de música; `seed_audio` é para efeitos/voz),
1 crédito por trilha de 16 s. Gere **3 variações** com a estrutura escrita em segundos no prompt e
escolha **medindo** (ninguém aqui ouve; a escolha é por número):
```bash
higgsfield generate create sonilo_music --duration 16 --wait --json --prompt "Instrumental electronic pop
track for a 15-second brand showreel, 120 BPM. 0 to 3 seconds: sparse intro with muted plucks, ticking
percussion and a rising riser. At 3 seconds: a hard drop with punchy kick, clap and bright chords. Driving
energy, a one-beat silence break at 11 seconds, a final big hit with a short tail at 14 seconds. No vocals."
```
O modelo **não obedece** BPM nem segundos com precisão (pedido 128 → saiu 122, 130, 132). Por isso:

**Medir:** `python3 scripts/batida.py trilha.m4a --fps 30 --json grade.json` (BPM, fase, compassos,
onsets, drop) e um perfil por meio-tempo (volume, graves = bumbo, agudos) para "ver" a forma: intro,
entrada, cheio, break, fim. Critérios de escolha, em ordem:
1. **Tem arco** (intro mais baixa → entrada → cheio → uma parada → final). Loop chapado reprova: o
   filme precisa de silêncio ↔ rajada no som também.
2. **Bumbo legível** (graves alternando forte/fraco a cada tempo) = grade confiável.
3. **Fim limpo** (cauda curta, sem fade longo).

**Endireitar a grade:** se o BPM medido estiver a menos de ~3% de um BPM "redondo" para o fps
(a 30 fps: 120 BPM = 15 q por tempo; 112,5 = 16 q; 128,57 = 14 q), estique com
`ffmpeg -af "atempo=<alvo/medido>"` e desloque para o primeiro tempo 1 cair num quadro inteiro. Todo
corte passa a cair em quadro inteiro, sem arredondamento.

**Editar a música em compassos:** trilha gerada é matéria-prima. Corte e recoloque compassos inteiros
(no zero do tempo 1, com 5 ms de crossfade) para o arco caber no filme: estender a intro, criar a
parada antes do soco, trocar o fim. É o que editor de reel faz.

**Sintetizar (último recurso):** `scripts/sfx.py` tem o kit de efeitos; trilha sintetizada soa
amadora perto de uma gerada. Use só se a geração falhar.

## 2 · A grade (a 30 fps, 120 BPM)

| Unidade | Segundos | Quadros |
|---|---|---|
| 1 tempo | 0,5 | 15 |
| ½ tempo (colcheia) | 0,25 | 7,5 → use 7/8 alternando |
| 1 compasso | 2,0 | 60 |
| 15 s | 7,5 compassos | 450 |

`t(compasso c, tempo k) = t0 + (c−1)·4b + (k−1)·b`. Escreva a tabela de beats do filme em
**compasso.tempo** (ex.: "3.1 = drop"), não em segundos soltos: é o que mantém tudo na batida
quando a trilha mudar.

## 3 · Onde cada coisa pousa

| Evento visual | Onde na grade | Som |
|---|---|---|
| Palavras do hook | colcheias/semínimas da intro | digitar, tique |
| Zoom-through do pivô | tempo 1 da primeira entrada da bateria | whoosh (pico no quadro do soco) |
| Nascer do chip | 1 tempo antes da rajada | clique + caça-níquel |
| **Maior mudança de enquadramento** | **o drop** | impacto + subdrop |
| Cortes da rajada | onsets/tempos; durações variadas (1, 1, ½, ½, 1, 2 tempos) | nada extra (a música corta) |
| Troca de mundo | tempo 1 de um compasso | swish/whoosh |
| Frase cômica | a parada da música (ou crie uma) | silêncio ou sopro reverso |
| **Soco final** | tempo 1 depois da parada | impacto + clique nativo da marca |
| Lockup | último tempo 1; segura até o fim | cauda da trilha |

## 4 · Desenho de som (`scripts/sfx.py`)
- `cues.json` marca o **pico** de cada som no quadro do evento visual; a função sabe onde fica o
  próprio pico (whoosh a 72% da duração, riser no fim, impacto no começo).
- Ganhos de partida: música −3 dB; whoosh −8; swish −12; clique −10; tique −16; caça-níquel −12;
  impacto −4; subdrop −6; riser −10; ding −9. A música abaixa ~4 dB por 250 ms sob cada impacto.
- Master em −14 LUFS integrado, pico −1 dBTP (`loudnorm`), 48 kHz / 24 bits.
- Som nativo da marca: **não copie** o áudio proprietário (ex.: sons do app); use um equivalente
  genérico (o `ding` do kit é um sino neutro).

## 5 · Conferir no fim
```bash
python3 scripts/batida.py trilha-final.wav --fps 30 --video render.mp4   # % de cortes na grade
python3 scripts/aceite.py render.mp4 --contra referencia.mp4 --trilha trilha-final.wav --fps 30
```
Meta: ≥70% dos cortes a ≤2 q de batida/onset (a referência faz 94%; o reel do YouTube, 100%).
A fase da grade é medida pelo **grave** (bumbo): medida pelo fluxo total, os hats e os SFX puxam a
fase ~65 ms e o teste reprova cortes que estão no bumbo. Trilha alinhada à mão: passe `--t0`.
