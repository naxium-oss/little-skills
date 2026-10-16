---
name: dom-and-webgl-coordinate-synchronization
description: "Use when \"dom and webgl coordinate synchronization\" is the work. Recompute DOM-to-world mappings after layout, font loading, resize, and camera changes."
---

# DOM and WebGL Coordinate Synchronization

Recompute DOM-to-world mappings after layout, font loading, resize, and camera changes.

1. Normalize scroll progress against measured layout.
2. Synchronize DOM and WebGL coordinate systems after resize.
3. Lazy-load assets and provide static or reduced-motion alternatives.

Example:
```text
Normalize scroll progress against measured layout.
```

Check: Check scroll bounds, fast reversals, touch scrolling, thermal slowdown, cleanup, and a readable non-WebGL fallback.
