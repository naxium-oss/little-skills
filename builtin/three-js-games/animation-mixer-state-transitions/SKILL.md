---
name: animation-mixer-state-transitions
description: "Use when \"animation mixer state transitions\" is the work. Define blend, interruption, loop, and completion rules and remove obsolete event listeners."
---

# Animation Mixer State Transitions

Define blend, interruption, loop, and completion rules and remove obsolete event listeners.

1. Separate fixed-step simulation from rendering.
2. Align physics units and input semantics.
3. Validate collisions, state transitions, and resource budgets using recorded input sequences.

Example:
```text
Separate fixed-step simulation from rendering.
```

Check: Measure frame-time distributions rather than only average FPS; test pause, focus loss, pointer-lock exit, and checkpoint restoration.
