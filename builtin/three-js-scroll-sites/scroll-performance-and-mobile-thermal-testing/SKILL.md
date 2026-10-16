---
name: scroll-performance-and-mobile-thermal-testing
description: "Use when \"scroll performance and mobile thermal testing\" is the work. Measure sustained scrolling on real mobile hardware, including thermal throttling and battery impact."
---

# Scroll Performance and Mobile Thermal Testing

Measure sustained scrolling on real mobile hardware, including thermal throttling and battery impact.

1. Normalize scroll progress against measured layout.
2. Synchronize DOM and WebGL coordinate systems after resize.
3. Lazy-load assets and provide static or reduced-motion alternatives.

Example:
```text
Normalize scroll progress against measured layout.
```

Check: Check scroll bounds, fast reversals, touch scrolling, thermal slowdown, cleanup, and a readable non-WebGL fallback.
