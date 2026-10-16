---
name: c-storage-duration-linkage
description: "Use when \"c storage duration linkage\" is the work. Static storage duration is distinct from internal linkage."
---

# C Storage Duration & Linkage

Static storage duration is distinct from internal linkage.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```c
static int next(void) {
static int value = 0;
return ++value;
```

Check: Do not edit the assert to match a surprising result.
