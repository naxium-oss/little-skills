---
name: test-isolation-and-fixture-design
description: "Use when \"test isolation and fixture design\" is the work. relying on test execution order for setup (test B assumes test A already ran and created data)."
---

# Test Isolation and Fixture Design

relying on test execution order for setup (test.

1. Do not: relying on test execution order for setup (test B assumes test A already ran.
2. Do not: sharing one database/connection across parallel test workers without transaction isolation, causing cross-test data races.

Example:
```bash
read the runner config and the test script in the manifest
```

Check: Do not: relying on test execution order for setup (test B assumes test A already ran and created.
