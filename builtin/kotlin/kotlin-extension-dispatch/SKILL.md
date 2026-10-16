---
name: kotlin-extension-dispatch
description: "Use when \"kotlin extension dispatch\" is the work. Extensions are resolved by the declared receiver type."
---

# Kotlin Extension Dispatch

Extensions are resolved by the declared receiver type.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```kotlin
open class Animal
class Cat : Animal()
fun Animal.name() = "animal"
```

Check: Do not edit the assert to match a surprising result.
