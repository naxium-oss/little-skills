---
name: generics-type-erasure-and-wildcards
description: "Use when \"generics type erasure and wildcards\" is the work. attempting new T[10] inside a generic class, hitting a compile error due to type erasure preventing generic array."
---

# Generics, Type Erasure, and Wildcards

attempting new T[10] inside.

1. Do not: attempting new T[10] inside a generic class, hitting a compile error due to type.
2. Do not: using an unbounded wildcard or the wrong PECS direction, either over-restricting valid callers or.

Example:
```java
public static double sumOfList(List<? extends Number> list) {   // producer: read-only, covariant
```

Check: Do not: attempting new.
