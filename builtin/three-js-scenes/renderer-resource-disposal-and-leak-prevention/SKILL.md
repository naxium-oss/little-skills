---
name: renderer-resource-disposal-and-leak-prevention
description: "Use when \"renderer resource disposal and leak prevention\" is the work. Track ownership of geometries, materials, textures, render targets, listeners, and renderer resources."
---

# Renderer Resource Disposal and Leak Prevention

Track ownership of geometries, materials, textures, render targets, listeners, and renderer resources.

1. Pin the Three.js revision and matching addons.
2. Validate coordinate spaces, asset units, color pipeline, and renderer capabilities.

Example:
```text
Pin the Three.js revision and matching addons.
```

Check: Test asset-load failures, resize, context loss, frustum behavior, GPU limits, and repeated mount/unmount memory use.
