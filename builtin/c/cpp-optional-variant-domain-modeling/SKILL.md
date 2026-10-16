---
name: cpp-optional-variant-domain-modeling
description: "Use when \"c optional variant domain modeling\" is the work. optional represents zero or one value, while variant represents one of several alternatives."
---

# C++ optional & variant Domain Modeling

optional represents zero or one value, while variant represents one of several alternatives.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```cpp
std::optional<int> find(bool present) {
if (present) return 0;
return std::nullopt;
```

Check: Do not edit the assert to match a surprising result.
