---
name: metamorphic-test-design
description: "Use when \"metamorphic test design\" is the work. Define transformations whose outputs should preserve a known relation even without an exact oracle."
---

# Metamorphic Test Design

Define transformations whose outputs should preserve a known relation even without an exact oracle.

1. Identify observable behavior and test boundaries.
2. Create deterministic fixtures covering normal, boundary, and failure paths.
3. Verify that a deliberate defect causes a meaningful test failure.

Example:
```text
Identify observable behavior and test boundaries.
```

Check: Confirm tests fail for the intended reason; control clocks and randomness; report quarantined tests rather than treating them.
