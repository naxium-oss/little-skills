---
name: raycasting-and-object-interaction
description: "Use when \"raycasting and object interaction\" is the work. Convert pointer coordinates correctly and filter hits by interactable state and occlusion policy."
---

# Raycasting and Object Interaction

Convert pointer coordinates correctly and filter hits by interactable state and occlusion policy.

1. Separate fixed-step simulation from rendering.
2. Align physics units and input semantics.
3. Validate collisions, state transitions, and resource budgets using recorded input sequences.

Example:
```text
Separate fixed-step simulation from rendering.
```

Check: Measure frame-time distributions rather than only average FPS; test pause, focus loss, pointer-lock exit, and checkpoint restoration.
