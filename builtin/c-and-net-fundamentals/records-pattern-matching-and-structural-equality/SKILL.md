---
name: records-pattern-matching-and-structural-equality
description: "Use when \"records pattern matching and structural equality\" is the work. assuming a record containing a mutable reference-type field (like a List<T>) is fully immutable, when the list itself."
---

# Records, Pattern Matching, and Structural Equality

assuming a record containing a.

1. Do not: assuming a record containing a mutable reference-type field (like a List<T>) is fully immutable.
2. Do not: switching an existing class to a record without checking for reliance on reference equality.

Example:
```bash
dotnet --info
```

Check: Do not: assuming a record containing a mutable reference-type.
