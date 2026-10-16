---
name: built-in-tooling-test-lint-format-bench
description: "Use when \"built in tooling test lint format bench\" is the work. assuming deno fmt/deno lint rules match Prettier/ESLint defaults exactly."
---

# Built-in Tooling: Test, Lint, Format, Bench

assuming deno fmt/deno lint.

1. Do not: assuming deno fmt/deno lint rules match Prettier/ESLint defaults exactly.
2. Do not: omitting --allow- flags on CI test runs and getting permission-denied failures unrelated to actual.

Example:
```bash
deno test --allow-net --coverage=cov_profile
```

Check: Do not: assuming deno fmt/deno lint rules match Prettier/ESLint defaults exactly.
