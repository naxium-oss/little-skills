---
name: debug-bug-repro
description: "Use when \"cannot reproduce\", \"it does not work\", or \"minimal repro\". Not when the failing command is already in hand."
---

# Reproduce first

No failing command, no patch.

1. Write the version, the action, and the exact error.
2. Run the user's command once, unchanged.
3. Shrink the input until one small case still fails.

Example:
```text
One row, one request. That request fails the same way.
```

Check: Do not patch code you cannot make fail.
