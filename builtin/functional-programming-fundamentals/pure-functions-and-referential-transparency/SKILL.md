---
name: pure-functions-and-referential-transparency
description: "Use when \"pure functions and referential transparency\" is the work. claiming a function is pure while it mutates an object passed by reference, silently affecting the callers data."
---

# Pure Functions and Referential Transparency

claiming a function is.

1. Do not: claiming a function is "pure" while it mutates an object passed by reference, silently.
2. Do not: hiding a side effect (logging, caching) inside a function presented as a pure computation.

Example:
```bash
locate the effects: I/O, clock, randomness, mutation
```

Check: Do not: claiming a function is "pure" while it mutates an object passed by reference, silently affecting the.
