---
name: fragments-and-query-reusability
description: "Use when \"fragments and query reusability\" is the work. defining near-identical fragments in multiple places instead of sharing one canonical fragment, causing inconsistent field selections across the."
---

# Fragments and Query Reusability

defining near-identical fragments in.

1. Do not: defining near-identical fragments in multiple places instead of sharing one canonical fragment, causing inconsistent.
2. Do not: over-fragmenting trivial single-use selections, adding indirection without meaningful reuse benefit.

Example:
```bash
query __schema { types { name } } against the running endpoint
```

Check: Do not: defining near-identical fragments in multiple places instead of sharing one canonical fragment, causing inconsistent field selections.
