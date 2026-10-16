---
name: kotlin-collection-sequence-pipelines
description: "Use when \"kotlin collection sequence pipelines\" is the work. Sequences defer intermediate operations but are not automatically faster."
---

# Kotlin Collection & Sequence Pipelines

Sequences defer intermediate operations but are not automatically faster.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```kotlin
val result = listOf(1, 2, 3, 4).asSequence()
.filter { it % 2 == 0 }.map { it * 10 }.toList()
check(result == listOf(20, 40))
```

Check: Do not edit the assert to match a surprising result.
