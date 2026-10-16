---
name: dpo-objective-and-reference-model-verification
description: "Use when \"dpo objective and reference model verification\" is the work. Check log-probability sums, sequence masking, beta convention, and frozen reference behavior."
---

# DPO Objective and Reference Model Verification

Check log-probability sums, sequence masking, beta convention, and frozen reference behavior.

1. Pin the algorithm implementation and inspect the actual objective.
2. Audit preference or reward data and reference-policy configuration.

Example:
```text
Pin the algorithm implementation and inspect the actual objective.
```

Check: Validate sign conventions, masking, group statistics, rollout budgets, reward calibration, reference freezing, and exploit resistance.
