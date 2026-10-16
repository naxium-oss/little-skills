---
name: supervised-example-formatting-and-label-masking
description: "Use when \"supervised example formatting and label masking\" is the work. Decode inputs and labels side by side and verify masking excludes unintended prompt and padding tokens."
---

# Supervised Example Formatting and Label Masking

Decode inputs and labels side by side and verify masking excludes unintended prompt and padding tokens.

1. Pin model, tokenizer, dataset, trainer, and dependency revisions.
2. Inspect tokenized examples and label masks.

Example:
```text
Pin model, tokenizer, dataset, trainer, and dependency revisions.
```

Check: Check optimizer groups, schedule units, effective batch size, RNG restoration, evaluation contamination, forgetting, and checkpoint compatibility.
