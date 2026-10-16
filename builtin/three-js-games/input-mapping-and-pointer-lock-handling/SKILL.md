---
name: input-mapping-and-pointer-lock-handling
description: "Use when \"input mapping and pointer lock handling\" is the work. Map physical inputs to actions and handle focus loss, pointer-lock denial, and remapping."
---

# Input Mapping and Pointer Lock Handling

Map physical inputs to actions and handle focus loss, pointer-lock denial, and remapping.

1. Separate fixed-step simulation from rendering.
2. Align physics units and input semantics.

Example:
```text
Separate fixed-step simulation from rendering.
```

Check: Measure frame-time distributions rather than only average FPS; test pause, focus loss, pointer-lock exit, and checkpoint restoration.
