---
name: minimal-reproduction-extraction
description: "Use when \"minimal reproduction extraction\" is the work. Remove unrelated files, dependencies, and input dimensions while retaining the same failure mechanism."
---

# Minimal Reproduction Extraction

Remove unrelated files, dependencies, and input dimensions while retaining the same failure mechanism.

1. Read repository instructions before running commands.
2. Locate entry points, build definitions, and pinned dependencies.
3. Minimize the failing input and reproduce it in a disposable clean environment.

Example:
```text
Read repository instructions before running commands.
```

Check: Verify the failure before the fix and success after it; preserve commands, exit codes, checksums, and nondeterminism controls.
