---
name: dockerfile-layer-caching-and-build-context
description: "Use when \"dockerfile layer caching and build context\" is the work. copying the entire source tree before installing dependencies, invalidating the dependency-install cache layer on every source change."
---

# Dockerfile Layer Caching and Build Context

copying the entire source tree before installing dependencies.

1. Do not: copying the entire source tree before installing dependencies, invalidating the dependency-install cache layer on.
2. Do not: missing a .dockerignore, bloating build context and accidentally baking in local secrets or .env.

Example:
```dockerfile
FROM node:22.11.0-bookworm-slim AS deps
```

Check: Do not: copying the entire source tree before installing.
