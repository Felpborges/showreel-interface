---
name: showreel-interface
description: >-
  Método de design + motion para SHOWREELS, REELS DE MARCA, SIZZLES e PROMOS curtos (15s, 30s,
  60s) no estilo "a interface narra", destilado da perícia quadro a quadro do SHOWREEL 2025 (Misha
  Ruchko): hook-provocação montado palavra a palavra, CHIPS de UI como títulos de capítulo, o
  trabalho/produto invadindo a tela em galerias de CARDS (leque 3D, carrossel 9:16, parede, tela
  cheia ↔ card), dois mundos alternados (escuro/claro), toda transição feita por um elemento da
  cena (zoom-through, chip que vira risco, card que vira tela), cortes cravados na batida e
  rajada ↔ silêncio medidos em números. Reusável para QUALQUER marca: traduz cada dispositivo do
  filme para a UI nativa da marca (ex.: YouTube → busca, chips de filtro, thumbnails com selo de
  duração, barra de progresso vermelha, Inscrever-se + sino). Constrói em HyperFrames com música
  primeiro, cards estáticos antes de animar e teste de aceite numérico. Use SEMPRE que pedirem
  showreel, reel ou vídeo de marca curto, "reel de 15 segundos sobre X", vídeo sobre o
  YouTube/Instagram/um app/uma plataforma, portfólio em vídeo, sizzle, vinheta de lançamento com
  cara de interface, "no estilo daquele showreel", "chips e cards", ou ritmo de showreel com a UI
  de uma marca, mesmo sem citar a skill. NÃO use para editar gravação do Felipe falando
  (edicao-aiverso/edicao-video), aula (aula-html), roteiro (criador-de-roteiros) nem para periciar
  OUTRA referência (motion-por-referencia).
license: MIT
metadata:
  author: Felipe Borges
  version: "1.0"
---

# Showreel Interface — a interface narra

> Destilado da perícia do **SHOWREEL 2025 (Misha Ruchko)** — Vimeo 1124592722 · 55s · 24 fps ·
> música ~152 BPM. Números, quadros e contatos: `referencias/pericia-showreel-2025.md` e
> `referencias/pericia/`. Da referência a gente copia **método e sensação** (esqueleto, ritmo,
> física, gramática de transição). **Nunca o conteúdo**: tema, copy, fonte, cores e marca são
> sempre do projeto.

## 0 · O mecanismo (decore esta frase)

**A interface conta a história.** Um hook-provocação é *montado na tela* palavra a palavra; cada
capítulo é uma **etiqueta de UI que se aperta** (o chip); o trabalho ou o produto **invade a tela
como prova**, em galerias de cards, preso à batida; e **toda emenda é um elemento da cena virando a
transição**. O filme fecha invertendo a frase do começo.

Antes de desenhar, responda por escrito: **qual é o chip do meu projeto, qual é a prova, e qual
frase o final inverte?** Sem as três respostas você tem "cenas bonitas", não um filme.

## 1 · Por que a referência é tão boa (o que esta skill protege)

