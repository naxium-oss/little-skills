---
name: nested-field-migration-and-normalization
description: "Use when \"nested field migration and normalization\" is the work. Define old and new schemas and test nested missing, null, array, and mixed-type cases."
---

# Nested Field Migration and Normalization

Define old and new schemas and test nested missing, null, array, and mixed-type cases.

1. Inspect encoding, record schema, identifiers, and dataset size.
2. Stream transformations into a new artifact rather than overwriting the source.

Example:
```text
Inspect encoding, record schema, identifiers, and dataset size.
```

Check: Test malformed lines, empty files, Unicode, nested nulls, duplicates, memory bounds, and deterministic output under repeated runs.
