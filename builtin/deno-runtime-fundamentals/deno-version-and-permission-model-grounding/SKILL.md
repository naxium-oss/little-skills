---
name: deno-version-and-permission-model-grounding
description: "Use when \"deno version and permission model grounding\" is the work. running with --allow-all/-A out of convenience in production, defeating the sandboxing model."
---

# Deno Version and Permission Model Grounding

running with --allow-all/-A out of convenience.

1. Do not: running with --allow-all/-A out of convenience in production, defeating the sandboxing model.
2. Do not: assuming Deno 1.x npm/node compatibility docs apply unchanged to Deno 2.x.

Example:
```bash
deno check .
```

Check: Do not: running with --allow-all/-A out of convenience in production, defeating the sandboxing model.
