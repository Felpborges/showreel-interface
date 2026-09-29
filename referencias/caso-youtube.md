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
