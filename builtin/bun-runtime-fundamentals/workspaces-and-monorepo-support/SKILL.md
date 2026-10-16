---
name: workspaces-and-monorepo-support
description: "Use when \"workspaces and monorepo support\" is the work. assuming pnpm-specific workspace features (like strict dependency isolation) apply identically under Bun."
---

# Workspaces and Monorepo Support

assuming pnpm-specific workspace features (like strict dependency isolation) apply identically under Bun.

1. Do not: assuming pnpm-specific workspace features (like strict dependency isolation) apply identically under Bun.
2. Do not: forgetting to re-run install after adding a new workspace package.

Example:
```json
{ "name": "root", "workspaces": ["packages/*"] }
```

Check: Do not: assuming pnpm-specific workspace features (like strict dependency isolation) apply identically under Bun.
