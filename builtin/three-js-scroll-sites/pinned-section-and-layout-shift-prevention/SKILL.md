---
name: pinned-section-and-layout-shift-prevention
description: "Use when \"pinned section and layout shift prevention\" is the work. Reserve stable space and verify pin offsets across dynamic content and responsive breakpoints."
---

# Pinned Section and Layout Shift Prevention

Reserve stable space and verify pin offsets across dynamic content and responsive breakpoints.

1. Normalize scroll progress against measured layout.
2. Synchronize DOM and WebGL coordinate systems after resize.
3. Lazy-load assets and provide static or reduced-motion alternatives.

Example:
```text
Normalize scroll progress against measured layout.
```

Check: Check scroll bounds, fast reversals, touch scrolling, thermal slowdown, cleanup, and a readable non-WebGL fallback.
