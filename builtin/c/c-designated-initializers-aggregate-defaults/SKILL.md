---
name: c-designated-initializers-aggregate-defaults
description: "Use when \"c designated initializers aggregate defaults\" is the work. Unspecified aggregate members are initialized as zero according to their types."
---

# C Designated Initializers & Aggregate Defaults

Unspecified aggregate members are initialized as zero according to their types.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```c
struct point { int x; int y; };
struct point p = {.y = 4};
assert(p.x == 0 && p.y == 4);
```

Check: Do not edit the assert to match a surprising result.
