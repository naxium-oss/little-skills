---
name: distributeddataparallel-correctness
description: "Use when \"distributeddataparallel correctness\" is the work. Verify rank-local data sharding, gradient synchronization, unused parameters, and collective order."
---

# DistributedDataParallel Correctness

Verify rank-local data sharding, gradient synchronization, unused parameters, and collective order.

1. Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
2. Audit tensor shape, dtype, device, and gradient flow.
3. Reduce failures to a small deterministic training step before optimizing.

Example:
```text
Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
```

Check: Test numerical tolerances, worker randomness, distributed synchronization, checkpoint round trips, compile fallbacks, and profiler overhead.
