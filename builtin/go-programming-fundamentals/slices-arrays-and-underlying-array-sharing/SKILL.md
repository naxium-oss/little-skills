---
name: slices-arrays-and-underlying-array-sharing
description: "Use when \"slices arrays and underlying array sharing\" is the work. assuming slicing always creates an independent copy, then being surprised when appending to a sub-slice corrupts data in."
---

# Slices, Arrays, and Underlying Array Sharing

assuming slicing always creates an.

1. Do not: assuming slicing always creates an independent copy, then being surprised when appending to a.
2. Do not: passing a slice into a goroutine without considering that concurrent appends from multiple goroutines.

Example:
```go
original := make([]int, 3, 5)
```

Check: Do not: assuming slicing always creates an independent copy, then being surprised when appending to a sub-slice corrupts.
