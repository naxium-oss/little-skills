---
name: torch-compile-graph-break-diagnosis
description: "Use when \"torch compile graph break diagnosis\" is the work. Capture graph-break diagnostics and separate unsupported operations from dynamic-shape recompilation."
---

# torch.compile Graph Break Diagnosis

Capture graph-break diagnostics and separate unsupported operations from dynamic-shape recompilation.

1. Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
2. Audit tensor shape, dtype, device, and gradient flow.

Example:
```text
Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
```

Check: Test numerical tolerances, worker randomness, distributed synchronization, checkpoint round trips, compile fallbacks, and profiler overhead.
