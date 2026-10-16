---
name: read-the-error
description: "Use when \"exit code\", \"error message\", or \"read the traceback\". Not when the command has not been run."
---

# Read the error

The last frame in your code is the first place to look.

1. Copy the command, the exit code, and the first error line.
2. Find the last frame that is project code.
3. Explain that line before editing a dependency.

Example:
```text
Exit 1. TypeError at src/cart.ts:18. items is undefined.
```

Check: Do not patch a library frame first.
