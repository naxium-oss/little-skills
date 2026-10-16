---
name: java-collection-mutability-views
description: "Use when \"java collection mutability views\" is the work. An unmodifiable view can reflect changes to its backing collection."
---

# Java Collection Mutability & Views

An unmodifiable view can reflect changes to its backing collection.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```java
List<String> source = new ArrayList<>(List.of("a"));
List<String> view = Collections.unmodifiableList(source);
List<String> snapshot = List.copyOf(source);
```

Check: Do not edit the assert to match a surprising result.
