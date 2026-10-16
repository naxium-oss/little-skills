---
name: interactive-debugger-breakpoint-planning
description: "Use when \"interactive debugger breakpoint planning\" is the work. Place conditional breakpoints around invariant transitions and inspect state before corruption propagates."
---

# Interactive Debugger Breakpoint Planning

Place conditional breakpoints around invariant transitions and inspect state before corruption propagates.

1. Reproduce the symptom and preserve the earliest causal evidence.
2. Rank competing hypotheses and choose a discriminating observation.
3. Minimize the failing input and change one cause at a time.

Example:
```text
Reproduce the symptom and preserve the earliest causal evidence.
```

Check: Show a failing baseline, the causal mechanism, a passing regression, and a check that the fix did not.
