---
name: counterexample-driven-logic-checking
description: "Use when \"counterexample driven logic checking\" is the work. Actively construct an input that breaks each proposed invariant before trusting the implementation."
---

# Counterexample-Driven Logic Checking

Actively construct an input that breaks each proposed invariant before trusting the implementation.

1. Write explicit inputs, outputs, invariants, and stop conditions.
2. Decompose the task into independently checkable steps.
3. Trace a worked example and a counterexample before implementing the smallest change.

Example:
```text
Write explicit inputs, outputs, invariants, and stop conditions.
```

Check: Each step must have a checkable artifact; stop rather than guessing when critical context or tools are unavailable.
