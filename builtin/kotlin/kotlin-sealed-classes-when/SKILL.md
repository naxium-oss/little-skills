---
name: kotlin-sealed-classes-when
description: "Use when \"kotlin sealed classes when\" is the work. Use sealed hierarchies for known domain cases."
---

# Kotlin Sealed Classes & when

Use sealed hierarchies for known domain cases.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```kotlin
sealed interface Result
data class Success(val value: Int) : Result
data class Failure(val reason: String) : Result
```

Check: Do not edit the assert to match a surprising result.
