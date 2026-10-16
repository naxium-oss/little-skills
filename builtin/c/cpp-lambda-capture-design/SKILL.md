---
name: cpp-lambda-capture-design
description: "Use when \"c lambda capture design\" is the work. Value captures store copies; reference captures require the referenced object to outlive the closure."
---

# C++ Lambda Capture Design

Value captures store copies; reference captures require the referenced object to outlive the closure.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```cpp
int value = 1;
auto snapshot = [value] { return value; };
auto live = [&value] { return value; };
```

Check: Do not edit the assert to match a surprising result.
