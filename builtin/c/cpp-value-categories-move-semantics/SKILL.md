---
name: cpp-value-categories-move-semantics
description: "Use when \"c value categories move semantics\" is the work. std::move casts to an rvalue reference; the selected operation performs the move."
---

# C++ Value Categories & Move Semantics

std::move casts to an rvalue reference; the selected operation performs the move.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```cpp
std::string source = "payload";
std::string target = std::move(source);
assert(target == "payload");
```

Check: Do not edit the assert to match a surprising result.
