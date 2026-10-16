---
name: immutability-and-persistent-data-structures
description: "Use when \"immutability and persistent data structures\" is the work. assuming a spread-copy ({...obj}) deep-clones nested structures, when it only shallow-copies one level."
---

# Immutability and Persistent Data Structures

assuming a spread-copy ({...obj}) deep-clones nested.

1. Do not: assuming a spread-copy ({...obj}) deep-clones nested structures, when it only shallow-copies one level.
2. Do not: relying on convention-only "treat as immutable" objects that a different part of the codebase.

Example:
```bash
locate the effects: I/O, clock, randomness, mutation
```

Check: Do not: assuming.
