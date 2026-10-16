---
name: structural-typing-and-type-narrowing
description: "Use when \"structural typing and type narrowing\" is the work. using as casts to silence narrowing instead of fixing the discriminant."
---

# Structural Typing and Type Narrowing

using as casts to silence narrowing instead of fixing the discriminant.

1. Do not: using as casts to silence narrowing instead of fixing the discriminant.
2. Do not: forgetting an exhaustiveness check, so new union members compile silently unhandled.

Example:
```typescript
type Shape =
| { kind: "circle"; radius: number }
| { kind: "rect"; width: number; height: number };
```

Check: Do not: using as casts to silence narrowing instead of fixing the discriminant.
