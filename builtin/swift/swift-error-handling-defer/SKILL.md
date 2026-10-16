---
name: swift-error-handling-defer
description: "Use when \"swift error handling defer\" is the work. defer runs on scope exit in reverse order."
---

# Swift Error Handling & defer

defer runs on scope exit in reverse order.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```swift
enum ParseError: Error { case invalid }
func number(_ text: String) throws -> Int {
guard let value = Int(text) else { throw ParseError.invalid }
```

Check: Do not edit the assert to match a surprising result.
