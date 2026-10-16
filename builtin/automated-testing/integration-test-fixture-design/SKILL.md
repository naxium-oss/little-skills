---
name: integration-test-fixture-design
description: "Use when \"integration test fixture design\" is the work. Use realistic dependency fixtures with isolated state, deterministic setup, and reliable teardown."
---

# Integration Test Fixture Design

Use realistic dependency fixtures with isolated state, deterministic setup, and reliable teardown.

1. Identify observable behavior and test boundaries.
2. Create deterministic fixtures covering normal, boundary, and failure paths.
3. Verify that a deliberate defect causes a meaningful test failure.

Example:
```text
Identify observable behavior and test boundaries.
```

Check: Confirm tests fail for the intended reason; control clocks and randomness; report quarantined tests rather than treating them.
