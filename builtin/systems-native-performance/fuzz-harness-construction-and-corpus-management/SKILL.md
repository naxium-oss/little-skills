---
name: fuzz-harness-construction-and-corpus-management
description: "Use when \"fuzz harness construction and corpus management\" is the work. Build deterministic bounded harnesses and preserve crashes, seeds, minimized corpora, and sanitizer settings."
---

# Fuzz Harness Construction and Corpus Management

Build deterministic bounded harnesses and preserve crashes, seeds, minimized corpora, and sanitizer settings.

1. Capture compiler, linker, target triple, ABI, libc, and build flags.
2. Inspect symbols and ownership boundaries.

Example:
```text
Capture compiler, linker, target triple, ABI, libc, and build flags.
```

Check: Test unsupported CPU features, sanitizer blind spots, crashes, handle leaks, partial writes, and binary compatibility across supported targets.
