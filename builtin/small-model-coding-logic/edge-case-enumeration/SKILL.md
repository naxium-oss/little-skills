---
name: edge-case-enumeration
description: "Use when \"edge case enumeration\" is the work. Enumerate empty, singleton, boundary, malformed, extreme, repeated, and concurrent inputs as applicable."
---

# Edge-Case Enumeration

Enumerate empty, singleton, boundary, malformed, extreme, repeated, and concurrent inputs as applicable.

1. Write explicit inputs, outputs, invariants, and stop conditions.
2. Decompose the task into independently checkable steps.
3. Trace a worked example and a counterexample before implementing the smallest change.

Example:
```text
Write explicit inputs, outputs, invariants, and stop conditions.
```

Check: Each step must have a checkable artifact; stop rather than guessing when critical context or tools are unavailable.
