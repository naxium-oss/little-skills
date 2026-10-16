---
name: move-semantics-and-copy-elision
description: "Use when \"move semantics and copy elision\" is the work. forgetting noexcept on a move constructor, causing std::vector to fall back to copying during reallocation for exception-safety guarantees."
---

# Move Semantics and Copy Elision

forgetting noexcept on a.

1. Do not: forgetting noexcept on a move constructor, causing std::vector to fall back to copying during.
2. Do not: using std::move on an object still needed afterward, leaving it in a valid-but-unspecified emptied.

Example:
```cpp
class Buffer {
```

Check: Do not: forgetting noexcept on a move constructor, causing std::vector to fall back to copying during reallocation for.
