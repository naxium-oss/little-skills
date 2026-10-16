---
name: dataloader-throughput-and-worker-debugging
description: "Use when \"dataloader throughput and worker debugging\" is the work. Measure data wait, worker startup, serialization, shared memory, pinning, and deterministic seeding."
---

# DataLoader Throughput and Worker Debugging

Measure data wait, worker startup, serialization, shared memory, pinning, and deterministic seeding.

1. Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
2. Audit tensor shape, dtype, device, and gradient flow.

Example:
```text
Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
```

Check: Test numerical tolerances, worker randomness, distributed synchronization, checkpoint round trips, compile fallbacks, and profiler overhead.
