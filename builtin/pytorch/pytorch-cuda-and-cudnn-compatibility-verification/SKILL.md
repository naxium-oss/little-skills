---
name: pytorch-cuda-and-cudnn-compatibility-verification
description: "Use when \"pytorch cuda and cudnn compatibility verification\" is the work. Distinguish driver, toolkit, bundled CUDA, cuDNN, architecture support, and installed wheel build."
---

# PyTorch, CUDA, and cuDNN Compatibility Verification

Distinguish driver, toolkit, bundled CUDA, cuDNN.

1. Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
2. Audit tensor shape, dtype, device, and gradient flow.

Example:
```text
Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
```

Check: Test numerical tolerances, worker randomness, distributed synchronization, checkpoint round trips, compile fallbacks, and profiler overhead.
