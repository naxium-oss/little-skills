---
name: optimizer-and-learning-rate-schedule-validation
description: "Use when \"optimizer and learning rate schedule validation\" is the work. Verify parameter groups, weight decay exclusions, step counts, warmup, and effective batch size."
---

# Optimizer and Learning-Rate Schedule Validation

Verify parameter groups, weight decay exclusions, step counts, warmup, and effective batch size.

1. Pin model, tokenizer, dataset, trainer, and dependency revisions.
2. Inspect tokenized examples and label masks.

Example:
```text
Pin model, tokenizer, dataset, trainer, and dependency revisions.
```

Check: Check optimizer groups, schedule units, effective batch size, RNG restoration, evaluation contamination, forgetting, and checkpoint compatibility.
