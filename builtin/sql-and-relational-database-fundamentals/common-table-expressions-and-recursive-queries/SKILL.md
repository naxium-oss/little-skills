---
name: common-table-expressions-and-recursive-queries
description: "Use when \"common table expressions and recursive queries\" is the work. writing a recursive CTE without a termination/cycle guard on data that could contain a cycle, triggering a runtime."
---

# Common Table Expressions and Recursive Queries

writing a recursive CTE without.

1. Do not: writing a recursive CTE without a termination/cycle guard on data that could contain a.
2. Do not: using a CTE purely for readability on a query planner that doesn't inline it.

Example:
```sql
WITH RECURSIVE org_chart AS (
```

Check: Do not: writing a recursive CTE without a termination/cycle guard on data that could contain a cycle, triggering.
