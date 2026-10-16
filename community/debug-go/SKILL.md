---
name: debug-go
description: "Use when \"go Data race\", \"Data race\". Not when explaining working go code."
---

# Debug go

Reproduce the go failure with the project command, then change one thing.

1. Data race: Run `go test -race ./...`; the report names the two goroutines and the variable.
2. Panic: nil pointer: Read the stack and the receiver; nil maps and slices are legal to.
3. `err` silently swallowed: Check `if err != nil` shadowing (`:=` creates a new err in nested.

Example:
```text
go build ./...
```

Check: The same command that failed has to pass.
