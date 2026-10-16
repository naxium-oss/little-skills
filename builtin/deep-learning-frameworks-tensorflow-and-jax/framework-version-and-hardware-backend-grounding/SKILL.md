---
name: framework-version-and-hardware-backend-grounding
description: "Use when \"framework version and hardware backend grounding\" is the work. assuming GPU is in use because code runs without checking tf.config.list_physical_devices(GPU)/jax.devices() actually lists an accelerator."
---

# Framework Version and Hardware Backend Grounding

assuming GPU is in use because code.

1. Do not: assuming GPU is in use because code "runs" without checking tf.config.list_physical_devices('GPU')/jax.devices() actually lists an.
2. Do not: mixing TensorFlow versions with incompatible Keras versions installed separately.

Example:
```bash
print the framework version, accelerator list, and default dtype policy
```

Check: Do not: assuming GPU.
