---
name: c-structs-unions-tagged-data
description: "Use when \"c structs unions tagged data\" is the work. Keep a union’s tag synchronized with the member being stored."
---

# C Structs, Unions & Tagged Data

Keep a union’s tag synchronized with the member being stored.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```c
enum kind { INTEGER, REAL };
struct value {
enum kind kind;
```

Check: Do not edit the assert to match a surprising result.
