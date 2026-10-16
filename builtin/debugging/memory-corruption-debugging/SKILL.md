---
name: memory-corruption-debugging
description: "Use when \"memory corruption debugging\" is the work. Use compatible sanitizers, allocation traces, and minimized fixtures to identify the first invalid access."
---

# Memory Corruption Debugging

Use compatible sanitizers, allocation traces, and minimized fixtures to identify the first invalid access.

1. Reproduce the symptom and preserve the earliest causal evidence.
2. Rank competing hypotheses and choose a discriminating observation.
3. Minimize the failing input and change one cause at a time.

Example:
```text
Reproduce the symptom and preserve the earliest causal evidence.
```

Check: Show a failing baseline, the causal mechanism, a passing regression, and a check that the fix did not.
