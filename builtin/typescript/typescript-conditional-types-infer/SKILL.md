---
name: typescript-conditional-types-infer
description: "Use when \"typescript conditional types infer\" is the work. A conditional with a naked type parameter distributes over unions."
---

# TypeScript Conditional Types & infer

A conditional with a naked type parameter distributes over unions.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```typescript
type ElementOf<T> = T extends readonly (infer U)[] ? U : never;
type Item = ElementOf<readonly string[]>;
const item: Item = "ok";
```

Check: Do not edit the assert to match a surprising result.
