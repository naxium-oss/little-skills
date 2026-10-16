---
name: cpu-profiling-and-hotspot-analysis
description: "Use when \"cpu profiling and hotspot analysis\" is the work. Collect symbolized profiles and distinguish wall time, CPU time, blocked time, and sampling bias."
---

# CPU Profiling and Hotspot Analysis

Collect symbolized profiles and distinguish wall time, CPU time, blocked time, and sampling bias.

1. Choose workload distributions and performance budgets before measuring.
2. Isolate warmup, steady state, and teardown.
3. Collect profiles and repeated baseline/candidate samples on comparable hardware.

Example:
```text
Choose workload distributions and performance budgets before measuring.
```

Check: Retain raw samples, sample counts, noise estimates, runtime flags, and scaling curves; avoid conclusions from a single run.
