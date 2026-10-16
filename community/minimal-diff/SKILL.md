---
name: minimal-diff
description: "Use when \"only change\", \"smallest diff\", \"minimal change\", or \"don't refactor\". Not when DRY or cleanup."
---

# Smallest diff

Touch only the lines the ask needs.

1. Name the lines that must change.
2. Leave rename, format, and drive-by fixes out.
3. Show the diff against the ask.

Example:
```text
Changed the null guard. Did not rename the function.
```

Check: A drive-by rewrite is a different task.
