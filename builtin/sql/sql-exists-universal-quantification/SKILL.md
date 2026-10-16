---
name: sql-exists-universal-quantification
description: "Use when \"sql exists universal quantification\" is the work. EXISTS checks whether any row qualifies."
---

# SQL EXISTS & Universal Quantification

EXISTS checks whether any row qualifies.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```sql
SELECT EXISTS (SELECT 1 FROM (VALUES (1), (2)) AS v(n) WHERE n > 1);
-- expected: true
SELECT NOT EXISTS (
```

Check: Do not edit the assert to match a surprising result.
