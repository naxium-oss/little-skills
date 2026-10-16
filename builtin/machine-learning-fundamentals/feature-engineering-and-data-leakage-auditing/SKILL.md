---
name: feature-engineering-and-data-leakage-auditing
description: "Use when \"feature engineering and data leakage auditing\" is the work. engineering a feature using an aggregate that includes the target rows own future outcome, creating leakage invisible in."
---

# Feature Engineering and Data Leakage Auditing

engineering a feature using an.

1. Do not: engineering a feature using an aggregate that includes the target row's own future outcome.
2. Do not: computing feature statistics on the full dataset (train+test combined) instead of only from information.

Example:
```bash
record dataset identity, row counts, and split boundaries before training
```

Check: Do not: engineering a feature using an aggregate that.
