---
name: task-decomposition-into-verifiable-steps
description: "Use when \"task decomposition into verifiable steps\" is the work. Convert the request into a dependency-ordered checklist whose steps each yield a verifiable artifact."
---

# Task Decomposition into Verifiable Steps

Convert the request into a dependency-ordered checklist whose steps each yield a verifiable artifact.

1. Write explicit inputs, outputs, invariants, and stop conditions.
2. Decompose the task into independently checkable steps.
3. Trace a worked example and a counterexample before implementing the smallest change.

Example:
```text
Write explicit inputs, outputs, invariants, and stop conditions.
```

Check: Each step must have a checkable artifact; stop rather than guessing when critical context or tools are unavailable.
