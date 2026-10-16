---
name: swift-access-control-api-surface
description: "Use when \"swift access control api surface\" is the work. private, fileprivate, internal, public, and open define different boundaries."
---

# Swift Access Control & API Surface

private, fileprivate, internal, public, and open define different boundaries.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```swift
public struct Counter {
public private(set) var value = 0
public init() {}
```

Check: Do not edit the assert to match a surprising result.
