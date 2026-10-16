---
name: resumable-and-idempotent-data-processing
description: "Use when \"resumable and idempotent data processing\" is the work. Use stable stage keys, atomic checkpoints, and replay-safe writes and simulate interruption."
---

# Resumable and Idempotent Data Processing

Use stable stage keys, atomic checkpoints, and replay-safe writes and simulate interruption.

1. Verify source license, acquisition consent, schema, and provenance.
2. Define quality gates before processing.
3. Use resumable idempotent stages with stable identifiers and leakage-aware split boundaries.

Example:
```text
Verify source license, acquisition consent, schema, and provenance.
```

Check: Audit PII handling, rejected records, label agreement, distribution shifts, schema evolution, restart behavior, and checksums.
