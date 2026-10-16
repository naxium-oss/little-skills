---
name: numerical-stability-and-nan-diagnosis
description: "Use when \"numerical stability and nan diagnosis\" is the work. Locate the first non-finite value and compare scale, precision, clipping, and stable formulations."
---

# Numerical Stability and NaN Diagnosis

Locate the first non-finite value and compare scale, precision, clipping, and stable formulations.

1. Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
2. Audit tensor shape, dtype, device, and gradient flow.

Example:
```text
Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
```

Check: Test numerical tolerances, worker randomness, distributed synchronization, checkpoint round trips, compile fallbacks, and profiler overhead.
