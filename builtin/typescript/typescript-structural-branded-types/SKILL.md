---
name: typescript-structural-branded-types
description: "Use when \"typescript structural branded types\" is the work. Brands add compile-time distinctions but no runtime checks."
---

# TypeScript Structural & Branded Types

Brands add compile-time distinctions but no runtime checks.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```typescript
declare const userBrand: unique symbol;
type UserId = string & { readonly [userBrand]: true };
function userId(value: string): UserId {
```

Check: Do not edit the assert to match a surprising result.
