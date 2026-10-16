---
name: voxel-terrain
description: "Use when \"voxel terrain\", \"infinite voxel terrain\" is the work. Generate terrain that stays consistent as the player moves away and comes back, without growing memory, without seams."
---

# Infinite voxel terrain

Generate terrain that stays consistent as the player moves away and comes back, without growing memory, without seams, and without a frame-time.

1. Everything derives from one world function.
2. Chunking.
3. Meshing.

Example:
```ts
const worldCell = (seed: number, x: number, y: number, z: number): number => {
```

Check: Seams at chunk borders: neighbour data missing when meshing, or a height function that samples noise at the.
