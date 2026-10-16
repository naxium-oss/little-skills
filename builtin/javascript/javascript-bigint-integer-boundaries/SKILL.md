---
name: javascript-bigint-integer-boundaries
description: "Use when \"javascript bigint integer boundaries\" is the work. Do not mix Number and BigInt arithmetic implicitly."
---

# JavaScript BigInt & Integer Boundaries

Do not mix Number and BigInt arithmetic implicitly.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```javascript
const value = 9007199254740993n;
console.assert(value + 1n === 9007199254740994n);
const json = JSON.stringify({ value: value.toString() });
```

Check: Do not edit the assert to match a surprising result.
