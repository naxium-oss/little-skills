---
name: moving-platform-passenger-motion
description: "Use when \"moving platform passenger motion\" is the work. Transfer platform displacement consistently and handle detachment, crushing, and changing directions."
---

# Moving Platform Passenger Motion

Transfer platform displacement consistently and handle detachment, crushing, and changing directions.

1. Define simulation units, collision shapes, and input buffering windows.
2. Use fixed-step or swept movement where needed.
3. Replay deterministic level fixtures around boundaries and moving geometry.

Example:
```text
Define simulation units, collision shapes, and input buffering windows.
```

Check: Test corners, one-way platforms, moving passengers, jump boundaries, restart behavior, and softlocks; separate feel tuning from correctness.
