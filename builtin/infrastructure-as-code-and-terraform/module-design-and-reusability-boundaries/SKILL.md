---
name: module-design-and-reusability-boundaries
description: "Use when \"module design and reusability boundaries\" is the work. referencing a module by a mutable branch (?ref=main) instead of a pinned tag, causing unreviewed changes to propagate."
---

# Module Design and Reusability Boundaries

referencing a module by a.

1. Do not: referencing a module by a mutable branch (?ref=main) instead of a pinned tag, causing.
2. Do not: designing a module with too many tightly-coupled responsibilities, making it hard to reuse across.

Example:
```hcl
module "vpc" {
```

Check: Do not: referencing a module by a mutable branch (?ref=main) instead of a pinned tag, causing unreviewed changes.
