---
name: reproduction-to-regression-test-conversion
description: "Use when \"reproduction to regression test conversion\" is the work. Create a regression assertion that fails before the fix and passes after it for the intended reason."
---

# Reproduction-to-Regression-Test Conversion

Create a regression assertion that fails before the fix and passes after it for the intended reason.

1. Read repository instructions before running commands.
2. Locate entry points, build definitions, and pinned dependencies.
3. Minimize the failing input and reproduce it in a disposable clean environment.

Example:
```text
Read repository instructions before running commands.
```

Check: Verify the failure before the fix and success after it; preserve commands, exit codes, checksums, and nondeterminism controls.
