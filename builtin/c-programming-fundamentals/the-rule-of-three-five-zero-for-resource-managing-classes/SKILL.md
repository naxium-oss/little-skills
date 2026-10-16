---
name: the-rule-of-three-five-zero-for-resource-managing-classes
description: "Use when \"the rule of three five zero for resource managing classes\" is the work."
---

# The Rule of Three/Five/Zero for Resource-Managing

leaving a class with a.

1. Do not: leaving a class with a raw owning pointer member to use compiler-generated copy semantics.
2. Do not: following the Rule of Three/Five when the Rule of Zero (composing RAII members) would.

Example:
```cpp
class Buffer {   // Rule of Zero: no manual resource management needed
```

Check: Do not: leaving a.
