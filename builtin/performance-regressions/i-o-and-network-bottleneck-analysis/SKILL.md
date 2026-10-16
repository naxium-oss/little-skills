---
name: i-o-and-network-bottleneck-analysis
description: "Use when \"i o and network bottleneck analysis\" is the work. Measure queueing, serialization, disk waits, network transfer, and dependency response time separately."
---

# I/O and Network Bottleneck Analysis

Measure queueing, serialization, disk waits, network transfer, and dependency response time separately.

1. Choose workload distributions and performance budgets before measuring.
2. Isolate warmup, steady state, and teardown.
3. Collect profiles and repeated baseline/candidate samples on comparable hardware.

Example:
```text
Choose workload distributions and performance budgets before measuring.
```

Check: Retain raw samples, sample counts, noise estimates, runtime flags, and scaling curves; avoid conclusions from a single run.
