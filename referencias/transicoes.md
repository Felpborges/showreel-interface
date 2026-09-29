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
