---
name: character-movement-and-camera-control
description: "Use when \"character movement and camera control\" is the work. Separate movement intent, collision response, camera smoothing, and coordinate-space conversion."
---

# Character Movement and Camera Control

Separate movement intent, collision response, camera smoothing, and coordinate-space conversion.

1. Separate fixed-step simulation from rendering.
2. Align physics units and input semantics.
3. Validate collisions, state transitions, and resource budgets using recorded input sequences.

Example:
```text
Separate fixed-step simulation from rendering.
```

Check: Measure frame-time distributions rather than only average FPS; test pause, focus loss, pointer-lock exit, and checkpoint restoration.
