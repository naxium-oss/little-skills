---
name: positional-encoding-compatibility-analysis
description: "Use when \"positional encoding compatibility analysis\" is the work. Verify positional indexing, length extension, cached decoding offsets, and checkpoint compatibility."
---

# Positional Encoding Compatibility Analysis

Verify positional indexing, length extension, cached decoding offsets, and checkpoint compatibility.

1. Pin the paper revision and reference-code commit.
2. Map equations and tensor shapes to implementation modules.
3. Compare parameter-matched and compute-matched baselines using controlled training and evaluation.

Example:
```text
Pin the paper revision and reference-code commit.
```

Check: Report implementation deviations, initialization, seeds, data revisions, training budgets, ablations, and uncertainty; avoid unqualified superiority claims.
