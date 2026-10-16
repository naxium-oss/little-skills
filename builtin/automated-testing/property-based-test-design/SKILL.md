---
name: property-based-test-design
description: "Use when \"property based test design\" is the work. Generate valid input domains and check invariants with reproducible seeds and shrinking."
---

# Property-Based Test Design

Generate valid input domains and check invariants with reproducible seeds and shrinking.

1. Identify observable behavior and test boundaries.
2. Create deterministic fixtures covering normal, boundary, and failure paths.
3. Verify that a deliberate defect causes a meaningful test failure.

Example:
```text
Identify observable behavior and test boundaries.
```

Check: Confirm tests fail for the intended reason; control clocks and randomness; report quarantined tests rather than treating them.
