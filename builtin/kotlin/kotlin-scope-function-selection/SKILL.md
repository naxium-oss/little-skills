---
name: kotlin-scope-function-selection
description: "Use when \"kotlin scope function selection\" is the work. Distinguish whether the lambda exposes this or it and whether the function returns the receiver or lambda result."
---

# Kotlin Scope Function Selection

Distinguish whether the lambda exposes this or it and whether the function returns the receiver or lambda result.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```kotlin
val values = mutableListOf<Int>().apply { add(1); add(2) }
```

Check: Do not edit the assert to match a surprising result.
