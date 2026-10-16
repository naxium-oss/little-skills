---
name: object-equality-hashcode-contracts-and-collections
description: "Use when \"object equality hashcode contracts and collections\" is the work. overriding equals() and forgetting hashCode(), breaking HashMap/HashSet membership checks."
---

# Object Equality, hashCode Contracts, and Collections

overriding equals() and forgetting hashCode(), breaking HashMap/HashSet membership checks.

1. Do not: overriding equals() and forgetting hashCode(), breaking HashMap/HashSet membership checks.
2. Do not: using a mutable object with a mutable-field-based hashCode() as a map key, then mutating.

Example:
```java
public final class Point {
private final int x, y;
```

Check: Do not: overriding equals() and forgetting hashCode(), breaking HashMap/HashSet membership checks.
