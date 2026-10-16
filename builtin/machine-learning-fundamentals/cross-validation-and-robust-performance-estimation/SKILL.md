---
name: cross-validation-and-robust-performance-estimation
description: "Use when \"cross validation and robust performance estimation\" is the work. fitting a preprocessing step on the entire dataset before running cross-validation, leaking information across folds and inflating reported."
---

# Cross-Validation and Robust Performance Estimation

fitting a preprocessing step.

1. Do not: fitting a preprocessing step on the entire dataset before running cross-validation, leaking information across.
2. Do not: using plain k-fold (not stratified/grouped) on imbalanced or clustered data, producing folds that don't.

Example:
```bash
record dataset identity, row counts, and split boundaries before training
```

Check: Do not: fitting a preprocessing step on the entire.
