---
name: end-to-end-user-journey-testing
description: "Use when \"end to end user journey testing\" is the work. Exercise complete user goals including invalid input, interruption, recovery, and persisted outcomes."
---

# End-to-End User Journey Testing

Exercise complete user goals including invalid input, interruption, recovery, and persisted outcomes.

1. Identify observable behavior and test boundaries.
2. Create deterministic fixtures covering normal, boundary, and failure paths.
3. Verify that a deliberate defect causes a meaningful test failure.

Example:
```text
Identify observable behavior and test boundaries.
```

Check: Confirm tests fail for the intended reason; control clocks and randomness; report quarantined tests rather than treating them.
