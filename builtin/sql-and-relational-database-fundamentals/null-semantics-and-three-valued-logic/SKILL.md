---
name: null-semantics-and-three-valued-logic
description: "Use when \"null semantics and three valued logic\" is the work. using NOT IN (SELECT ...) against a subquery that can return NULL, causing the entire NOT IN to."
---

# NULL Semantics and Three-Valued Logic

using NOT IN (SELECT ...).

1. Do not: using NOT IN (SELECT ...) against a subquery that can return NULL, causing the.
2. Do not: assuming AVG treats NULL as 0 instead of excluding it from the divisor.

Example:
```sql
SELECT * FROM users WHERE deleted_at IS NULL;         -- correct
```

Check: Do not: using NOT IN (SELECT ...) against a subquery that can return NULL, causing the entire NOT.
