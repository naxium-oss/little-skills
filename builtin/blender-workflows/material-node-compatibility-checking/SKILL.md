---
name: material-node-compatibility-checking
description: "Use when \"material node compatibility checking\" is the work. Confirm supported nodes and rendering differences across Blender engines and export targets."
---

# Material Node Compatibility Checking

Confirm supported nodes and rendering differences across Blender engines and export targets.

1. Verify Blender build, Python API, addons, and renderer configuration.
2. Normalize units and transforms without destroying source assets.
3. Validate topology, materials, animation, and export in a round-trip fixture.

Example:
```text
Verify Blender build, Python API, addons, and renderer configuration.
```

Check: Keep original files; compare geometry, normals, texture paths, skin weights, and animation timing after import into the target.
