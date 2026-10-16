---
name: build-flags-and-environment-variable-grounding
description: "Use when \"build flags and environment variable grounding\" is the work. Compare compile-time substitutions with runtime environment values; redact secrets while preserving whether they are set."
---

# Build Flags and Environment Variable Grounding

Compare compile-time substitutions with runtime environment values; redact secrets while preserving whether they are set.

1. Identify the actual executable or service endpoint used by the failing process.
2. Compare shell resolution with the application process.
3. Collect a machine-readable environment manifest.

Example:
```text
Identify the actual executable or service endpoint used by the failing process.
```

Check: Repeat the check in a clean shell and the real execution context; explain every mismatch.
