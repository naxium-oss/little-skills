---
name: tensor-shape-dtype-and-device-auditing
description: "Use when \"tensor shape dtype and device auditing\" is the work. Record tensor dimensions, strides, dtype, device, layout, and expected broadcasting at boundaries."
---

# Tensor Shape, Dtype, and Device Auditing

Record tensor dimensions, strides, dtype, device.

1. Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
2. Audit tensor shape, dtype, device, and gradient flow.

Example:
```text
Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
```

Check: Test numerical tolerances, worker randomness, distributed synchronization, checkpoint round trips, compile fallbacks, and profiler overhead.
