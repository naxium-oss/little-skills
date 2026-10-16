---
name: swift-enums-associated-values
description: "Use when \"swift enums associated values\" is the work. Associated values are stored per case; raw values are fixed identifiers."
---

# Swift Enums & Associated Values

Associated values are stored per case; raw values are fixed identifiers.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```swift
enum Load { case idle; case ready(String); case failed(String) }
func label(_ state: Load) -> String {
switch state {
```

Check: Do not edit the assert to match a surprising result.
