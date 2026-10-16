---
name: joins-and-cardinality-reasoning
description: "Use when \"joins and cardinality reasoning\" is the work. joining to a one-to-many table and then summing a column from the one side, inflating totals by the."
---

# Joins and Cardinality Reasoning

joining to a one-to-many table.

1. Do not: joining to a one-to-many table and then summing a column from the "one" side.
2. Do not: using INNER JOIN where LEFT JOIN was intended, silently dropping rows with no match.

Example:
```sql
SELECT o.id, o.total, COUNT(oi.id) AS item_count
```

Check: Do not: joining to.
