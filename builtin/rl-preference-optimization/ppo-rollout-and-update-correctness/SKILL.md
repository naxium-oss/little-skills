---
name: ppo-rollout-and-update-correctness
description: "Use when \"ppo rollout and update correctness\" is the work. Verify rollout-policy freshness, advantage estimation, clipping, value targets, and minibatch updates."
---

# PPO Rollout and Update Correctness

Verify rollout-policy freshness, advantage estimation, clipping, value targets, and minibatch updates.

1. Pin the algorithm implementation and inspect the actual objective.
2. Audit preference or reward data and reference-policy configuration.

Example:
```text
Pin the algorithm implementation and inspect the actual objective.
```

Check: Validate sign conventions, masking, group statistics, rollout budgets, reward calibration, reference freezing, and exploit resistance.
