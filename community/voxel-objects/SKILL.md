---
name: voxel-objects
description: "Use when \"voxel object\", \"making voxel objects\" is the work. Turn an idea into a voxel model that renders correctly the first time: a cell list with a."
---

# Making voxel objects

Turn an idea into a voxel model that renders correctly the first time: a cell list with a convention, a construction order.

1. Silhouette, one layer thick, from the side the object is recognised from.
2. Depth, extrude the silhouette along the axis that reads as thickness, then trim the corners that.

Example:
```ts
const cells = new Map<string, number>();
```

Check: Off by half a cell: the renderer places a cube's centre at the cell coordinate while the model.