1. **É um argumento, não uma colagem.** Loop aberto no quadro 0 ("você NÃO quer esse cara no time"),
   promessa ("aqui está o porquê"), provas, e a mesma frase invertida no fim ("você deveria
   contratá-lo"). O espectador fica para ver o loop fechar.
2. **A linguagem visual é a ferramenta do próprio assunto.** Um motion designer fala a língua do
   After Effects: caixa de seleção com alças, etiqueta com ×, timeline de áudio. O público lê
   competência antes de ler uma palavra. Por isso, no nosso projeto, **a UI é a da marca**.
3. **Um título de capítulo reconhecível** (o chip), repetido 6×. Em 5s o espectador aprende a
   gramática e passa a *esperar* o próximo chip; essa antecipação é retenção.
4. **Cada prova no formato do próprio conteúdo**: vídeo curto em card 9:16, vídeo longo em tela
   cheia, som como timeline, cor como antes/depois. O enquadramento é o argumento.
5. **Dois mundos** (escuro/claro) marcam os capítulos no nível macro, antes de qualquer palavra.
6. **Rajada ↔ silêncio, medidos:** amplitude 5,3×, 40% do filme em quase-parada, cortes a cada 6–13
   quadros nas rajadas, **94% deles a ≤2 quadros de uma batida**. O chip parado (0,5–1s) é o vale
   antes do soco.
7. **Nenhuma transição genérica**: texto vira risco, chip vira risco, card vira tela, tela vira card.
   Há sempre UM elemento condutor que o olho segue.
8. **Física de câmera real**: antecipação lenta (6–8 q) → rajada curta com motion blur (2–3 q) →
   assentamento longo (10–12 q). Parado é nítido, rápido é borrado.
9. **Humor com tempo**: a piada segura ~1s de quase-silêncio e faz o soco final bater. A energia é
   confiante e brincalhona, nunca desesperada nem "vendedora".

## 2 · O arco (escale pela duração)

| Função | O que acontece | 15 s | 30 s | 60 s |
|---|---|---|---|---|
| **Hook-provocação** | frase palavra a palavra; 1–2 palavras-chave dentro do *dispositivo de título* | 0–2,5 | 0–3 | 0–3,5 |
| **Pivô** | zoom-through → promessa ("aqui está o porquê") + chip nasce de um botão "+" | 2,5–4 | 3–6 | 3,5–6,5 |
| **Capítulos** | chip → rajada de prova no formato certo, 1 enquadramento novo por capítulo | 2 caps · 4–11,5 | 3–4 caps · 6–24 | 5–6 caps · 6,5–45 |
| **Payoff** | 1 q de vazio → frase cômica/virada segura ~1s → **SOCO**: a frase do hook invertida | 11,5–13 | 24–27 | 45–49 |
| **Lockup** | identidade + CTA + moldura (cabeçalho) de volta; segura parado; música desce | 13–15 | 27–30 | 49–60 |

Em 15s não cabe tudo: **2 capítulos, 1 drop, 1 soco**. O drop da música recebe a maior mudança de
enquadramento do filme (na referência: o card da frente vira a tela cheia exatamente no drop).

## 3 · Os dispositivos — e a tradução para a marca

A referência tem seis dispositivos. No projeto novo, **cada um vira o átomo nativo da UI da marca**,
aquele que o público já conhece de tela. É isso que faz a identidade ser inconfundível sem copiar a
referência. Planilha, critérios e exemplos (YouTube, Instagram, Spotify, SaaS):
`referencias/traducao-de-marca.md`.

| Slot | Na referência | Função no filme | YouTube (caso testado) | Produto/SaaS genérico |
|---|---|---|---|---|
| **Título** | caixa de seleção com alças (ciano/coral), inclinada ±2–3° | destacar a palavra-chave do hook | logo + barra de busca digitando; a barra de progresso sublinha a palavra-chave | campo, comando ou prompt do produto |
| **Capítulo** | chip pílula com ×: "+" → pílula → caça-níquel → selecionado | nomear o capítulo | chips de filtro da home ("Tudo", "Shorts", "Ao vivo") | tag, filtro ou aba do produto |
| **Prova** | cards (raio ≈9% da largura, sombra difusa), 16:9 e 9:16 | mostrar o trabalho | thumbnails com selo de duração; Shorts 9:16 | telas e cards reais do produto |
| **Linha do tempo** | clips de áudio num plano 3D | processo, volume, escala | barra de progresso vermelha + scrubber | gráfico, timeline, log |
| **Anotação** | círculo rastreado sobre o footage | apontar um detalhe | sino, like, "Inscrito", contador subindo | cursor, clique, toast |
| **Lockup** | cartão de perfil + contatos + cabeçalho | CTA e assinatura | cabeçalho do canal + Inscrever-se → Inscrito + **ícone + /@handle** | marca + CTA + URL |

**O dispositivo é da marca; a gramática é da referência.** Se a marca não tem átomo para um slot,
use o slot neutro (a versão da referência, na paleta da marca). Nunca invente um "átomo" que finja
ser da marca, porque o público reconhece a falsificação na hora.

### Conformidade de marca: leia as diretrizes ANTES de desenhar
No teste do YouTube, três violações só apareceram quando a pesquisa leu `brand.youtube`: logo abaixo
do tamanho mínimo, blur aplicado ao logo numa transição e logo completo no fecho de um vídeo que
divulga canal. Por isso, na F1, escreva para a marca do projeto:
- **Tamanho mínimo e respiro** do logo e do ícone (YouTube: 100 px de altura; respiro = triângulo).
- **O que o logo pode sofrer** numa transição. Regra conservadora: só corte, fade, deslocamento e
  escala uniforme. Nunca blur, rotação, skew, stretch, recolor, sombra ou contorno. O movimento
  forte fica com os átomos de UI, não com o logo.
- **A assinatura de CTA regulamentar** (YouTube: ícone oficial + "/@handle" em Roboto; o logo
  completo não divulga canal).
- **Licença das fontes da marca.** Fonte "restrita" (ex.: YouTube Sans) só entra com aviso
  explícito, e a versão segura (fonte livre da UI, ex.: Roboto) é entregue junto.
- **Uso de UI/marca em mídia** que exija aprovação: diga à pessoa, não decida por ela.

## 4 · Dois mundos

A referência alterna escuro `#222` e claro `#ECEBEC` por capítulo. No projeto, os dois mundos vêm
da marca: se ela tem modo escuro e claro (YouTube `#0F0F0F`/`#FFFFFF`), **esses são os mundos**. Um
mundo por capítulo; a troca **nunca** é por crossfade: acontece pelo condutor (a tela cheia encolhe
e revela o outro mundo em volta; um chicote corta para o outro). Fundo nunca chapado: uma onda ou
fita enorme a 2–4% de contraste, derivando devagar.

## 5 · Gramática de transições

Quadros a 24 fps (≈ a 30 fps). Receitas GSAP seek-safe, anatomia e armadilhas:
`referencias/transicoes.md`.

| ID | Nome | Quadros | Condutor | Use quando |
|---|---|---|---|---|
| T1 | **Zoom-through** | 8 antecipação + 3 rajada + 10 assentamento (≈10+4+12) | a caixa/palavra-chave, cujas bordas viram riscos | hook → pivô; saída de qualquer tela de texto |
| T2 | **Botão → chip → caça-níquel** | 6 + 14 + 2 (≈8+18+3) | o "+" que gira 45° e vira "×" | nascer de cada capítulo |
| T3 | **Baralho 3D → mergulho** | 3 + 18 + 12 (≈4+22+15) | o card da frente, que vira a tela cheia | entrar na primeira prova; cravar no drop |
| T4 | **Tela cheia → card** | 7 + 10 + 2 (≈9+12+3) | a borda do footage, que ganha raio e sombra | trocar de mundo; sair de uma rajada |
| T5 | **Empurra → encolhe com cortina → parede** | 6 + 22 + 15 + 30 | a cortina vertical (antes/depois) | mostrar transformação; revelar volume |
| T6 | **Chicote** | 1–2 (≈2–3) | o grupo inteiro, com blur direcional | corte de mundo na batida forte |
| T7 | **Smear de chip → corte** | 1 + 3 + corte (≈1+4) | o chip esticando até virar risco de tela inteira | chip → rajada de amostras |
| T8 | **Vazio → frase cômica → soco** | 1 + 8 + 22 + 3 + 1 + 12 | a frase, que encolhe antes do soco | payoff |

**As seis leis de física** (valem para qualquer tween do filme):
1. **Antecipação → rajada → assentamento.** Ease-in lento (6–8 q) → 2–3 q de rajada → ease-out longo
   (10–12 q, `expo.out`/`power4.out`). A rajada é curta; o assentamento é longo.
2. **Motion blur só na rajada.** Parado é nítido; lento é nítido; só o que atravessa mais de uma
   largura própria por quadro ganha blur (1–3 elementos por filme, não todo tween).
3. **Continuidade de vetor.** O que entra na cena nova entra na direção em que a cena velha saiu.
4. **O elemento vira a transição.** Não existe camada de "transição"; existe um elemento que muda
   de papel.
5. **Deriva só nas seguras**, ≤3% de escala ao longo da segura. Mantém a quase-parada viva sem
   subir a energia. Fora das seguras, parado é parado.
6. **O soco pousa na batida** (≤2 q), e o drop recebe a maior mudança de enquadramento.

## 6 · Enquadramentos (o formato prova o conteúdo)

Tipografia central · tela cheia · card flutuante · par de cards 9:16 com chip no meio · carrossel de
verticais · leque/baralho 3D · parede de cards com recuo de câmera · grade 2×2 com anotações ·
plano 3D inclinado (timeline) · UI em tela cheia (a página da marca). Em 15s use **≥4 enquadramentos
distintos** (a variedade é metade da energia) e **no máximo 1 novo por capítulo**. Quando escolher,
pense no formato do conteúdo mostrado: vertical é card 9:16, longo é tela cheia, volume é parede.

## 7 · Ritmo e música: a música vem ANTES da animação

Detalhe, matemática da grade e kit de som: `referencias/ritmo-e-audio.md`.

1. **Trilha primeiro, escolhida por medição.** Gere 3–6 trilhas (Higgsfield `sonilo_music`, 1 crédito
   cada, com a estrutura escrita em segundos no prompt) e **meça** cada uma:
   `python3 scripts/batida.py trilha.m4a --fps 30` → BPM, fase (pelo bumbo), compassos, drop.
   O modelo não obedece BPM nem segundos (pedido 128 → saiu 122/130/132); escolha a que tem **arco**
   (intro → drop → parada → fim) e bumbo legível. Loop chapado reprova.
   Depois **endireite a grade**: estique para um BPM que caia em quadro inteiro (a 30 fps, 120 BPM =
   15 q por tempo) com `ffmpeg -af atempo=<medido→alvo>` e desloque para o drop cair num tempo 1.
2. **Monte a grade de batidas** e só então os beats: palavras do hook em colcheias/semínimas; o
   zoom-through num tempo forte; o drop = a maior mudança de enquadramento; cortes nos onsets
   (≤2 q); chip parado por 1–2 tempos; soco num tempo 1; lockup pousa no 1 do último compasso.
3. **Cortes com duração variada** dentro da rajada (1, 1, ½, ½, 1, 2 tempos), nunca todos iguais.
   A 150 BPM e 24 fps, 1 tempo = 9,6 q.
4. **Som desenhado**: whoosh em todo chicote, clique em todo chip, tique no caça-níquel, impacto no
   drop e no soco, e o som nativo da marca quando existir (ex.: o "ding" do sino). `scripts/sfx.py`.
5. **Metas para 15s** (escaladas da referência): amplitude ≥ 3,7×; quase-parada ≥ 30%; picos ≥ 2;
   ≥ 3 cortes duros; ≥ 70% dos cortes a ≤2 q de uma batida. Teste: `scripts/aceite.py` (mede a
   referência com o mesmo método; o reel do YouTube fez 100% contra 94% da referência).

## 8 · Tipografia e cor (papéis; a marca preenche)

- **Uma família**, dois papéis: **Título** (Title Case ou sentence case, bold/black, 64–100 px a
  1080p, gradiente vertical sutil ou cor chapada; brilho só se a marca aceitar) e **Rótulo** (CAIXA
  ALTA, medium, 26–34 px, tracking +2–4%). Sem itálico, sem texto 3D, sem contorno.
- **Dois acentos no máximo, com semântica fixa**: A = "selecionando/ferramenta", B = "escolhido/CTA".
  Mais um *sinal de capítulo* opcional, só num capítulo. A cor de verdade vem do conteúdo (footage,
  thumbnails); a UI é quase monocromática.
- **Legibilidade de reel**: em 1080×1920, nada lido abaixo de 44 px; em 1920×1080, nada abaixo de 26 px.

## 9 · O processo (fases e portões)

Herda o contrato do Felipe (`motion-por-referencia` + `edicao-aiverso`): perícia com números, cards
estáticos antes de animar, esqueleto único, portões mecânicos, aceite numérico.

| Fase | Entrega | Portão |
|---|---|---|
| **F0 · Entrada** | brief em 5 linhas: marca, assunto, duração, formato (16:9/9:16), CTA; motor = HyperFrames (`npx hyperframes --version`) | as três respostas do §0 escritas |
| **F1 · Marca** | `marca.md`: tokens verificados (hex, fonte, raios, componentes) + logos oficiais + tabela de tradução dos 6 slots + **regras de uso** (§3, conformidade) | nenhum token "no olho"; cada um com fonte; regras de logo e CTA escritas |
| **F2 · Assets e pesquisa** | dados reais (números com fonte), assets do projeto (thumbs, telas, footage), fontes locais com glifos PT-BR. Pesquisa de marca e coleta de dados rodam em paralelo (agentes) enquanto a trilha é escolhida | todo número tem fonte; todo asset conferido; **capítulo sem prova real não existe** (o canal do teste tinha 0 Shorts: o capítulo "Shorts" caiu) |
| **F3 · Música e grade** | trilha + `grade.json` (batidas/compassos em s e quadros) + mapa de SFX | BPM medido, drop localizado |
| **F4 · Beats + copy** | `ESTRUTURA.md` (beat, janela em compassos, enquadramento, condutor da emenda) + `copy.txt` (toda string em tela, literal, "nada além disso aparece") | cada beat prova o mecanismo |
| **F5 · Cards estáticos** | `cards.html`: um card por beat no momento-chave, assets reais, notas "o que se move primeiro / emenda", mapa de emendas, tokens + proibições, risco nº1 e plano B | crítica (`loop-de-design` ou críticos em paralelo) + **aprovação da pessoa** |
| **F6 · Construção** | projeto HyperFrames: host + sub-composições (`referencias/transicoes.md`, `referencias/componentes.md`), harness por frame | cada frame conferido em 3–4 instantes |
| **F7 · Portões** | `portoes.py` (glifos, paleta, seek-safety) + `npx hyperframes check` | zero erro |
| **F8 · Render + aceite** | MP4 + contato (meio de cada beat, ±2 q de cada emenda) + `scripts/aceite.py` | aceite aprovado, ou reprovação explicada |

**Autonomia:** se a pessoa pediu a cadeia inteira de uma vez ("analisa, cria e já faz o reel"),
entregue os cards como arquivo de progresso (para ela poder redirecionar) e siga; diga isso no fim.
Se não, pare na F5 e espere a aprovação.

## 10 · HyperFrames: o que muda neste estilo

Receitas completas em `referencias/transicoes.md` e `referencias/componentes.md`. O essencial:

- **Tempo vem da grade**: `t = compasso*4*b + tempo*b` (b = 60/BPM), arredondado ao quadro
  (`Math.round(t*fps)/fps`). Nunca "no olho".
- **Corte duro** = dois clipes encostados (`data-start`/`data-duration`), sem tween.
- **Card ↔ tela cheia**: anime `scale` + `clipPath: inset(… round Rpx)` num wrapper com a sombra num
  irmão; nunca `width/height/top/left` (lint `gsap_non_transform_motion` e sem motion blur).
- **3D**: container com `perspective` + filhos `transformStyle:"preserve-3d"`; anime
  `rotationY/rotationX/z`. Um único container 3D por cena.
- **Motion blur**: componente de registro `motion-blur` (`data-hf-motion-blur`) em 1–3 elementos
  que socam, ou blur direcional falso (`scaleX` 1→4 + `filter: blur()`) nos riscos de T1/T7.
- **Eco**: 3–5 clones pré-criados no markup, cada um com o próprio tween atrasado 1 q e opacidade
  .45/.25/.12. Seek-safe (sem callback).
- **Seek-safety e estado inicial**: só tween de propriedade; repouso via CSS ou `gsap.set` fora da
  timeline; nada de `onUpdate`, `Math.random`, `Date.now`.
- **Arquitetura que funcionou** (`exemplos/youtube-15s/`): host com os mundos como camadas de fundo
  (`class="clip"` full-bleed) + uma sub-composição transparente por beat, **sobrepostas 2–3 q nas
  emendas** que atravessam frames (quem sai fica por cima: z-index explícito + `isolation:isolate`);
  sistema de design num `assets/<marca>.css` ligado por `<link>` **dentro** do `<template>` (vale no
  harness e no motor); um vídeo que continua entre frames reusa o arquivo com `data-media-start`.
- **Verificação por frame**: copie `scripts/harness.html` e `scripts/shoot.sh` para `<projeto>/_dev/`
  e rode `_dev/shoot.sh 01-nome 0F0F0F 0.2 1.3 1.8` (fundo do mundo, instantes locais). O harness
  **não** aplica `data-start` de filhos nem alterna vídeos: cromo e legendas por clipe vão por
  `tl.set` de opacidade; vídeos se conferem no render (`hyperframes render` leva ~20 s para 15 s).
- **Lint**: estado "selecionado" feito por sobreposição (chip claro sobre o escuro) precisa de
  `data-layout-allow-overlap`; contador que rola e cards que saem do slot, de
  `data-layout-allow-overflow`. Reserve isso para o intencional e prove no snapshot.

## 11 · O que NÃO fazer

- Crossfade entre capítulos. Cortes todos do mesmo tamanho. Blur em movimento lento.
- Mais de dois acentos. UI genérica "tipo app" no lugar da UI real da marca. Átomo inventado que
  finge ser da marca. Logo distorcido, recolorido ou fora das diretrizes da marca.
- Copiar da referência: a copy ("You Don't Want This…"), o ciano/coral, a fonte, os exemplos.
- Animar antes da grade de batidas. Colocar 4 capítulos em 15s. Encher todo quadro de movimento
  (sem silêncio não há soco).
- Texto de preenchimento legível que não é do projeto: feeds e listas de fundo são *greeked*
  (ilegíveis de propósito) ou são dados reais.
- Chamar de pronto um filme que reprovou no aceite sem dizer isso.
- Protagonista pequeno: o texto do hook e o objeto de cada beat atravessam 40–80% da largura. Barra
  inteira com texto de 50 px lê como "tela de computador", não como filme.
- Logo abaixo do mínimo da marca, logo com efeito (blur, rotação, sombra) ou logo completo onde a
  diretriz pede o ícone. Fonte restrita da marca sem avisar a pessoa e sem versão segura.
- Capítulo sem prova real (formato que o canal/produto não tem) para "completar a estrutura".

## 12 · Arquivos

- `referencias/pericia-showreel-2025.md`: a perícia completa (estrutura por beat, design medido,
  movimento em números, física de cada transição) + `referencias/pericia/` (números em JSON; as
  grades e tiras de quadros são obra de terceiros, ficam só na máquina local: regenere com
  `scripts/grade.py` a partir do vídeo, comandos no topo da perícia).
- `referencias/traducao-de-marca.md`: como mapear os 6 slots para qualquer marca, com exemplos.
- `referencias/transicoes.md`: T1–T8 com anatomia, receita GSAP seek-safe e armadilhas.
- `referencias/componentes.md`: HTML/CSS/GSAP dos componentes (título, chip, card, leque 3D,
  carrossel, parede, timeline, anotação, cabeçalho, lockup).
- `referencias/ritmo-e-audio.md`: grade de batidas, colocação de cortes, trilha, SFX, mixagem.
- `referencias/caso-youtube.md`: o teste prático (reel de 15s sobre o YouTube): decisões, números,
  o que deu errado, como foi corrigido e o que ficou pendente.
- `exemplos/youtube-15s/`: o projeto do teste (host, 6 frames, `yt.css`, `cues.json`, `ESTRUTURA.md`,
  `copy.txt`, folha do filme) — modelo de código para vestir outra marca.
- `scripts/batida.py` (BPM, fase pelo bumbo, compassos, drop, alinhamento de cortes; `--t0` para
  trilha alinhada à mão) · `scripts/grade.py` (folha de contato com carimbo de tempo; o ffmpeg daqui
  não tem `drawtext`) · `scripts/sfx.py` (kit de som sintetizado + `mix` com cues, "abafar" e
  loudnorm −14 LUFS) · `scripts/aceite.py` (aceite com metas escaladas pela duração e alinhamento
  da referência medido pelo mesmo método) · `scripts/harness.html` + `scripts/shoot.sh`
  (verificação de um frame em vários instantes).
- Skills irmãs: `motion-por-referencia` (perícia de outra referência, `portoes.py`),
  `edicao-aiverso` (identidade AiVerso e harness), `hyperframes-*` (motor), `loop-de-design`
  (críticos), `higgsfield-generate` (trilha, imagens).
