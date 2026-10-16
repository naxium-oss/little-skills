---
name: build-tool-transformation-pipelines-vite-webpack-esbuild
description: "Use when \"build tool transformation pipelines vite webpack esbuild\" is the work."
---

# Build Tool Transformation Pipelines (Vite/webpack/esbuild)

assuming dev-server behavior (unminified.

1. Do not: assuming dev-server behavior (unminified, unbundled, HMR-enabled) predicts production build output correctness, missing production-only bugs.
2. Do not: misordering plugins so a transform runs on already-transformed (or not-yet-transformed) code, causing subtle build.

Example:
```bash
read the lockfile format and the declared manager in the manifest
```

Check: Do not: assuming dev-server.
