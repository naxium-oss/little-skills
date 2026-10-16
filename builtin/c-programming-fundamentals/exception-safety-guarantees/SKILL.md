---
name: exception-safety-guarantees
description: "Use when \"exception safety guarantees\" is the work. assuming the strong exception-safety guarantee applies to a function that was never actually designed or tested for it."
---

# Exception Safety Guarantees

assuming the strong exception-safety guarantee applies to a function that was.

1. Do not: assuming the strong exception-safety guarantee applies to a function that was never actually designed.
2. Do not: performing a resizing/reallocation operation that mutates existing state before a potentially-throwing step completes, violating.

Example:
```cpp
void Container::push_back_strong(T value) {
```

Check: Do not: assuming the strong exception-safety guarantee applies to a function that was never actually designed or tested.
