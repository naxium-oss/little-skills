---
name: mocking-stubbing-and-fidelity-tradeoffs
description: "Use when \"mocking stubbing and fidelity tradeoffs\" is the work. mocking so extensively that a test verifies nothing but the mocks own configuration."
---

# Mocking, Stubbing, and Fidelity Tradeoffs

mocking so extensively that a test verifies nothing but the mock's own configuration.

1. Do not: mocking so extensively that a test verifies nothing but the mock's own configuration.
2. Do not: letting a mock's response shape drift from the real API's actual current shape without.

Example:
```bash
read the runner config and the test script in the manifest
```

Check: Do not: mocking so extensively that a test verifies nothing but the mock's own configuration.
