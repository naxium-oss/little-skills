---
name: stacking-contexts-and-z-index
description: "Use when \"stacking contexts and z index\" is the work. raising z-index indefinitely as a fix without understanding the actual stacking context tree."
---

# Stacking Contexts and z-index

raising z-index indefinitely as a "fix".

1. Do not: raising z-index indefinitely as a "fix" without understanding the actual stacking context tree.
2. Do not: not realizing position: static elements ignore z-index entirely.

Example:
```bash
grep -rn "!important" --include=*.css . | wc -l
```

Check: Do not: raising z-index indefinitely as a "fix" without understanding the actual stacking context tree.
