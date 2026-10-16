---
name: debug-typescript
description: "Use when \"typescript Build fails on types only\", \"Build fails on types only\". Not when explaining working typescript code."
---

# Debug typescript

Reproduce the typescript failure with the project command, then change one thing.

1. Build fails on types only: Run `tsc --noEmit` and read the first error; null/undefined narrowing and.
2. Runs but types disagree: An `as` cast or `any` is hiding the real type; remove casts.
3. Path alias not resolving: Check tsconfig `paths` + `baseUrl` and that the bundler (vite/webpack) mirrors them.

Example:
```text
tsc --noEmit
```

Check: The same command that failed has to pass.
