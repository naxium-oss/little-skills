---
name: performance-budget-enforcement
description: "Use when \"performance budget enforcement\" is the work. Define budgets and statistically robust failure thresholds before running the performance gate."
---

# Performance Budget Enforcement

Define budgets and statistically robust failure thresholds before running the performance gate.

1. Choose workload distributions and performance budgets before measuring.
2. Isolate warmup, steady state, and teardown.
3. Collect profiles and repeated baseline/candidate samples on comparable hardware.

Example:
```text
Choose workload distributions and performance budgets before measuring.
```

Check: Retain raw samples, sample counts, noise estimates, runtime flags, and scaling curves; avoid conclusions from a single run.
