---
name: jump-buffering-and-coyote-time
description: "Use when \"jump buffering and coyote time\" is the work. Measure buffer and grace windows in simulation time and test exact threshold boundaries."
---

# Jump Buffering and Coyote Time

Measure buffer and grace windows in simulation time and test exact threshold boundaries.

1. Define simulation units, collision shapes, and input buffering windows.
2. Use fixed-step or swept movement where needed.
3. Replay deterministic level fixtures around boundaries and moving geometry.

Example:
```text
Define simulation units, collision shapes, and input buffering windows.
```

Check: Test corners, one-way platforms, moving passengers, jump boundaries, restart behavior, and softlocks; separate feel tuning from correctness.
