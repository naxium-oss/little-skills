---
name: swift-structs-copy-on-write-values
description: "Use when \"swift structs copy on write values\" is the work. Swift collections provide value semantics even when storage is shared internally."
---

# Swift Structs & Copy-on-Write Values

Swift collections provide value semantics even when storage is shared internally.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```swift
var a = [1, 2]
var b = a
b.append(3)
```

Check: Do not edit the assert to match a surprising result.
