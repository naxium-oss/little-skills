---
name: game-state-and-checkpoint-management
description: "Use when \"game state and checkpoint management\" is the work. Serialize stable gameplay state and validate checkpoint restoration without duplicate side effects."
---

# Game State and Checkpoint Management

Serialize stable gameplay state and validate checkpoint restoration without duplicate side effects.

1. Separate fixed-step simulation from rendering.
2. Align physics units and input semantics.
3. Validate collisions, state transitions, and resource budgets using recorded input sequences.

Example:
```text
Separate fixed-step simulation from rendering.
```

Check: Measure frame-time distributions rather than only average FPS; test pause, focus loss, pointer-lock exit, and checkpoint restoration.
