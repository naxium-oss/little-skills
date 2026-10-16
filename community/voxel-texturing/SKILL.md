---
name: voxel-texturing
description: "Use when \"voxel texture\", \"texturing 3d voxels\" is the work. Give voxels a surface without breaking the two things that make voxel rendering fast: instancing and a handful."
---

# Texturing 3D voxels

Give voxels a surface without breaking the two things that make voxel rendering fast: instancing and a handful of draw calls.

1. One tile per material: split the world into one InstancedMesh per tile.
2. Per-face UV attribute in the geometry: build a box whose six faces each carry the UVs.

Example:
```text
One tile per material: split the world into one InstancedMesh per tile.
```

Check: Say not run when the check did not run.
