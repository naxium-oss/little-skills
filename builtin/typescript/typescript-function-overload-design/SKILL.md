---
name: typescript-function-overload-design
description: "Use when \"typescript function overload design\" is the work. Overload signatures define the public callable surface."
---

# TypeScript Function Overload Design

Overload signatures define the public callable surface.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```typescript
function lengthOf(value: string): number;
function lengthOf(value: unknown[]): number;
function lengthOf(value: string | unknown[]): number {
```

Check: Do not edit the assert to match a surprising result.
