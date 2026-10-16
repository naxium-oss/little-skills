---
name: animation-cancellation-and-cleanup
description: "Use when \"animation cancellation and cleanup\" is the work. Define ownership and cancellation semantics for overlapping animations and component removal."
---

# Animation Cancellation and Cleanup

Define ownership and cancellation semantics for overlapping animations and component removal.

1. Verify units, scales, coordinate systems, and animation timing.
2. Implement cancellation and lifecycle cleanup.
3. Profile representative data sizes and provide reduced-motion or static alternatives.

Example:
```text
Verify units, scales, coordinate systems, and animation timing.
```

Check: Test resize, high-DPI screens, empty and extreme data, interrupted motion, and background tabs; verify labels and units.
