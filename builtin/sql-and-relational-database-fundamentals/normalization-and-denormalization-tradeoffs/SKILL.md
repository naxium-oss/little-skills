---
name: normalization-and-denormalization-tradeoffs
description: "Use when \"normalization and denormalization tradeoffs\" is the work. over-normalizing a read-heavy analytics workload, forcing expensive multi-way joins on every dashboard query."
---

# Normalization and Denormalization Tradeoffs

over-normalizing a read-heavy analytics workload, forcing.

1. Do not: over-normalizing a read-heavy analytics workload, forcing expensive multi-way joins on every dashboard query.
2. Do not: denormalizing without a clear update strategy, letting duplicated data silently drift out of sync.

Example:
```sql
-- Normalized: avoids storing customer name redundantly on every order
```

Check: Do not: over-normalizing a read-heavy analytics workload.
