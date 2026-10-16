---
name: explain-codebase
description: "Use when \"explain\", \"describe\", \"tell me\", \"show me\", or \"how does\" about existing code. Not when your plan, bug, fix, broken, error, or crash."
---

# Explain the code

Explain only files you opened this turn.

1. Search for the noun they named.
2. Read the entry and the next function it calls.
3. Describe that path with file names.

Example:
```text
POST /login -> auth.login in src/auth.ts. Stop there.
```

Check: A file you did not read is not read.
