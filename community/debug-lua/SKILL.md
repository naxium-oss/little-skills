---
name: debug-lua
description: "Use when \"lua attempt to index nil\", \"attempt to index nil\". Not when explaining working lua code."
---

# Debug lua

Reproduce the lua failure with the project command, then change one thing.

1. attempt to index nil: The error names the variable; check table construction and the 1-based indexing.
2. Off-by-one in loops: Lua arrays start at 1; `for i=1,#t` vs `0,#t-1`, verify with the smallest.

Example:
```text
lua script.lua
```

Check: The same command that failed has to pass.
