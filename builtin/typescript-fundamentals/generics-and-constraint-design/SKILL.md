---
name: generics-and-constraint-design
description: "Use when \"generics and constraint design\" is the work. overusing generics where a union or simple overload would be clearer."
---

# Generics and Constraint Design

overusing generics where a union or simple overload would be clearer.

1. Do not: overusing generics where a union or simple overload would be clearer.
2. Do not: forgetting constraints, causing T to infer as unknown and requiring casts downstream.

Example:
```typescript
function pluck<T, K extends keyof T>(items: T[], key: K): T[K][] {
return items.map((item) => item[key]);
}
```

Check: Do not: overusing generics where a union or simple overload would be clearer.
