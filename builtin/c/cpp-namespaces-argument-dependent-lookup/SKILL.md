---
name: cpp-namespaces-argument-dependent-lookup
description: "Use when \"c namespaces argument dependent lookup\" is the work. Unqualified calls can find functions in associated namespaces of their arguments."
---

# C++ Namespaces & Argument-Dependent Lookup

Unqualified calls can find functions in associated namespaces of their arguments.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```cpp
namespace geometry {
struct Point { int x; };
int coordinate(Point p) { return p.x; }
```

Check: Do not edit the assert to match a surprising result.
