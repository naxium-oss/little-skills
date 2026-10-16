---
name: mutations-optimistic-updates-and-cache-consistency
description: "Use when \"mutations optimistic updates and cache consistency\" is the work. returning a mutation response missing fields other active queries depend on, leaving those queries cached data stale until."
---

# Mutations, Optimistic Updates, and Cache Consistency

returning a mutation response missing.

1. Do not: returning a mutation response missing fields other active queries depend on, leaving those queries'.
2. Do not: configuring optimistic updates without proper rollback handling, leaving the UI in an inconsistent state.

Example:
```bash
query __schema { types { name } } against the running endpoint
```

Check: Do not: returning a mutation response missing fields other active queries depend on, leaving those queries' cached data.
