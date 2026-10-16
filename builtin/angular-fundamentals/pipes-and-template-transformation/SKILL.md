---
name: pipes-and-template-transformation
description: "Use when \"pipes and template transformation\" is the work. marking a pipe pure: false for convenience, causing it to run on every change-detection cycle across the whole."
---

# Pipes and Template Transformation

marking a pipe pure: false.

1. Do not: marking a pipe pure: false for convenience, causing it to run on every change-detection.
2. Do not: mutating an array/object in place and expecting a pure pipe watching it to re-render.

Example:
```typescript
@Pipe({ name: "truncate" })
```

Check: Do not: marking a pipe pure: false for convenience, causing it to run on every change-detection cycle across.
