---
name: sql-collations-text-comparison
description: "Use when \"sql collations text comparison\" is the work. Collation controls comparison semantics and can affect indexes and uniqueness."
---

# SQL Collations & Text Comparison

Collation controls comparison semantics and can affect indexes and uniqueness.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```sql
SELECT value FROM (VALUES ('a'), ('B'), ('A')) AS input(value)
ORDER BY value COLLATE "C";
-- PostgreSQL C collation illustration: A, B, a
```

Check: Do not edit the assert to match a surprising result.
