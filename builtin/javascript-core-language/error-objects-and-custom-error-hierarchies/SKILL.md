---
name: error-objects-and-custom-error-hierarchies
description: "Use when \"error objects and custom error hierarchies\" is the work. throwing strings (throw failed) which lose stack traces."
---

# Error Objects and Custom Error Hierarchies

throwing strings (throw "failed") which lose stack traces.

1. Do not: throwing strings (throw "failed") which lose stack traces.
2. Do not: catching errors broadly and re-throwing a new error without preserving cause (new Error("wrap", {.

Example:
```javascript
class ValidationError extends Error {
constructor(message, field) {
super(message);
```

Check: Do not: throwing strings (throw "failed") which lose stack traces.
