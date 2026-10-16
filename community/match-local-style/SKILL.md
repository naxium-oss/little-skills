---
name: match-local-style
description: "Use when \"match the style\", \"same style\", or \"follow the existing code\". Not when there is no nearby code."
---

# Match the file

Copy the style of the file you are editing.

1. Read the neighboring function.
2. Use its names, types, and error style.
3. Do not introduce a new pattern for one call.

Example:
```text
Neighbors throw AppError. Throw AppError, not a string.
```

Check: A new helper style for one function will not be followed later.
