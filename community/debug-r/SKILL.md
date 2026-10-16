---
name: debug-r
description: "Use when \"r as.numeric on a factor\", \"as.numeric on a factor\". Not when explaining working r code."
---

# Debug r

Reproduce the r failure with the project command, then change one thing.

1. as.numeric on a factor: Factors convert to their integer codes, not labels; `as.character` first or `readr`.
2. Recycling: Vector recycling silently repeats short vectors; check `length()` of the operands before the operation.

Example:
```text
Rscript script.R
```

Check: The same command that failed has to pass.
