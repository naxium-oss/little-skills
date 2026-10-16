---
name: debug-javascript
description: "Use when \"javascript Unhandled rejection\", \"Unhandled rejection\". Not when explaining working javascript code."
---

# Debug javascript

Reproduce the javascript failure with the project command, then change one thing.

1. Unhandled rejection: Every `async` boundary needs a catch or await; add `process.on('unhandledRejection')` temporarily and trace which.
2. Works locally, fails in CI: Compare Node versions and lockfile; check env vars, case-sensitive file names.
3. Race: Look for shared mutable state, missing awaits, and `Promise.all` mutating the same array; make the.

Example:
```text
npm test
```

Check: The same command that failed has to pass.
