# Perícia do SHOWREEL 2025 (Misha Ruchko) — a fonte de todas as regras desta skill

> Vimeo 1124592722 (baixar pelo player: `yt-dlp "https://player.vimeo.com/video/1124592722"`; a URL
> normal pede login). Medido em 29/09/2026 com `pericia-movimento.py` (motion-por-referencia),
> `scripts/batida.py` e `scripts/grade.py`. Imagens em `pericia/` (só na cópia local; quadros de obra
> de terceiros não vão para o repositório público): grades de 4 quadros/s com carimbo de tempo, tiras
> quadro a quadro de cada transição (T1–T8) e quatro quadros em resolução cheia. Para regenerar:
> `python3 scripts/grade.py REF.mp4 pericia/grade.png --ini 0 --fim 14 --fps 4`.
> **É referência de método, não de conteúdo**: nada de copy, cor, fonte ou exemplo dela vai para o
> projeto.

## Ritmo × música (o achado que mais pesa)
- Trilha a **149,75 BPM** (1 tempo = 0,4007 s = 9,6 q a 24 fps; compasso = 1,603 s).
- O **drop** cai no tempo 1 do **compasso 6 = 8,057 s (q193)** — exatamente o quadro em que o card
  da frente do baralho 3D vira a tela cheia. A maior mudança de enquadramento mora no drop.
- **32 de 34 cortes (94%)** caem a ≤2 quadros de uma batida ou de um onset forte, com a fase da
  grade medida pelo bumbo (`batida.py`); 28 de 34 a ≤2 q de uma colcheia. Os fora são cortes do
  trecho de footage que seguem o som do próprio footage.
- O hook (0–8 s) não tem bumbo: é tipografia sobre efeitos e riser. A grade manda do drop em diante.

## Perícia · Camada 1 — Estrutura

**Referência:** "SHOWREEL 2025", Misha Ruchko (2D motion designer & video editor) · Vimeo 1124592722
**Técnico:** 55,23s · 1920×1080 (origem 4K) · 23,976 fps · 1.324 quadros · com áudio (música eletrônica ~152 BPM, batida = 0,395s ≈ 9,5 quadros)

## O mecanismo, numa frase

> **A interface conta a história.** Cada capítulo é uma *etiqueta que se aperta* (um chip de UI),
> e o trabalho de verdade invade a tela como prova, preso à batida. Toda emenda é um elemento da
> cena atual *virando* a transição.

