---
name: data-attributes-and-progressive-javascript-hooks
description: "Use when \"data attributes and progressive javascript hooks\" is the work. using CSS classes as JS behavior hooks, so a designers class rename silently breaks functionality."
---

# Data Attributes and Progressive JavaScript Hooks

using CSS classes as JS behavior hooks.

1. Do not: using CSS classes as JS behavior hooks, so a designer's class rename silently breaks.
2. Do not: storing large or sensitive data in data- attributes, which are visible in page source.

Example:
```html
<button data-action="add-to-cart" data-product-id="42">Add to cart</button>
```

Check: Do not: using CSS.
