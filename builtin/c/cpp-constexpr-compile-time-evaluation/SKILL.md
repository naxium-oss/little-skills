---
name: cpp-constexpr-compile-time-evaluation
description: "Use when \"c constexpr compile time evaluation\" is the work. constexpr permits constant evaluation when arguments and context allow it."
---

# C++ constexpr & Compile-Time Evaluation

constexpr permits constant evaluation when arguments and context allow it.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```cpp
constexpr int square(int x) { return x * x; }
static_assert(square(4) == 16);
constexpr int size = square(2);
```

Check: Do not edit the assert to match a surprising result.
