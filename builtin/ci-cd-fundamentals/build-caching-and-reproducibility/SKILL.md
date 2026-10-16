---
name: build-caching-and-reproducibility
description: "Use when \"build caching and reproducibility\" is the work. keying a cache only by branch name, silently serving stale dependencies after a lockfile update on the same."
---

# Build Caching and Reproducibility

keying a cache only by branch name, silently serving.

1. Do not: keying a cache only by branch name, silently serving stale dependencies after a lockfile.
2. Do not: never testing a cold/no-cache build, only discovering a reproducibility break during an actual cache.

Example:
```bash
read the workflow triggers, permissions, and runner labels
```

Check: Do not: keying a cache only by branch name, silently serving stale dependencies after a lockfile update on.
