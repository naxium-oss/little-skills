---
name: type-error
description: "Use when \"type error\", \"undefined is not\", or \"cannot read properties\". Not when the checker was not run."
---

# Type error

Read the type the checker names. Do not silence it.

1. Copy the type error line and the file.
2. Open that symbol and its caller.
3. Change the type or the value so the checker agrees. Rerun it.

Example:
```text
cart.ts(18): items is possibly undefined. Guard it. Rerun tsc.
```

Check: Do not delete the check or cast to any to go green.
