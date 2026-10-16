---
name: typescript-declaration-file-authoring
description: "Use when \"typescript declaration file authoring\" is the work. Declarations describe actual JavaScript behavior; they do not implement it."
---

# TypeScript Declaration File Authoring

Declarations describe actual JavaScript behavior; they do not implement it.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```typescript
// local-math.d.ts, for a matching local module
export declare function twice(value: number): number;
// local-math.js, matching runtime implementation
```

Check: Do not edit the assert to match a surprising result.
