---
name: c-integer-promotions-conversions
description: "Use when \"c integer promotions conversions\" is the work. Small integer operands often promote to int before arithmetic."
---

# C Integer Promotions & Conversions

Small integer operands often promote to int before arithmetic.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```c
unsigned char a = 200, b = 100;
int result = a + b;
assert(result == 300);
```

Check: Do not edit the assert to match a surprising result.
