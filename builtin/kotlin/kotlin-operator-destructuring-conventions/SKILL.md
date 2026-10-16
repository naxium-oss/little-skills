---
name: kotlin-operator-destructuring-conventions
description: "Use when \"kotlin operator destructuring conventions\" is the work. Operators map to named functions with required signatures."
---

# Kotlin Operator & Destructuring Conventions

Operators map to named functions with required signatures.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```kotlin
data class Point(val x: Int, val y: Int) {
operator fun plus(other: Point) = Point(x + other.x, y + other.y)
}
```

Check: Do not edit the assert to match a surprising result.
