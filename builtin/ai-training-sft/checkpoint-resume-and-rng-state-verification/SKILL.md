---
name: checkpoint-resume-and-rng-state-verification
description: "Use when \"checkpoint resume and rng state verification\" is the work. Restore model, optimizer, scheduler, scaler, sampler, and all RNG states and compare continuation."
---

# Checkpoint Resume and RNG State Verification

Restore model, optimizer, scheduler, scaler, sampler, and all RNG states and compare continuation.

1. Pin model, tokenizer, dataset, trainer, and dependency revisions.
2. Inspect tokenized examples and label masks.

Example:
```text
Pin model, tokenizer, dataset, trainer, and dependency revisions.
```

Check: Check optimizer groups, schedule units, effective batch size, RNG restoration, evaluation contamination, forgetting, and checkpoint compatibility.
