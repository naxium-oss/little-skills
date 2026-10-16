---
name: gltf-loading-and-asset-validation
description: "Use when \"gltf loading and asset validation\" is the work. Validate GLTF structure, extensions, external resources, decoder versions, and failure handling."
---

# GLTF Loading and Asset Validation

Validate GLTF structure, extensions, external resources, decoder versions, and failure handling.

1. Pin the Three.js revision and matching addons.
2. Validate coordinate spaces, asset units, color pipeline, and renderer capabilities.
3. Measure GPU memory and dispose owned resources at lifecycle boundaries.

Example:
```text
Pin the Three.js revision and matching addons.
```

Check: Test asset-load failures, resize, context loss, frustum behavior, GPU limits, and repeated mount/unmount memory use.
