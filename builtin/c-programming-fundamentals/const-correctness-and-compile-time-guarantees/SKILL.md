---
name: const-correctness-and-compile-time-guarantees
description: "Use when \"const correctness and compile time guarantees\" is the work. omitting const on methods that dont modify state, preventing them from being called on const object references/parameters elsewhere."
---

# Const-Correctness and Compile-Time Guarantees

omitting const on methods that.

1. Do not: omitting const on methods that don't modify state, preventing them from being called on.
2. Do not: overusing mutable to silence const-correctness errors instead of properly separating logical constness (observable behavior).

Example:
```cpp
class Matrix {
```

Check: Do not: omitting const on methods that don't modify state, preventing them from being called on const object.
