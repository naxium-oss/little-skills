---
name: mixed-precision-and-numerical-stability
description: "Use when \"mixed precision and numerical stability\" is the work. enabling mixed precision on hardware without Tensor Core support, gaining no speedup while adding complexity."
---

# Mixed Precision and Numerical Stability

enabling mixed precision on hardware without Tensor Core support, gaining no speedup while adding complexity.

1. Do not: enabling mixed precision on hardware without Tensor Core support, gaining no speedup while adding.
2. Do not: skipping loss scaling with float16, causing gradient underflow that silently stalls training with no.

Example:
```bash
print the framework version, accelerator list, and default dtype policy
```

Check: Do not: enabling mixed precision on hardware without Tensor Core support, gaining no speedup while adding complexity.
