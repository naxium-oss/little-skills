---
name: installed-runtime-version-verification
description: "Use when \"installed runtime version verification\" is the work. Resolve executable symlinks and compare the runtime path inside the actual process, not only the login shell."
---

# Installed Runtime Version Verification

Resolve executable symlinks and compare the runtime path inside the actual process, not only the login shell.

1. Identify the actual executable or service endpoint used by the failing process.
2. Compare shell resolution with the application process.
3. Collect a machine-readable environment manifest.

Example:
```text
Identify the actual executable or service endpoint used by the failing process.
```

Check: Repeat the check in a clean shell and the real execution context; explain every mismatch.
