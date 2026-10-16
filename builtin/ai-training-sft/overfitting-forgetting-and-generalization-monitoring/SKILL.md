---
name: overfitting-forgetting-and-generalization-monitoring
description: "Use when \"overfitting forgetting and generalization monitoring\" is the work. Track held-out quality, domain retention, memorization, calibration, and data-dependent failure slices."
---

# Overfitting, Forgetting, and Generalization Monitoring

Track held-out quality, domain retention, memorization, calibration, and data-dependent failure slices.

1. Pin model, tokenizer, dataset, trainer, and dependency revisions.
2. Inspect tokenized examples and label masks.

Example:
```text
Pin model, tokenizer, dataset, trainer, and dependency revisions.
```

Check: Check optimizer groups, schedule units, effective batch size, RNG restoration, evaluation contamination, forgetting, and checkpoint compatibility.
