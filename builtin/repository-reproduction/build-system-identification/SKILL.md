---
name: build-system-identification
description: "Use when \"build system identification\" is the work. Identify the authoritative build graph, generated files, toolchain pins, and platform-specific targets."
---

# Build System Identification

Identify the authoritative build graph, generated files, toolchain pins, and platform-specific targets.

1. Read repository instructions before running commands.
2. Locate entry points, build definitions, and pinned dependencies.
3. Minimize the failing input and reproduce it in a disposable clean environment.

Example:
```text
Read repository instructions before running commands.
```

Check: Verify the failure before the fix and success after it; preserve commands, exit codes, checksums, and nondeterminism controls.
