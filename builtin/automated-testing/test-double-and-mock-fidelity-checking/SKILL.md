---
name: test-double-and-mock-fidelity-checking
description: "Use when \"test double and mock fidelity checking\" is the work. Compare mocked responses, timing, errors, and state transitions against the actual dependency contract."
---

# Test Double and Mock Fidelity Checking

Compare mocked responses, timing, errors, and state transitions against the actual dependency contract.

1. Identify observable behavior and test boundaries.
2. Create deterministic fixtures covering normal, boundary, and failure paths.
3. Verify that a deliberate defect causes a meaningful test failure.

Example:
```text
Identify observable behavior and test boundaries.
```

Check: Confirm tests fail for the intended reason; control clocks and randomness; report quarantined tests rather than treating them.
