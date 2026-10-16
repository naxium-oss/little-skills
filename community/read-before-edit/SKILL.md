---
name: read-before-edit
description: "Use when \"edit the file\", \"update the file\", or \"modify the file\". Not when how many or explain."
---

# Read before edit

Do not edit a file you have not opened.

1. Open the file and the caller.
2. Then make the edit.
3. If the file is missing, say so.

Example:
```text
Opened src/parse.ts lines 40-80. Then changed the guard.
```

Check: A patch on an unread file is a guess.
