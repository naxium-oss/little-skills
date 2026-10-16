---
name: automatic-mixed-precision-configuration
description: "Use when \"automatic mixed precision configuration\" is the work. Verify autocast scope, scaler behavior, accumulation, optimizer steps, and dtype-sensitive operations."
---

# Automatic Mixed Precision Configuration

Verify autocast scope, scaler behavior, accumulation, optimizer steps, and dtype-sensitive operations.

1. Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
2. Audit tensor shape, dtype, device, and gradient flow.

Example:
```text
Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
```

Check: Test numerical tolerances, worker randomness, distributed synchronization, checkpoint round trips, compile fallbacks, and profiler overhead.
