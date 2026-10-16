---
name: typescript-template-literal-types
description: "Use when \"typescript template literal types\" is the work. Template literal types enumerate combinations of finite unions."
---

# TypeScript Template Literal Types

Template literal types enumerate combinations of finite unions.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```typescript
type EventName = `${"user" | "team"}:${"created" | "deleted"}`;
const event: EventName = "user:created";
// @ts-expect-error invalid suffix
```

Check: Do not edit the assert to match a surprising result.
