---
name: svg-visual-verification
description: "Use when \"check the svg\", \"visual feedback and verification for svg\" is the work."
---

# Visual feedback and verification for SVG

Decide whether an SVG is correct by looking at pixels, at the size a user will see it, on the background it.

1. Render, do not read.
2. The checks that find real defects.
3. Compare against intent, not against your memory.

Example:
```js
const img = new Image();
img.src = "data:image/svg+xml;utf8," + encodeURIComponent(svg);
```

Check: Say not run when the check did not run.
