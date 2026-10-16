---
name: repository-instruction-and-convention-discovery
description: "Use when \"repository instruction and convention discovery\" is the work. Read root and nested repository instructions and infer conventions from nearby maintained code."
---

# Repository Instruction and Convention Discovery

Read root and nested repository instructions and infer conventions from nearby maintained code.

1. Read repository instructions before running commands.
2. Locate entry points, build definitions, and pinned dependencies.
3. Minimize the failing input and reproduce it in a disposable clean environment.

Example:
```text
Read repository instructions before running commands.
```

Check: Verify the failure before the fix and success after it; preserve commands, exit codes, checksums, and nondeterminism controls.
