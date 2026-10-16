---
name: defer-panic-and-recover-semantics
description: "Use when \"defer panic and recover semantics\" is the work. calling recover() outside of a directly deferred function, having no effect and letting the panic crash the program."
---

# Defer, Panic, and Recover Semantics

calling recover() outside of.

1. Do not: calling recover() outside of a directly deferred function, having no effect and letting the.
2. Do not: overusing panic/recover as a general error-handling mechanism instead of Go's idiomatic explicit error return.

Example:
```go
func safeDivide(a, b int) (result int, err error) {
```

Check: Do not: calling recover() outside of a directly deferred.
