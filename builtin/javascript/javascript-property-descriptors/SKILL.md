---
name: javascript-property-descriptors
description: "Use when \"javascript property descriptors\" is the work. Descriptor flags default to false in defineProperty."
---

# JavaScript Property Descriptors

Descriptor flags default to false in defineProperty.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```javascript
const item = {};
Object.defineProperty(item, "id", { value: 7, enumerable: true });
console.assert(item.id === 7);
```

Check: Do not edit the assert to match a surprising result.
