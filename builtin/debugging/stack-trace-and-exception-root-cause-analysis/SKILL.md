---
name: stack-trace-and-exception-root-cause-analysis
description: "Use when \"stack trace and exception root cause analysis\" is the work. Find the earliest causal failure rather than the last wrapper exception and correlate source maps."
---

# Stack Trace and Exception Root-Cause Analysis

Find the earliest causal failure rather than the last wrapper exception and correlate source maps.

1. Reproduce the symptom and preserve the earliest causal evidence.
2. Rank competing hypotheses and choose a discriminating observation.

Example:
```text
Reproduce the symptom and preserve the earliest causal evidence.
```

Check: Show a failing baseline, the causal mechanism, a passing regression, and a check that the fix did not.
