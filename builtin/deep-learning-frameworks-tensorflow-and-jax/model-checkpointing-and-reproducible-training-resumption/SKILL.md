---
name: model-checkpointing-and-reproducible-training-resumption
description: "Use when \"model checkpointing and reproducible training resumption\" is the work. checkpointing only model weights and not optimizer state, causing a resumed runs adaptive optimizer (Adam, etc.) to restart."
---

# Model Checkpointing and Reproducible Training Resumption

checkpointing only model weights and.

1. Do not: checkpointing only model weights and not optimizer state, causing a resumed run's adaptive optimizer.
2. Do not: assuming a restored checkpoint guarantees full reproducibility without also fixing the data pipeline's shuffle.

Example:
```bash
print the framework version, accelerator list, and default dtype policy
```

Check: Do not: checkpointing only model weights and not optimizer.
