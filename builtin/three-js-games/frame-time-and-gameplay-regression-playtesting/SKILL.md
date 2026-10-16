---
name: frame-time-and-gameplay-regression-playtesting
description: "Use when \"frame time and gameplay regression playtesting\" is the work. Replay gameplay fixtures while measuring frame-time tails, input response, and state correctness."
---

# Frame-Time and Gameplay Regression Playtesting

Replay gameplay fixtures while measuring frame-time tails, input response, and state correctness.

1. Separate fixed-step simulation from rendering.
2. Align physics units and input semantics.
3. Validate collisions, state transitions, and resource budgets using recorded input sequences.

Example:
```text
Separate fixed-step simulation from rendering.
```

Check: Measure frame-time distributions rather than only average FPS; test pause, focus loss, pointer-lock exit, and checkpoint restoration.
