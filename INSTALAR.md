# Instalar a skill `showreel-interface` v1.0

> **Como usar este arquivo:** copie o conteúdo INTEIRO (do início ao fim) e cole
> numa conversa do Claude Code. A instrução para o Claude já está aqui embaixo.
> Depois que ele terminar, reinicie a sessão do Claude Code para a skill aparecer.

---

## Instrução para o Claude Code

Instale a skill abaixo na minha máquina. Faça exatamente isto:

1. Crie a pasta `~/.claude/skills/showreel-interface/` (e as subpastas `scripts/` e `referencias/`).
2. Para cada bloco marcado com `### ARQUIVO: <caminho>`, grave um arquivo nesse
   caminho, relativo à pasta da skill, com **exatamente** o conteúdo que está
   dentro da cerca de código logo abaixo do título — sem acrescentar, remover
   ou reformatar nada.
3. Dê permissão de execução aos scripts:
   `chmod +x ~/.claude/skills/showreel-interface/scripts/*.py ~/.claude/skills/showreel-interface/scripts/*.sh`.
4. Confirme listando a árvore final e rodando
   `python3 ~/.claude/skills/showreel-interface/scripts/batida.py --help`.
5. Me avise que preciso reiniciar a sessão para a skill carregar.

Não instale dependências sem me perguntar. As usadas são: `ffmpeg`,
`pip install numpy scipy opencv-python pillow fonttools`, `npx hyperframes` e a
skill `motion-por-referencia` (https://github.com/Felpborges/motion-por-referencia),
que o teste de aceite usa. A pasta `exemplos/` só vem pelo `git clone` do repositório.

---
### ARQUIVO: SKILL.md

````markdown
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
````

---
### ARQUIVO: referencias/pericia-showreel-2025.md

````markdown
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
````

---
### ARQUIVO: referencias/traducao-de-marca.md

````markdown
# Tradução de marca — os 6 slots vestidos com a UI nativa

O showreel de referência é bom porque **fala a língua da ferramenta do próprio assunto** (um motion
designer mostrando caixa de seleção, etiqueta e timeline). Para qualquer marca, a pergunta é a mesma:
**qual é a UI que o público desta marca já tem na memória muscular?** É ela que vai narrar.

## O procedimento (F1 da skill)

1. **Inventário de átomos.** Abra o produto/site real (navegador embutido ou captura) e liste os
   componentes que alguém reconheceria de relance, **sem o logo**: botões, chips/tags, cards, barras,
   contadores, ícones de ação, estados (selecionado, ativo, ao vivo), microcopy fixa ("Inscrever-se",
   "Seguir", "Adicionar à playlist"). Para cada um: cor exata, raio, altura, fonte, peso, estado
   ativo. Fonte de cada número (CSS do site, brand guidelines, captura medida). Nada "no olho".
2. **Teste da silhueta.** Um átomo só entra se for reconhecível em preto e branco, sem logo, em
   0,5 s. (A barra de progresso vermelha do YouTube passa; um botão azul genérico não.)
3. **Mapa dos 6 slots.** Preencha a tabela abaixo. Cada slot recebe o átomo que faz **a mesma
   função narrativa** do dispositivo da referência, não o que se parece com ele.
4. **Dois mundos.** Se a marca tem modo claro e escuro, esses são os mundos. Senão: fundo da marca +
   o seu oposto de luminância com a mesma temperatura.
5. **Acentos.** A marca manda: no máximo 2 com semântica (A = ação/seleção, B = escolhido/CTA) e,
   se a marca tiver, 1 cor de assinatura que aparece **pouco e sempre no mesmo papel**.
6. **Tipografia.** A fonte da marca (se licenciável) ou a da UI do produto. Uma família, dois papéis.
7. **Diretrizes.** Leia as regras de uso do logo (respiro, tamanho mínimo, não distorcer/recolorir/
   animar). Onde a diretriz proíbe animar o logo, anime o **entorno** (o logo entra por corte, fica
   parado e nítido) e deixe o movimento para os átomos de UI.
8. **Teste do filme sem logo.** Tape o logo nos cards estáticos: a marca ainda é óbvia? Se não, a
   tradução falhou; volte ao passo 1 e troque átomos genéricos por nativos.

## A tabela

| Slot | Função narrativa | Critério do átomo nativo |
|---|---|---|
| **Título** | destacar a palavra-chave do hook enquanto a frase se monta | um campo onde se *escreve* ou *seleciona* na marca (busca, prompt, editor, compositor) |
| **Capítulo** | nomear o capítulo; o espectador aprende e passa a esperar | um seletor da marca (chip, tag, aba, filtro, categoria) com estado "ativo" |
| **Prova** | mostrar o trabalho/produto no formato certo | o card de conteúdo da marca (thumbnail, post, faixa, tela) com os metadados reais |
| **Linha do tempo** | processo, volume, progresso | a barra/linha/gráfico nativo (progresso, stories, waveform, analytics) |
| **Anotação** | apontar um detalhe, dar o "clique" | um estado de interação da marca (curtir, seguir, sino, check, toast) |
| **Lockup** | assinatura + CTA | a página de perfil/cabeçalho da marca + o botão de ação principal |

## Caso YouTube (o teste prático desta skill — tokens verificados em `caso-youtube.md`)

| Slot | Átomo | Como se move (gramática da referência) |
|---|---|---|
| Título | **logo oficial (≥100 px) + barra de busca** no plano de abertura; push para a busca digitando o hook; a **barra de progresso** sublinha a palavra-chave | digitação nas colcheias; zoom-through atravessando a busca, a barra vira o risco (T1); o logo sai só por fade/deslocamento |
| Capítulo | **chips de filtro** da home ("Tudo", "Shorts", "Ao vivo"…) | a fileira rola na horizontal e trava no chip do capítulo, que fica selecionado (T2 nativo) |
| Prova | **thumbnails 16:9 com selo de duração** (grade da home, com título + canal + views) e **Shorts 9:16** | baralho 3D de thumbnails (T3), mergulho no drop para o "player" em tela cheia |
| Linha do tempo | **barra de progresso vermelha** com scrubber e marcas de capítulo | o risco do zoom-through É a barra vermelha; ela corre e vira transição |
| Anotação | **Inscrever-se → Inscrito + sino**, like, contador de views subindo | clique com ripple nativo, contador rolando (caça-níquel de números) |
| Lockup | **cabeçalho do canal** (avatar redondo, nome, @handle, inscritos, botão) + **assinatura regulamentar: ícone oficial + "/@handle"** | o botão vira "Inscrito" com o sino; a assinatura entra por fade + deslocamento e segura parada |

Mundos: modo escuro `#0F0F0F` e modo claro `#FFFFFF` (os dois da própria UI). Acento A = branco/preto
de seleção (o chip ativo inverte), acento B = o **vermelho #FF0033** (o #FF0000 é o antigo), só em:
ícone, barra de progresso (`linear-gradient(90deg,#FF0033 80%,#FF2791)`, medido no player), scrubber e o
soco final. Fonte: Roboto (UI, OFL) e, nos títulos, YouTube Sans **só com aviso** (fonte restrita do
Google) + versão Roboto para publicar. Tokens completos: `exemplos/youtube-15s/yt.css`.

## Outras marcas (esboço rápido do mapa)

| Marca | Título | Capítulo | Prova | Linha do tempo | Anotação | Lockup |
|---|---|---|---|---|---|---|
| **Instagram** | campo de legenda / busca | abas do perfil (grade, reels, marcados) | posts 4:5 e reels 9:16 | barra de stories segmentada | coração do like, "Seguir" | cabeçalho do perfil |
| **Spotify** | busca | chips de gênero/filtro | capas quadradas + faixas | barra de reprodução + waveform | coração verde, "Adicionado" | perfil do artista + "Seguir" |
| **Notion/SaaS** | comando "/" ou prompt | abas/tags de banco de dados | páginas/cards do produto | timeline/gantt | check, toast, cursor de colaborador | logo + CTA + URL |
| **AiVerso (Felipe)** | prompt do Claude Code | pills da identidade (ponto azul/marigold/coral) | cards brancos raio 24 com os motions dele | escada pontilhada | caixa de seleção + cursor | marca A-V + aiverso.tech |

## Quando a marca não tem átomo para um slot
Use o slot **neutro** (a forma da referência: caixa de seleção, pílula com ×, card com sombra) na
paleta e na fonte da marca. É honesto e consistente. O que não se faz é fabricar um "componente
oficial" que a marca não tem: o público percebe, e o filme perde a autoridade que a tradução deu.
````

---
### ARQUIVO: referencias/transicoes.md

````markdown
# Transições T1–T8 — anatomia, receita e armadilhas

Tudo aqui é **seek-safe** (só tween de propriedade; nada de `onUpdate`/`onComplete`/`Math.random`)
e respeita o contrato do HyperFrames: estado inicial no CSS ou em `gsap.set()` **fora** da
timeline, nunca `tl.set` na posição 0; anime `x/y/scale/rotation*/opacity/filter/clipPath`, nunca
`top/left/width/height/fontSize` (lint `gsap_non_transform_motion`, e o motion blur não enxerga).

Convenções das receitas:
```js
var FPS = 30, q = 1 / FPS;            // 1 quadro
var b = 60 / BPM;                     // 1 tempo
function Q(t){ return Math.round(t * FPS) / FPS; }   // encaixa no quadro
// T = instante do EVENTO (o quadro em que o soco acontece), vindo da grade de batidas
```
Os números de quadros da perícia são a 24 fps; a 30 fps multiplique por 1,25 e arredonde.

---

## T1 · Zoom-through (texto → cena)
**Anatomia (24 fps):** 8 q de antecipação (escala 1,00→1,15, ease-in) · 3 q de rajada (escala ×6–8,
blur, leve rotação 3D; as bordas da caixa viram riscos coloridos que atravessam o quadro) · a cena
nova já está por trás e assenta de 0,55→1,0 em ~10 q (`expo.out`).
**Condutor:** a palavra-chave dentro do dispositivo de título. **Use:** hook → pivô.
```js
// cena A (texto) e cena B (próxima) estão no MESMO frame, B por baixo com opacity 0
tl.to("#fA-bloco", { scale: 1.15, duration: 10*q, ease: "power2.in" }, T - 14*q);
tl.to("#fA-bloco", { scale: 7, rotationX: 14, rotationZ: -3, filter: "blur(16px)",
                     duration: 4*q, ease: "power4.in" }, T - 4*q);
tl.to("#fA-bloco", { opacity: 0, duration: 2*q, ease: "none" }, T - 2*q);
// riscos: 2 barras finas na cor do acento, que nascem nas bordas da caixa e saem do quadro
tl.fromTo("#fA-risco1", { scaleX: .2, opacity: 0 }, { scaleX: 4, x: -900, opacity: 1,
           duration: 4*q, ease: "power3.in" }, T - 4*q);
tl.to("#fA-risco1", { opacity: 0, duration: 2*q }, T);
// cena B nasce pequena e assenta (o assentamento é longo)
tl.fromTo("#fB-cena", { scale: .55, opacity: 0 }, { scale: 1, opacity: 1,
           duration: 12*q, ease: "expo.out" }, T - 1*q);
```
**Armadilhas:** blur acima de ~20px em texto grande custa caro no render; o `opacity:0` do bloco
precisa acontecer nos 2 últimos quadros, senão sobra um borrão parado. Não use `perspective` no
root: coloque `transformPerspective: 1200` no próprio bloco.

## T2 · Botão → chip → caça-níquel
**Anatomia:** botão circular "+" (≈ altura da pílula) · estica na horizontal em 6 q enquanto o "+"
gira 45° e vira "×" · o texto rola na vertical por ~14 q com blur, desacelerando, passando por 2–3
opções e travando na certa · troca para "selecionado" em 1–2 q e o brilho cresce por ~4 q.
**Condutor:** o "+" que vira "×". **Use:** nascer de cada capítulo.
```html
<div class="chip" id="fN-chip">                 <!-- pílula com largura FINAL; é recortada -->
  <div class="chip-janela"><div class="chip-rolo" id="fN-rolo">
    <span>OPÇÃO A</span><span>OPÇÃO B</span><span>ALVO</span></div></div>
  <div class="chip-x" id="fN-x">+</div>
</div>
```
```js
var W = 520, H = 120, R = (W - H) / 2;          // recorte começa num círculo
gsap.set("#fN-chip", { clipPath: `inset(0px ${R}px 0px ${R}px round 999px)` });
tl.to("#fN-chip", { clipPath: "inset(0px 0px 0px 0px round 999px)", duration: 8*q,
                    ease: "power3.out" }, T);
tl.fromTo("#fN-x", { rotation: 0, x: 0 }, { rotation: 45, x: 0, duration: 8*q, ease: "power3.out" }, T);
// rolo: cada <span> tem a altura da janela; o rolo sobe 2 linhas e trava
tl.fromTo("#fN-rolo", { y: 0, filter: "blur(6px)" }, { y: -2 * H, filter: "blur(0px)",
           duration: 18*q, ease: "power4.out" }, T + 6*q);
// estado selecionado (troca seca + brilho crescendo)
tl.to("#fN-chip", { backgroundColor: "#0F0F0F", color: "#FFFFFF", duration: 2*q }, T + 24*q);
```
**Armadilhas:** animar `width` dispara lint e quebra o raio; o recorte (`clipPath inset … round`)
mantém a pílula perfeita em qualquer largura. Coloque o "×" como texto "+" girado, não um ícone
diferente: é a continuidade do elemento que vende o truque. **Tradução de marca:** se a marca tem
chips em fileira (YouTube), o caça-níquel vira **a fileira rolando na horizontal e travando no chip
certo**, que então fica selecionado; mesmo mecanismo, átomo nativo.

## T3 · Baralho 3D → mergulho
**Anatomia:** o título explode com eco em 2–3 q · um baralho de 8–14 cards em perspectiva gira
~18 q (a câmera orbita) · o card da frente endireita e cresce até ocupar o quadro em ~12 q e
**pousa no drop**.
**Condutor:** o card da frente. **Use:** entrar na primeira prova.
```js
// palco 3D: um container com perspective; cards com transformStyle preserve-3d
gsap.set("#fN-palco", { perspective: 1600 });
gsap.set(".fN-card", { transformStyle: "preserve-3d" });
cards.forEach(function(el, i){
  tl.fromTo(el, { x: 1400 + i*40, z: -i*90, rotationY: -62, rotationZ: 6, opacity: 0 },
                { x: -i*70, z: -i*90, rotationY: -28 + i*1.5, rotationZ: 2, opacity: 1,
                  duration: 16*q, ease: "power3.out" }, T - 30*q + i*q);
});
// o card da frente NÃO está no palco 3D: é um elemento 2D que parte da posição projetada
tl.fromTo("#fN-frente", { x: 330, y: 70, scale: .42, rotationY: -26, transformPerspective: 1600,
                          clipPath: "inset(0px round 40px)" },
          { x: 0, y: 0, scale: 1, rotationY: 0, clipPath: "inset(0px round 0px)",
            duration: 14*q, ease: "power3.inOut" }, T - 14*q);   // termina NO drop
```
**Armadilhas:** um único contexto 3D por cena; `preserve-3d` não atravessa `overflow:hidden` nem
`filter` (achata). Por isso o card que mergulha é 2D (aproximação da projeção), não o do baralho.

## T4 · Tela cheia → card
**Anatomia:** 7 q encolhendo 100→86–90% ganhando raio e sombra (o outro mundo aparece em volta) ·
~10 q de deriva lateral lenta · saída em chicote em 2 q · o próximo elemento entra **no mesmo vetor**.
**Condutor:** a borda do footage. **Use:** trocar de mundo; sair de uma rajada.
```js
// #fN-w = wrapper do footage (overflow hidden); #fN-sombra = irmão com box-shadow e mesmo raio
tl.fromTo("#fN-w", { scale: 1, clipPath: "inset(0px round 0px)" },
          { scale: .88, clipPath: "inset(0px round 32px)", duration: 9*q, ease: "power3.out" }, T);
tl.fromTo("#fN-sombra", { scale: 1, opacity: 0 }, { scale: .88, opacity: 1, duration: 9*q,
           ease: "power3.out" }, T);
tl.to(["#fN-w", "#fN-sombra"], { x: -48, duration: 12*q, ease: "none" }, T + 9*q);
tl.to(["#fN-w", "#fN-sombra"], { y: -1400, duration: 3*q, ease: "power4.in" }, T + 21*q);
tl.fromTo("#fN-proximo", { y: 700, filter: "blur(10px)" }, { y: 0, filter: "blur(0px)",
           duration: 12*q, ease: "expo.out" }, T + 22*q);   // mesmo vetor (de baixo p/ cima)
```
**Armadilhas:** o raio do `clipPath` é local (escala junto); 32px × 0,88 ≈ 28px visíveis. A sombra
num irmão, não no wrapper: `clip-path` corta a própria sombra.

## T5 · Empurra → encolhe com cortina → parede
**Anatomia:** o footage entra empurrando pela lateral em 6 q · segura ~22 q (versão "antes") ·
encolhe para card em ~15 q **enquanto uma cortina vertical revela a versão "depois"** · recuo de
câmera para uma parede de cards em ~30 q.
**Condutor:** a cortina. **Use:** transformação (antes/depois); revelar volume.
```js
// duas camadas do mesmo footage: #fN-antes (filtro "antes") e #fN-depois por cima
gsap.set("#fN-depois", { clipPath: "inset(0% 100% 0% 0%)" });
tl.fromTo("#fN-par", { x: -1920 }, { x: 0, duration: 7*q, ease: "power4.out" }, T);
tl.to("#fN-depois", { clipPath: "inset(0% 0% 0% 0%)", duration: 18*q, ease: "power2.inOut" }, T + 34*q);
tl.to("#fN-par", { scale: .5, duration: 18*q, ease: "power3.inOut" }, T + 34*q);
tl.fromTo("#fN-parede", { scale: 1.9 }, { scale: 1, duration: 36*q, ease: "power3.out" }, T + 40*q);
```

## T6 · Chicote
**Anatomia:** o grupo inteiro atravessa em 1–2 q com blur direcional enorme; corte duro na batida.
```js
tl.to("#fN-grupo", { x: -2600, filter: "blur(24px)", duration: 2*q, ease: "power4.in" }, T - 2*q);
// o clip seguinte começa em T (corte duro no host)
```
Motion blur verdadeiro: componente `motion-blur` do registro (`data-hf-motion-blur`) no elemento que
move, ou a opção de render do motor. Blur de `filter` é uma aproximação sem direção: aceitável
em 2 q, feio em 6.

## T7 · Smear de chip → corte
**Anatomia:** chip parado · estica em X (×1,3) em 1 q · vira um risco de tela inteira (×6–9 em X,
blur) em 3 q · **corte duro por trás do risco, na batida**.
```js
tl.to("#fN-chip", { scaleX: 1.3, duration: 1*q, ease: "power2.in" }, T - 5*q);
tl.to("#fN-chip", { scaleX: 9, scaleY: .55, filter: "blur(14px)", duration: 4*q,
                    ease: "power4.in" }, T - 4*q);
// corte: o próximo clip começa exatamente em T
```

## T8 · Vazio → frase cômica → soco
**Anatomia:** 1 q de fundo vazio · palavras entram da direita com blur em cascata (8 q) · segura
encolhendo devagar 1,0→0,8 (~22 q) · encolhe mais rápido 3 q (antecipação) · **soco**: a frase final
entra a ×1,4 com um risco do acento (1 q) · assenta ×1,4→×0,85 em ~12 q.
```js
palavras.forEach(function(el, i){
  tl.fromTo(el, { x: 260, opacity: 0, filter: "blur(12px)" }, { x: 0, opacity: 1,
             filter: "blur(0px)", duration: 8*q, ease: "expo.out" }, T0 + q + i*2*q);
});
tl.to("#fN-frase", { scale: .82, duration: 26*q, ease: "sine.inOut" }, T0 + 10*q);
tl.to("#fN-frase", { scale: .3, opacity: 0, duration: 4*q, ease: "power4.in" }, SOCO - 4*q);
tl.fromTo("#fN-soco", { scale: 1.45, opacity: 0 }, { scale: 1.45, opacity: 1, duration: q }, SOCO);
tl.to("#fN-soco", { scale: .9, duration: 14*q, ease: "expo.out" }, SOCO + q);
```

## Eco (rastro de cópias) — usado em T3 e em entradas fortes
3–5 clones pré-criados no markup (`aria-hidden`), cada um com o mesmo tween atrasado 1 q e
opacidade .45 / .25 / .12. Sem callback, sem `Math.random`. É mais barato que o motion blur e dá o
"stutter" da referência.

## Onde cada T mora no arco
| Arco | Transições típicas |
|---|---|
| Hook → pivô | T1 |
| Pivô → capítulo 1 | T2 (nascer do chip) + T3 (mergulho no drop) |
| Entre capítulos | T4 (trocar de mundo) ou T6 (chicote na batida forte) |
| Chip → rajada de amostras | T7 |
| Rajada → payoff | T6 ou T4 + 1 q vazio |
| Payoff → lockup | T8 (o soco já é a entrada do lockup) |

## Como ficaram no caso YouTube (valores que passaram no render — `exemplos/youtube-15s/frames/`)
- **T1** (`01-busca`): câmera externa `#f01-cam` (origem no "play") por fora do palco do push. Antecipação
  `scale 1→1.1` em 5 q (`power2.in`), rajada `→7.5` + `rotationX 12, rotationZ −2, blur 14px` em 4 q
  (`power4.in`), opacidade a 0 nos 3 últimos. O risco é a **barra de progresso** sob a palavra: ela
  escala junto e atravessa. A cena seguinte começa 3 q antes do corte (host sobrepõe os clipes).
- **T2 nativo** (`02-porque`, `04-em-alta`): chip selecionado = cópia clara por cima do chip escuro
  (`tl.set` de opacidade por tique; roleta desacelerando 2,58→2,64→2,71→2,79→2,88→**3,00**). Na grade,
  o caça-níquel é por slot: `overflow:hidden` no slot, o card velho sobe −470 px com blur 6 px e o
  novo sobe de +470 px, 9 q `power3.inOut`, 1 q de defasagem entre slots.
- **T3** (`02-porque`): card da frente 2D com `transformPerspective 1500` à esquerda do centro
  (x −200); baralho num palco com `perspective-origin` no centro do card da frente, cards a
  `x −200+140k, z −110k, rotationY −30`. Mergulho em 13 q `power3.inOut` para `scale 1920/840`,
  `clipPath inset(round 18→0)`, pousando no drop.
- **T4 como recuo de câmera** (`04-em-alta`): a página inteira começa em `scale 1920/540` com o slot 0
  ocupando a tela (mesmo vídeo e timecode do frame anterior) e recua para 1 em 19 q `power3.inOut`;
  o raio do slot 0 vai de 0 a 16 px junto. Troca de mundo sem crossfade.
- **T6** (`04-em-alta`): página `x −2700, scaleX 1.08, blur 22px` em 7 q `power4.in`; corte duro no tempo.
- **T8** (`05`→`06`): palavras da direita com blur (8 q, 2 q de cascata), segura encolhendo
  1→0,86 em 1,45 s, encolhe a 0,3 em 5 q; soco com risco de tela inteira que se recolhe à barra cheia.
````

---
### ARQUIVO: referencias/componentes.md

````markdown
# Componentes — o kit neutro (versão da referência, na paleta da marca)

Use estes quando a marca não tem átomo nativo para o slot (ver `traducao-de-marca.md`). Medidas a
1920×1080; a 2560×1440 multiplique por 1,333. Tokens em variáveis CSS para trocar de marca sem tocar
no markup:

```css
:root{
  --mundo-escuro:#222222; --mundo-claro:#ECEBEC; --tinta:#FBFCFC; --tinta-2:#9A9A9A;
  --acento-a:#0CF5F5;  /* seleção/ferramenta */   --acento-b:#F06A6D; /* escolhido/CTA */
  --fonte:"Marca", system-ui, sans-serif;
  --raio-card:48px; --sombra-card:0 20px 60px rgba(0,0,0,.18), 0 4px 12px rgba(0,0,0,.06);
}
```

## Dispositivo de título — caixa de seleção com alças
```html
<div class="sel" id="fN-sel"><span class="sel-txt">Palavra-chave</span>
  <i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></div>
```
```css
.sel{position:relative;display:inline-block;padding:18px 44px;border:4px solid var(--acento-a);
     background:color-mix(in srgb,var(--acento-a) 15%,transparent);
     box-shadow:0 0 18px color-mix(in srgb,var(--acento-a) 45%,transparent)}
.sel-txt{font:700 88px/1 var(--fonte);color:var(--tinta);text-shadow:0 0 14px rgba(255,255,255,.35)}
.h{position:absolute;width:24px;height:24px;background:#fff;border-radius:4px;box-shadow:0 2px 6px rgba(0,0,0,.35)}
.tl{left:-14px;top:-14px}.tr{right:-14px;top:-14px}.bl{left:-14px;bottom:-14px}.br{right:-14px;bottom:-14px}
```
Entrada: a caixa "desenha" de 0,6→1 em escala X com inclinação −3°, as alças pipocam 1 q depois
(stagger 1 q). Uma caixa com acento A, a outra (se houver) com acento B e inclinação oposta.

## Chip de capítulo — pílula com ×
Markup e animação completos em `transicoes.md` (T2). CSS base:
```css
.chip{position:absolute;height:120px;width:520px;border-radius:999px;display:flex;align-items:center;
      justify-content:center;gap:28px;background:#fff;color:#2A2D33;
      box-shadow:0 18px 40px rgba(0,0,0,.14)}
.chip-janela{height:120px;overflow:hidden}
.chip-rolo span{display:block;height:120px;line-height:120px;font:600 34px var(--fonte);
                letter-spacing:.03em;text-transform:uppercase}
.chip-x{font:500 44px/1 var(--fonte)}
/* selecionado, mundo escuro */
.chip.sel-escuro{background:rgba(40,20,20,.55);color:var(--acento-b);border:3px solid var(--acento-b);
                 box-shadow:0 0 34px color-mix(in srgb,var(--acento-b) 55%,transparent)}
```
No mundo claro o chip é branco chapado, sem brilho. No escuro, o estado "selecionado" ganha o acento.

## Card de prova
```css
.card{position:absolute;overflow:hidden;border-radius:var(--raio-card);box-shadow:var(--sombra-card)}
.card img,.card video{width:100%;height:100%;object-fit:cover;display:block}
.card.escuro{border:14px solid #3A3A3A}   /* moldura/bisel no mundo escuro */
```
Raio ≈ 9% da largura (9:16 de 525 px → 48 px; 16:9 de 640 px → 32 px). Sombra difusa, nunca dura.

## Leque / baralho 3D
Um palco (`perspective:1600px`) e 8–14 cards com `transform-style:preserve-3d`; posições por índice
(`x:-i*70, z:-i*90, rotationY:-28+i*1.5`). O card que mergulha é um elemento 2D separado (T3).

## Carrossel de verticais
Três colunas de cards 9:16 (525×930 a 1080p) com passo 640 px; cada coluna é um trilho vertical
`y` que desliza um card inteiro por vez em 8 q (`power3.inOut`) com blur de 6 px só nos 3 q do
meio. O chip fica no vão central.

## Parede de cards (recuo de câmera)
Grade de 5×4 cards mistos (16:9 e 9:16), gap 28 px, num container que começa em escala 1,9 (um card
enche a tela) e recua para 1,0 em ~36 q (`power3.out`), derivando 40 px na diagonal até o fim.
Cards de fundo podem ser *greeked* (imagem desfocada) se não houver material real suficiente.

## Linha do tempo 3D
Plano inclinado (`rotationX:52°, rotationZ:-8°`, perspective 1400) com faixas de clips; cada clip
é uma barra arredondada com uma forma de onda em SVG (path pré-calculado, não aleatório). O plano
desliza em X continuamente durante o capítulo.

## Anotação rastreada
Círculo de traço 4 px na cor da tinta, 120 px, que desenha (`stroke-dashoffset`) em 6 q e segue um
ponto do footage por keyframes `x/y` escritos à mão (3–5 chaves), não por tracking automático.

## Cabeçalho-moldura
Rótulos nos cantos superiores (28 px, CAIXA ALTA, `--tinta-2`, margem 120/90 px): esquerda = o que é
o filme, direita = o ano/versão. Só na abertura e no fecho: é a moldura que diz "começou/acabou".

## Lockup
Card de identidade (foto/avatar numa moldura) + título de fecho + 2–3 linhas de CTA em cascata
(rótulo → seta → valor), entrando 2 q uma depois da outra com blur 8→0. Segura parado ≥ 1,5 s.

## Kit de marca completo (exemplo real)
`exemplos/youtube-15s/yt.css` é o kit do YouTube em escala de vídeo (~2,4× a UI): tokens dos dois
modos, vermelho #FF0033 e o gradiente da barra, busca, chips, thumbnail com selo de duração,
metadados de card, player (trilho, preenchimento, scrubber) e Inscrever-se/Inscrito. Para outra
marca, copie a estrutura do arquivo e troque os valores pelos medidos na F1.
````

---
### ARQUIVO: referencias/ritmo-e-audio.md

````markdown
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
````

---
### ARQUIVO: referencias/caso-youtube.md

````markdown
# Caso YouTube — o teste prático desta skill (29/09/2026)

Reel de 15 s sobre o YouTube, com o canal do Felipe (@FelipeBorgesFalaIA) como exemplo.
Projeto: `Desktop/Conteudo/Roteiro Videos/showreel/reel-youtube/` · entrega em `showreel/entrega/`.
Cópia executável do projeto em `exemplos/youtube-15s/` (host, 6 frames, `yt.css`, `cues.json`,
`ESTRUTURA.md`, `copy.txt`). Folha do filme: `exemplos/youtube-15s/folha-do-reel.jpg`.

## As três respostas (§0)
- **Chip:** os chips reais da aba Vídeos do canal ("Mais recentes", "Em alta", "Mais antigos").
- **Prova:** o conteúdo real do canal: thumbnails, trechos dos vídeos, 162.717 visualizações do nº 1.
- **Frase invertida (v1):** "não aperte o play" (digitada na busca) → "Aperte o play." (o soco). Na revisão, o hook virou "acesse Felipe Borges Fala IA!" (ver abaixo).

## Mapa (1920×1080 · 30 fps · 120 BPM · 1 tempo = 15 q)
| Frame | Janela | O que prova | Transição de saída |
|---|---|---|---|
| f01 busca | 0–2,1 | logo oficial 110 px + barra de busca; push 2× para a digitação em close (texto de 100 px) | T1: a barra de progresso sob "play" vira o risco |
| f02 porquê | 1,9–4,0 | "Vou te mostrar por quê." + chips na roleta, trava em 3,00 no clique | T3: baralho 3D das thumbs; o card da frente vira tela cheia **em 4,00 (drop)** |
| f03 player | 4,0–6,0 | 5 cortes duros na grade (4,00 / 4,50 / 5,00 / 5,25 / 5,50) com o cromo do player trocando | cromo some em 4 q |
| f04 em alta | 6,0–10,0 | câmera recua do vídeo para a grade da aba Vídeos; "Em alta" reordena a grade como **caça-níquel por slot**; o nº 1 soca, o contador rola até 162.717 | T6: chicote para a esquerda, corte em 10,00 |
| f05 só mais um | 10,0–12,0 | 1 q vazio; "só mais um vídeo…" + card nativo **"A seguir"** com o anel de contagem; música abafada | encolhe rápido (antecipação) |
| f06 aperte | 12,0–15,0 | soco "Aperte o play." com a barra cheia; cabeçalho real do canal; Inscrever-se → Inscrito + sino; assinatura **ícone + /@handle** | segura parado |

## Números
| Medida | Reel | Referência | Meta (escalada) |
|---|---|---|---|
| Amplitude | 22,1× (Roboto: 15,1×) | 5,3× | ≥ 3,7× |
| Quase-parada | 61% | 40% | ≥ 30% |
| Picos | 2 | 8 | ≥ 2 |
| Cortes duros | 6 | 34 | ≥ 3 |
| Cortes na batida (fase pelo bumbo) | **100%** | 94% | ≥ 70% |
| Render | 20 s por versão (M5, 4 workers) | — | — |

## O que funcionou (e virou regra na skill)
1. **Tradução de marca com átomos reais**: busca, chips, grade de thumbs com selo de duração e "▷ 7,7 mil · há 18 h", cromo do player, contador, "A seguir", Inscrever-se → Inscrito, assinatura ícone + /@handle. Sem logo animado: a identidade vem da UI.
2. **Os dois mundos = os dois modos da UI** (#0F0F0F / #FFFFFF). A troca acontece por condutor: o player encolhe e a grade clara aparece em volta (T4 como recuo de câmera numa "página").
3. **Caça-níquel nativo**: o T2 da referência (texto rolando no chip) virou a roleta da seleção dos chips e a grade rolando slot a slot no "Em alta". Mesmo mecanismo, átomo do YouTube.
4. **A barra de progresso como fio condutor** do filme: sublinha "play" no hook, vira o risco do zoom-through, aparece no player e volta **cheia** sob "Aperte o play.".
5. **Música medida, não escolhida no ouvido**: 6 trilhas Sonilo (1 crédito cada). Pedidas a 128/124/126/120/120/120 BPM, saíram ≈122/130/132/120*/120/96 (*com paradas irregulares). Escolhida a v5 (intro filtrada de 2 compassos, drop em 4,02 s, bumbo em todo tempo, parada no fim). Esticada com `atempo=0.99460` para 120,00 BPM e deslocada 0,107 s: drop em 4,000 s e todos os bumbos a ≤0,3 q da grade.

## O que deu errado e como foi corrigido
- **Escala do hook**: primeira versão com a barra inteira e o texto a 50 px (só ~20% da largura). Correção: plano de estabelecimento (logo + barra) e push 2× para a digitação em close.
- **Leque 3D escorrendo para fora do quadro**: o ponto de fuga precisa estar no card da frente e o card da frente à esquerda do centro; o baralho abre para a direita dentro do quadro.
- **Harness mente em clipes temporizados**: o `_dev/harness.html` não aplica `data-start` de filhos, e empilha todos os vídeos. Cromo/legendas por clipe → visibilidade via `tl.set` (vale no harness e no motor); vídeos se conferem no render real.
- **Medidor de ritmo enviesado**: a fase da grade estimada pelo fluxo total (hats + SFX) errava ~65 ms e reprovava cortes que estavam no bumbo. Correção: fase pelo grave (`batida.py` usa a banda <160 Hz) e `--t0` quando a trilha foi alinhada à mão.
- **Conformidade de marca** (achada pela pesquisa, `showreel/pesquisa/youtube-marca.md`): logo a 46 px (mínimo é 100 px), blur no logo durante o zoom-through (proibido: efeito) e o logo completo no fecho de um vídeo que divulga canal (a regra é ícone + "/@handle"). Corrigidos na v2: logo 110 px só com deslocamento/escala uniforme/fade; assinatura final = ícone 100 px + "/@FelipeBorgesFalaIA" em Roboto.
- **Dado real manda no roteiro**: o plano tinha um capítulo "Shorts", mas o canal tem 0 Shorts. Em vez de fabricar prova, os capítulos viraram os chips que o canal tem.

## Revisão do Felipe (29/09/2026): o hook virou CTA
O texto digitado passou de "não aperte o play" para **"acesse Felipe Borges Fala IA!"** (pedido dele:
"funciona mais o texto"). Consequências aplicadas: 5 palavras na grade (0,50 / 0,75 / 1,00 / 1,25 e
"IA!" na semicolcheia 1,375), um clique a mais na trilha, a barra de progresso sob "Fala IA!", campo
de busca 800→860 px para o texto de 1.299 px no close não deixar a lupa cortada, o close
recentralizado pela largura **medida no navegador** (`getBoundingClientRect` no harness) e a origem do
zoom-through movida para o centro de "Fala IA!". Lição: com hook em forma de CTA, "Vou te mostrar por
quê." passa a responder ao imperativo, e o arco fica CTA → prova → CTA (Aperte o play → Inscrito).
Aceite depois da revisão: amplitude 14,8×, 61% quase-parada, 100% dos cortes na batida (aprovado).

## Pendências e riscos (informar a pessoa)
- **YouTube Sans** é "Google Restricted" (todos os direitos reservados). Entregue em duas versões: YouTube Sans (fidelidade, uso interno) e Roboto (OFL, segura para publicar). Troca = 1 linha (`--fonte-display` em `yt.css`).
- **Uso de marca em mídia**: as diretrizes pedem aprovação (Brand Use Request Form) para logos/ícones/elementos de UI em mídia; o vídeo não pode sugerir parceria ou endosso. Decisão da pessoa.
- **Próximos passos naturais**: versão 9:16 (recompor, não cortar); motion blur de verdade (componente `motion-blur` do registro) no chicote e no mergulho; animações Lottie oficiais de like e sino (achadas em `assets/marca/ui/lottie/`).
````

---
### ARQUIVO: scripts/batida.py

````python
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
````

---
### ARQUIVO: scripts/grade.py

````python
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
````

---
### ARQUIVO: scripts/sfx.py

````python
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
````

---
### ARQUIVO: scripts/aceite.py

````python
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
````

---
### ARQUIVO: scripts/harness.html

````html
<!doctype html>
<!-- Harness de verificação de UM frame: http://localhost:8765/_harness.html?frame=07-resultados&t=1.2
     Monta o <template> do frame em #root (1920x1080), carrega o GSAP e faz seek(t) na timeline registrada.
     Fundo xadrez cinza/branco para enxergar transparência nos frames de câmera. -->
<html lang="pt-BR"><head><meta charset="utf-8"><base href="/">
<style>
  html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#888}
  body{background-image:linear-gradient(45deg,#777 25%,transparent 25%),linear-gradient(-45deg,#777 25%,transparent 25%),linear-gradient(45deg,transparent 75%,#777 75%),linear-gradient(-45deg,transparent 75%,#777 75%);background-size:80px 80px;background-position:0 0,0 40px,40px -40px,-40px 0}
  #stage{position:absolute;inset:0;width:1920px;height:1080px}
  .clip{position:absolute;inset:0}
</style>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
</head><body><div id="stage"></div>
<script>
(async function(){
  var q=new URLSearchParams(location.search);
  var frame=q.get('frame'), t=parseFloat(q.get('t')||'0'); var bg=q.get('bg'); if(bg){document.body.style.background='#'+bg;}
  window.__timelines = window.__timelines || {};
  var html=await (await fetch('/compositions/frames/'+frame+'.html')).text();
  var doc=new DOMParser().parseFromString(html,'text/html');
  var tpl=doc.querySelector('template');
  if(!tpl){ document.title='SEM TEMPLATE'; return; }
  var frag=document.importNode(tpl.content,true);
  // scripts clonados via importNode não executam: recriar
  var scripts=[...frag.querySelectorAll('script')].map(s=>{var n=document.createElement('script');n.textContent=s.textContent;s.remove();return n;});
  document.getElementById('stage').appendChild(frag);
  await document.fonts.ready;
  scripts.forEach(n=>document.body.appendChild(n));
  var id=document.querySelector('#stage #root')?.getAttribute('data-composition-id');
  var tl=window.__timelines[id];
  document.title=(tl?'OK ':'SEM TIMELINE ')+id+' t='+t+' dur='+(tl?tl.duration().toFixed(2):'-');
  if(tl){ tl.pause(0); tl.seek(t,false); }
  var vids=document.querySelectorAll('#stage video');
  vids.forEach(v=>{ var ms=parseFloat(v.getAttribute('data-media-start')||'0'); var st=parseFloat(v.getAttribute('data-start')||'0'); try{ v.pause(); v.currentTime=Math.max(0, ms + t - st); }catch(e){} });
  var tag=document.createElement('div'); tag.textContent=document.title; tag.style.cssText='position:absolute;left:16px;bottom:12px;font:600 26px/1 monospace;color:#fff;background:rgba(0,0,0,.6);padding:8px 12px;border-radius:8px;z-index:99999';
  document.body.appendChild(tag);
})();
</script></body></html>
````

---
### ARQUIVO: scripts/shoot.sh

````bash
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
````

---
### ARQUIVO: scripts/gerar-instalador.py

````python
#!/usr/bin/env python3
"""Gera o INSTALAR.md — a skill inteira num arquivo só, para copiar e colar.

Quem recebe o INSTALAR.md não precisa de git nem de terminal: copia o conteúdo
inteiro, cola no Claude Code, e o Claude recria cada arquivo no caminho certo.
A pasta exemplos/ e os JSON da perícia ficam de fora (vêm pelo git clone).

Rode de qualquer pasta; ele acha a raiz da skill sozinho. Rode de novo sempre
que mudar qualquer arquivo, senão o instalador fica defasado do repositório.
"""

import datetime
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "INSTALAR.md"
NOME = "showreel-interface"

# ordem fixa: o SKILL.md primeiro, porque é o que o Claude lê para entender o resto
ARQUIVOS = [
    "SKILL.md",
    "referencias/pericia-showreel-2025.md",
    "referencias/traducao-de-marca.md",
    "referencias/transicoes.md",
    "referencias/componentes.md",
    "referencias/ritmo-e-audio.md",
    "referencias/caso-youtube.md",
    "scripts/batida.py",
    "scripts/grade.py",
    "scripts/sfx.py",
    "scripts/aceite.py",
    "scripts/harness.html",
    "scripts/shoot.sh",
    "scripts/gerar-instalador.py",
    "README.md",
]

LINGUAGEM = {".md": "markdown", ".py": "python", ".html": "html", ".sh": "bash", ".json": "json"}


def versao():
    m = re.search(r'version:\s*"([^"]+)"', (RAIZ / "SKILL.md").read_text(encoding="utf-8"))
    return m.group(1) if m else "?"


def cerca(conteudo):
    """Cerca de crases mais longa do que qualquer cerca dentro do arquivo, para
    que os blocos ```bash do SKILL.md continuem válidos dentro do bloco maior."""
    maior = max((len(m) for m in re.findall(r"`{3,}", conteudo)), default=0)
    return "`" * max(4, maior + 1)


def main():
    partes = []
    partes.append(f"""# Instalar a skill `{NOME}` v{versao()}

> **Como usar este arquivo:** copie o conteúdo INTEIRO (do início ao fim) e cole
> numa conversa do Claude Code. A instrução para o Claude já está aqui embaixo.
> Depois que ele terminar, reinicie a sessão do Claude Code para a skill aparecer.

---

## Instrução para o Claude Code

Instale a skill abaixo na minha máquina. Faça exatamente isto:

1. Crie a pasta `~/.claude/skills/{NOME}/` (e as subpastas `scripts/` e `referencias/`).
2. Para cada bloco marcado com `### ARQUIVO: <caminho>`, grave um arquivo nesse
   caminho, relativo à pasta da skill, com **exatamente** o conteúdo que está
   dentro da cerca de código logo abaixo do título — sem acrescentar, remover
   ou reformatar nada.
3. Dê permissão de execução aos scripts:
   `chmod +x ~/.claude/skills/{NOME}/scripts/*.py ~/.claude/skills/{NOME}/scripts/*.sh`.
4. Confirme listando a árvore final e rodando
   `python3 ~/.claude/skills/{NOME}/scripts/batida.py --help`.
5. Me avise que preciso reiniciar a sessão para a skill carregar.

Não instale dependências sem me perguntar. As usadas são: `ffmpeg`,
`pip install numpy scipy opencv-python pillow fonttools`, `npx hyperframes` e a
skill `motion-por-referencia` (https://github.com/Felpborges/motion-por-referencia),
que o teste de aceite usa. A pasta `exemplos/` só vem pelo `git clone` do repositório.

---
""")
    for rel in ARQUIVOS:
        caminho = RAIZ / rel
        conteudo = caminho.read_text(encoding="utf-8")
        if not conteudo.endswith("\n"):
            conteudo += "\n"
        c = cerca(conteudo)
        lang = LINGUAGEM.get(caminho.suffix, "")
        partes.append(f"### ARQUIVO: {rel}\n\n{c}{lang}\n{conteudo}{c}\n\n---\n")

    partes.append(
        f"*Gerado por `scripts/gerar-instalador.py` em "
        f"{datetime.date.today().isoformat()} · {len(ARQUIVOS)} arquivos · "
        f"skill v{versao()}. Não edite este arquivo à mão — edite a skill e regenere.*\n"
    )
    SAIDA.write_text("".join(partes), encoding="utf-8")
    print(f"INSTALAR.md gerado: {len(ARQUIVOS)} arquivos, {SAIDA.stat().st_size} bytes")


if __name__ == "__main__":
    main()
````

---
### ARQUIVO: README.md

````markdown
# showreel-interface

Skill do Claude Code para criar **showreels, reels de marca e promos curtos (15s, 30s, 60s)** no
estilo "a interface narra": um hook montado palavra a palavra, **chips de UI** como títulos de
capítulo, o trabalho ou o produto invadindo a tela em **galerias de cards** (leque 3D, tela cheia ↔
card, grade que rola como caça-níquel), dois mundos alternados (escuro e claro), toda transição feita
por um elemento da cena e **cortes cravados na batida da música**.

O que a torna reusável: cada peça do filme é **traduzida para a UI nativa da marca** do projeto. No
YouTube, por exemplo, o título vira a barra de busca, o chip vira os filtros da aba Vídeos, a prova
vira a grade de thumbnails com selo de duração e o fecho vira o Inscrever-se → Inscrito com a
assinatura oficial (ícone + /@handle). A identidade sai da interface da marca, não de um logo animado.

Nasceu da perícia quadro a quadro do **SHOWREEL 2025 de Misha Ruchko**
([vimeo.com/1124592722](https://vimeo.com/1124592722)): estrutura, design e **movimento medido em
números** (amplitude 5,3×, 40% do filme em quase-parada, 94% dos cortes a ≤2 quadros da batida).
Deste repositório vêm só o método e as medidas; nenhum quadro, texto ou marca dele está aqui.

## Instalar

**Jeito 1 — clonar direto na pasta de skills:**

```bash
git clone https://github.com/Felpborges/showreel-interface.git ~/.claude/skills/showreel-interface
chmod +x ~/.claude/skills/showreel-interface/scripts/*.py ~/.claude/skills/showreel-interface/scripts/*.sh
```

**Jeito 2 — sem git:** abra o [`INSTALAR.md`](INSTALAR.md), copie o conteúdo inteiro e cole no
Claude Code. Ele cria os arquivos sozinho. (A pasta `exemplos/` e os JSON da perícia só vêm pelo
jeito 1.)

Depois de instalar, reinicie a sessão do Claude Code para a skill aparecer. Ela dispara sozinha com
pedidos como "faz um reel de 15 segundos sobre X", "showreel", "vídeo de marca curto" ou "vídeo
sobre o YouTube/Instagram/um app".

## O que precisa ter na máquina

| Para | Precisa de |
|---|---|
| medir a trilha, grades de quadros, teste de aceite | `ffmpeg` + `ffprobe`, `python3` com `numpy`, `scipy`, `opencv-python`, `pillow` |
| teste de aceite e portões | a skill [`motion-por-referencia`](https://github.com/Felpborges/motion-por-referencia) (usa o `pericia-movimento.py` e o `portoes.py` dela) + `pip install fonttools` |
| construir e renderizar (motor padrão) | Node + `npx hyperframes` |
| verificação por frame (`shoot.sh`) | Google Chrome (headless) |
| gerar a trilha | conta no Higgsfield (`sonilo_music`) — opcional; os efeitos sonoros o `sfx.py` sintetiza |

Skills que ela chama quando existem (opcionais): `motion-por-referencia`, `hyperframes` (e os
domínios `hyperframes-core`, `hyperframes-animation`, `hyperframes-cli`), `loop-de-design`,
`higgsfield-generate`. Sem elas a skill continua funcionando; faz aquela parte à mão.

## Estrutura

```
showreel-interface/
├── SKILL.md                               ← o mecanismo, o arco, os 6 slots, as fases e os portões
├── referencias/
│   ├── pericia-showreel-2025.md           ← a perícia completa (estrutura, design, movimento em números)
│   ├── pericia/                           ← medidas em JSON (quadros só na cópia local)
│   ├── traducao-de-marca.md               ← como vestir os 6 slots com a UI nativa de qualquer marca
│   ├── transicoes.md                      ← T1–T8 com anatomia, receita GSAP seek-safe e valores testados
│   ├── componentes.md                     ← kit neutro (seleção, chip, card, leque 3D, parede, lockup)
│   ├── ritmo-e-audio.md                   ← trilha escolhida por medição, grade de batidas, SFX, mixagem
│   └── caso-youtube.md                    ← o teste prático: decisões, números, erros e correções
├── scripts/
│   ├── batida.py                          ← BPM, fase pelo bumbo, compassos, drop, cortes × batida
│   ├── grade.py                           ← folha de contato com carimbo de tempo
│   ├── sfx.py                             ← kit de som sintetizado + mix por cues (−14 LUFS)
│   ├── aceite.py                          ← teste de aceite com metas escaladas pela duração
│   ├── harness.html + shoot.sh            ← fotografa um frame HyperFrames em vários instantes
│   └── gerar-instalador.py                ← regenera o INSTALAR.md
├── exemplos/youtube-15s/                  ← o projeto do teste (host, 6 frames, yt.css, cues, folha)
├── INSTALAR.md                            ← a skill num arquivo só, pra copiar e colar
└── README.md
```

## O teste: reel de 15s sobre o YouTube

Feito com a própria skill, para o canal [@FelipeBorgesFalaIA](https://www.youtube.com/@FelipeBorgesFalaIA):
busca "acesse Felipe Borges Fala IA!" → chips do canal → baralho 3D das thumbs reais → o card vira o
player no drop → a grade da aba Vídeos rola para "Em alta" → o nº 1 soca (162.717 visualizações) →
"só mais um vídeo…" → "Aperte o play." → Inscrito. Folha do filme em
[`exemplos/youtube-15s/folha-do-reel.jpg`](exemplos/youtube-15s/folha-do-reel.jpg).

| Medida | Reel | Referência | Meta |
|---|---|---|---|
| Amplitude (pico ÷ mediana) | 14,8× | 5,3× | ≥ 3,7× |
| Filme em quase-parada | 61% | 40% | ≥ 30% |
| Cortes na batida | 100% | 94% | ≥ 70% |

O exemplo mostra o código; os assets dele (thumbnails, trechos de vídeo, fontes, logos e trilha)
não fazem parte do repositório.

## Uso de marcas de terceiros

A skill manda ler as diretrizes da marca **antes** de desenhar: tamanho mínimo e respiro do logo, o
que o logo pode sofrer numa transição (só corte, fade, deslocamento e escala uniforme), a assinatura
de CTA regulamentar e a licença das fontes. No caso do YouTube: logo e ícone oficiais com no mínimo
100 px de altura e sem efeito, divulgação de canal com ícone + "/@handle", e **YouTube Sans é fonte
restrita do Google**, então o exemplo sai em duas versões (YouTube Sans e Roboto, a segura para
publicar). Usar logos e UI de uma marca em mídia pode exigir aprovação dela; essa decisão é de quem
publica o vídeo.

## Atualizar o INSTALAR.md

Mudou qualquer arquivo? Regenere o instalador antes de commitar:

```bash
python3 scripts/gerar-instalador.py
```

## Licença

MIT — Felipe Borges.
````

---
*Gerado por `scripts/gerar-instalador.py` em 2026-09-29 · 15 arquivos · skill v1.0. Não edite este arquivo à mão — edite a skill e regenere.*
