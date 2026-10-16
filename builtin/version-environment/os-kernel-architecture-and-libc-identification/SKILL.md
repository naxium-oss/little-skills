---
name: os-kernel-architecture-and-libc-identification
description: "Use when \"os kernel architecture and libc identification\" is the work. Capture distribution, kernel, CPU architecture, endianness, and libc family and version independently."
---

# OS, Kernel, Architecture, and libc Identification

Capture distribution, kernel, CPU architecture, endianness, and libc family and version independently.

1. Identify the actual executable or service endpoint used by the failing process.
2. Compare shell resolution with the application process.
3. Collect a machine-readable environment manifest.

Example:
```text
Identify the actual executable or service endpoint used by the failing process.
```

Check: Repeat the check in a clean shell and the real execution context; explain every mismatch.
