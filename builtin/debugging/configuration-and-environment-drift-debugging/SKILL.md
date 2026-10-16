---
name: configuration-and-environment-drift-debugging
description: "Use when \"configuration and environment drift debugging\" is the work. Diff effective configuration, runtime paths, lockfiles, and deployment artifacts across environments."
---

# Configuration and Environment Drift Debugging

Diff effective configuration, runtime paths, lockfiles, and deployment artifacts across environments.

1. Reproduce the symptom and preserve the earliest causal evidence.
2. Rank competing hypotheses and choose a discriminating observation.
3. Minimize the failing input and change one cause at a time.

Example:
```text
Reproduce the symptom and preserve the earliest causal evidence.
```

Check: Show a failing baseline, the causal mechanism, a passing regression, and a check that the fix did not.
