---
name: monorepo-workspaces-and-dependency-hoisting
description: "Use when \"monorepo workspaces and dependency hoisting\" is the work. importing a package that resolves successfully only due to hoisting from a sibling workspaces dependency, without declaring it."
---

# Monorepo Workspaces and Dependency Hoisting

importing a package that resolves.

1. Do not: importing a package that resolves successfully only due to hoisting from a sibling workspace's.
2. Do not: running build scripts without configuring task-graph caching (Turborepo/Nx), rebuilding unaffected packages on every change.

Example:
```bash
read the lockfile format and the declared manager in the manifest
```

Check: Do not: importing a package that resolves successfully only due to hoisting from a sibling workspace's dependency, without.
