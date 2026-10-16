---
name: structured-log-schema-and-sensitive-data-review
description: "Use when \"structured log schema and sensitive data review\" is the work. Define stable structured fields and redact secrets and personal data before logs cross trust boundaries."
---

# Structured Log Schema and Sensitive Data

Define stable structured fields and redact secrets and personal data before logs cross trust boundaries.

1. Define user-visible SLIs and measurement windows.
2. Verify telemetry schemas, units, context propagation, and cardinality.

Example:
```text
Define user-visible SLIs and measurement windows.
```

Check: Check sensitive data, dropped telemetry, sampling bias, clock skew, capacity assumptions, incident evidence, and post-fix regression coverage.
