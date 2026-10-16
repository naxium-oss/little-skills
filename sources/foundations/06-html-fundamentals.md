# HTML Fundamentals

## Document Structure and Parsing Verification
Browsers parse HTML leniently, auto-correcting malformed markup in ways that vary by engine; verify actual rendered DOM structure with browser DevTools rather than assuming the source markup is what executes.
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Page Title</title>
  </head>
  <body></body>
</html>
```
Inspect the "Elements" panel in DevTools to confirm the browser didn't silently close a tag early or move an element (e.g., a `<div>` inside a `<p>` closes the `<p>` automatically per the HTML parsing spec).
**Pitfalls:** omitting `<!doctype html>`, triggering quirks mode with different box-model/layout behavior; assuming invalid nesting (block inside inline) renders as authored across all browsers.

## Semantic Elements and Document Outline
Semantic tags (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`) communicate structure to assistive technology and search engines beyond what `<div>` conveys; verify the accessibility tree reflects intended landmarks.
```html
<body>
  <header><nav aria-label="Primary">...</nav></header>
  <main>
    <article>
      <h1>Article Title</h1>
      <section aria-labelledby="comments-heading">
        <h2 id="comments-heading">Comments</h2>
      </section>
    </article>
  </main>
  <footer>...</footer>
</body>
```
Check with a screen reader or the DevTools Accessibility panel that landmarks are announced ("navigation," "main," "banner") rather than assuming semantic tags automatically fix all accessibility gaps.
**Pitfalls:** using `<div class="header">` purely for visual styling instead of `<header>`, losing landmark navigation for screen reader users; nesting multiple `<h1>` tags without checking the resulting document outline algorithm's actual current browser support.

## Forms, Input Types, and Native Validation
HTML forms support built-in validation via input `type`, `required`, `pattern`, and `min`/`max` attributes, reducing reliance on JavaScript for basic checks; verify actual validation messages and behavior per browser, since UI/wording differs.
```html
<form novalidate>
  <label for="email">Email</label>
  <input id="email" name="email" type="email" required autocomplete="email" />
  <label for="qty">Quantity</label>
  <input id="qty" name="qty" type="number" min="1" max="10" step="1" />
  <button type="submit">Submit</button>
</form>
```
Test `:invalid`/`:valid` CSS pseudo-classes and the `ValidityState` API in actual target browsers rather than assuming uniform behavior, and confirm server-side validation exists as the authoritative check since client-side validation is bypassable.
**Pitfalls:** relying solely on client-side `required`/`pattern` validation without server-side enforcement; forgetting `<label for>` association, breaking click-to-focus and screen reader announcements.

## Media Elements and Responsive Images
`<picture>`, `srcset`, and `sizes` let browsers select the optimal image variant for viewport and pixel density, avoiding fixed hardcoded image URLs. Verify actual network requests in DevTools to confirm the expected variant loads.
```html
<picture>
  <source srcset="hero-narrow.avif 800w, hero-wide.avif 1600w" type="image/avif" sizes="100vw" />
  <img src="hero-fallback.jpg" alt="Product overview illustration" width="1600" height="900" loading="lazy" />
</picture>
```
Always set explicit `width`/`height` (or `aspect-ratio` in CSS) to prevent cumulative layout shift while images load, and verify `loading="lazy"` doesn't delay above-the-fold content.
**Pitfalls:** omitting `alt` text (or using empty `alt=""` incorrectly for meaningful images); lazy-loading hero/LCP images, hurting perceived load performance.

## Metadata, SEO, and Social Sharing Tags
`<meta>` tags control document behavior, search indexing hints, and social preview cards (Open Graph, Twitter Cards); verify actual rendering with each platform's real preview debugger since cached crawls can show stale data.
```html
<meta name="description" content="Concise, accurate page summary under 160 characters." />
<meta property="og:title" content="Page Title" />
<meta property="og:image" content="https://example.com/preview.png" />
<link rel="canonical" href="https://example.com/page" />
```
Confirm `og:image` URLs are absolute and publicly reachable (not behind auth) by testing with the platform's actual scraper/debugger tool, and re-scrape after changes since results are cached.
**Pitfalls:** using relative URLs for `og:image`, which many scrapers fail to resolve; forgetting `rel="canonical"` on paginated or duplicate-content pages, hurting SEO signal consolidation.

