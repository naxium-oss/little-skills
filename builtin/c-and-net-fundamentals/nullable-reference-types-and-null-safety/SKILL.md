---
name: nullable-reference-types-and-null-safety
description: "Use when \"nullable reference types and null safety\" is the work. enabling nullable reference types but leaving warnings as non-blocking, letting null-safety violations accumulate unnoticed."
---

# Nullable Reference Types and Null Safety

enabling nullable reference types but leaving warnings.

1. Do not: enabling nullable reference types but leaving warnings as non-blocking, letting null-safety violations accumulate unnoticed.
2. Do not: using the null-forgiving operator (!) to silence warnings without actually verifying the value can't.

Example:
```bash
dotnet --info
```

Check: Do not: enabling nullable reference types but leaving warnings as non-blocking, letting null-safety violations accumulate unnoticed.
