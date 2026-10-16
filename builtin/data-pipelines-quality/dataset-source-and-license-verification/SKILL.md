---
name: dataset-source-and-license-verification
description: "Use when \"dataset source and license verification\" is the work. Verify acquisition source, dataset revision, license scope, consent, and downstream usage restrictions."
---

# Dataset Source and License Verification

Verify acquisition source, dataset revision, license scope, consent, and downstream usage restrictions.

1. Verify source license, acquisition consent, schema, and provenance.
2. Define quality gates before processing.
3. Use resumable idempotent stages with stable identifiers and leakage-aware split boundaries.

Example:
```text
Verify source license, acquisition consent, schema, and provenance.
```

Check: Audit PII handling, rejected records, label agreement, distribution shifts, schema evolution, restart behavior, and checksums.
