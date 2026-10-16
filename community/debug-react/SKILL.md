---
name: debug-react
description: "Use when \"react Infinite re-render loop\", \"Infinite re-render loop\". Not when explaining working react code."
---

# Debug react

Reproduce the react failure with the project command, then change one thing.

1. Infinite re-render loop: State set during render or an effect with no dep change; log the.
2. Stale closure in effects: An effect captures an old prop/state; list the value in the dep.
3. List wrong: Index keys cause wrong reconciliation when items move; use stable ids.

Example:
```text
npm test
```

Check: The same command that failed has to pass.
