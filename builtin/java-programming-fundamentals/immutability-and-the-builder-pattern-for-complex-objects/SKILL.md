---
name: immutability-and-the-builder-pattern-for-complex-objects
description: "Use when \"immutability and the builder pattern for complex objects\" is the work. accepting a mutable collection/array in a constructor without copying it, allowing external code to mutate the immutable objects."
---

# Immutability and the Builder Pattern for

accepting a mutable collection/array in.

1. Do not: accepting a mutable collection/array in a constructor without copying it, allowing external code to.
2. Do not: returning an internal mutable field directly from a getter, letting callers mutate it and.

Example:
```java
public final class HttpRequestConfig {
```

Check: Do not: accepting a mutable collection/array in a constructor.
