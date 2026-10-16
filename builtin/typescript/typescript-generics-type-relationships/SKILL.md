---
name: typescript-generics-type-relationships
description: "Use when \"typescript generics type relationships\" is the work. Use one type parameter for values that must remain related."
---

# TypeScript Generics & Type Relationships

Use one type parameter for values that must remain related.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```typescript
function first<T>(values: readonly T[]): T | undefined {
return values[0];
}
```

Check: Do not edit the assert to match a surprising result.
