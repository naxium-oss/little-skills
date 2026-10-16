---
name: autograd-graph-and-gradient-debugging
description: "Use when \"autograd graph and gradient debugging\" is the work. Inspect leaf status, detach paths, in-place updates, gradient accumulation, and missing gradients."
---

# Autograd Graph and Gradient Debugging

Inspect leaf status, detach paths, in-place updates, gradient accumulation, and missing gradients.

1. Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
2. Audit tensor shape, dtype, device, and gradient flow.

Example:
```text
Verify PyTorch build, accelerator runtime, driver, hardware, and distributed configuration.
```

Check: Test numerical tolerances, worker randomness, distributed synchronization, checkpoint round trips, compile fallbacks, and profiler overhead.
