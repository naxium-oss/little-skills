---
name: lockfile-and-dependency-graph-inspection
description: "Use when \"lockfile and dependency graph inspection\" is the work. Compare manifest ranges with lockfile resolutions and flag lockfile changes caused by installation."
---

# Lockfile and Dependency Graph Inspection

Compare manifest ranges with lockfile resolutions and flag lockfile changes caused by installation.

1. Identify the actual executable or service endpoint used by the failing process.
2. Compare shell resolution with the application process.
3. Collect a machine-readable environment manifest.

Example:
```text
Identify the actual executable or service endpoint used by the failing process.
```

Check: Repeat the check in a clean shell and the real execution context; explain every mismatch.
