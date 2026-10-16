---
name: typescript-tuple-variadic-modeling
description: "Use when \"typescript tuple variadic modeling\" is the work. Tuples document positions and lengths; arrays represent variable homogeneous collections."
---

# TypeScript Tuple & Variadic Modeling

Tuples document positions and lengths; arrays represent variable homogeneous collections.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```typescript
type Coordinate = readonly [x: number, y: number];
function distance([x, y]: Coordinate) {
return Math.hypot(x, y);
```

Check: Do not edit the assert to match a surprising result.
