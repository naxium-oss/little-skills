---
name: schema-aware-dataset-merging
description: "Use when \"schema aware dataset merging\" is the work. Validate input schemas and define field conflict, missing-value, and type-promotion rules."
---

# Schema-Aware Dataset Merging

Validate input schemas and define field conflict, missing-value, and type-promotion rules.

1. Inspect encoding, record schema, identifiers, and dataset size.
2. Stream transformations into a new artifact rather than overwriting the source.

Example:
```text
Inspect encoding, record schema, identifiers, and dataset size.
```

Check: Test malformed lines, empty files, Unicode, nested nulls, duplicates, memory bounds, and deterministic output under repeated runs.
