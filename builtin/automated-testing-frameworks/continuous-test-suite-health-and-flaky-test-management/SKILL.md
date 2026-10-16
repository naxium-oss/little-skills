---
name: continuous-test-suite-health-and-flaky-test-management
description: "Use when \"continuous test suite health and flaky test management\" is the work. habitually re-running a failing CI job until it passes without investigating why it flaked, normalizing a culture of."
---

# Continuous Test Suite Health and Flaky

habitually re-running a failing CI.

1. Do not: habitually re-running a failing CI job until it passes without investigating why it flaked.
2. Do not: quarantining a flaky test indefinitely without a tracked follow-up to actually fix or remove.

Example:
```bash
read the runner config and the test script in the manifest
```

Check: Do not: habitually re-running a failing CI job until.
