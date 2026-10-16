---
name: scroll-to-scene-progress-mapping
description: "Use when \"scroll to scene progress mapping\" is the work. Map scroll offsets to clamped normalized progress using measured section start and end positions."
---

# Scroll-to-Scene Progress Mapping

Map scroll offsets to clamped normalized progress using measured section start and end positions.

1. Normalize scroll progress against measured layout.
2. Synchronize DOM and WebGL coordinate systems after resize.
3. Lazy-load assets and provide static or reduced-motion alternatives.

Example:
```text
Normalize scroll progress against measured layout.
```

Check: Check scroll bounds, fast reversals, touch scrolling, thermal slowdown, cleanup, and a readable non-WebGL fallback.
