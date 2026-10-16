---
name: dataset-quality-gate-automation
description: "Use when \"dataset quality gate automation\" is the work. Set documented thresholds and produce actionable reports without silently dropping failed records."
---

# Dataset Quality Gate Automation

Set documented thresholds and produce actionable reports without silently dropping failed records.

1. Verify source license, acquisition consent, schema, and provenance.
2. Define quality gates before processing.
3. Use resumable idempotent stages with stable identifiers and leakage-aware split boundaries.

Example:
```text
Verify source license, acquisition consent, schema, and provenance.
```

Check: Audit PII handling, rejected records, label agreement, distribution shifts, schema evolution, restart behavior, and checksums.
