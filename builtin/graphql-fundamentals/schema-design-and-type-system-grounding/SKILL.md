---
name: schema-design-and-type-system-grounding
description: "Use when \"schema design and type system grounding\" is the work. marking a field non-nullable when the underlying data source can legitimately be absent, causing cascading null propagation errors."
---

# Schema Design and Type System Grounding

marking a field non-nullable.

1. Do not: marking a field non-nullable when the underlying data source can legitimately be absent, causing.
2. Do not: exposing internal database field names directly in the schema, coupling the API contract to.

Example:
```bash
query __schema { types { name } } against the running endpoint
```

Check: Do not: marking a field non-nullable when the underlying.
