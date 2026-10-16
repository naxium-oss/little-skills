---
name: duplicate-and-near-duplicate-removal
description: "Use when \"duplicate and near duplicate removal\" is the work. Specify normalization and similarity thresholds and audit retained representatives and false matches."
---

# Duplicate and Near-Duplicate Removal

Specify normalization and similarity thresholds and audit retained representatives and false matches.

1. Inspect encoding, record schema, identifiers, and dataset size.
2. Stream transformations into a new artifact rather than overwriting the source.
3. Validate counts, invariants, deterministic ordering, and checksums.

Example:
```text
Inspect encoding, record schema, identifiers, and dataset size.
```

Check: Test malformed lines, empty files, Unicode, nested nulls, duplicates, memory bounds, and deterministic output under repeated runs.
