---
name: algorithmic-scaling-regression-detection
description: "Use when \"algorithmic scaling regression detection\" is the work. Measure increasing input sizes and fit plausible scaling models instead of extrapolating one point."
---

# Algorithmic Scaling Regression Detection

Measure increasing input sizes and fit plausible scaling models instead of extrapolating one point.

1. Choose workload distributions and performance budgets before measuring.
2. Isolate warmup, steady state, and teardown.
3. Collect profiles and repeated baseline/candidate samples on comparable hardware.

Example:
```text
Choose workload distributions and performance budgets before measuring.
```

Check: Retain raw samples, sample counts, noise estimates, runtime flags, and scaling curves; avoid conclusions from a single run.
