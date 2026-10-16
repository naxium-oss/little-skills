---
name: svg-authoring
description: "Use when \"svg icon\", \"author an svg\", \"making svgs\" is the work."
---

# Making SVGs

Produce an SVG that renders correctly at the sizes it will be used at, is readable by the next person who opens.

1. Set the coordinate space first.
2. Structure in layers.

Example:
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" role="img">
```

Check: Invisible shape: viewBox mismatch (coordinates outside it), fill="none" with no stroke, or a zero width or height.
