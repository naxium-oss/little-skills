---
name: java-sealed-hierarchy-modeling
description: "Use when \"java sealed hierarchy modeling\" is the work. Sealed types declare permitted direct subtypes."
---

# Java Sealed Hierarchy Modeling

Sealed types declare permitted direct subtypes.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```java
sealed interface Shape permits Circle, Square {}
record Circle(double radius) implements Shape {}
record Square(double side) implements Shape {}
```

Check: Do not edit the assert to match a surprising result.