É um argumento, não uma colagem: abre com uma provocação ao contrário ("você NÃO quer esse cara no
time"), promete o porquê, prova capítulo a capítulo e fecha a mesma frase invertida ("você deveria
contratá-lo"). O loop aberto no quadro 0 só fecha no segundo 47.

## Beats

| # | Janela | Mundo | O que diz | Enquadramento | Emenda de SAÍDA (o que o olho segue) |
|---|---|---|---|---|---|
| 01 | 0,0–3,0 | escuro | Hook palavra a palavra: "You / Don't Want This / **Motion Designer** / & **Video Editor** / On Your Team" — palavras-chave dentro de **caixas de seleção** (ciano / vermelho) | tipografia central, cabeçalho SHOWREEL · 2025 nos cantos | **zoom-through**: câmera atravessa o texto; as bordas das caixas viram riscos ciano/vermelho (3 q) |
| 02 | 3,0–6,5 | escuro | "Here's Why" (caixa ciano) + "LET'S CHECK HIS SKILL SET" + botão "+" que vira **chip** e sorteia "LONG-FORM VIDEOS" | tipografia central | título explode com eco; **leque 3D** de cards entra pela direita |
| 03 | 6,5–13,7 | escuro→footage | Cap. 1 · vídeo longo: baralho 3D gira, o card da frente **vira a tela cheia no drop (8,0s)**; montagem tela cheia com cortes a cada 8–13 q | 3D → tela cheia | corte duro para footage que **encolhe e vira card** sobre o mundo claro |
| 04 | 13,7–23,0 | claro | Cap. 2 · "SHORT-FORM VIDEOS": cards 9:16 tipo celular deslizam em colunas; carrossel de 3 | chip central + cards verticais | cards saem; chip "rola" o texto (caça-níquel) para o próximo |
| 05 | 23,0–29,0 | claro→footage→claro | Cap. 3 · "COLOR GRADING": footage tela cheia entra empurrando, **encolhe para card enquanto a cortina revela o antes/depois**; câmera recua para **parede de cards** | tela cheia → card → parede | **chicote horizontal** da parede inteira (1–2 q), corte para o escuro |
| 06 | 29,0–32,3 | escuro | Cap. 4 · "SFX" (chip vermelho) sobre **timeline de áudio em 3D** (clips verdes com forma de onda); "MOTION DESIGN" (chip ciano) sobe | plano 3D inclinado | o chip **estica até virar um risco** ciano de tela inteira; corte por trás do risco |
| 07 | 32,3–38,5 | cor cheia | Cap. 5 · motion design: rajada de 12 amostras, cortes a cada 6–9 q **cravados na batida** | tela cheia + trios de cards | chip "EFFECTS" entra borrado |
| 08 | 38,5–44,7 | escuro/claro | Cap. 6 · "EFFECTS": footage com efeitos; volta ao claro em grade 2×2 com **anotações rastreadas** (círculos) | tela cheia → grade 2×2 | grade sai em chicote; **1 quadro de vazio** |
| 09 | 44,7–48,2 | escuro | Payoff: "Wow, He Seems Like a Great Guy!" (pausa cômica ~1s, encolhendo) → **SOCO**: "You Should Hire Him" (caixa vermelha) | tipografia | a caixa encolhe e desliza; o cartão de perfil entra |
| 10 | 48,2–55,2 | escuro | Fecho: card de perfil + "Thanks for Watching!" + contatos em cascata (EMAIL / LINKEDIN / TELEGRAM → ); cabeçalho volta | layout de cartão | segura parado ~5s; música some 51,5→53 |

## Como fecha

Card de perfil (foto em moldura escura) + título + 3 linhas de contato em cascata, cabeçalho
SHOWREEL · 2025 de volta nos cantos → **segura parado** → música desce → cauda quieta. É o padrão
lockup → segura → cauda quieta, com a diferença de que o lockup é uma *pessoa* (o filme vende alguém).

## Por que a estrutura funciona

1. **Loop aberto no hook e fechado no fim** (head fake): "You Don't Want This…" → "Here's Why" →
   provas → "You Should Hire Him". A frase final é a de abertura invertida.
2. **Capítulos com título idêntico** (o chip): o espectador aprende a gramática em 5s e passa a
   *esperar* o próximo chip. Seis chips em 55s = um capítulo a cada ~7s.
3. **Cada capítulo prova no formato do próprio conteúdo**: vídeo curto em card 9:16, vídeo longo em
   tela cheia, SFX como timeline de áudio, color grading como antes/depois. O enquadramento é o argumento.
4. **Dois mundos alternados** (escuro ↔ claro) marcam a troca de capítulo no nível macro, antes de
   qualquer palavra.
5. **Humor no payoff** ("Wow, He Seems Like a Great Guy!") segura ~1s de quase-silêncio visual antes
   do soco final. O riso é o vale que faz o soco bater.

## Perícia · Camada 2 — Design

Amostrado de quadros reais (k-means em `quadros/`), não adivinhado.

## Paleta (com papéis)

| Papel | Cor | Onde pode | Onde NUNCA |
|---|---|---|---|
| Mundo escuro | `#222222` (±`#252525`) | fundo dos capítulos de tipografia, SFX, fecho | atrás de footage (footage é sempre tela cheia ou card) |
| Mundo claro | `#ECEBEC` (+ faixa `#E6E6E6`/`#FFFFFF`) | fundo das galerias de cards | nunca com chip de brilho neon (no claro o chip é branco chapado) |
| Tinta alta | `#FBFCFC` | texto em caixa, alças, chip branco | — |
| Tinta média | `#9A9A9A`→`#CFCFCF` (gradiente vertical) | texto fora da caixa, cabeçalho, contatos | nunca em palavra-chave |
| Acento A · seleção | ciano `#0CF5F5` | caixa de seleção, chip "motion/effects" | nunca em footage, nunca no mundo claro |
| Acento B · selecionado/CTA | coral `#F06A6D` (`#F67A7B`) | caixa da palavra-alvo, chip "ativo", soco final | nunca junto com ciano na MESMA peça, exceto no hook |
| Sinal de capítulo | verde `#51FC69` | só na timeline de áudio | fora do capítulo SFX |

**Dois acentos, com semântica fixa.** Ciano = "estou selecionando" (a ferramenta). Coral = "escolhido"
(o que importa, o CTA). A cor de verdade do filme vem do trabalho (footage); a UI é quase monocromática.

## Herói + âncora
Não há objeto herói; o herói é o **trabalho**. A âncora que lê em todo capítulo é o **chip**: pílula
com texto em caixa alta + ícone ×. É o elemento que o espectador reconhece de longe.

## Tipografia
- **Uma família** geométrica (tipo Gilroy), dois papéis:
  - **Título:** Title Case, bold, 64–100px a 1080p, tracking ~0, **gradiente vertical** (branco no
    topo → cinza embaixo); dentro de caixa ganha **brilho** branco suave.
  - **Rótulo:** CAIXA ALTA, medium/semibold, 26–34px, tracking +2–4%, cor única.
- Entrada de texto: **palavra por palavra** (1 palavra a cada 4–6 q), ou **caça-níquel** vertical
  dentro do chip; saída por zoom-through, eco ou encolhimento.
- Sem itálico, sem serif, sem texto 3D extrudado, sem contorno em texto.

## Componentes (medidos a 1080p)
- **Caixa de seleção:** traço 4px + brilho da mesma cor; preenchimento = acento a ~15%; **4 alças**
  brancas quadradas ~24px (raio 4px, sombra leve); caixa **inclinada ±2–3°** (ciano gira para um
  lado, coral para o outro).
- **Chip:** pílula (raio total), 520×130 no plano de detalhe; estados: (1) botão circular "+" branco
  → (2) estica na horizontal → (3) texto rola vertical (caça-níquel) → (4) assenta → (5)
  *selecionado*: fundo escuro translúcido, borda + texto no acento, brilho externo. O "+" **gira 45° e
  vira ×**. No mundo claro: branco chapado, texto `#2A2D33`, sombra difusa, sem brilho.
- **Card:** raio ≈ 9% da largura do card (9:16 de 525px → ~48px); sombra difusa (blur ~60px, y +20px,
  ~18%); no escuro ganha moldura/bisel `#3A3A3A` de ~14px.
- **Timeline de áudio:** clips com forma de onda verde em plano 3D inclinado, deslizando.
- **Anotação:** círculo de traço branco/ciano que segue um elemento do footage.
- **Cabeçalho:** "SHOWREEL" (esq.) · "2025" (dir.), 28px caixa alta `#CFCFCF`, margem 120px/90px; aparece
  só na abertura e no fecho (moldura do filme).

## Fundo
Nunca chapado: uma **fita/onda gigante muito suave** (contraste de 2–4%) atravessando o quadro na
diagonal, derivando devagar. No claro, a mesma fita em branco sobre `#ECEBEC`.

## Movimento permitido / proibido
**Permitido:** zoom-through; empurrão lento (ease-in) de antecipação; chicote com motion blur
direcional; eco (cópias em rastro); leque/baralho 3D com perspectiva; tela cheia ↔ card (escala +
raio + sombra); cortina de antes/depois; parede de cards com recuo de câmera; caça-níquel no chip;
"+" → "×"; deriva lenta contínua durante as seguras; corte duro na batida.
**Proibido:** crossfade genérico entre capítulos; bounce/elástico com overshoot visível; partícula;
lens flare; vinheta; grão; texto 3D; rotação 2D gratuita; tremor de câmera contínuo.

## Câmera
**Móvel e virtual.** Push-in lento (antecipação) → soco; recuo para revelar grade/parede; órbita 3D só
nos leques. Toda câmera "rápida" tem motion blur; toda câmera "lenta" é quase imperceptível (deriva).

## Render
Motion blur: **sim, forte, direcional**, só nos quadros rápidos (2–4 q). Brilho: só em acento (caixas,
chip selecionado). Aberração cromática: só nos chicotes. Grão/vinheta/flare: **não**.

## Lei de camadas (híbrido UI 2D + footage)
A UI é chapada e nunca recebe a luz do footage; o footage nunca vira chapado. Eles só interagem
fisicamente: o card projeta sombra no papel; o footage *entra* num card e *sai* de um card.

## Perícia · Camada 3 — Movimento

Medido com `pericia-movimento.py` (energia quadro a quadro, baldes de 0,5s) + `audio_beats.py`
(fluxo espectral, andamento, alinhamento corte ↔ batida). Dados crus em `movimento.json`.

## Números da referência (55s)

| Medida | Valor |
|---|---|
| Amplitude (pico ÷ mediana) | **5,3x** (mediana 6,97 · pico 36,90) |
| Filme em quase-parada | **40%** (inclui ~7s de fecho parado) |
| Picos (socos) | 8 → 3,0 · 7,0–8,0 · 29,0 · 41,5 · 43,0 · 44,5 |
| Cortes duros | **34** (0,62 por segundo) |
| Andamento da trilha | **~152 BPM** (batida 0,395s = 9,5 q) |
| Cortes a ≤2 q de uma batida forte | 17 de 34 (e **todos** da metade em diante: 29–46s) |
| Rajadas de corte | 9,4–11,3s: a cada 8–13 q · 34,5–36,1s: a cada **6–9 q** |

**Leitura:** o filme alterna **rajada e silêncio**. Os vales (0–2,5s; 3,5–6,3s; 45,5–46,3s; fecho) são
UI parada ou deriva lenta; os picos são chicotes de 2–4 quadros. O chip é sempre um **vale curto**
(0,5–1,0s parado) logo antes de uma rajada, que é a respiração antes do soco.

## Metas derivadas (escala 55s → para 15s ver a skill)
- amplitude ≥ 3,7x · quase-parada ≥ 30% · ≥ 5 picos · corte duro obrigatório em algum ponto.

## A física de cada transição (contada quadro a quadro)

| ID | Nome | Quadros (a 24 fps) | Física |
|---|---|---|---|
| T1 | **Zoom-through** (texto → cena) | 8 + 3 + 10 | empurrão ease-in 1,00→1,15 em 8 q (antecipação) · 3 q de rajada: escala ×6–8 com blur e rotação 3D, as bordas das caixas viram riscos coloridos · cena nova já está atrás, nasce em ~0,55 e assenta em 1,0 em ~10 q (ease-out expo) |
| T2 | **Botão → chip → caça-níquel** | 6 + 14 + 2 | círculo "+" estica na horizontal em 6 q, o "+" gira 45° e vira "×" · texto rola vertical com blur em ~14 q, desacelerando, passa por 2–3 opções e trava na certa · troca para "selecionado" em 1–2 q e o brilho cresce por ~4 q |
| T3 | **Baralho 3D → mergulho** | 3 + 18 + 12 | título explode com eco (cópias em rastro) em 2–3 q · baralho de cards em perspectiva gira ~18 q · o card da frente endireita e cresce até ocupar o quadro em ~12 q, **pousando no drop** |
| T4 | **Tela cheia → card** | 7 + 10 + 2 | footage encolhe 100→90% em 7 q ganhando raio e sombra (o mundo claro aparece em volta) · deriva lateral lenta ~10 q · sai em chicote vertical em 2 q · o chip entra **no mesmo vetor** do chicote (o movimento atravessa o corte) |
| T5 | **Empurra → encolhe com cortina → parede** | 6 + 22 + 15 + 30 | footage empurra pela esquerda em 6 q · segura ~22 q · encolhe para card em ~15 q **enquanto uma cortina vertical revela o antes/depois** · recuo de câmera para parede de cards em ~30 q |
| T6 | **Chicote de parede** | 2 | a parede inteira atravessa em 1–2 q com blur horizontal enorme; corte duro para o mundo escuro na batida |
| T7 | **Smear de chip → corte** | 1 + 3 + corte | chip parado · estica em X (×1,3) em 1 q · vira risco de tela inteira (×6 em X, blur X) em 3 q · **corte duro por trás do risco, na batida** |
| T8 | **Vazio → texto cômico → soco** | 1 + 8 + 22 + 3 + 1 + 12 | 1 q de fundo vazio · palavras entram da direita com blur em cascata (8 q) · segura encolhendo devagar 1,0→0,8 (~22 q) · encolhe mais rápido (3 q, antecipação) · **soco**: "You Should Hire Him" em ×1,4 com risco coral (1 q) · assenta ×1,4→×0,85 em ~12 q |

## Regras de física que se repetem
1. **Antecipação → rajada → assentamento.** Quase toda transição é ease-in lento (6–8 q) → 2–3 q de
   rajada com blur → ease-out longo (10–12 q). A rajada é curta; o assentamento é longo.
2. **Motion blur só na rajada.** Parado é nítido; rápido é borrado. Nunca blur em elemento lento.
3. **Continuidade de vetor.** O que entra na cena nova entra na direção em que a cena velha saiu.
4. **O elemento vira a transição.** Texto vira risco, chip vira risco, card vira tela, tela vira card.
   Não existe "transição" como camada separada.
5. **Deriva nas seguras.** Nenhum quadro é 100% congelado fora do fecho: escala 1,00→1,03 ao longo
   da segura (quase imperceptível), o que mantém a quase-parada viva sem subir a energia.
6. **O soco pousa na batida** (≤2 q), e o **drop da música** recebe a maior mudança de enquadramento
   (card → tela cheia no 8,0s).
