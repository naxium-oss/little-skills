---
name: network-request-failure-debugging
description: "Use when \"network request failure debugging\" is the work. Separate DNS, connection, TLS, proxy, HTTP, application, and dependency failures with observed traces."
---

# Network Request Failure Debugging

Separate DNS, connection, TLS, proxy, HTTP, application, and dependency failures with observed traces.

1. Reproduce the symptom and preserve the earliest causal evidence.
2. Rank competing hypotheses and choose a discriminating observation.
3. Minimize the failing input and change one cause at a time.

Example:
```text
Reproduce the symptom and preserve the earliest causal evidence.
```

Check: Show a failing baseline, the causal mechanism, a passing regression, and a check that the fix did not.
