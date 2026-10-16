---
name: lazy-scene-initialization-and-asset-preloading
description: "Use when \"lazy scene initialization and asset preloading\" is the work. Initialize near visibility with cancellable loading and avoid blocking primary page content."
---

# Lazy Scene Initialization and Asset Preloading

Initialize near visibility with cancellable loading and avoid blocking primary page content.

1. Normalize scroll progress against measured layout.
2. Synchronize DOM and WebGL coordinate systems after resize.
3. Lazy-load assets and provide static or reduced-motion alternatives.

Example:
```text
Normalize scroll progress against measured layout.
```

Check: Check scroll bounds, fast reversals, touch scrolling, thermal slowdown, cleanup, and a readable non-WebGL fallback.
