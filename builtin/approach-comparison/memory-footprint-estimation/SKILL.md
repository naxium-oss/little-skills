---
name: memory-footprint-estimation
description: "Use when \"memory footprint estimation\" is the work. Account for objects, indexes, buffers, fragmentation, concurrency, and peak temporary allocations."
---

# Memory Footprint Estimation

Account for objects, indexes, buffers, fragmentation, concurrency, and peak temporary allocations.

1. Extract hard constraints and weighted criteria before comparing alternatives.
2. Compute bounds for memory, latency, and cost with units.
3. Use a representative spike to test the most uncertain assumptions.

Example:
```text
Extract hard constraints and weighted criteria before comparing alternatives.
```

Check: Perform sensitivity analysis; reject incompatible alternatives before ranking; separate measured values from estimates.
