---
name: memory-leak-regression-detection
description: "Use when \"memory leak regression detection\" is the work. Repeat lifecycle operations and examine retained-object growth after appropriate cleanup and collection."
---

# Memory Leak Regression Detection

Repeat lifecycle operations and examine retained-object growth after appropriate cleanup and collection.

1. Choose workload distributions and performance budgets before measuring.
2. Isolate warmup, steady state, and teardown.
3. Collect profiles and repeated baseline/candidate samples on comparable hardware.

Example:
```text
Choose workload distributions and performance budgets before measuring.
```

Check: Retain raw samples, sample counts, noise estimates, runtime flags, and scaling curves; avoid conclusions from a single run.
