---
name: contract-testing-between-services
description: "Use when \"contract testing between services\" is the work. Verify producer and consumer expectations for field presence, error schemas, and compatibility evolution."
---

# Contract Testing Between Services

Verify producer and consumer expectations for field presence, error schemas, and compatibility evolution.

1. Identify observable behavior and test boundaries.
2. Create deterministic fixtures covering normal, boundary, and failure paths.
3. Verify that a deliberate defect causes a meaningful test failure.

Example:
```text
Identify observable behavior and test boundaries.
```

Check: Confirm tests fail for the intended reason; control clocks and randomness; report quarantined tests rather than treating them.
