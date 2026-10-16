---
name: promises-async-await-and-error-propagation
description: "Use when \"promises async await and error propagation\" is the work. using Promise.all when partial failures should be tolerated."
---

# Promises, async/await, and Error Propagation

using Promise.all when partial failures should be tolerated.

1. Do not: using Promise.all when partial failures should be tolerated.
2. Do not: forgetting await inside a .map() callback, producing an array of pending Promises instead of.

Example:
```javascript
async function loadUser(id) {
try {
const res = await fetch(`/api/users/${id}`);
```

Check: Do not: using Promise.all when partial failures should be tolerated.
