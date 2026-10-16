---
name: deno-deploy-and-edge-runtime-constraints
description: "Use when \"deno deploy and edge runtime constraints\" is the work. assuming full filesystem/network access identical to local development once deployed to an edge isolate runtime."
---

# Deno Deploy and Edge Runtime Constraints

assuming full filesystem/network access identical to local.

1. Do not: assuming full filesystem/network access identical to local development once deployed to an edge isolate.
2. Do not: not checking the platform's specific cold-start and execution-time limits before deploying a long-running task.

Example:
```typescript
Deno.serve((req) => new Response("hello from the edge"));
```

Check: Do not: assuming full filesystem/network access identical to.
