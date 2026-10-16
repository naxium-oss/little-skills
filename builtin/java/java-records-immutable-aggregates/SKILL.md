---
name: java-records-immutable-aggregates
description: "Use when \"java records immutable aggregates\" is the work. Record component references are final, but referenced collections can remain mutable."
---

# Java Records & Immutable Aggregates

Record component references are final, but referenced collections can remain mutable.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```java
record Team(List<String> members) {
Team { members = List.copyOf(members); }
}
```

Check: Do not edit the assert to match a surprising result.
