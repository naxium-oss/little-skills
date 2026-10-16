---
name: kotlin-delegated-properties
description: "Use when \"kotlin delegated properties\" is the work. lazy postpones initialization until first access."
---

# Kotlin Delegated Properties

lazy postpones initialization until first access.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```kotlin
var calls = 0
val value by lazy { calls++; 42 }
check(calls == 0)
```

Check: Do not edit the assert to match a surprising result.
