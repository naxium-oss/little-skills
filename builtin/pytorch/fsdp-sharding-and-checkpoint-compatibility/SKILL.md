---
name: fsdp-sharding-and-checkpoint-compatibility
description: "Use when \"fsdp sharding and checkpoint compatibility\" is the work. Pin sharding strategy and checkpoint format and test save/load across intended world sizes."
---

# FSDP Sharding and Checkpoint Compatibility

Pin sharding strategy and checkpoint format and test save/load across intended world sizes.

1. Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
2. Audit tensor shape, dtype, device, and gradient flow.

Example:
```text
Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
```

Check: Test numerical tolerances, worker randomness, distributed synchronization, checkpoint round trips, compile fallbacks, and profiler overhead.
