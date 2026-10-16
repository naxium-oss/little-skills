---
name: kotlin-java-interop-boundaries
description: "Use when \"kotlin java interop boundaries\" is the work. Java nullability may arrive as platform types."
---

# Kotlin Java Interop Boundaries

Java nullability may arrive as platform types.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```kotlin
// Java
public final class Legacy {
public static String name() { return null; }
```

Check: Do not edit the assert to match a surprising result.
