---
name: go-zero-values-constructors
description: "Use when \"go zero values constructors\" is the work. Exploit useful zero values, but provide constructors when invariants require initialization."
---

# Go Zero Values & Constructors

Exploit useful zero values, but provide constructors when invariants require initialization.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```go
type Counter struct { value int }
func (c *Counter) Increment() { c.value++ }
var c Counter
```

Check: Do not edit the assert to match a surprising result.
