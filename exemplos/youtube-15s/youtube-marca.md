# YouTube: marca, UI e números (pesquisa para o showreel de 15s)

*Coleta: 29/09/2026 · Local: Brasil (hl=pt-BR, gl=BR), sessão deslogada, viewport 1280×800 · Build medido do youtube.com: desktop `d57c41d2`, player `fb50cd46`, CSS `ytmainappweb.kevlar_base.T7R4-F9gvFk`.*

**Legenda:** **[VERIFICADO]** li em fonte primária ou medi nesta pesquisa (CSS baixado, valor computado no navegador, arquivo oficial conferido). **[INFERIDO]** dedução minha a partir das fontes. **[TERCEIROS]** número de fonte não oficial. **[OFICIAL]** número publicado pelo YouTube/Google.

**Método:** (1) páginas oficiais `brand.youtube` e zips oficiais; (2) HTML + CSS do youtube.com baixados com `curl` (User-Agent de Chrome desktop) e tokens extraídos; (3) valores *computados* medidos no navegador embutido (claro e escuro) em `/@YouTube/videos`, `/@YouTube/shorts`, `/results` e `/watch?v=jNQXAC9IVRw`; (4) números só de blog/fonte oficial, com terceiros marcados.

---

## 0. Cola rápida para o builder

```css
:root {
  /* marca (brand.youtube/color) */
  --yt-red: #FF0033;          /* YouTube Red: logo, ícone, barra de progresso, scrubber */
  --yt-almost-black: #212121; /* texto do logo full color / logo mono */
  --yt-white: #FFFFFF;
  /* UI (valores computados no youtube.com, 29/09/2026) */
  --yt-bg-light: #FFFFFF;   --yt-bg-dark: #0F0F0F;
  --yt-text-light: #0F0F0F; --yt-text-dark: #F1F1F1;
  --yt-text2-light: #606060; --yt-text2-dark: #AAAAAA;
  --yt-tonal-light: rgba(0,0,0,.05); --yt-tonal-dark: rgba(255,255,255,.10); /* chips, like, compartilhar, "Inscrito" */
  --yt-live: #E1002D;       /* AO VIVO (usado a 90%: rgba(225,0,45,.9)) */
  --yt-magenta: #FF2791;
  --yt-progress: linear-gradient(90deg, #FF0033 80%, #FF2791);
  --yt-brand-gradient: linear-gradient(45deg, #E1002D 30%, #E01378 85%);
  --yt-font-ui: Roboto, Arial, sans-serif; /* pilha idêntica à do youtube.com */
}
```

Fontes locais: `assets/fontes/fontes.css` (Roboto, livre). YouTube Sans / YouTube Display estão em `assets/fontes/restritas-google/` **só como referência** (licença restrita, ver §3).

---

## 1. Logos oficiais (arquivos baixados)

### 1.1 O que o site oficial oferece [VERIFICADO]
- `https://www.youtube.com/howyoutubeworks/resources/brand-resources/` redireciona para **`https://brand.youtube/`**. Subpáginas: `/youtube-logo`, `/youtube-icon`, `/color`, `/promoting-your-channel`, `/podcast-badges`, `/naming-and-third-party-content`, `/swag-and-merchandise`, `/entertainment-and-media`, `/api-and-device-partners`.
- Downloads: **"Core YouTube logo"** e **"Core YouTube icon"** (zips). As páginas Logo, Icon e Promoting apontam para URLs diferentes, mas os arquivos são **byte a byte idênticos** (SHA-256 do zip do logo `d4b6177d…`, do ícone `ca9b5104…`). Datas internas dos arquivos: **04/06/2025** (criados no Adobe Illustrator 29.0).
  - Logo: `https://www.gstatic.com/marketing-cms/52/7d/637fef5a4788a97747e6feabc4aa/youtube-logo.zip`
  - Ícone: `https://www.gstatic.com/marketing-cms/89/d9/cf95c4f345709f4998dc581221b0/youtube-icon.zip`
- Formatos dentro dos zips: `.ai` (PDF 1.6), `.eps`, `.pdf` (CMYK, impressão) e `.png` (digital). **Não há SVG.** Não existe seção nem download de **Shorts** no brand.youtube.

### 1.2 Arquivos entregues em `assets/marca/`

