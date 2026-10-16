---
name: route-handlers-middleware-and-edge-runtime
description: "Use when \"route handlers middleware and edge runtime\" is the work. using fs, crypto (Node variant), or large native dependencies inside Edge middleware and hitting a build error."
---

# Route Handlers, Middleware, and Edge Runtime

using fs, crypto (Node variant), or large native.

1. Do not: using fs, crypto (Node variant), or large native dependencies inside Edge middleware and hitting.
2. Do not: assuming middleware runs after route handlers rather than before, missing its actual request-interception order.

Example:
```typescript
// app/api/users/route.ts
```

Check: Do not: using fs.
