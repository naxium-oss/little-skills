---
name: clean-dry-code
description: "Use when \"DRY\", \"D.R.Y.\", \"cleanup\", \"clean up\", \"refactor\", \"dead code\", \"break down\", \"break into\", \"split into\", \"split my\", or \"split it\". Not when pull request, or the plan."
---

# Clean without new behavior

Same inputs, same outputs. Only the shape moves.

1. Search for the copies or the unused code and read them.
2. Extract, delete unused, or split a function. No new behavior.

Example:
```text
parse() in a.ts and b.ts becomes parse.ts. Tests still pass.
```

Check: A cleanup that changes a return.
