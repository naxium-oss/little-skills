---
name: scene-graph-and-transform-debugging
description: "Use when \"scene graph and transform debugging\" is the work. Distinguish local and world transforms and verify update order, parenting, and matrix conventions."
---

# Scene Graph and Transform Debugging

Distinguish local and world transforms and verify update order, parenting, and matrix conventions.

1. Pin the Three.js revision and matching addons.
2. Validate coordinate spaces, asset units, color pipeline, and renderer capabilities.
3. Measure GPU memory and dispose owned resources at lifecycle boundaries.

Example:
```text
Pin the Three.js revision and matching addons.
```

Check: Test asset-load failures, resize, context loss, frustum behavior, GPU limits, and repeated mount/unmount memory use.
