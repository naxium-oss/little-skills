---
name: node-compatibility-layer-verification
description: "Use when \"node compatibility layer verification\" is the work. assuming a popular npm package just works under Deno without running its actual test suite in the target."
---

# Node Compatibility Layer Verification

assuming a popular npm package "just works" under Deno.

1. Do not: assuming a popular npm package "just works" under Deno without running its actual test.
2. Do not: hitting a native Node addon dependency that has no Deno-compatible equivalent, blocking migration entirely.

Example:
```typescript
import { readFileSync } from "node:fs";
```

Check: Do not: assuming a popular npm package "just works" under Deno without running its actual test suite in.
