---
name: debug-c
description: "Use when \"c Buffer overflow\", \"Buffer overflow\". Not when explaining working c code."
---

# Debug c

Reproduce the c failure with the project command, then change one thing.

1. Buffer overflow: ASan names the exact allocation and the overflow site; check loop bounds and `strcpy`/`sprintf`.
2. Use-after-free: ASan catches both; check ownership discipline, who frees, and does a copy of the pointer.
3. Pointer arithmetic off: `p[i]` vs `*(p + i)` with `sizeof` in the stride; integer truncation in.

Example:
```text
make
```

Check: The same command that failed has to pass.
