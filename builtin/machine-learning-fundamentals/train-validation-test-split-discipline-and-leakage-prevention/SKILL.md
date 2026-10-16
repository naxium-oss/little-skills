---
name: train-validation-test-split-discipline-and-leakage-prevention
description: "Use when \"train validation test split discipline and leakage prevention\" is the work."
---

# Train/Validation/Test Split Discipline and Leakage Prevention

fitting a scaler/encoder on the full dataset.

1. Do not: fitting a scaler/encoder on the full dataset before splitting, leaking test-set statistics into training.
2. Do not: randomly splitting time-series data, allowing the model to "see the future" during training.

Example:
```bash
record dataset identity, row counts, and split boundaries before training
```

Check: Do not: fitting a.
