---
name: streams-and-backpressure
description: "Use when \"streams and backpressure\" is the work. chaining .pipe() without error handling on each stream, causing unhandled error events to crash the process."
---

# Streams and Backpressure

chaining .pipe() without error handling on each stream.

1. Do not: chaining .pipe() without error handling on each stream, causing unhandled 'error' events to crash.
2. Do not: buffering an entire stream into memory with on('data') collection instead of processing chunk-by-chunk.

Example:
```javascript
import { pipeline } from "node:stream/promises";
```

Check: Do not: chaining .pipe() without error handling on each.
