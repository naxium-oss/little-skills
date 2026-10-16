---
name: go-slices-backing-arrays
description: "Use when \"go slices backing arrays\" is the work. Slices are descriptors over arrays."
---

# Go Slices & Backing Arrays

Slices are descriptors over arrays.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```go
base := []int{1, 2, 3}
view := base[:2]
view[0] = 9
```

Check: Do not edit the assert to match a surprising result.
