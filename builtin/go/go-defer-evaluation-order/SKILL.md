---
name: go-defer-evaluation-order
description: "Use when \"go defer evaluation order\" is the work. Deferred call arguments are evaluated immediately; calls execute in reverse order on function return."
---

# Go defer & Evaluation Order

Deferred call arguments are evaluated immediately; calls execute in reverse order on function return.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```go
func sample() {
value := 1
defer fmt.Println(value)
```

Check: Do not edit the assert to match a surprising result.
