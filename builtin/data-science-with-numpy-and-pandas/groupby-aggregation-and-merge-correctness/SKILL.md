---
name: groupby-aggregation-and-merge-correctness
description: "Use when \"groupby aggregation and merge correctness\" is the work. merging on a key that has duplicates on the one side of an assumed many-to-one relationship, silently multiplying."
---

# GroupBy, Aggregation, and Merge Correctness

merging on a key.

1. Do not: merging on a key that has duplicates on the "one" side of an assumed.
2. Do not: forgetting dropna=False when NaN values in the groupby key should form their own group.

Example:
```bash
print df.dtypes, df.shape, and df.head() before transforming
```

Check: Do not: merging on a key that has duplicates.
