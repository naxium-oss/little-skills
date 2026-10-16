---
name: data-provenance-and-lineage-tracking
description: "Use when \"data provenance and lineage tracking\" is the work. Link every derived record and artifact to source identifiers and transformation versions."
---

# Data Provenance and Lineage Tracking

Link every derived record and artifact to source identifiers and transformation versions.

1. Verify source license, acquisition consent, schema, and provenance.
2. Define quality gates before processing.
3. Use resumable idempotent stages with stable identifiers and leakage-aware split boundaries.

Example:
```text
Verify source license, acquisition consent, schema, and provenance.
```

Check: Audit PII handling, rejected records, label agreement, distribution shifts, schema evolution, restart behavior, and checksums.
