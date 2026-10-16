---
name: deterministic-dataset-splitting
description: "Use when \"deterministic dataset splitting\" is the work. Pin seed, algorithm, input ordering, and split ratios and retain membership manifests."
---

# Deterministic Dataset Splitting

Pin seed, algorithm, input ordering, and split ratios and retain membership manifests.

1. Inspect encoding, record schema, identifiers, and dataset size.
2. Stream transformations into a new artifact rather than overwriting the source.
3. Validate counts, invariants, deterministic ordering, and checksums.

Example:
```text
Inspect encoding, record schema, identifiers, and dataset size.
```

Check: Test malformed lines, empty files, Unicode, nested nulls, duplicates, memory bounds, and deterministic output under repeated runs.
