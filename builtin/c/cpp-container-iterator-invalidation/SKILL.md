---
name: cpp-container-iterator-invalidation
description: "Use when \"c container iterator invalidation\" is the work. Different containers and operations invalidate different iterators."
---

# C++ Container & Iterator Invalidation

Different containers and operations invalidate different iterators.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```cpp
std::vector<int> values{1, 2, 3, 4};
for (auto it = values.begin(); it != values.end();) {
```

Check: Do not edit the assert to match a surprising result.
