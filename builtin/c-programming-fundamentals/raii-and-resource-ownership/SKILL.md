---
name: raii-and-resource-ownership
description: "Use when \"raii and resource ownership\" is the work. using raw new/delete instead of smart pointers, leaking memory on an exception path that skips the delete."
---

# RAII and Resource Ownership

using raw new/delete instead of smart pointers, leaking.

1. Do not: using raw new/delete instead of smart pointers, leaking memory on an exception path that.
2. Do not: forgetting a mutex lock's scope, holding it far longer than needed and creating contention.

Example:
```cpp
void process(const std::string& path) {
```

Check: Do not: using raw new/delete instead of smart pointers, leaking memory on an exception path that skips the.
