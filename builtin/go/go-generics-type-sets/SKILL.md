---
name: go-generics-type-sets
description: "Use when \"go generics type sets\" is the work. Type sets constrain which operations are valid."
---

# Go Generics & Type Sets

Type sets constrain which operations are valid.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```go
type Integer interface { ~int | ~int64 }
func Sum[T Integer](values []T) T {
var result T
```

Check: Do not edit the assert to match a surprising result.
