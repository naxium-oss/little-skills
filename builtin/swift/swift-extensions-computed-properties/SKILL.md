---
name: swift-extensions-computed-properties
description: "Use when \"swift extensions computed properties\" is the work. Extensions can add computed properties but not ordinary stored instance properties."
---

# Swift Extensions & Computed Properties

Extensions can add computed properties but not ordinary stored instance properties.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```swift
extension Int {
var isEven: Bool { self % 2 == 0 }
}
```

Check: Do not edit the assert to match a surprising result.
