---
name: debug-swift
description: "Use when \"swift Fatal: force unwrap of nil\", \"Fatal: force unwrap of nil\". Not when explaining working swift code."
---

# Debug swift

Reproduce the swift failure with the project command, then change one thing.

1. Fatal: force unwrap of nil: Every `!` is a potential crash; the crash report names the.
2. Data disappears: Structs copy; check whether the mutation applied to the copy, use `inout`, classes, or.
3. Retain cycle: Closures capturing `self` strongly inside a stored closure; capture lists `[weak self]`.

Example:
```text
swift build
```

Check: The same command that failed has to pass.
