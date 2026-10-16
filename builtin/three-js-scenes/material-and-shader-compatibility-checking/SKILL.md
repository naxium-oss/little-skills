---
name: material-and-shader-compatibility-checking
description: "Use when \"material and shader compatibility checking\" is the work. Verify shader language, defines, material features, renderer backend, and GPU capability requirements."
---

# Material and Shader Compatibility Checking

Verify shader language, defines, material features, renderer backend, and GPU capability requirements.

1. Pin the Three.js revision and matching addons.
2. Validate coordinate spaces, asset units, color pipeline, and renderer capabilities.

Example:
```text
Pin the Three.js revision and matching addons.
```

Check: Test asset-load failures, resize, context loss, frustum behavior, GPU limits, and repeated mount/unmount memory use.
