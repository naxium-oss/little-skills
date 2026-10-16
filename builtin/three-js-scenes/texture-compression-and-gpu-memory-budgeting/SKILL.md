---
name: texture-compression-and-gpu-memory-budgeting
description: "Use when \"texture compression and gpu memory budgeting\" is the work. Verify supported compressed texture formats and estimate mipmapped GPU allocation, not file size."
---

# Texture Compression and GPU Memory Budgeting

Verify supported compressed texture formats and estimate mipmapped GPU allocation, not file size.

1. Pin the Three.js revision and matching addons.
2. Validate coordinate spaces, asset units, color pipeline, and renderer capabilities.

Example:
```text
Pin the Three.js revision and matching addons.
```

Check: Test asset-load failures, resize, context loss, frustum behavior, GPU limits, and repeated mount/unmount memory use.
