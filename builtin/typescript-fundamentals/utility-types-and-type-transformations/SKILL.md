---
name: utility-types-and-type-transformations
description: "Use when \"utility types and type transformations\" is the work. manually duplicating a shape derived from another type instead of using Pick/Omit, causing drift when the source type."
---

# Utility Types and Type Transformations

manually duplicating a shape derived from another type instead.

1. Do not: manually duplicating a shape derived from another type instead of using Pick/Omit, causing drift.
2. Do not: Reasoning about types without checking tsconfig strictness.

Example:
```typescript
interface User { id: number; name: string; email: string; }
```

Check: Do not: manually duplicating a shape derived from another type instead of using Pick/Omit, causing drift when the.
