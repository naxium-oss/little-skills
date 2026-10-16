---
name: go-struct-embedding-composition
description: "Use when \"go struct embedding composition\" is the work. Embedding promotes selectors, but the embedded value remains a field."
---

# Go Struct Embedding & Composition

Embedding promotes selectors, but the embedded value remains a field.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```go
type Named struct { Name string }
func (n Named) Label() string { return n.Name }
type User struct { Named; ID int }
```

Check: Do not edit the assert to match a surprising result.
