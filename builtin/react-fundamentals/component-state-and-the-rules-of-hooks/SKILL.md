---
name: component-state-and-the-rules-of-hooks
description: "Use when \"component state and the rules of hooks\" is the work. calling hooks conditionally (if (x) useState()), which desyncs hook order between renders and throws or corrupts state silently."
---

# Component State and the Rules of

calling hooks conditionally (if.

1. Do not: calling hooks conditionally (if (x) useState()), which desyncs hook order between renders and throws.
2. Do not: reading a state variable right after calling its setter and expecting the updated value.

Example:
```javascript
function Counter() {
```

Check: Do not: calling hooks conditionally (if (x) useState()), which desyncs hook order between renders and throws or corrupts.
