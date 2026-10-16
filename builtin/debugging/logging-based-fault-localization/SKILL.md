---
name: logging-based-fault-localization
description: "Use when \"logging based fault localization\" is the work. Add structured correlation points at boundaries without logging secrets or distorting timing excessively."
---

# Logging-Based Fault Localization

Add structured correlation points at boundaries without logging secrets or distorting timing excessively.

1. Reproduce the symptom and preserve the earliest causal evidence.
2. Rank competing hypotheses and choose a discriminating observation.
3. Minimize the failing input and change one cause at a time.

Example:
```text
Reproduce the symptom and preserve the earliest causal evidence.
```

Check: Show a failing baseline, the causal mechanism, a passing regression, and a check that the fix did not.
