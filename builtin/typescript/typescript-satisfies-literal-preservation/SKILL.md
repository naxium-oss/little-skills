---
name: typescript-satisfies-literal-preservation
description: "Use when \"typescript satisfies literal preservation\" is the work. satisfies checks assignability without replacing the expression type with the target type."
---

# TypeScript satisfies & Literal Preservation

satisfies checks assignability without replacing the expression type with the target type.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```typescript
type Route = { path: string; method: "GET" | "POST" };
const route = { path: "/items", method: "GET" } satisfies Route;
```

Check: Do not edit the assert to match a surprising result.
