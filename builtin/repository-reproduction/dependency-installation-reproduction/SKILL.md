---
name: dependency-installation-reproduction
description: "Use when \"dependency installation reproduction\" is the work. Install using the committed lockfile in a disposable environment and preserve resolver output."
---

# Dependency Installation Reproduction

Install using the committed lockfile in a disposable environment and preserve resolver output.

1. Read repository instructions before running commands.
2. Locate entry points, build definitions, and pinned dependencies.
3. Minimize the failing input and reproduce it in a disposable clean environment.

Example:
```text
Read repository instructions before running commands.
```

Check: Verify the failure before the fix and success after it; preserve commands, exit codes, checksums, and nondeterminism controls.
