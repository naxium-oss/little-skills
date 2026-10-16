---
name: deadlock-and-race-condition-debugging
description: "Use when \"deadlock and race condition debugging\" is the work. Construct wait-for graphs and inspect lock ordering, ownership, scheduling, and cancellation interactions."
---

# Deadlock and Race Condition Debugging

Construct wait-for graphs and inspect lock ordering, ownership, scheduling, and cancellation interactions.

1. Reproduce the symptom and preserve the earliest causal evidence.
2. Rank competing hypotheses and choose a discriminating observation.
3. Minimize the failing input and change one cause at a time.

Example:
```text
Reproduce the symptom and preserve the earliest causal evidence.
```

Check: Show a failing baseline, the causal mechanism, a passing regression, and a check that the fix did not.