| Arquivo | O que é | Origem | Conferência |
|---|---|---|---|
| `yt-logo-fullcolor-almostblack.svg` / `.png` | Logo completo: ícone #FF0033 + texto #212121 (para fundo claro) | zip oficial (`yt_logo_fullcolor_almostblack_digital`) | PNG 1705×573 com alfa; cores dominantes #FF0033, #212121, #FFFFFF |
| `yt-logo-fullcolor-white.svg` / `.png` | Logo completo: ícone #FF0033 + texto #FFFFFF (fundo escuro) | zip oficial | PNG 1705×573; #FF0033, #FFFFFF |
| `yt-logo-mono-almostblack.svg` / `.png` | Logo monocromático #212121, triângulo vazado | zip oficial | PNG 1705×573; só #212121 |
| `yt-logo-mono-white.svg` / `.png` | Logo monocromático #FFFFFF, triângulo vazado | zip oficial | PNG 1705×573; só #FFFFFF |
| `yt-icon-red.svg` / `.png` | Ícone (play) #FF0033 com triângulo branco | zip oficial (`yt_icon_red_digital`) | PNG 1255×1075; #FF0033 + #FFFFFF |
| `yt-icon-mono-almostblack.svg` / `.png` | Ícone #212121, triângulo vazado | zip oficial | PNG 1255×1075 |
| `yt-icon-mono-white.svg` / `.png` | Ícone #FFFFFF, triângulo vazado | zip oficial | PNG 1255×1075 |
| `yt-logo-site-header-as-served.svg` | Logo do cabeçalho do youtube.com, 93×20, como servido (só removi o `id` interno) | `<svg>` inline no HTML de `https://www.youtube.com/` | XML válido; ícone `#FF0033`; texto sem `fill` (o site pinta via CSS) |
| `yt-logo-site-header-currentcolor.svg` | Mesmo SVG, com o grupo do texto em `fill="currentColor"` | idem (só troquei o atributo de cor do grupo; paths intactos) | no site o texto sai **#000** no claro e **#FFF** no escuro (computado) |
| `yt-shorts-icon-red.svg` | Ícone do Shorts (vermelho #f03 + triângulo branco), 24×24 | DOM do youtube.com: cabeçalho da prateleira de Shorts na busca | renderizado e conferido |

**Como os SVGs oficiais foram feitos [VERIFICADO]:** o `.ai` oficial é PDF; li o *content stream* da página (FlateDecode), converti os operadores de caminho (`m l c v y h re f`) para `path` SVG aplicando só a matriz do próprio arquivo e a inversão do eixo Y. Nenhuma coordenada foi redesenhada. viewBox = ArtBox do Illustrator (limites exatos do desenho), com origem normalizada por `translate`. **Prova:** renderizei cada SVG e comparei pixel a pixel com o PNG oficial correspondente: diferença média de 0,2 a 4 em 255, só nas bordas (antialias). O triângulo vazado das versões mono confere. Os PNG oficiais trazem a margem do artboard (logo: 818×275 pt exportado a 150 dpi = 1705×573 px); os SVG vêm recortados no desenho, então a área de respiro (§7) tem de ser respeitada na composição.

**Geometria útil (medida no vetor oficial) [VERIFICADO]:**
- Logo completo: 621,0 × 138,1 (proporção **4,497 : 1**). Ícone dentro do logo: 197,2 × 138,1; vão ícone→"Y" = 19,1 (≈ 14% da altura do logo).
- Ícone: 396,5 × 277,8 (proporção **1,4275 : 1**). Triângulo: largura = 37,0% da altura do ícone; altura = 42,9%.
- O logo do cabeçalho do site é uma versão de UI com proporções próprias (ícone 29×20 = 1,45 : 1). Para marca, prefira os SVGs oficiais convertidos.

**Shorts [VERIFICADO + INFERIDO]:** não há logo do Shorts para download oficial (nem lockup "ícone + Shorts"). O que o próprio youtube.com usa é o ícone vermelho 24 px ao lado do título em texto (ex.: "Últimos Shorts em: YouTube Brasil", Roboto 20px/700). Não montei lockup: seria criar logo.

### 1.3 Ícones de UI e animações oficiais (`assets/marca/ui/`)
Copiados do DOM do youtube.com em 29/09/2026 (paths intactos; `fill="currentColor"` para herdar a cor do texto): `ui-verified-badge.svg` (selo verificado), `ui-views-play-outline.svg` (▷ antes das views), `ui-like-outline.svg`, `ui-live-broadcast.svg` (ícone do selo AO VIVO, 12×12), `ui-shorts-outline.svg` (menu lateral), `ui-home.svg`, `ui-subscriptions.svg`, `ui-kebab-menu.svg` (⋮ dos cards). Todos renderizados e conferidos.

`assets/marca/ui/lottie/`: animações **oficiais** do YouTube (Lottie 5.12.1, 60 fps, 120 quadros, 48×48), achadas no bundle JS do site:
- `animated_like_icon_light_v5.json` / `_dark_v5.json` ← `https://www.gstatic.com/youtube/img/lottie/animated_like_icon/`
- `subscribe_action_bell_icon_light_v4.json` / `_dark_v4.json` ← `https://www.gstatic.com/youtube/img/lottie/subscribe_action/`

Status de uso: ícones de UI e Lottie são elementos da interface do YouTube; servem de referência de desenho e de tempo de movimento. Colocá-los num vídeo publicado cai na mesma regra de "Entretenimento e mídia" da §7 [INFERIDO].

Assinatura de movimento (lida dos keyframes) [VERIFICADO]:
- **Like:** antecipação em 3 quadros (encolhe a 30% e gira 6°), pop de 50% → **120%** com giro 15° → −10° em ~0,22 s (quadros 4→17), assenta em 100% no quadro 37 (0,62 s) e para de girar no quadro 60 (1,0 s); partículas de explosão entre 0,13 s e 0,6 s nas cores **#FF0033 e #FF2791**.
- **Sino:** pêndulo amortecido 0 → −15° → **40°** → −30° → 15° → −5° → 2° → −0,5° → 0 em **1,25 s**, com o badalo oscilando em contrafase.

---

## 2. Cores e tokens

### 2.1 Paleta oficial da marca [VERIFICADO, brand.youtube/color]
| Nome oficial | Hex |
|---|---|
| YouTube Red | **#FF0033** |
| Almost Black | **#212121** |
| "Almost White" (a página usa esse nome) | **#FFFFFF** |

Regras associadas: o logo full color combina o ícone vermelho com texto #212121 (fundo branco/imagem clara) ou #FFFFFF; o triângulo do ícone vermelho é sempre branco.

### 2.2 O vermelho mudou em 2024–2025 [VERIFICADO]
- **Antes:** #FF0000 (vermelho puro, desde o logo de 2017). Continua no CSS como legado: `--yt-deprecated-brand-youtube-red: #f00` (também `--yt-deprecated-brand-medium-red: #c00`).
- **Agora:** **#FF0033**, mais frio. A página do logo marca como NOVO que o vermelho do ícone foi atualizado para #FF0033; os arquivos do zip são de 04/06/2025. Na UI a troca chegou no fim de 2024 e foi explicada pelo time de design em fev/2025 (Google Design; 9to5Google 12/02/2025; Android Authority 15/02/2025): o vermelho antigo parecia alto demais em momentos-chave, puxava para laranja em algumas telas e causava *burn-in* em TVs.
- **Gradiente vermelho → magenta** entrou junto: barra de progresso, botões de Gostei e Inscrever-se, selo Premium, anel de ao vivo e ícones de tópicos; o gradiente vai a **45° com o magenta à direita** (sentido de avanço). O vermelho puro fica reservado a marcas, identidade e momentos-assinatura da UI.
- Na UI atual o vermelho de marca é o token `--yt-sys-color-baseline--static-brand-red: #f03` (= #FF0033), usado no player (`.ytp-swatch-background-color`), no scrubber (computado: `rgb(255, 0, 51)`) e no ícone do cabeçalho.

### 2.3 Tokens da UI atual (youtube.com) [VERIFICADO]
Os antigos `--yt-spec-*` **não existem mais como variáveis nomeadas** no CSS atual (só sobrou 1 referência a `--yt-spec-text-primary` e aliases `--premium-yt-spec-*`). O sistema agora tem tokens nomeados `--yt-sys-color-baseline--*` (definidos em `html` e `html[dark]`) e tokens com nome em hash (`--t…`) que os componentes realmente usam. Onde os dois divergem, vale o **computado** (coluna da direita). Os valores são [VERIFICADO]. A correspondência "nome legado → atual" da 1ª coluna é por papel e valor [INFERIDO]; só estes nomes `yt-spec` aparecem ligados a um token em hash pelos aliases `--premium-yt-spec-*`: base-background, raised-background, additive-background, outline, text-primary, text-secondary, button-chip-background-hover e themed-green.

| Papel (nome legado → atual) | Claro | Escuro | Computado na página |
|---|---|---|---|
| base-background → `--yt-sys-color-baseline--base-background` | #FFFFFF | #0F0F0F | fundo `ytd-app`: #FFFFFF / #0F0F0F |
| raised-background → `…--raised-background` | #FFFFFF | #212121 | — |
| menu-background → `…--menu-background` | #FFFFFF | #282828 | — |
| text-primary → token hash `--tffc2fd3a644f6275` (o nomeado `…--text-primary` declara #030303 / #FFF) | #0F0F0F | #F1F1F1 | títulos: #0F0F0F / #F1F1F1 |
| text-secondary → `…--text-secondary` | #606060 | #AAAAAA | metadados: #606060 / #AAAAAA |
| text-disabled → `…--text-disabled` | #909090 | #717171 | — |
| badge-chip-background → `…--additive-background` | rgba(0,0,0,.05) | rgba(255,255,255,.10) | chip inativo, like, compartilhar |
| 10-percent-layer → `…--tonal-background` / `…--button-chip-background-hover` | rgba(0,0,0,.10) | rgba(255,255,255,.10) / .20 | hover de chips/botões |
| outline → `…--outline` | rgba(0,0,0,.10) | rgba(255,255,255,.20) | — |
| inverted-background (chip ativo, Inscrever-se) → `…--inverted-background` | #0F0F0F | #F1F1F1 | Inscrever-se: fundo #0F0F0F texto #F1F1F1 (claro) · fundo #F1F1F1 texto #0F0F0F (escuro) |
| static-brand-red → `…--static-brand-red` | #FF0033 | #FF0033 | scrubber `rgb(255,0,51)` |
| `…--red-indicator` | #E1002D | #E1002D | AO VIVO: rgba(225,0,45,.9) |
| `…--overlay-background-brand` | rgba(225,0,45,.9) | idem | — |
| `…--brand-red-contrast` / `…--error-indicator` | #C30027 | #FF5577 | — |
| `…--red-3` / `…--red-4` | #FF5577 / #FE2A54 | #FF0033 / #FE2A54 | — |
| `…--static-magenta` | #FF2791 | #FF2791 | fim do gradiente da barra |
| `…--call-to-action` (links, azul) | #065FD4 | #3EA6FF | — |
| `…--themed-green` | #107516 | #2BA640 | — |
| `…--wordmark-text` | #000000 | #FFFFFF | texto do logo do cabeçalho: #000 / #FFF |
| `…--overlay-text-primary` / `…--overlay-text-secondary` | #FFF / rgba(255,255,255,.7) | idem | — |
| `…--overlay-background-medium` | rgba(0,0,0,.6) | idem | selo de duração |
| `…--static-black` | #0F0F0F | #0F0F0F | — |

Fonte dos tokens: `https://www.youtube.com/s/_/ytmainappweb/_/ss/k=ytmainappweb.kevlar_base.T7R4-F9gvFk.L.B1.O/am=AAAAAALAEACbBQ/d=0/rs=AGKMywFI1mNEk2Fsfs8x3FIHeNq221rt-Q` (3 MB; blocos `html{…}` e `html[dark]{…}` com 154 tokens `--yt-sys-color-baseline--*` + 5 `--yt-deprecated-*`). Player: `https://www.youtube.com/s/player/fb50cd46/www-player.css`.

### 2.4 Gradientes literais do CSS [VERIFICADO]
| Onde | Valor |
|---|---|
| Barra de progresso do player (`.ytp-play-progress`, computado) | `linear-gradient(90deg, #f03 80%, #ff2791)` |
| Barra "continuar assistindo" na thumbnail, barras de capítulo | mesmo gradiente acima |
| Botão com gradiente de marca (`…BrandGradient.…Filled`) | `linear-gradient(45deg, #e1002d 30%, #e01378 85%)`, texto #FFF |
| Anel de ao vivo no avatar (`.ytSpecAvatarShapeLiveRing:after`) | `linear-gradient(to top right, #e1002d 60%, #e01378 85%)`, anel de 2px |
| Chip "personalizado por IA" | `linear-gradient(to right, #7f0e7f, #007a65)` |

---

## 3. Tipografia

| Uso no youtube.com | Família | Evidência |
|---|---|---|
| Praticamente toda a UI | **Roboto, Arial, sans-serif** | 2.453 declarações no CSS; `--yt-ref-typography-values--font-family: Roboto,Arial,sans-serif`; computado em títulos, chips e botões [VERIFICADO] |
| Títulos "display" (cabeçalhos de página, promoções, landing pages) | **"YouTube Sans", Roboto, sans-serif** | `--yt-ref-typography-values--display-font-family`; 152 declarações; pesos 300 (light) e 700 (heavy) [VERIFICADO] |
| Player (tempo e textos do player) | "YouTube Noto", Roboto, Arial | computado em `.ytp-time-display` [VERIFICADO] |
| "Marquee" | "YouTube Marquee Beta", Roboto | token `--yt-ref-typography-values--marquee-font-family` [VERIFICADO] |
| Identidade de marca 2026 | **YouTube Display** (Sharp Type) | lançada com a nova identidade visual em jan/2026 (Marketing Dive 20/01/2026; Design Compass 28/01/2026) |

Escala tipográfica da UI (tokens `--yt-ref-typography-values--*`, html font-size = 10px) [VERIFICADO]: body/action XS 10 · S 12 · M 14 · L 16 · XL 18 px; title S 18 · M 20 · L 22; headline XS 18 · S 20 · M 24 · L 32; display XS 24 (28) · S 32 (36) · M 40 (48) · L 56 (64). Pesos: 300/400/500/600/700/900.

Medidas computadas: título do card 16px/500 (entrelinha 22px) · metadados 14px/400 (20px) · título na página de vídeo 20px/700 (28px) · nome do canal 16px/500 · "X mi de inscritos" 12px/400 · chips e botões 14px/500 · selo de duração 12px/500 · cabeçalho de prateleira 20px/700.

**YouTube Sans e YouTube Display são servidas publicamente pelo Google Fonts** (é assim que o youtube.com carrega: `//fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=YouTube+Sans:wght@300..900`), mas o CSS delas aponta para `https://fonts.google.com/license/googlerestricted`, que diz que **essas fontes não são open source** e manda procurar alternativas livres no fonts.google.com. Metadados dos arquivos: "Copyright 2019 Google LLC. All Rights Reserved." (YouTube Sans) e "Copyright 2025 Google LLC. All Rights Reserved." (YouTube Display), sem campo de licença. **Status: proprietárias, sem licença para terceiros.** Baixei porque o briefing pediu, mas separei em `restritas-google/` para uso só como referência visual.

**Roboto: a licença atual é SIL Open Font License 1.1, não Apache 2.0.** O arquivo baixado (v3.015, 2026) declara `https://openfontlicense.org` e o repositório `google/fonts` lista Roboto em `/ofl/roboto` (licença "OFL"). Versões antigas eram Apache 2.0. As duas permitem uso comercial em vídeo.

### Arquivos em `assets/fontes/`
| Arquivo | Conteúdo | URL de origem |
|---|---|---|
| `roboto-variavel-latin.woff2` (37,5 KB) | Roboto variável, eixo wght 100–900 (cobre 400/500/700/900) | `https://fonts.gstatic.com/s/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBHMdazQ.woff2` |
| `roboto-variavel-latin-ext.woff2` (24,4 KB) | idem, subconjunto latin-ext | `…/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3KUBHMdazTgWw.woff2` |
| `fontes.css` | `@font-face` locais da Roboto (`font-display: block`) | gerado da CSS API `css2?family=Roboto:wght@400;500;700;900` |
| `restritas-google/youtube-sans-variavel-latin(-ext).woff2` | YouTube Sans v32, variável wght 300–900 (nome interno "YouTube Sans Light 48pt") | `https://fonts.gstatic.com/s/youtubesans/v32/Qw38ZQNGEDjaO2m6tqIqX5E-AVS5_rSejo46_PCTRspJ0OosolrBEJL3HO_T7fHoCVHx.woff2` (latin) e `…HO_d7fHoCVHxtvY.woff2` (latin-ext) |
| `restritas-google/youtube-display-variavel-latin(-ext).woff2` | YouTube Display v3 (versão 1.009), variável wght 400–900 | `https://fonts.gstatic.com/s/youtubedisplay/v3/lW-mwj8dK3Xd92-ClMRhI7sbzFe6KerlFAke7w.woff2` (latin) e `…J-rlFAke76nu.woff2` (latin-ext) |
| `restritas-google/fontes-restritas.css` | `@font-face` das duas, com o aviso de licença | — |

Pedi os pesos 400/500/700/900: a API devolve **o mesmo arquivo variável** para todos. **PT-BR [VERIFICADO]:** o subconjunto *latin* das três famílias contém ç ã õ é ê á í ó ú à â ô ü, maiúsculas, º ª € R$ … “ ” – — • · (checado no `cmap` e num specimen renderizado nos pesos 400–900). O *latin-ext* complementa acentos fora do Latin-1 (não é necessário para português, mas foi incluído).

Existem ainda as famílias restritas "YouTube Sans Dark" (400) e "YouTube Marquee" / "YouTube Marquee Beta" (400) no Google Fonts; não baixei. [VERIFICADO]

Observação visual [INFERIDO]: YouTube Display é condensada e pesada, parente direta das letras do logo; YouTube Sans é geométrica e mais larga. O wordmark do logo **não é uma fonte**: é desenho (use os arquivos de logo).

---

## 4. Geometria dos componentes da UI (2025–2026)

*"Computado" = medido com `getComputedStyle` no navegador embutido em 29/09/2026. "CSS" = lido no CSS baixado (pode incluir variantes em teste).*

| Componente | Medidas e cores | Fonte |
|---|---|---|
| Base | `html{font-size:10px}` (1rem = 10px); corpo em Roboto | computado |
| Cabeçalho | altura 56px (`--ytd-toolbar-height`); logo renderizado 93×20 px; "BR" em 10px #606060 | CSS + computado |
| Grade de vídeos | card 347×273 px em janela de 1280px; espaço entre cards 16px (`--ytd-rich-grid-item-margin`) | computado + CSS |
| Thumbnail | 16:9 (`padding-top:56.25%`); raio **12px** (grande, computado na grade); 8px (médio); 4px (pequeno) | computado + CSS |
| Selo de duração | fundo **rgba(0,0,0,.6)**, texto #FFF, Roboto **12px/500**, entrelinha 18px, padding 1px 4px, raio **4px**, altura 20px; distância da borda 2/4/8px conforme o tamanho | computado + CSS |
| Selo de duração (variante nova em teste) | rgba(0,0,0,.3) + blur 8px, raio 10px, padding 0 6px | CSS |
| Barra "continuar assistindo" na thumb | 4px; trilho #909090 (claro) / #717171 (escuro); preenchimento com o gradiente vermelho→magenta | CSS |
| Chips de filtro | altura **32px**, raio **8px**, padding 0 12px, Roboto 14px/500 (entrelinha 20px). **Selecionado:** claro #0F0F0F com texto #F1F1F1 · escuro #F1F1F1 com texto #0F0F0F. **Não selecionado:** claro rgba(0,0,0,.05) com texto #0F0F0F · escuro rgba(255,255,255,.1) com texto #F1F1F1. Espaço 12px na barra de filtros do feed (1º chip a 24px da borda); 8px nas nuvens de chips (`yt-chip-cloud-renderer`) | computado (cores, medidas) + CSS (espaços) |
| Botão Inscrever-se | pílula **40px** de altura, raio **20px**, padding 0 16px, Roboto 14px/500; claro fundo **#0F0F0F** texto **#F1F1F1**; escuro fundo **#F1F1F1** texto **#0F0F0F**; largura de "Inscrever-se" ≈ 109px | computado (canal e /watch) |
| Estado "Inscrito" | mesma pílula em estilo tonal: rgba(0,0,0,.05) / rgba(255,255,255,.1), texto #0F0F0F / #F1F1F1, com ícone de sino e seta | [INFERIDO] do CSS (não medi logado) |
| Animação do Inscrever-se | há wrappers `yt-smartimation` / `ytAnimatedAction*` para uma animação Lottie sobre o botão | CSS [VERIFICADO]; gatilho exato [INFERIDO] |
| Gostei / Não gostei | pílula segmentada de 40px; esquerda raio 20px 0 0 20px, direita 0 20px 20px 0; fundo rgba(0,0,0,.05); texto #0F0F0F 14px/500 ("19 mi"); divisória 1px × 24px a 8px do topo, rgba(0,0,0,.2); "Não gostei" só ícone, 56px | computado |
| Compartilhar / Salvar | pílula tonal 40px, raio 20px, rgba(0,0,0,.05) | computado |
| Página de vídeo | título 20px/700 (28px); canal 16px/500; "6,64 mi de inscritos" 12px/400 #606060; avatar 40px redondo; caixa de descrição rgba(0,0,0,.05) com raio 12px | computado |
| Barra de busca (escuro) | campo 40px com borda 1px **#303030**, fundo **#121212**, raio 40px 0 0 40px; botão da lupa **64×40px**, fundo rgba(255,255,255,.08), borda #303030, raio 0 40px 40px 0 | computado |
| Barra de busca (claro) | campo #FFF, borda #C6C6C6, sombra interna 0 1px 2px #EEE; botão #F8F8F8 com borda #D3D3D3; foco com borda #1C62B9; texto 16px/400; botão de voz redondo ao lado | CSS |
| Barra de busca (variante "unificada" em teste) | 48px, pílula inteira raio 40px, borda rgba(0,0,0,.1) | CSS (não estava ativa na sessão) |
| Player: barra de progresso (player novo "delhi-modern") | contêiner 6px; trilho rgba(40,40,40,.6) comprimido a 66,7% (≈4px parado, 6px no hover), ponta esquerda com raio 3px; assistido `linear-gradient(90deg,#f03 80%,#ff2791)`; carregado rgba(255,255,255,.4) | computado |
| Player: scrubber | círculo **12px #FF0033**; no hover cresce ×1,67 (≈20px) em 0,2 s `cubic-bezier(.05,0,0,1)` | computado + CSS |
| Player: controles | barra inferior 56px, recuo 12px; play/pause círculo 40px rgba(0,0,0,.3); pílula do tempo 40px, raio 28px, rgba(0,0,0,.3), 14px/500 #EEE ("0:01 / 0:19") | computado |
| Player clássico (legado no CSS) | barra 5px; scrubber 13px, hover ×1,54 | CSS |
| Selo verificado | nos cards 14×14px na cor do texto secundário (#606060 / #AAAAAA); no cabeçalho do canal 24px | computado |
| Views na grade (formato 2026) | ícone ▷ 12px + "2,2 mi" (aria: "2,2 milhões de visualizações") + "há 1 mês"; separadores com margem 0 4px | computado |
| Selo AO VIVO | fundo **rgba(225,0,45,.9)**, texto #FFF "AO VIVO", 12px/500, entrelinha 18px, raio 2px (4px na thumbnail), altura 18px, com ícone de transmissão 12px | computado + CSS |
| Avatar ao vivo | anel 2px com `linear-gradient(to top right,#e1002d 60%,#e01378 85%)` a 4px do avatar; etiqueta #E1002D, raio 4px, 10px/500 maiúsculo | CSS |
| Card de Shorts | proporção **2:3** na grade do canal e na busca (208×311 / 216×324 px), raio **8px**; título 16px/500 #0F0F0F e "44 mil visualizações" 14px/400 #606060 **abaixo** da imagem; selo "Novo" rgba(0,0,0,.6) | computado |
| Card de Shorts (variante com texto sobre a imagem) | texto branco sobre degradê rgba(0,0,0,.6)→transparente, padding 8px; título 14px/500 e views 12px/400 com sombra 0 1px 2px rgba(0,0,0,.8). Existe ainda variante 9:16 (`padding-top:178%`) | CSS |
| Prateleira de Shorts | ícone vermelho 24px + título 20px/700 ("Últimos Shorts em: …") | computado |
| Tela final (end screen) | elementos com borda 1px rgba(255,255,255,.4) e sombra 0 0 4px rgba(0,0,0,.5); canal/inscrever-se em círculo; vídeo com duração rgba(0,0,0,.8) raio 2px. Regras: últimos 5 a 20 s, até 4 elementos em 16:9, vídeo com no mínimo 25 s | CSS + Ajuda do YouTube |

**Formatos de contagem em PT-BR vistos na página [VERIFICADO]:** "46,4 mi de inscritos" · "1,6 mil vídeos" · "438 mi de visualizações" · "44 mil visualizações" · "20 mil visualizações" · "há 21 anos" · "há 1 mês" · "há 7 dias" · "há 22 h" · "há 2 sem." (busca, abreviado) · "3,6 mi • há 2 sem." · "19 mi" (likes) · "687 assistindo" · "7,1 mil assistindo" · "Novo" · "AO VIVO". Na página de vídeo, visualizações e likes usam **números que rolam dígito a dígito** (animação de contador) [VERIFICADO no DOM].

---

## 5. Números do YouTube

| Métrica | Valor | Data | Fonte | Tipo |
|---|---|---|---|---|
| Visualizações diárias de Shorts | **mais de 200 bilhões por dia** (média) | anunciado em 18/06/2025; repetido em 21/01/2026 | https://blog.youtube/news-and-events/neal-mohan-cannes-2025/ · https://blog.youtube/inside-youtube/the-future-of-youtube-2026/ | [OFICIAL] |
| Pagamentos | **mais de US$ 100 bilhões** a criadores, artistas e empresas de mídia nos 4 anos anteriores | anunciado no Made on YouTube (16/09/2025); repetido em 21/01/2026 | https://blog.youtube/inside-youtube/the-future-of-youtube-2026/ · https://www.cnbc.com/2025/09/16/youtube-creators-pay.html | [OFICIAL] |
| Vídeos enviados | **mais de 20 milhões por dia** (média de mar/2025) | 23/04/2025 | https://blog.youtube/news-and-events/happy-birthday-youtube-20/ · https://blog.youtube/press/ | [OFICIAL] |
| Acervo total | **mais de 20 bilhões de vídeos** | 23/04/2025 | idem | [OFICIAL] |
| Horas enviadas por minuto | mais de 500 h/min | último dado oficial: 2019–2020 | https://blog.youtube/news-and-events/appealspeech/ (jul/2020) | [OFICIAL, DESATUALIZADO] |
| Horas assistidas por dia | **mais de 1 bilhão de horas por dia só em TVs** | 18/06/2025 | https://blog.youtube/news-and-events/neal-mohan-cannes-2025/ | [OFICIAL] (não há total global atualizado) |
| Podcasts | 1 bilhão de pessoas por mês assistem a podcasts no YouTube | 18/06/2025 | idem | [OFICIAL] |
| Usuários logados por mês | "mais de 2 bilhões" é o último número oficial amplo (2019); Shorts: mais de 2 bilhões de logados/mês (Google, resultado do 2º tri de 2023) | 2019 / 25-07-2023 | https://www.techradar.com/news/over-2-billion-youtube-users-are-logged-in-and-watching-every-month · https://techcrunch.com/2023/07/25/google-says-2-billion-logged-in-monthly-users-are-watching-youtube-shorts/ | [OFICIAL, antigo, via imprensa] |
| Alcance global estimado | 2,53 bilhões (alcance publicitário) | jan/2025 | https://datareportal.com/essential-youtube-stats | [TERCEIROS] |
| Brasil, alcance | **150 milhões** (alcance publicitário; 70,4% da população; +6 mi em 1 ano) | out/2025 | https://datareportal.com/reports/digital-2026-brazil | [TERCEIROS] |
| Brasil, TV | **80 milhões** de pessoas assistem ao YouTube na TV conectada; TV passou o celular como tela principal em casa (53% da audiência em CTV) | dados de abr/2025; post de 09/10/2025 | https://blog.youtube/intl/pt-br/news-and-events/youtube-brandcast-2025-tv-conectada-brasil/ | [OFICIAL] (a fatia de 53% é Kantar) |
| Primeiro vídeo | "Me at the zoo", enviado em **23/04/2005 às 20:31:52 (PDT)**, 19 s, 438.280.528 views em 29/09/2026 | — | metadados da própria página `https://www.youtube.com/watch?v=jNQXAC9IVRw` | [VERIFICADO] |
| 20 anos | celebrados em **2025**; post oficial em 23/04/2025 (aniversário do primeiro envio) | 23/04/2025 | https://blog.youtube/news-and-events/happy-birthday-youtube-20/ | [OFICIAL] |
| Engajamento | mais de 3,5 bilhões de likes por dia e mais de 100 milhões de comentários por dia (2024); mais de 300 clipes com 1 bilhão de views | 23/04/2025 | idem | [OFICIAL] |
| Receita 2025 | mais de US$ 60 bilhões (anúncios + assinaturas; 1ª vez que a Alphabet abriu o total) | resultado do 4º tri de 2025, divulgado em fev/2026 | https://www.tubefilter.com/2026/02/05/alphabet-q4-2025-youtube-earnings-revenue-60-billion/ | [OFICIAL via imprensa] |

Os 5 mais fortes para tela: 200 bilhões de views/dia no Shorts · US$ 100 bi pagos em 4 anos · 20 milhões de vídeos por dia · 20 bilhões de vídeos no total · 1 bilhão de horas por dia na TV (e, para o Brasil, 80 milhões na TV / 150 milhões de alcance). Não achei número oficial atual de usuários mensais: não usar "2,7 bi" como oficial.

---

## 6. Linguagem visual: os átomos que fazem parecer YouTube

1. **Botão play vermelho** (ícone oficial #FF0033, triângulo branco, 1,4275 : 1). É o átomo nº 1; logo completo só quando fizer sentido (ver §7).
2. **Barra de progresso** fina com trilho escuro translúcido, preenchimento `#FF0033 → #FF2791` (o magenta só nos últimos 20%) e **scrubber redondo #FF0033** que cresce no hover.
3. **Thumbnail 16:9 com raio 12px + selo de duração** no canto inferior direito (preto 60%, texto branco 12px/500, raio 4px).
4. **Card da grade:** thumbnail → título 16px/500 em até 2 linhas → metadados cinza 14px ("canal ✓ · ▷ 2,2 mi · há 1 mês") → menu ⋮. No feed da home entra ainda o avatar redondo do canal à esquerda do título [INFERIDO: o feed deslogado veio vazio, não medi].
5. **Chips de filtro** (32px, raio 8px): o ativo é o único preto/branco invertido; os outros em cinza 5%.
6. **Inscrever-se** (pílula 40px preta no tema claro) que vira **"Inscrito" com sino** tonal; o sino balança (pêndulo amortecido de 1,25 s, Lottie oficial).
7. **Gostei** em pílula segmentada tonal com contador ("19 mi"); o like dá um pop 120% com partículas vermelho/magenta (Lottie oficial).
8. **Selo de verificado** (círculo com check, 14px, cinza) ao lado do nome do canal.
9. **Contadores em PT-BR** ("438 mi de visualizações", "há 21 anos", "46,4 mi de inscritos") e dígitos rolando.
10. **Shorts:** ícone vermelho do Shorts, cards verticais com raio 8px, texto de views.
11. **AO VIVO:** etiqueta vermelha #E1002D a 90% e anel em gradiente #E1002D → #E01378 no avatar.
12. **Barra de busca** em pílula dividida (campo + botão da lupa 64px) com o botão de voz redondo ao lado.
13. **Tela final** com elementos de vídeo e o círculo "Inscrever-se" nos últimos 5 a 20 s.
14. **Dois mundos:** tema claro (#FFFFFF / #0F0F0F) e escuro (#0F0F0F / #F1F1F1): o escuro é o mais associado ao consumo de vídeo [INFERIDO].
15. **Movimento da identidade 2026** (primeiro sistema de motion oficial): thumbnails que balançam e quicam reagindo ao conteúdo e leve tremida de câmera, imitando vídeo de criador (Marketing Dive, 20/01/2026). Serve de referência para mover **cards e UI**, não o logo.

---

## 7. Proibições e regras da marca

**Logo** (brand.youtube/youtube-logo) [VERIFICADO, parafraseado]:
- Baixar sempre a versão mais recente e seguir as diretrizes.
- Full color: ícone vermelho com texto #212121 (fundo branco/imagem clara) ou #FFFFFF; triângulo sempre branco. Mono (#212121 ou #FFFFFF) quando o full color não tiver contraste, com triângulo vazado.
- **Área de respiro:** definida pelo triângulo do ícone; nada pode invadir. No diagrama oficial, as laterais usam a largura do triângulo e topo/base a altura dele (≈ 37% e ≈ 43% da altura do logo, medido).
- **Tamanho mínimo:** altura de **100 px** no digital e 3,1 mm impresso (a página do ícone repete o mesmo texto).
- **Mau uso** (o logo "nunca deve ser alterado"): não contornar; não recolorir (paletas próprias); não aplicar sombras nem efeitos; **não girar nem inclinar**; não achatar; não esticar.

**Ícone** (brand.youtube/youtube-icon): 3 versões (vermelha, #212121, #FFFFFF); mesmas regras: sem traço/contorno, sem cores próprias, sem sombra, sem girar/inclinar, sem achatar/esticar.

**Divulgar o próprio canal** (brand.youtube/promoting-your-channel), o caso deste showreel:
- Convenção obrigatória: **ícone do YouTube + "/@handle"** em uma linha (ex.: ícone + /@felipeborgesfalaia); pode vir um chamado em texto simples antes ou depois ("Inscreva-se").
- **Não usar o logo completo para promover o canal**, nem dentro de frase.
- Em rodapés/assinaturas junto de outras redes, usar o ícone (não o logo), respeitando o respiro.

**Outras regras:**
- Produtos/merch: marca do YouTube só acompanhada do handle do criador; logo sozinho não é aprovado.
- "YouTuber"/"Tuber": uso informal para pessoas; não usar em nomes oficiais de séries, livros, programas, canais, domínios ou marcas.
- **Entretenimento e mídia:** qualquer inserção de logos, ícones ou **elementos de UI (botões, páginas, capturas de celular)** em mídia (TV, clipe, filme, livro) precisa de aprovação pelo Brand Use Request Form, em inglês; imprensa está isenta. A retratação tem de ser positiva ou neutra.
- Diretrizes da API (developers.google.com, atualizadas em 20/08/2025): não alterar, distorcer, obstruir ou remover elementos da marca; não mudar cores de logos e ícones; logo totalmente visível, nunca parcialmente coberto; não ser o elemento mais proeminente; não sugerir endosso ou associação.
- O YouTube se reserva o direito de contestar usos inadequados.

**Animar o logo: o que exatamente dizem.** Nenhuma das 9 páginas do brand.youtube nem as diretrizes da API fala literalmente em "animar" [VERIFICADO]. O que existe é: nunca alterar, mais a lista de proibições (girar, inclinar, achatar, esticar, contorno, sombra/efeitos, recolorir) e, na API, não cobrir parcialmente nem distorcer. Leitura conservadora [INFERIDO]:
- **Pode:** entrar/sair por corte, fade de opacidade, deslocamento, escala **uniforme** (mantendo ≥ 100 px de altura e o respiro).
- **Não pode:** girar, *skew*/tilt 3D, *squash & stretch* ou quique elástico que deforme, desenhar o contorno (*stroke draw-on*), brilho/sombra/*blur* de movimento, trocar cor ou aplicar gradiente no logo, "morfar" o triângulo, animar letras do wordmark separadamente, revelar por máscara que cubra parte do logo.
- O próprio YouTube tem uma animação oficial de abertura (logo que expande e contrai com a barra de progresso, segundo o Google Design); não recriar como se fosse oficial.

---

## 8. Implicações para o showreel [INFERIDO]

1. A assinatura final deve seguir a regra de canal: **ícone oficial + "/@felipeborgesfalaia" em Roboto**, não o logo completo.
2. O "cara de YouTube" deve vir dos **átomos de UI** (§6) montados com os tokens medidos (§2 e §4), não de um logo animado.
3. Vermelho #FF0033 para marca, barra e scrubber; #E1002D só para ao vivo; gradiente até #FF2791 só em barra/like/anel.
4. Roboto (OFL) em todo texto de UI. YouTube Sans/Display só se houver autorização: são restritas.
5. Risco a decidir pelo Felipe: as diretrizes pedem aprovação para elementos de UI em mídia; evitar qualquer frase que sugira parceria ou endosso do YouTube.

---

## Fontes consultadas
- Marca: https://brand.youtube/ · https://brand.youtube/youtube-logo · https://brand.youtube/youtube-icon · https://brand.youtube/color · https://brand.youtube/promoting-your-channel · https://brand.youtube/swag-and-merchandise · https://brand.youtube/naming-and-third-party-content · https://brand.youtube/entertainment-and-media · https://brand.youtube/api-and-device-partners · https://developers.google.com/youtube/terms/branding-guidelines
- Vermelho novo: https://design.google/library/youtube-new-red-color · https://9to5google.com/2025/02/12/youtube-red-magenta/ · https://www.androidauthority.com/youtube-new-red-color-3526528/
- Identidade 2026: https://www.marketingdive.com/news/youtube-revamps-visual-identity-as-entertainment-landscape-shifts/809983/ · https://designcompass.org/en/2026/01/28/youtube-disaplay/
- UI/tokens: https://www.youtube.com/ (HTML) · CSS `kevlar_base` (URL em §2.3) · https://www.youtube.com/s/player/fb50cd46/www-player.css · https://www.youtube.com/s/desktop/d57c41d2/cssbin/www-main-desktop-home-page-skeleton.css
- Fontes: https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900 · https://fonts.googleapis.com/css2?family=YouTube+Sans:wght@300..900 · https://fonts.googleapis.com/css2?family=YouTube+Display:wght@400..900 · https://fonts.google.com/license/googlerestricted · https://raw.githubusercontent.com/google/fonts/main/ofl/roboto/METADATA.pb
- Tela final: https://support.google.com/youtube/answer/6388789?hl=pt-BR
- Números: links na tabela da §5.
