---
name: cross-version-performance-comparison
description: "Use when \"cross version performance comparison\" is the work. Use identical artifacts and workload controls while changing only the runtime or dependency version."
---

# Cross-Version Performance Comparison

Use identical artifacts and workload controls while changing only the runtime or dependency version.

1. Choose workload distributions and performance budgets before measuring.
2. Isolate warmup, steady state, and teardown.
3. Collect profiles and repeated baseline/candidate samples on comparable hardware.

Example:
```text
Choose workload distributions and performance budgets before measuring.
```

Check: Retain raw samples, sample counts, noise estimates, runtime flags, and scaling curves; avoid conclusions from a single run.
