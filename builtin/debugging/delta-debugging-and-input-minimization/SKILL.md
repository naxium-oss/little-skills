---
name: delta-debugging-and-input-minimization
description: "Use when \"delta debugging and input minimization\" is the work. Reduce input and configuration systematically while checking that the same failure signature persists."
---

# Delta Debugging and Input Minimization

Reduce input and configuration systematically while checking that the same failure signature persists.

1. Reproduce the symptom and preserve the earliest causal evidence.
2. Rank competing hypotheses and choose a discriminating observation.
3. Minimize the failing input and change one cause at a time.

Example:
```text
Reproduce the symptom and preserve the earliest causal evidence.
```

Check: Show a failing baseline, the causal mechanism, a passing regression, and a check that the fix did not.
