---
name: flaky-test
description: "Use when \"flaky test\", \"sometimes fails\", or \"intermittent failure\". Not when it fails every time."
---

# Pin a flake

A flake is a repro you have not captured yet.

1. Run the test in a loop until it fails.
2. Save the seed, timing, or order that failed.
3. Remove the clock, network, or shared state that moved.

Example:
```text
Failed on run 12 when the clock crossed a second boundary.
```

Check: Do not retry-away a flake in CI and call it fixed.
