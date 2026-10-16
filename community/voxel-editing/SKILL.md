---
name: voxel-editing
description: "Use when \"edit voxels\", \"editing voxel objects\" is the work."
---

# Editing voxel objects

Apply a change to a model that already exists, without regenerating.

1. Format: a .vox/JSON cell list, an array in a source file, a generated script, an exported.
2. Convention: cell size, origin, axis order.

Example:
```text
Format: a .vox/JSON cell list, an array in a source file, a generated script.
```

Check: The edit vanished: written to a generated file that was then regenerated, or written to the wrong coordinate.
