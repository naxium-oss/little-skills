---
name: full-fine-tuning-versus-peft-comparison
description: "Use when \"full fine tuning versus peft comparison\" is the work. Compare quality, memory, optimizer state, throughput, merge behavior, and deployment constraints fairly."
---

# Full Fine-Tuning versus PEFT Comparison

Compare quality, memory, optimizer state, throughput, merge behavior, and deployment constraints fairly.

1. Pin model, tokenizer, dataset, trainer, and dependency revisions.
2. Inspect tokenized examples and label masks.

Example:
```text
Pin model, tokenizer, dataset, trainer, and dependency revisions.
```

Check: Check optimizer groups, schedule units, effective batch size, RNG restoration, evaluation contamination, forgetting, and checkpoint compatibility.
