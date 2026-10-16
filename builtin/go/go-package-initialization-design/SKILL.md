---
name: go-package-initialization-design
description: "Use when \"go package initialization design\" is the work. Prefer explicit setup functions over hidden init side effects."
---

# Go Package Initialization Design

Prefer explicit setup functions over hidden init side effects.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```go
// package settings
package settings
type Config struct { Port int }
```

Check: Do not edit the assert to match a surprising result.
