---
name: rl-stability-and-sample-efficiency-comparison
description: "Use when \"rl stability and sample efficiency comparison\" is the work. Normalize environment interactions and compute while reporting seed variance and failed runs."
---

# RL Stability and Sample Efficiency Comparison

Normalize environment interactions and compute while reporting seed variance and failed runs.

1. Pin the algorithm implementation and inspect the actual objective.
2. Audit preference or reward data and reference-policy configuration.
3. Run small controlled updates with logged rewards, KL, gradients, and held-out behavior.

Example:
```text
Pin the algorithm implementation and inspect the actual objective.
```

Check: Validate sign conventions, masking, group statistics, rollout budgets, reward calibration, reference freezing, and exploit resistance.
