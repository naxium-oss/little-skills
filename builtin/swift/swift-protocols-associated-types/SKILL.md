---
name: swift-protocols-associated-types
description: "Use when \"swift protocols associated types\" is the work. Associated types represent relationships inside a conforming type."
---

# Swift Protocols & Associated Types

Associated types represent relationships inside a conforming type.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```swift
protocol Source {
associatedtype Element
func get() -> Element
```

Check: Do not edit the assert to match a surprising result.
