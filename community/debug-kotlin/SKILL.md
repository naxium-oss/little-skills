---
name: debug-kotlin
description: "Use when \"kotlin NullPointerException from Java interop\", \"NullPointerException from Java interop\". Not when explaining working kotlin code."
---

# Debug kotlin

Reproduce the kotlin failure with the project command, then change one thing.

1. NullPointerException from Java interop: Platform types (String!) can be null; the stack shows the call, add.
2. lateinit property not initialized: The stack names the property; check initialization order in constructors vs init.
3. Coroutine leaks: GlobalScope or missing Job cancellation; the caller should own the scope and cancel it.

Example:
```text
./gradlew test
```

Check: The same command that failed has to pass.
