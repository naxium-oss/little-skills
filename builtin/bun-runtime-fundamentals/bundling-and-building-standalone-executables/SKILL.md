---
name: bundling-and-building-standalone-executables
description: "Use when \"bundling and building standalone executables\" is the work. assuming a --compile binary built on macOS runs on a Linux container without cross-target flags."
---

# Bundling and Building Standalone Executables

assuming a --compile binary built on macOS.

1. Do not: assuming a --compile binary built on macOS runs on a Linux container without cross-target.
2. Do not: missing native addons that don't bundle correctly into a single binary.

Example:
```bash
bun build ./src/index.ts --outdir ./dist --target browser --minify
```

Check: Do not: assuming a --compile binary built on macOS runs on a Linux container without cross-target flags.
