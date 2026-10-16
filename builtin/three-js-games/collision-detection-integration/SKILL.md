---
name: collision-detection-integration
description: "Use when \"collision detection integration\" is the work. Align collider geometry with scene transforms and test high-speed and boundary contacts."
---

# Collision Detection Integration

Align collider geometry with scene transforms and test high-speed and boundary contacts.

1. Separate fixed-step simulation from rendering.
2. Align physics units and input semantics.
3. Validate collisions, state transitions, and resource budgets using recorded input sequences.

Example:
```text
Separate fixed-step simulation from rendering.
```

Check: Measure frame-time distributions rather than only average FPS; test pause, focus loss, pointer-lock exit, and checkpoint restoration.
