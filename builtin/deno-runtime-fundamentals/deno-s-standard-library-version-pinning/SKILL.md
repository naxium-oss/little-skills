---
name: deno-s-standard-library-version-pinning
description: "Use when \"deno s standard library version pinning\" is the work."
---

# Deno's Standard Library Version Pinning

assuming all @std modules share one version.

1. Do not: assuming all @std modules share one version number and upgrading them as a monolith.
2. Do not: relying on a pre-1.0.

Example:
```json
{ "imports": { "@std/path": "jsr:@std/path@^1.0.0", "@std/testing": "jsr:@std/testing@^1.0.5" } }
```

Check: Do not: assuming all.
