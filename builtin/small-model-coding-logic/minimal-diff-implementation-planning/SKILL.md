---
name: minimal-diff-implementation-planning
description: "Use when \"minimal diff implementation planning\" is the work. Identify the smallest change set and leave unrelated formatting, dependencies, and behavior untouched."
---

# Minimal-Diff Implementation Planning

Identify the smallest change set and leave unrelated formatting, dependencies, and behavior untouched.

1. Write explicit inputs, outputs, invariants, and stop conditions.
2. Decompose the task into independently checkable steps.
3. Trace a worked example and a counterexample before implementing the smallest change.

Example:
```text
Write explicit inputs, outputs, invariants, and stop conditions.
```

Check: Each step must have a checkable artifact; stop rather than guessing when critical context or tools are unavailable.
