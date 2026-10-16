---
name: constraint-extraction-before-implementation
description: "Use when \"constraint extraction before implementation\" is the work. Extract explicit requirements, implicit invariants, forbidden changes, and acceptance checks before editing."
---

# Constraint Extraction Before Implementation

Extract explicit requirements, implicit invariants, forbidden changes, and acceptance checks before editing.

1. Write explicit inputs, outputs, invariants, and stop conditions.
2. Decompose the task into independently checkable steps.
3. Trace a worked example and a counterexample before implementing the smallest change.

Example:
```text
Write explicit inputs, outputs, invariants, and stop conditions.
```

Check: Each step must have a checkable artifact; stop rather than guessing when critical context or tools are unavailable.
