---
name: physics-engine-version-and-unit-alignment
description: "Use when \"physics engine version and unit alignment\" is the work. Confirm engine revision, timestep, unit scale, collision margins, and integration conventions."
---

# Physics Engine Version and Unit Alignment

Confirm engine revision, timestep, unit scale, collision margins, and integration conventions.

1. Separate fixed-step simulation from rendering.
2. Align physics units and input semantics.
3. Validate collisions, state transitions, and resource budgets using recorded input sequences.

Example:
```text
Separate fixed-step simulation from rendering.
```

Check: Measure frame-time distributions rather than only average FPS; test pause, focus loss, pointer-lock exit, and checkpoint restoration.