## HTML Templates, Slots, and Custom Elements
The native `<template>` element holds inert markup for later cloning, and Custom Elements (Web Components) let you define reusable tags without a framework; verify actual browser support and Shadow DOM encapsulation behavior for the target audience.
```html
<template id="card-template">
  <style>.card { border: 1px solid #ccc; padding: 1rem; }</style>
  <div class="card"><slot name="title"></slot><slot></slot></div>
</template>
<script>
class UserCard extends HTMLElement {
  connectedCallback() {
    const tpl = document.getElementById("card-template").content.cloneNode(true);
    this.attachShadow({ mode: "open" }).appendChild(tpl);
  }
}
customElements.define("user-card", UserCard);
</script>
```
Verify Shadow DOM style encapsulation actually isolates styles as expected by inspecting computed styles in DevTools, since global stylesheets do not penetrate a closed/open shadow root by default.
**Pitfalls:** assuming global CSS resets apply inside shadow roots; forgetting `customElements.define` must run before the tag is parsed, or upgrading won't happen until the script executes.

## Iframes, Sandboxing, and Embedded Content
`<iframe>` embeds another document with its own browsing context; the `sandbox` attribute restricts capabilities (scripts, forms, top-navigation) unless explicitly allowed, critical for embedding untrusted content safely.
```html
<iframe
  src="https://widget.example.com/embed"
  sandbox="allow-scripts allow-same-origin"
  referrerpolicy="no-referrer"
  loading="lazy"
  title="Embedded widget">
</iframe>
```
Verify the exact combination of `sandbox` tokens against the widget's actual functional requirements by testing broken behavior first, then adding only the minimum tokens needed.
**Pitfalls:** combining `allow-scripts` and `allow-same-origin` carelessly, which together can let sandboxed content escape the sandbox by rewriting its own restrictions; embedding third-party iframes without `referrerpolicy`, leaking referrer URLs.

## Data Attributes and Progressive JavaScript Hooks
`data-*` attributes store custom data readable via `dataset` in JS without inventing non-standard attributes; they're the correct hook point for behavior instead of parsing class names or IDs meant for styling.
```html
<button data-action="add-to-cart" data-product-id="42">Add to cart</button>
<script>
document.querySelectorAll("[data-action='add-to-cart']").forEach((btn) => {
  btn.addEventListener("click", () => addToCart(btn.dataset.productId));
});
</script>
```
Verify `dataset` camelCases hyphenated attribute names automatically (`data-product-id` → `dataset.productId`) rather than assuming a direct string match.
**Pitfalls:** using CSS classes as JS behavior hooks, so a designer's class rename silently breaks functionality; storing large or sensitive data in `data-*` attributes, which are visible in page source.

# CSS Fundamentals

## Cascade, Specificity, and Source Order
CSS rules are resolved by origin/importance, specificity (ID > class/attribute/pseudo-class > element), then source order for ties; verify actual computed specificity with DevTools rather than guessing why a style "isn't applying."
```css
#nav .item { color: blue; }      /* specificity: 1,1,0 */
.nav-item { color: red; }        /* specificity: 0,1,0, loses to the rule above */
```
Use the DevTools "Computed" panel to see which rule won and why, and prefer flat specificity (classes) over ID selectors and `!important` to keep the cascade predictable.
**Pitfalls:** reaching for `!important` to force a win instead of fixing specificity/source order, which compounds into unmaintainable overrides; assuming later-defined CSS files always win regardless of specificity.

## Box Model and Sizing
Every element has content, padding, border, and margin; `box-sizing: border-box` (recommended globally) makes width/height include padding and border, avoiding the classic "why is this wider than I set it" bug.
```css
*, *::before, *::after { box-sizing: border-box; }
.card { width: 300px; padding: 1.5rem; border: 1px solid #ddd; }
```
Verify actual rendered box dimensions in DevTools' box model diagram, especially when margins collapse between adjacent block elements, a frequently misunderstood behavior.
**Pitfalls:** forgetting `border-box` reset and being surprised padding/border inflate the total size beyond the declared `width`; not accounting for vertical margin collapse between siblings or parent/child blocks.

## Flexbox Layout Model
Flexbox distributes space along a main axis and cross axis within a container; `flex-direction`, `justify-content`, `align-items`, and the `flex` shorthand on children (grow/shrink/basis) control layout. Verify actual axis orientation before debugging alignment, since `row` vs `column` swaps which properties control what.
```css
.toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.75rem;
}
.toolbar .spacer { flex: 1 1 auto; }
```
Use DevTools' flexbox overlay to visualize the main/cross axis and computed gaps rather than guessing from property names alone.
**Pitfalls:** confusing `justify-content` (main axis) with `align-items` (cross axis) after changing `flex-direction`; using `flex: 1` on children expecting equal width without accounting for differing `flex-basis`/content sizes.

