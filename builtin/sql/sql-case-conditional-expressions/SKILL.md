---
name: sql-case-conditional-expressions
description: "Use when \"sql case conditional expressions\" is the work. CASE without ELSE returns NULL when no branch matches."
---

# SQL CASE & Conditional Expressions

CASE without ELSE returns NULL when no branch matches.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```sql
SELECT n, CASE
WHEN n < 0 THEN 'negative'
WHEN n = 0 THEN 'zero'
```

Check: Do not edit the assert to match a surprising result.
