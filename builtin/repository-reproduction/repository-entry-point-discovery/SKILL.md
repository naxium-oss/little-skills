---
name: repository-entry-point-discovery
description: "Use when \"repository entry point discovery\" is the work. Trace build and runtime entry points through manifests, scripts, imports, and executable configuration."
---

# Repository Entry-Point Discovery

Trace build and runtime entry points through manifests, scripts, imports, and executable configuration.

1. Read repository instructions before running commands.
2. Locate entry points, build definitions, and pinned dependencies.
3. Minimize the failing input and reproduce it in a disposable clean environment.

Example:
```text
Read repository instructions before running commands.
```

Check: Verify the failure before the fix and success after it; preserve commands, exit codes, checksums, and nondeterminism controls.
