---
name: sprite-animation-state-machines
description: "Use when \"sprite animation state machines\" is the work. Define animation transitions from authoritative gameplay state rather than incidental input alone."
---

# Sprite Animation State Machines

Define animation transitions from authoritative gameplay state rather than incidental input alone.

1. Define simulation units, collision shapes, and input buffering windows.
2. Use fixed-step or swept movement where needed.
3. Replay deterministic level fixtures around boundaries and moving geometry.

Example:
```text
Define simulation units, collision shapes, and input buffering windows.
```

Check: Test corners, one-way platforms, moving passengers, jump boundaries, restart behavior, and softlocks; separate feel tuning from correctness.
