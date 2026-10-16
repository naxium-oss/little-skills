---
name: c-header-translation-unit-design
description: "Use when \"c header translation unit design\" is the work. Headers declare shared interfaces; one translation unit defines externally linked objects."
---

# C Header & Translation Unit Design

Headers declare shared interfaces; one translation unit defines externally linked objects.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```c
/* counter.h */
extern int count;
int increment(void);
```

Check: Do not edit the assert to match a surprising result.
