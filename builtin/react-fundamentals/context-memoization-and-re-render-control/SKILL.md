---
name: context-memoization-and-re-render-control
description: "Use when \"context memoization and re render control\" is the work. wrapping every component in React.memo without profiling, adding comparison overhead with no measured benefit."
---

# Context, Memoization, and Re-Render Control

wrapping every component in React.memo without profiling.

1. Do not: wrapping every component in React.memo without profiling, adding comparison overhead with no measured benefit.
2. Do not: passing a new inline object/function as a context value every render, defeating consumers' memoization.

Example:
```javascript
const value = useMemo(() => ({ user, theme }), [user, theme]); // stable identity
```

Check: Do not: wrapping every.
