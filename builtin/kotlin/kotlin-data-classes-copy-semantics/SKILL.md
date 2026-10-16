---
name: kotlin-data-classes-copy-semantics
description: "Use when \"kotlin data classes copy semantics\" is the work. Generated equals and copy use primary-constructor properties."
---

# Kotlin Data Classes & Copy Semantics

Generated equals and copy use primary-constructor properties.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```kotlin
data class Point(val x: Int, val y: Int)
val a = Point(1, 2)
val b = a.copy(x = 3)
```

Check: Do not edit the assert to match a surprising result.
