---
name: pii-detection-and-dataset-redaction
description: "Use when \"pii detection and dataset redaction\" is the work. Detect and redact sensitive fields while assessing residual re-identification risk and access controls."
---

# PII Detection and Dataset Redaction

Detect and redact sensitive fields while assessing residual re-identification risk and access controls.

1. Verify source license, acquisition consent, schema, and provenance.
2. Define quality gates before processing.
3. Use resumable idempotent stages with stable identifiers and leakage-aware split boundaries.

Example:
```text
Verify source license, acquisition consent, schema, and provenance.
```

Check: Audit PII handling, rejected records, label agreement, distribution shifts, schema evolution, restart behavior, and checksums.
