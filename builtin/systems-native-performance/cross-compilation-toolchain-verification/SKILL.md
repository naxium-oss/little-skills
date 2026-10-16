---
name: cross-compilation-toolchain-verification
description: "Use when \"cross compilation toolchain verification\" is the work. Pin compiler, sysroot, target triple, linker, libc, and target execution or emulation environment."
---

# Cross-Compilation Toolchain Verification

Pin compiler, sysroot, target triple, linker, libc, and target execution or emulation environment.

1. Capture compiler, linker, target triple, ABI, libc, and build flags.
2. Inspect symbols and ownership boundaries.

Example:
```text
Capture compiler, linker, target triple, ABI, libc, and build flags.
```

Check: Test unsupported CPU features, sanitizer blind spots, crashes, handle leaks, partial writes, and binary compatibility across supported targets.
