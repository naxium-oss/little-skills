---
name: factory-and-builder-patterns-for-object-construction
description: "Use when \"factory and builder patterns for object construction\" is the work. wrapping a trivial constructor in a Factory for future flexibility that never materializes."
---

# Factory and Builder Patterns for Object

wrapping a trivial constructor in a Factory "for future flexibility" that never materializes.

1. Do not: wrapping a trivial constructor in a Factory "for future flexibility" that never materializes.
2. Do not: making a Builder mutable and shared across threads without considering thread-safety of the builder.

Example:
```bash
map the callers and the concrete types actually constructed
```

Check: Do not: wrapping a trivial constructor in a Factory "for future flexibility" that never materializes.
