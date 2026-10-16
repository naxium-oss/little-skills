---
name: draw-call-reduction-and-instancing
description: "Use when \"draw call reduction and instancing\" is the work. Batch compatible geometry and inspect actual draw calls, culling, and instance-update cost."
---

# Draw Call Reduction and Instancing

Batch compatible geometry and inspect actual draw calls, culling, and instance-update cost.

1. Separate fixed-step simulation from rendering.
2. Align physics units and input semantics.
3. Validate collisions, state transitions, and resource budgets using recorded input sequences.

Example:
```text
Separate fixed-step simulation from rendering.
```

Check: Measure frame-time distributions rather than only average FPS; test pause, focus loss, pointer-lock exit, and checkpoint restoration.
