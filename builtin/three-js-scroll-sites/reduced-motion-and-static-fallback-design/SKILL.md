---
name: reduced-motion-and-static-fallback-design
description: "Use when \"reduced motion and static fallback design\" is the work. Provide readable static content and bypass nonessential motion when the preference is enabled."
---

# Reduced-Motion and Static Fallback Design

Provide readable static content and bypass nonessential motion when the preference is enabled.

1. Normalize scroll progress against measured layout.
2. Synchronize DOM and WebGL coordinate systems after resize.
3. Lazy-load assets and provide static or reduced-motion alternatives.

Example:
```text
Normalize scroll progress against measured layout.
```

Check: Check scroll bounds, fast reversals, touch scrolling, thermal slowdown, cleanup, and a readable non-WebGL fallback.
