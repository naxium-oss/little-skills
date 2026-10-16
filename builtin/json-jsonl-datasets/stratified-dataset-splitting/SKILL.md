---
name: stratified-dataset-splitting
description: "Use when \"stratified dataset splitting\" is the work. Preserve class proportions without violating grouping or leakage constraints and report rare classes."
---

# Stratified Dataset Splitting

Preserve class proportions without violating grouping or leakage constraints and report rare classes.

1. Inspect encoding, record schema, identifiers, and dataset size.
2. Stream transformations into a new artifact rather than overwriting the source.
3. Validate counts, invariants, deterministic ordering, and checksums.

Example:
```text
Inspect encoding, record schema, identifiers, and dataset size.
```

Check: Test malformed lines, empty files, Unicode, nested nulls, duplicates, memory bounds, and deterministic output under repeated runs.
