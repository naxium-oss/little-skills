---
name: verification-before-completion
description: "Use when \"are we done\", \"mark complete\", or \"before finishing\". Not when still reproducing."
---

# Verify before done

Done means a check that could have failed has passed.

1. Run the project test, typecheck, or the narrow proving command.
2. If it cannot be run, say not run.
3. Put leftover risk in the report.

Example:
```text
npm test exit 0. Typecheck not run.
```

Check: Do not imply a check passed when it did not run.
