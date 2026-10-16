---
name: metrics-cardinality-and-unit-validation
description: "Use when \"metrics cardinality and unit validation\" is the work. Validate metric type and units and bound label dimensions to prevent unbounded series growth."
---

# Metrics Cardinality and Unit Validation

Validate metric type and units and bound label dimensions to prevent unbounded series growth.

1. Define user-visible SLIs and measurement windows.
2. Verify telemetry schemas, units, context propagation, and cardinality.
3. Use controlled load and failure scenarios to validate alerts and recovery behavior.

Example:
```text
Define user-visible SLIs and measurement windows.
```

Check: Check sensitive data, dropped telemetry, sampling bias, clock skew, capacity assumptions, incident evidence, and post-fix regression coverage.
