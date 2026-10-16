---
name: flaky-test-diagnosis-and-quarantine
description: "Use when \"flaky test diagnosis and quarantine\" is the work. Quantify flakiness, identify causes, attach ownership and expiry to quarantine, and prevent silent omission."
---

# Flaky Test Diagnosis and Quarantine

Quantify flakiness, identify causes, attach ownership and expiry to quarantine, and prevent silent omission.

1. Identify observable behavior and test boundaries.
2. Create deterministic fixtures covering normal, boundary, and failure paths.
3. Verify that a deliberate defect causes a meaningful test failure.

Example:
```text
Identify observable behavior and test boundaries.
```

Check: Confirm tests fail for the intended reason; control clocks and randomness; report quarantined tests rather than treating them.
