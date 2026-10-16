---
name: scroll-scrubbed-camera-path-animation
description: "Use when \"scroll scrubbed camera path animation\" is the work. Parameterize camera paths smoothly and inspect orientation continuity and near-plane intersections."
---

# Scroll-Scrubbed Camera Path Animation

Parameterize camera paths smoothly and inspect orientation continuity and near-plane intersections.

1. Normalize scroll progress against measured layout.
2. Synchronize DOM and WebGL coordinate systems after resize.
3. Lazy-load assets and provide static or reduced-motion alternatives.

Example:
```text
Normalize scroll progress against measured layout.
```

Check: Check scroll bounds, fast reversals, touch scrolling, thermal slowdown, cleanup, and a readable non-WebGL fallback.
