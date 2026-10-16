---
name: resize-and-orientation-change-handling
description: "Use when \"resize and orientation change handling\" is the work. Update renderer, camera, pixel ratio, and scroll ranges without duplicating listeners or scenes."
---

# Resize and Orientation Change Handling

Update renderer, camera, pixel ratio, and scroll ranges without duplicating listeners or scenes.

1. Normalize scroll progress against measured layout.
2. Synchronize DOM and WebGL coordinate systems after resize.
3. Lazy-load assets and provide static or reduced-motion alternatives.

Example:
```text
Normalize scroll progress against measured layout.
```

Check: Check scroll bounds, fast reversals, touch scrolling, thermal slowdown, cleanup, and a readable non-WebGL fallback.
