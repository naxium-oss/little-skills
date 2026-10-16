---
name: reconciliation-keys-and-list-rendering
description: "Use when \"reconciliation keys and list rendering\" is the work."
---

# Reconciliation, Keys, and List Rendering

using key={index} on lists that.

1. Do not: using key={index} on lists that can reorder, filter, or have items inserted/removed, causing input.
2. Do not: regenerating keys (e.g., Math.random()) every render, forcing full remounts and losing state/focus.

Example:
```javascript
{items.map((item) => (
```

Check: Do not: using key={index}.
