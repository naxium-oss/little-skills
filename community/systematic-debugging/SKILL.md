---
name: systematic-debugging
description: "Use when \"wrong result\", \"stack trace\", \"pytest fails\", or \"this bug\". Not when explain how working code is structured."
---

# Debug from evidence

One cause, one change, then the same command again.

1. Reproduce with a command and save the exact error.
2. Change one thing that the error points at.
3. Rerun that same command.

Example:
```text
test_empty fails on None. Guard the empty list. Rerun test_empty.
```

Check: A second edit before the rerun hides which change worked.
