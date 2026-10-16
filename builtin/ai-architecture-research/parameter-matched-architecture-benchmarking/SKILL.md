---
name: parameter-matched-architecture-benchmarking
description: "Use when \"parameter matched architecture benchmarking\" is the work. Match trainable parameters and account for embedding, tied weights, and inactive expert parameters."
---

# Parameter-Matched Architecture Benchmarking

Match trainable parameters and account for embedding, tied weights, and inactive expert parameters.

1. Pin the paper revision and reference-code commit.
2. Map equations and tensor shapes to implementation modules.
3. Compare parameter-matched and compute-matched baselines using controlled training and evaluation.

Example:
```text
Pin the paper revision and reference-code commit.
```

Check: Report implementation deviations, initialization, seeds, data revisions, training budgets, ablations, and uncertainty; avoid unqualified superiority claims.
