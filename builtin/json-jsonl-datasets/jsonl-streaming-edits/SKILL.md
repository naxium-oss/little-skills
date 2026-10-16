---
name: jsonl-streaming-edits
description: "Use when \"jsonl streaming edits\" is the work. Process bounded chunks and write atomically to a new artifact with line-level error reporting."
---

# JSONL Streaming Edits

Process bounded chunks and write atomically to a new artifact with line-level error reporting.

1. Inspect encoding, record schema, identifiers, and dataset size.
2. Stream transformations into a new artifact rather than overwriting the source.
3. Validate counts, invariants, deterministic ordering, and checksums.

Example:
```text
Inspect encoding, record schema, identifiers, and dataset size.
```

Check: Test malformed lines, empty files, Unicode, nested nulls, duplicates, memory bounds, and deterministic output under repeated runs.
