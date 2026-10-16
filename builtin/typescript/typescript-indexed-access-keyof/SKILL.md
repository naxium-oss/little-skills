---
name: typescript-indexed-access-keyof
description: "Use when \"typescript indexed access keyof\" is the work. K extends keyof T restricts valid keys while T[K] preserves the selected property type."
---

# TypeScript Indexed Access & keyof

K extends keyof T restricts valid keys while T[K] preserves the selected property type.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```typescript
function get<T, K extends keyof T>(obj: T, key: K): T[K] {
```

Check: Do not edit the assert to match a surprising result.
