---
name: c-enum-bitmask-modeling
description: "Use when \"c enum bitmask modeling\" is the work. Enum alternatives are not automatically bit flags."
---

# C enum & Bitmask Modeling

Enum alternatives are not automatically bit flags.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```c
enum permission { READ = 1u << 0, WRITE = 1u << 1, EXECUTE = 1u << 2.
unsigned permissions = READ | WRITE;
assert((permissions & READ) != 0);
```

Check: Do not edit the assert to match a surprising result.
