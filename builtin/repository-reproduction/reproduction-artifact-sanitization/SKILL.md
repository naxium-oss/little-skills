---
name: reproduction-artifact-sanitization
description: "Use when \"reproduction artifact sanitization\" is the work. Remove credentials and personal data without changing the mechanism that triggers the defect."
---

# Reproduction Artifact Sanitization

Remove credentials and personal data without changing the mechanism that triggers the defect.

1. Read repository instructions before running commands.
2. Locate entry points, build definitions, and pinned dependencies.
3. Minimize the failing input and reproduce it in a disposable clean environment.

Example:
```text
Read repository instructions before running commands.
```

Check: Verify the failure before the fix and success after it; preserve commands, exit codes, checksums, and nondeterminism controls.
