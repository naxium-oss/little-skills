---
name: tail-latency-regression-detection
description: "Use when \"tail latency regression detection\" is the work. Compare high-percentile latency with adequate sample counts and confidence under matched load."
---

# Tail-Latency Regression Detection

Compare high-percentile latency with adequate sample counts and confidence under matched load.

1. Choose workload distributions and performance budgets before measuring.
2. Isolate warmup, steady state, and teardown.
3. Collect profiles and repeated baseline/candidate samples on comparable hardware.

Example:
```text
Choose workload distributions and performance budgets before measuring.
```

Check: Retain raw samples, sample counts, noise estimates, runtime flags, and scaling curves; avoid conclusions from a single run.
