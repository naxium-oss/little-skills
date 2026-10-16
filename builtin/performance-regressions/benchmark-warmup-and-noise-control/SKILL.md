---
name: benchmark-warmup-and-noise-control
description: "Use when \"benchmark warmup and noise control\" is the work. Separate cold start, warmup, and steady state; control background load and execution order."
---

# Benchmark Warmup and Noise Control

Separate cold start, warmup, and steady state; control background load and execution order.

1. Choose workload distributions and performance budgets before measuring.
2. Isolate warmup, steady state, and teardown.
3. Collect profiles and repeated baseline/candidate samples on comparable hardware.

Example:
```text
Choose workload distributions and performance budgets before measuring.
```

Check: Retain raw samples, sample counts, noise estimates, runtime flags, and scaling curves; avoid conclusions from a single run.
