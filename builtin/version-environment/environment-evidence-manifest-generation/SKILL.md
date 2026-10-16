---
name: environment-evidence-manifest-generation
description: "Use when \"environment evidence manifest generation\" is the work. Emit a machine-readable manifest with artifact hashes, observation timestamps, commands, and unresolved fields."
---

# Environment Evidence Manifest Generation

Emit a machine-readable manifest with artifact hashes, observation timestamps, commands, and unresolved fields.

1. Identify the actual executable or service endpoint used by the failing process.
2. Compare shell resolution with the application process.
3. Collect a machine-readable environment manifest.

Example:
```text
Identify the actual executable or service endpoint used by the failing process.
```

Check: Repeat the check in a clean shell and the real execution context; explain every mismatch.
