---
name: pinia-state-management-patterns
description: "Use when \"pinia state management patterns\" is the work. calling useCartStore() outside of a component setup or an active Pinia instance (e.g., in a plain module at."
---

# Pinia State Management Patterns

calling useCartStore() outside of a.

1. Do not: calling useCartStore() outside of a component setup or an active Pinia instance (e.g., in.
2. Do not: mutating nested store state deeply without going through a documented pattern, making changes hard.

Example:
```javascript
export const useCartStore = defineStore("cart", {
```

Check: Do not: calling useCartStore() outside of a component setup or an active Pinia instance (e.g., in a plain.
