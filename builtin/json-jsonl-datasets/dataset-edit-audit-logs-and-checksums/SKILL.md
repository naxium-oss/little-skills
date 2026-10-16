---
name: dataset-edit-audit-logs-and-checksums
description: "Use when \"dataset edit audit logs and checksums\" is the work. Record input/output hashes, counts, rejected lines, transformation revision, parameters, and timestamps."
---

# Dataset Edit Audit Logs and Checksums

Record input/output hashes, counts, rejected lines, transformation revision, parameters, and timestamps.

1. Inspect encoding, record schema, identifiers, and dataset size.
2. Stream transformations into a new artifact rather than overwriting the source.

Example:
```text
Inspect encoding, record schema, identifiers, and dataset size.
```

Check: Test malformed lines, empty files, Unicode, nested nulls, duplicates, memory bounds, and deterministic output under repeated runs.
