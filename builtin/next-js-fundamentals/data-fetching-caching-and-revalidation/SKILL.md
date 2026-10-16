---
name: data-fetching-caching-and-revalidation
description: "Use when \"data fetching caching and revalidation\" is the work. assuming Next 14 caching defaults apply unchanged to a Next 15 project."
---

# Data Fetching, Caching, and Revalidation

assuming Next 14 caching defaults apply unchanged to a Next 15 project.

1. Do not: assuming Next 14 caching defaults apply unchanged to a Next 15 project.
2. Do not: forgetting to call revalidateTag/revalidatePath after a mutation, serving stale cached data indefinitely.

Example:
```tsx
const res = await fetch(`${API}/products/${id}`, {
```

Check: Do not: assuming Next 14 caching defaults apply unchanged to a Next 15 project.
