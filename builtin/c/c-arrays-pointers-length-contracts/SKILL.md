---
name: c-arrays-pointers-length-contracts
description: "Use when \"c arrays pointers length contracts\" is the work. Array parameters adjust to pointers."
---

# C Arrays, Pointers & Length Contracts

Array parameters adjust to pointers.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```c
int sum(const int *values, size_t count) {
int result = 0;
for (size_t i = 0; i < count; ++i) result += values[i];
```

Check: Do not edit the assert to match a surprising result.
