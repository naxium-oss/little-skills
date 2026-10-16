---
name: go-error-wrapping-inspection
description: "Use when \"go error wrapping inspection\" is the work. Use %w to preserve an error chain."
---

# Go Error Wrapping & Inspection

Use %w to preserve an error chain.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```go
var ErrMissing = errors.New("missing")
err := fmt.Errorf("read user: %w", ErrMissing)
fmt.Println(errors.Is(err, ErrMissing)) // true
```

Check: Do not edit the assert to match a surprising result.
