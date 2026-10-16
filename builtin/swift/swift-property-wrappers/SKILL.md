---
name: swift-property-wrappers
description: "Use when \"swift property wrappers\" is the work. A wrapper mediates storage and access; define initialization behavior as carefully as mutation behavior."
---

# Swift Property Wrappers

A wrapper mediates storage and access; define initialization behavior as carefully as mutation behavior.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```swift
@propertyWrapper
struct NonNegative {
private var value: Int
```

Check: Do not edit the assert to match a surprising result.
