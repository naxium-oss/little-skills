---
name: cpp-overload-resolution-fundamentals
description: "Use when \"c overload resolution fundamentals\" is the work. Exact matches usually beat conversions, but full ranking has additional rules."
---

# C++ Overload Resolution Fundamentals

Exact matches usually beat conversions, but full ranking has additional rules.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```cpp
int choose(int) { return 1; }
int choose(double) { return 2; }
assert(choose(3) == 1);
```

Check: Do not edit the assert to match a surprising result.
