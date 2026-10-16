---
name: java-equals-hashcode-contracts
description: "Use when \"java equals hashcode contracts\" is the work. Equal objects must have equal hash codes."
---

# Java equals & hashCode Contracts

Equal objects must have equal hash codes.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```java
record Point(int x, int y) {}
Point a = new Point(1, 2);
Point b = new Point(1, 2);
```

Check: Do not edit the assert to match a surprising result.
