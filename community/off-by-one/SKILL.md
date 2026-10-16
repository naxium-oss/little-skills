---
name: off-by-one
description: "Use when \"off by one\", \"off-by-one\", \"fencepost\", or \"index out of range\". Not when the loop is unwritten."
---

# Off by one

Write the first index and the last index before you edit the loop.

1. State whether the end is inclusive.
2. Test length 0, length 1, and the last index.
3. Prefer a half-open range.

Example:
```text
slice(0, n) keeps n items. Index n is past the end.
```

Check: A loop that works for one sample length is not checked.
