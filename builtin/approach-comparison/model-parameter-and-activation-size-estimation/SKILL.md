---
name: model-parameter-and-activation-size-estimation
description: "Use when \"model parameter and activation size estimation\" is the work. Calculate parameter, gradient, optimizer-state, activation, and temporary workspace memory separately."
---

# Model Parameter and Activation Size Estimation

Calculate parameter, gradient, optimizer-state, activation, and temporary workspace memory separately.

1. Extract hard constraints and weighted criteria before comparing alternatives.
2. Compute bounds for memory, latency, and cost with units.
3. Use a representative spike to test the most uncertain assumptions.

Example:
```text
Extract hard constraints and weighted criteria before comparing alternatives.
```

Check: Perform sensitivity analysis; reject incompatible alternatives before ranking; separate measured values from estimates.
