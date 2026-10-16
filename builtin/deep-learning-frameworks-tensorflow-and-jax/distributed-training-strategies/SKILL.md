---
name: distributed-training-strategies
description: "Use when \"distributed training strategies\" is the work. assuming multi-GPU training scales linearly without measuring actual wall-clock speedup, missing that communication overhead can dominate for small."
---

# Distributed Training Strategies

assuming multi-GPU training scales linearly.

1. Do not: assuming multi-GPU training scales linearly without measuring actual wall-clock speedup, missing that communication overhead.
2. Do not: forgetting to scale the learning rate (or use a warmup) when increasing global batch.

Example:
```bash
print the framework version, accelerator list, and default dtype policy
```

Check: Do not: assuming multi-GPU training scales linearly without measuring actual wall-clock speedup, missing that communication overhead can dominate.
