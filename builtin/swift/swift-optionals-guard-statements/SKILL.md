---
name: swift-optionals-guard-statements
description: "Use when \"swift optionals guard statements\" is the work. Optional binding unwraps values without force-unwrapping."
---

# Swift Optionals & Guard Statements

Optional binding unwraps values without force-unwrapping.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```swift
func greet(_ name: String?) -> String {
guard let name = name else { return "Hello guest" }
return "Hello \(name)"
```

Check: Do not edit the assert to match a surprising result.
