---
name: resolvers-and-the-n-1-query-problem
description: "Use when \"resolvers and the n 1 query problem\" is the work. instantiating a DataLoader instance globally instead of per-request, leaking stale or cross-user cached data."
---

# Resolvers and the N+1 Query Problem

instantiating a DataLoader instance globally instead of.

1. Do not: instantiating a DataLoader instance globally instead of per-request, leaking stale or cross-user cached data.
2. Do not: resolving nested lists without batching and only noticing the N+1 cost under production-scale data.

Example:
```bash
query __schema { types { name } } against the running endpoint
```

Check: Do not: instantiating a DataLoader instance globally instead.
