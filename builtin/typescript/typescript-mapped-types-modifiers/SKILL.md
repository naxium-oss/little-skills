---
name: typescript-mapped-types-modifiers
description: "Use when \"typescript mapped types modifiers\" is the work. Mapped types iterate property keys."
---

# TypeScript Mapped Types & Modifiers

Mapped types iterate property keys.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```typescript
type Mutable<T> = { -readonly [K in keyof T]: T[K] };
type Point = Mutable<{ readonly x: number }>;
const p: Point = { x: 1 };
```

Check: Do not edit the assert to match a surprising result.
