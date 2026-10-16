---
name: search-before-writing
description: "Use when \"add a helper\", \"is there already\", or \"where should this live\". Not when clone a product."
---

# Search before new code

Search for the behavior before you create it.

1. Search the name and a string a caller would use.
2. Reuse the hit, or say why it does not fit.
3. Then add the smallest new symbol.

Example:
```text
slugify already exists in src/text.ts. Call it.
```

Check: A second helper with the same job is a bug.
