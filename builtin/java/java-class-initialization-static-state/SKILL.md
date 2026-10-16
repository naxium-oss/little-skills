---
name: java-class-initialization-static-state
description: "Use when \"java class initialization static state\" is the work. Static initialization runs when the class is initialized, not on every instance construction."
---

# Java Class Initialization & Static State

Static initialization runs when the class is initialized, not on every instance construction.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```java
class Sequence {
static int count;
final int id = ++count;
```

Check: Do not edit the assert to match a surprising result.
