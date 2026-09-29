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
