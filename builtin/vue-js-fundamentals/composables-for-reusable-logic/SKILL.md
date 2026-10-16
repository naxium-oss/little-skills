---
name: composables-for-reusable-logic
description: "Use when \"composables for reusable logic\" is the work. defining reactive state as a module-level singleton inside a composable when each component actually needs independent state, causing."
---

# Composables for Reusable Logic

defining reactive state as a module-level singleton inside a composable when.

1. Do not: defining reactive state as a module-level singleton inside a composable when each component actually.
2. Do not: omitting onUnmounted cleanup, accumulating listeners across repeated mount/unmount cycles.

Example:
```javascript
export function useMousePosition() {
```

Check: Do not: defining reactive state as a module-level singleton inside a composable when each component actually needs independent.
