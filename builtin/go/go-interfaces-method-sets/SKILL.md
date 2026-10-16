---
name: go-interfaces-method-sets
description: "Use when \"go interfaces method sets\" is the work. Pointer and value receivers contribute differently to method sets."
---

# Go Interfaces & Method Sets

Pointer and value receivers contribute differently to method sets.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```go
type Reader interface { Read() string }
type Record struct { Value string }
func (r Record) Read() string { return r.Value }
```

Check: Do not edit the assert to match a surprising result.
