---
name: containerized-reproduction-packaging
description: "Use when \"containerized reproduction packaging\" is the work. Pin container image digests and include minimal sanitized inputs and exact reproduction commands."
---

# Containerized Reproduction Packaging

Pin container image digests and include minimal sanitized inputs and exact reproduction commands.

1. Read repository instructions before running commands.
2. Locate entry points, build definitions, and pinned dependencies.
3. Minimize the failing input and reproduce it in a disposable clean environment.

Example:
```text
Read repository instructions before running commands.
```

Check: Verify the failure before the fix and success after it; preserve commands, exit codes, checksums, and nondeterminism controls.
