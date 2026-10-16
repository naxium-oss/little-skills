---
name: fixed-timestep-game-loop-construction
description: "Use when \"fixed timestep game loop construction\" is the work. Use an accumulator with bounded catch-up and separate simulation state from interpolated rendering."
---

# Fixed-Timestep Game Loop Construction

Use an accumulator with bounded catch-up and separate simulation state from interpolated rendering.

1. Separate fixed-step simulation from rendering.
2. Align physics units and input semantics.
3. Validate collisions, state transitions, and resource budgets using recorded input sequences.

Example:
```text
Separate fixed-step simulation from rendering.
```

Check: Measure frame-time distributions rather than only average FPS; test pause, focus loss, pointer-lock exit, and checkpoint restoration.
