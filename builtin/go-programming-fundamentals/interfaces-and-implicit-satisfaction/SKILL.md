---
name: interfaces-and-implicit-satisfaction
description: "Use when \"interfaces and implicit satisfaction\" is the work. defining large, kitchen sink interfaces upfront instead of small consumer-defined ones, increasing coupling."
---

# Interfaces and Implicit Satisfaction

defining large, "kitchen sink" interfaces upfront instead of small consumer-defined ones, increasing coupling.

1. Do not: defining large, "kitchen sink" interfaces upfront instead of small consumer-defined ones, increasing coupling.
2. Do not: forgetting a pointer receiver method set differs from a value receiver's, causing a type.

Example:
```go
type Reader interface {
```

Check: Do not: defining large, "kitchen sink" interfaces upfront instead of small consumer-defined ones, increasing coupling.
