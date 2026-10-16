---
name: cpp-raii-special-member-functions
description: "Use when \"c raii special member functions\" is the work. Use owning standard-library members to obtain correct destruction and copy behavior."
---

# C++ RAII & Special Member Functions

Use owning standard-library members to obtain correct destruction and copy behavior.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```cpp
struct Document {
std::string title;
std::vector<int> pages;
```

Check: Do not edit the assert to match a surprising result.
