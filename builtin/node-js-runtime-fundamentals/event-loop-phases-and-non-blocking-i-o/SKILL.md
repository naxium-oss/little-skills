---
name: event-loop-phases-and-non-blocking-i-o
description: "Use when \"event loop phases and non blocking i o\" is the work. using synchronous filesystem/crypto calls (readFileSync, execSync) in a request handler."
---

# Event Loop Phases and Non-Blocking I/O

using synchronous filesystem/crypto calls (readFileSync.

1. Do not: using synchronous filesystem/crypto calls (readFileSync, execSync) in a request handler.
2. Do not: scheduling recursive process.nextTick calls that starve I/O.

Example:
```javascript
const fs = require("node:fs");
```

Check: Do not: using synchronous filesystem/crypto calls (readFileSync, execSync) in a request handler.
