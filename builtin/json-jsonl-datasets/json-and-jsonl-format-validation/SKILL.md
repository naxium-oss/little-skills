---
name: json-and-jsonl-format-validation
description: "Use when \"json and jsonl format validation\" is the work. Validate strict syntax, encoding, one-record-per-line structure, and documented duplicate-key policy."
---

# JSON and JSONL Format Validation

Validate strict syntax, encoding, one-record-per-line structure, and documented duplicate-key policy.

1. Inspect encoding, record schema, identifiers, and dataset size.
2. Stream transformations into a new artifact rather than overwriting the source.

Example:
```text
Inspect encoding, record schema, identifiers, and dataset size.
```

Check: Test malformed lines, empty files, Unicode, nested nulls, duplicates, memory bounds, and deterministic output under repeated runs.
