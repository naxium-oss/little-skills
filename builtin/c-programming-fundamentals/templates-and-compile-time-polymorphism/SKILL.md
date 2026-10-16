---
name: templates-and-compile-time-polymorphism
description: "Use when \"templates and compile time polymorphism\" is the work. relying on old-style SFINAE (std::enable_if) for constraints in a C++20-capable codebase, producing far less readable errors than concepts."
---

# Templates and Compile-Time Polymorphism

relying on old-style SFINAE.

1. Do not: relying on old-style SFINAE (std::enable_if) for constraints in a C++20-capable codebase, producing far less.
2. Do not: forgetting that each template instantiation for a distinct type generates separate compiled code, causing.

Example:
```cpp
template <typename T>
```

Check: Do not: relying on.
