# Reel "acesse Felipe Borges Fala IA!" — 15s sobre o YouTube (teste da skill `showreel-interface`)

**Brief:** marca = YouTube (UI nativa, modo escuro e claro) · exemplo = canal do Felipe
(@FelipeBorgesFalaIA, dados reais da API em 29/09/2026) · 15,0 s · 1920×1080 · 30 fps · PT-BR ·
CTA = Inscrever-se.

**As três respostas (§0 da skill):**
- **Chip** = os chips de filtro da aba Vídeos do canal ("Mais recentes", "Em alta", "Mais antigos").
- **Prova** = o conteúdo real do canal: thumbnails, trechos dos vídeos, 162.717 visualizações do nº 1.
- **Busca que abre o filme** = "acesse Felipe Borges Fala IA!" (revisão do Felipe, 29/09; a v1 abria com "não aperte o play", invertida no fim em "Aperte o play.")

**Mecanismo:** a interface do YouTube conta a história. Você digita "acesse Felipe Borges Fala IA!" na busca,
os chips do canal abrem as provas, e o filme fecha em "Aperte o play." e no botão Inscrever-se.

**Trilha:** `assets/audio/trilha-base-120.wav` (Higgsfield Sonilo, electro house, esticada para
120,00 BPM e deslocada para o drop cair em 4,000 s). 1 tempo = 0,5 s = 15 q; compasso = 2 s = 60 q.
Intro filtrada 0–4 s (sem bumbo) · **drop 3.1 = 4,00 s** · bumbo em todo tempo até ~13,6 s · parada e
cauda 13,6–15 s. Grade conferida: 20 bumbos a ≤0,3 q da grade.

Notação: `c.t` = compasso.tempo (1.1 = 0,0 s; 2.1 = 2,0 s; 3.1 = 4,0 s …). Quadros a 30 fps.

| Frame | Janela | Mundo | O que acontece (momento-chave) | Enquadramento | Emenda de saída (condutor) |
|---|---|---|---|---|---|
| **f01-busca** | 1.1–2.1 · 0,00–2,00 · q0–60 | escuro `#0F0F0F` | moldura: logo YouTube (esq.) + avatar do Felipe (dir.). Barra de busca gigante; caret piscando; digita **acesse · Felipe · Borges · Fala · IA!** nas colcheias (0,50 / 0,75 / 1,00 / 1,25 / 1,375); a **barra de progresso** corre sob "Fala IA!" (1,45–1,78) e o scrubber pousa no fim | UI em close (busca ≈ 70% da largura) | **T1 zoom-through em 2,00**: empurrão 1,70→2,00, rajada 4 q; a barra vermelha estica e vira o risco que atravessa o quadro |
| **f02-porque** | 2.1–3.1 · 2,00–4,00 · q60–120 | escuro | "Vou te mostrar por quê." nasce a 0,55 e assenta (2,00–2,40); fileira de chips entra (2,50); a seleção pula Mais antigos → Em alta → **Mais recentes** e trava no clique em **3,00**; o título explode em eco (3,20) e o **baralho 3D** das thumbs mais recentes entra pela direita (3,10–3,70) | tipografia central → leque 3D | **T3**: o card da frente (thumb do "12 DICAS…") endireita e cresce até a tela cheia, **pousando em 4,00 (o drop)** |
| **f03-player** | 3.1–4.1 · 4,00–6,00 · q120–180 | footage | o card virou o **player**: vídeo em tela cheia + barra de progresso vermelha com scrubber, tempo e título. Cortes duros na grade: 4,00 (aponta) · 4,50 (cartões) · 5,00 (estúdio) · 5,25 (aponta "1 profissional") · 5,50 (ok) — a cada corte a barra salta para outro vídeo | tela cheia | **T4 em 6,00**: o player encolhe para card (raio aparece) e revela o mundo claro |
| **f04-em-alta** | 4.1–6.1 · 6,00–10,00 · q180–300 | claro `#FFFFFF` | o card pousa na grade da aba Vídeos (3 colunas, títulos e "▷ 7,7 mil · há 21 h" reais); câmera recua (6,00–6,60); clique em **Em alta** (7,00); a grade **reordena** por popularidade (7,00–7,50); **8,00**: o nº 1 (162.717) soca para frente e o contador rola até **162.717 visualizações** (8,15–9,05); segura (9,05–9,70) | grade da aba Vídeos → card herói | **T6 chicote** para a esquerda em 9,80–10,00, corte duro em 10,00 |
| **f05-so-mais-um** | 6.1–7.1 · 10,00–12,00 · q300–360 | escuro | 1 q vazio; "só mais um vídeo…" entra da direita em cascata com blur (10,03–10,35); segura encolhendo 1,0→0,82 (10,35–11,80) com a música **abafada** (passa-baixa + −8 dB); encolhe rápido 11,80–11,97 | tipografia | **T8 soco em 12,00** |
| **f06-aperte** | 7.1–fim · 12,00–15,00 · q360–450 | escuro | **"Aperte o play."** soca a ×1,45 com o risco vermelho e assenta (12,00–12,45); sobe e dá lugar ao **cabeçalho do canal** (12,60–13,10): avatar, "Felipe Borges - Fala IA!", "@FelipeBorgesFalaIA · 16,3 mil inscritos · 53 vídeos", botão **Inscrever-se**; clique em 13,30 → **Inscrito** + sino tocando (13,35–13,90); moldura volta (logo + avatar nos cantos); segura parado até 15,00 | cabeçalho do canal | fim (cauda da música; fade 14,60–15,00) |

**Quase-parada planejada** (para o aceite): 0,00–1,40 (digitação é pouco movimento) · 2,40–2,90 ·
6,60–7,00 · 9,05–9,70 · 10,35–11,80 · 13,90–15,00 ≈ 5,2 s de 15 (35%). **Socos:** 2,00 · 3,20–4,00 ·
4,00–5,50 (cortes) · 6,00 · 7,00–7,50 · 8,00 · 9,80 · 12,00.

**Risco nº 1 e plano B:** o mergulho 3D (T3) em HTML — o card da frente é 2D separado do baralho;
se a emenda no drop "pular", plano B = o baralho some no último quadro e o card 2D já está na
posição projetada (corte invisível atrás do blur).

## Sons (pico no quadro do evento)
digitar 0,50/0,75/1,00/1,25/1,375 · riser 1,40→2,00 · whoosh 2,00 · impacto leve 2,00 · caça-níquel
2,55→3,00 (clique na trava) · whoosh 3,15 · riser 3,00→4,00 · impacto + subdrop 4,00 · swish 6,00 ·
clique 7,00 · swish 7,10 · impacto 8,00 · tiques 8,15–9,05 · whoosh 9,90 · abafar 10,00–11,95 ·
reverso →12,00 · impacto 12,00 · clique 13,30 · ding 13,40.
