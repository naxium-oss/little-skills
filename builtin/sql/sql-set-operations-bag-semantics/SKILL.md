---
name: sql-set-operations-bag-semantics
description: "Use when \"sql set operations bag semantics\" is the work. UNION deduplicates while UNION ALL preserves multiplicity."
---

# SQL Set Operations & Bag Semantics

UNION deduplicates while UNION ALL preserves multiplicity.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```sql
SELECT 1 AS n UNION ALL SELECT 1;
-- expected: two rows
SELECT 1 AS n UNION SELECT 1;
```

Check: Do not edit the assert to match a surprising result.
