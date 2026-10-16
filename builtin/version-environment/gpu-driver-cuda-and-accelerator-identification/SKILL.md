---
name: gpu-driver-cuda-and-accelerator-identification
description: "Use when \"gpu driver cuda and accelerator identification\" is the work. Distinguish driver-supported CUDA from the installed toolkit and the framework-bundled runtime."
---

# GPU, Driver, CUDA, and Accelerator Identification

Distinguish driver-supported CUDA from the installed toolkit and the framework-bundled runtime.

1. Identify the actual executable or service endpoint used by the failing process.
2. Compare shell resolution with the application process.
3. Collect a machine-readable environment manifest.

Example:
```text
Identify the actual executable or service endpoint used by the failing process.
```

Check: Repeat the check in a clean shell and the real execution context; explain every mismatch.
