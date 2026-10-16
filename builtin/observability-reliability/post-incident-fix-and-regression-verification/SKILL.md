---
name: post-incident-fix-and-regression-verification
description: "Use when \"post incident fix and regression verification\" is the work. Verify remediation under the original failure conditions and add regression coverage and ownership."
---

# Post-Incident Fix and Regression Verification

Verify remediation under the original failure conditions and add regression coverage and ownership.

1. Define user-visible SLIs and measurement windows.
2. Verify telemetry schemas, units, context propagation, and cardinality.
3. Use controlled load and failure scenarios to validate alerts and recovery behavior.

Example:
```text
Define user-visible SLIs and measurement windows.
```

Check: Check sensitive data, dropped telemetry, sampling bias, clock skew, capacity assumptions, incident evidence, and post-fix regression coverage.
