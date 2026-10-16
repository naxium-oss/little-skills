---
name: profiler-guided-training-optimization
description: "Use when \"profiler guided training optimization\" is the work. Profile representative steps with synchronization awareness and validate end-to-end gains after optimization."
---

# Profiler-Guided Training Optimization

Profile representative steps with synchronization awareness and validate end-to-end gains after optimization.

1. Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
2. Audit tensor shape, dtype, device, and gradient flow.

Example:
```text
Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
```

Check: Test numerical tolerances, worker randomness, distributed synchronization, checkpoint round trips, compile fallbacks, and profiler overhead.
