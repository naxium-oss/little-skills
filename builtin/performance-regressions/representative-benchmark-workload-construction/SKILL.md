---
name: representative-benchmark-workload-construction
description: "Use when \"representative benchmark workload construction\" is the work. Build workloads from observed request mixes, data sizes, concurrency, and realistic edge distributions."
---

# Representative Benchmark Workload Construction

Build workloads from observed request mixes, data sizes, concurrency, and realistic edge distributions.

1. Choose workload distributions and performance budgets before measuring.
2. Isolate warmup, steady state, and teardown.
3. Collect profiles and repeated baseline/candidate samples on comparable hardware.

Example:
```text
Choose workload distributions and performance budgets before measuring.
```

Check: Retain raw samples, sample counts, noise estimates, runtime flags, and scaling curves; avoid conclusions from a single run.
