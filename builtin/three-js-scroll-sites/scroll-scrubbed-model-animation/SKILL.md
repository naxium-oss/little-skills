---
name: scroll-scrubbed-model-animation
description: "Use when \"scroll scrubbed model animation\" is the work. Map progress to animation time explicitly and handle reversing, bounds, and unloaded models."
---

# Scroll-Scrubbed Model Animation

Map progress to animation time explicitly and handle reversing, bounds, and unloaded models.

1. Normalize scroll progress against measured layout.
2. Synchronize DOM and WebGL coordinate systems after resize.
3. Lazy-load assets and provide static or reduced-motion alternatives.

Example:
```text
Normalize scroll progress against measured layout.
```

Check: Check scroll bounds, fast reversals, touch scrolling, thermal slowdown, cleanup, and a readable non-WebGL fallback.