## CSS Grid Layout Model
CSS Grid defines two-dimensional layouts via explicit rows/columns and named template areas, distinct from flexbox's one-dimensional model; verify track sizing keywords (`fr`, `minmax`, `auto-fit`/`auto-fill`) produce the intended responsive behavior by resizing the viewport live.
```css
.layout {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
}
.dashboard {
  display: grid;
  grid-template-areas: "sidebar header" "sidebar main";
  grid-template-columns: 240px 1fr;
}
.dashboard .sidebar { grid-area: sidebar; }
```
Confirm `auto-fit` vs `auto-fill` choice matches intent: `auto-fit` collapses empty tracks, `auto-fill` preserves them, by testing with fewer items than columns.
**Pitfalls:** mixing up `auto-fit`/`auto-fill` and getting unexpected empty gaps or missing collapsing; naming grid areas inconsistently between `grid-template-areas` and child `grid-area` values, silently failing to place items.

## Responsive Design with Media and Container Queries
Media queries respond to viewport characteristics; container queries (broad support since 2023) respond to a containing element's size, enabling truly component-based responsive design. Verify actual browser support dates before relying on container queries for critical layouts.
```css
.card-grid { container-type: inline-size; container-name: cards; }
@container cards (min-width: 480px) {
  .card { grid-template-columns: 120px 1fr; }
}
@media (prefers-color-scheme: dark) {
  :root { --bg: #111; --fg: #eee; }
}
```
Test with real device widths and the DevTools device toolbar rather than only resizing the desktop browser window, since touch/viewport quirks differ.
**Pitfalls:** relying only on `min-width` media query breakpoints without testing intermediate widths, missing awkward layout states; assuming container queries are supported without checking the minimum target browser version.

## Custom Properties (CSS Variables) and Theming
Custom properties (`--name`) are runtime-resolved, cascade like normal properties, and can be updated via JavaScript or media queries, unlike Sass variables which are compile-time only. Verify inheritance scope, a variable defined on `:root` is globally available, but one scoped to a component only applies within it.
```css
:root { --spacing-unit: 8px; --color-primary: oklch(0.6 0.2 250); }
.button { padding: calc(var(--spacing-unit) * 2) calc(var(--spacing-unit) * 3); background: var(--color-primary); }
```
```javascript
document.documentElement.style.setProperty("--color-primary", "oklch(0.7 0.15 30)");
```
**Pitfalls:** assuming custom properties are statically inlined like preprocessor variables, missing their live-updating cascade behavior; forgetting a fallback value (`var(--x, default)`) causes the property to be invalid, not just "unset," if `--x` is undefined.

## Stacking Contexts and z-index
`z-index` only has effect on positioned elements and is scoped within a stacking context; a high `z-index` inside a low stacking context can still render behind a low `z-index` sibling in another context. Verify actual stacking with DevTools' 3D view or layer panel.
```css
.modal-overlay { position: fixed; inset: 0; z-index: 1000; }
.tooltip { position: absolute; z-index: 10; } /* useless if trapped in a low stacking context ancestor */
```
Check whether `transform`, `filter`, `opacity < 1`, or `will-change` on an ancestor unexpectedly created a new stacking context, trapping a high `z-index` descendant.
**Pitfalls:** raising `z-index` indefinitely as a "fix" without understanding the actual stacking context tree; not realizing `position: static` elements ignore `z-index` entirely.

## Modern Color Spaces and Functions
CSS now supports wide-gamut color spaces (`oklch`, `lab`, `color-mix()`) beyond sRGB hex/rgb, enabling perceptually uniform color manipulation; verify target browser support and provide fallbacks for older engines.
```css
.button {
  background: oklch(0.65 0.19 250);
  background: color-mix(in oklch, var(--color-primary) 80%, white);
}
@supports not (color: oklch(0 0 0)) {
  .button { background: #3b6fd6; }
}
```
Verify perceptual results visually across target displays, since wide-gamut colors can render differently (or get clamped) on non-P3 monitors.
**Pitfalls:** using `oklch`/`lab` without a fallback for browsers predating broad support; assuming `color-mix()` percentages behave linearly in all color spaces without checking the actual interpolation space specified.
