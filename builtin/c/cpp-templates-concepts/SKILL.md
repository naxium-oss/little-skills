---
name: cpp-templates-concepts
description: "Use when \"c templates concepts\" is the work. Concepts state syntactic requirements, not all semantic laws."
---

# C++ Templates & Concepts

Concepts state syntactic requirements, not all semantic laws.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```cpp
template<std::integral T>
T twice(T value) { return value + value; }
assert(twice(3) == 6);
```

Check: Do not edit the assert to match a surprising result.
