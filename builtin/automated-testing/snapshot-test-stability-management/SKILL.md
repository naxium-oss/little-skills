---
name: snapshot-test-stability-management
description: "Use when \"snapshot test stability management\" is the work. Normalize only irrelevant nondeterminism and require review of meaningful baseline changes."
---

# Snapshot Test Stability Management

Normalize only irrelevant nondeterminism and require review of meaningful baseline changes.

1. Identify observable behavior and test boundaries.
2. Create deterministic fixtures covering normal, boundary, and failure paths.
3. Verify that a deliberate defect causes a meaningful test failure.

Example:
```text
Identify observable behavior and test boundaries.
```

Check: Confirm tests fail for the intended reason; control clocks and randomness; report quarantined tests rather than treating them.
