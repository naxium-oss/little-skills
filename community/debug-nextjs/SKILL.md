---
name: debug-nextjs
description: "Use when \"nextjs Hydration mismatch\", \"Hydration mismatch\". Not when explaining working nextjs code."
---

# Debug nextjs

Reproduce the nextjs failure with the project command, then change one thing.

1. Hydration mismatch: Server and client render different HTML (Date.now, Math.random, localStorage); make the dynamic part client-only.
2. Server-only code in a client component: Importing Node APIs or secrets in a component with 'use.
3. Data stale: Caching: check `revalidate`, `fetch` cache options, and the router cache; force a fresh request.

Example:
```text
npm run build
```

Check: The same command that failed has to pass.
