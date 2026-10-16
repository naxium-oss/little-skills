---
name: load-stress-and-soak-test-design
description: "Use when \"load stress and soak test design\" is the work. Separate expected-load, overload, and long-duration goals and define safe abort thresholds."
---

# Load, Stress, and Soak Test Design

Separate expected-load, overload, and long-duration goals and define safe abort thresholds.

1. Define user-visible SLIs and measurement windows.
2. Verify telemetry schemas, units, context propagation, and cardinality.

Example:
```text
Define user-visible SLIs and measurement windows.
```

Check: Check sensitive data, dropped telemetry, sampling bias, clock skew, capacity assumptions, incident evidence, and post-fix regression coverage.
