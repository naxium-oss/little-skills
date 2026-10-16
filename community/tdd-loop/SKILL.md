---
name: tdd-loop
description: "Use when \"red green\", \"failing spec\", or \"tiny library\" in TypeScript or Python. Not when the suite already covers the behavior."
---

# Red, green, refactor

Paste the runner output. Do not claim green from memory.

1. Write one failing test.
2. Run it and keep the failure text.
3. Implement, rerun, and refactor only while that run stays green.

Example:
```text
FAIL expected a-b. After the edit, PASS expected a-b.
```

Check: No runner output means not green.
