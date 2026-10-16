---
name: c-declarators-function-pointers
description: "Use when \"c declarators function pointers\" is the work. Build declarations outward from the identifier."
---

# C Declarators & Function Pointers

Build declarations outward from the identifier.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```c
typedef int (*binary_op)(int, int);
int add(int a, int b) { return a + b; }
binary_op operation = add;
```

Check: Do not edit the assert to match a surprising result.
