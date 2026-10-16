---
name: concurrency-versus-parallelism-distinction
description: "Use when \"concurrency versus parallelism distinction\" is the work. using threads for CPU-bound work in a language with a global interpreter lock, expecting parallel speedup that doesnt."
---

# Concurrency versus Parallelism Distinction

using threads for CPU-bound work in a language with.

1. Do not: using threads for CPU-bound work in a language with a global interpreter lock, expecting.
2. Do not: assuming async/await alone provides parallelism when it only provides concurrency on a single thread.

Example:
```bash
identify every shared mutable resource and its guard
```

Check: Do not: using threads for CPU-bound work in a language with a global interpreter lock, expecting parallel speedup.
