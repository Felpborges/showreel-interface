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
