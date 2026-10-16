---
name: native-typescript-and-jsx-execution
description: "Use when \"native typescript and jsx execution\" is the work. treating a successful bun run as proof of type safety."
---

# Native TypeScript and JSX Execution

treating a successful bun run as proof of type safety.

1. Do not: treating a successful bun run as proof of type safety.
2. Do not: relying on decorators or TS features Bun's transpiler doesn't yet support without checking the.

Example:
```bash
bun run src/index.tsx
bunx tsc --noEmit         # separate type-check pass
```

Check: Do not: treating a successful bun run as proof of type safety.
