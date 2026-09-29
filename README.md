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
