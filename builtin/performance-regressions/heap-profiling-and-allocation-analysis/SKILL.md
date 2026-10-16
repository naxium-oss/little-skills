---
name: heap-profiling-and-allocation-analysis
description: "Use when \"heap profiling and allocation analysis\" is the work. Track retained versus allocated memory and attribute lifetime growth through heap snapshots."
---

# Heap Profiling and Allocation Analysis

Track retained versus allocated memory and attribute lifetime growth through heap snapshots.

1. Choose workload distributions and performance budgets before measuring.
2. Isolate warmup, steady state, and teardown.
3. Collect profiles and repeated baseline/candidate samples on comparable hardware.

Example:
```text
Choose workload distributions and performance budgets before measuring.
```

Check: Retain raw samples, sample counts, noise estimates, runtime flags, and scaling curves; avoid conclusions from a single run.
