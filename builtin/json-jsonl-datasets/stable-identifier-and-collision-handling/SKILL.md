---
name: stable-identifier-and-collision-handling
description: "Use when \"stable identifier and collision handling\" is the work. Use stable identifier derivation and explicit reject, rename, or merge behavior for collisions."
---

# Stable Identifier and Collision Handling

Use stable identifier derivation and explicit reject, rename, or merge behavior for collisions.

1. Inspect encoding, record schema, identifiers, and dataset size.
2. Stream transformations into a new artifact rather than overwriting the source.

Example:
```text
Inspect encoding, record schema, identifiers, and dataset size.
```

Check: Test malformed lines, empty files, Unicode, nested nulls, duplicates, memory bounds, and deterministic output under repeated runs.
