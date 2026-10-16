---
name: instruction-data-mixture-design
description: "Use when \"instruction data mixture design\" is the work. Specify source proportions, sampling, deduplication, quality gates, and domain evaluation coverage."
---

# Instruction Data Mixture Design

Specify source proportions, sampling, deduplication, quality gates, and domain evaluation coverage.

1. Pin model, tokenizer, dataset, trainer, and dependency revisions.
2. Inspect tokenized examples and label masks.
3. Run an overfit-on-small-batch check before a budgeted full experiment.

Example:
```text
Pin model, tokenizer, dataset, trainer, and dependency revisions.
```

Check: Check optimizer groups, schedule units, effective batch size, RNG restoration, evaluation contamination, forgetting, and checkpoint compatibility.
