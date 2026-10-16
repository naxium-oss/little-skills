---
name: kotlin-variance-reified-parameters
description: "Use when \"kotlin variance reified parameters\" is the work. out restricts a type parameter to producer positions."
---

# Kotlin Variance & Reified Parameters

out restricts a type parameter to producer positions.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```kotlin
interface Source<out T> { fun get(): T }
class TextSource : Source<String> { override fun get() = "ok" }
val source: Source<Any> = TextSource()
```

Check: Do not edit the assert to match a surprising result.
