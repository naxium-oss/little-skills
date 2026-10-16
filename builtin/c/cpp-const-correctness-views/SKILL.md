---
name: cpp-const-correctness-views
description: "Use when \"c const correctness views\" is the work. const limits access through a particular expression."
---

# C++ const Correctness & Views

const limits access through a particular expression.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```cpp
std::string text = "hello";
std::string_view view{text};
assert(view.substr(1, 3) == "ell");
```

Check: Do not edit the assert to match a surprising result.
