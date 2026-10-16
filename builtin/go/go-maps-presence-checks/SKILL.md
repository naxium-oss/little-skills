---
name: go-maps-presence-checks
description: "Use when \"go maps presence checks\" is the work. A map lookup returns the value type’s zero value for absence."
---

# Go Maps & Presence Checks

A map lookup returns the value type’s zero value for absence.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```go
scores := map[string]int{"Ada": 0}
value, ok := scores["Ada"]
fmt.Println(value, ok) // 0 true
```

Check: Do not edit the assert to match a surprising result.
