---
name: writing-plans
description: "Use when \"the plan\", \"break down the plan\", \"implementation plan\", or \"/plan\". Not when dead code or refactor."
---

# Write the plan

A plan names files and a check. It does not edit them.

1. Restate the ask in one sentence.
2. List the files to touch after reading them.
3. Name the command that proves each step.

Example:
```text
Touch src/parse.ts. Check: npm test -- parse.
```

Check: If they did not ask for a plan, implement instead.
