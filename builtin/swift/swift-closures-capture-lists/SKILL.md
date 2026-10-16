---
name: swift-closures-capture-lists
description: "Use when \"swift closures capture lists\" is the work. Capture lists can snapshot a value or weaken a reference."
---

# Swift Closures & Capture Lists

Capture lists can snapshot a value or weaken a reference.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```swift
var value = 1
let snapshot = { [value] in value }
let live = { value }
```

Check: Do not edit the assert to match a surprising result.
