---
name: frontend-on-a-small-model
description: "Use when \"on a 9B\", \"small model frontend\", or \"one section\". Not when you are not editing UI."
---

# Frontend on a small model

One section per turn, then render it.

1. Read the manifest, the route, and the token file.
2. Build one section. Do not restyle the whole page.
3. Copy real strings from the project. Do not invent prices or quotes.

Example:
```text
Edited the pricing section only. Screenshot at 390px and 1280px.
```

Check: A value that is not in the token file will drift next turn.
