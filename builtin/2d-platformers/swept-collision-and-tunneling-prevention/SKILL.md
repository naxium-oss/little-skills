---
name: swept-collision-and-tunneling-prevention
description: "Use when \"swept collision and tunneling prevention\" is the work. Use swept tests or bounded substeps for fast motion and verify earliest contact resolution."
---

# Swept Collision and Tunneling Prevention

Use swept tests or bounded substeps for fast motion and verify earliest contact resolution.

1. Define simulation units, collision shapes, and input buffering windows.
2. Use fixed-step or swept movement where needed.
3. Replay deterministic level fixtures around boundaries and moving geometry.

Example:
```text
Define simulation units, collision shapes, and input buffering windows.
```

Check: Test corners, one-way platforms, moving passengers, jump boundaries, restart behavior, and softlocks; separate feel tuning from correctness.
