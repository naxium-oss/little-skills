---
name: bun-version-and-compatibility-grounding
description: "Use when \"bun version and compatibility grounding\" is the work. assuming full Node API parity for less common modules."
---

# Bun Version and Compatibility Grounding

assuming full Node API parity for less common modules.

1. Do not: assuming full Node API parity for less common modules.
2. Do not: shipping to production without testing under the exact Bun version pinned in CI.

Example:
```bash
bun test
bun run build
```

Check: Do not: assuming full Node API parity for less common modules.
