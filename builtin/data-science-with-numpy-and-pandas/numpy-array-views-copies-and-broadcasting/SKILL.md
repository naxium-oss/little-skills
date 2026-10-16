---
name: numpy-array-views-copies-and-broadcasting
description: "Use when \"numpy array views copies and broadcasting\" is the work. mutating a slice expecting it to be an independent copy, unexpectedly corrupting the original array."
---

# NumPy Array Views, Copies, and Broadcasting

mutating a slice expecting it to be.

1. Do not: mutating a slice expecting it to be an independent copy, unexpectedly corrupting the original.
2. Do not: relying on ambiguous broadcasting shapes that "work" numerically but apply the operation along the.

Example:
```bash
print df.dtypes, df.shape, and df.head() before transforming
```

Check: Do not: mutating a slice expecting it to.
