---
name: java-optional-composition
description: "Use when \"java optional composition\" is the work. Use Optional primarily at return boundaries."
---

# Java Optional Composition

Use Optional primarily at return boundaries.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```java
Optional<String> name = Optional.of(" Ada ");
assert name.map(String::trim).orElse("Guest").equals("Ada");
int[] calls = {0};
```

Check: Do not edit the assert to match a surprising result.
