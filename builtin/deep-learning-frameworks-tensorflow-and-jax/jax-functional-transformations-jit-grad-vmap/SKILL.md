---
name: jax-functional-transformations-jit-grad-vmap
description: "Use when \"jax functional transformations jit grad vmap\" is the work."
---

# JAX Functional Transformations: jit, grad, vmap

attempting in-place array mutation (arr[0] = 1).

1. Do not: attempting in-place array mutation (arr[0] = 1) instead of arr.at[0].set(1), hitting an immutability error.
2. Do not: wrapping a function with Python-level side effects (logging counters, random without an explicit PRNG.

Example:
```bash
print the framework version, accelerator list, and default dtype policy
```

Check: Do not: attempting in-place.
