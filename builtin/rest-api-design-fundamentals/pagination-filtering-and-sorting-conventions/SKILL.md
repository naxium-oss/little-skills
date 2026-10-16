---
name: pagination-filtering-and-sorting-conventions
description: "Use when \"pagination filtering and sorting conventions\" is the work. using offset pagination on a frequently-mutated table, causing items to be skipped or duplicated across pages."
---

# Pagination, Filtering, and Sorting Conventions

using offset pagination on a frequently-mutated table, causing.

1. Do not: using offset pagination on a frequently-mutated table, causing items to be skipped or duplicated.
2. Do not: sorting without a unique tie-breaker field, producing nondeterministic page boundaries.

Example:
```bash
curl -sS -D - <endpoint> -o /dev/null
```

Check: Do not: using offset pagination on a frequently-mutated table.
