---
name: kotlin-null-safety-elvis-expressions
description: "Use when \"kotlin null safety elvis expressions\" is the work. Safe calls propagate null; Elvis provides a fallback."
---

# Kotlin Null Safety & Elvis Expressions

Safe calls propagate null; Elvis provides a fallback.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```kotlin
fun label(value: String?): String = value?.trim() ?: "Guest"
check(label(null) == "Guest")
check(label(" Ada ") == "Ada")
```

Check: Do not edit the assert to match a surprising result.
