---
name: sql-numeric-types-rounding-policy
description: "Use when \"sql numeric types rounding policy\" is the work. Fixed-precision decimal types still have scale and overflow behavior."
---

# SQL Numeric Types & Rounding Policy

Fixed-precision decimal types still have scale and overflow behavior.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```sql
SELECT CAST(2.675 AS numeric(8, 2));
-- PostgreSQL illustration: expected 2.68
```

Check: Do not edit the assert to match a surprising result.
