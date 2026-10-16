---
name: lora-target-module-and-rank-selection
description: "Use when \"lora target module and rank selection\" is the work. Inspect actual module names and compare rank and alpha settings with held-out task evidence."
---

# LoRA Target Module and Rank Selection

Inspect actual module names and compare rank and alpha settings with held-out task evidence.

1. Pin model, tokenizer, dataset, trainer, and dependency revisions.
2. Inspect tokenized examples and label masks.

Example:
```text
Pin model, tokenizer, dataset, trainer, and dependency revisions.
```

Check: Check optimizer groups, schedule units, effective batch size, RNG restoration, evaluation contamination, forgetting, and checkpoint compatibility.
