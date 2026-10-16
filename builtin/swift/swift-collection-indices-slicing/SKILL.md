---
name: swift-collection-indices-slicing
description: "Use when \"swift collection indices slicing\" is the work. Slices can preserve original indices."
---

# Swift Collection Indices & Slicing

Slices can preserve original indices.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```swift
let values = [10, 20, 30]
let tail = values[1...]
assert(tail.startIndex == 1)
```

Check: Do not edit the assert to match a surprising result.
