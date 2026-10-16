---
name: requestanimationframe-loop-correctness
description: "Use when \"requestanimationframe loop correctness\" is the work. Use frame timestamps, avoid duplicate loops, clamp long pauses, and cancel on teardown."
---

# RequestAnimationFrame Loop Correctness

Use frame timestamps, avoid duplicate loops, clamp long pauses, and cancel on teardown.

1. Verify units, scales, coordinate systems, and animation timing.
2. Implement cancellation and lifecycle cleanup.
3. Profile representative data sizes and provide reduced-motion or static alternatives.

Example:
```text
Verify units, scales, coordinate systems, and animation timing.
```

Check: Test resize, high-DPI screens, empty and extreme data, interrupted motion, and background tabs; verify labels and units.
