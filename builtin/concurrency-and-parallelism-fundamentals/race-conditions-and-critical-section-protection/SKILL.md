---
name: race-conditions-and-critical-section-protection
description: "Use when \"race conditions and critical section protection\" is the work. assuming a single Python/JS statement like counter += 1 is atomic when its actually a read-modify-write sequence."
---

# Race Conditions and Critical Section Protection

assuming a single Python/JS statement like counter +=.

1. Do not: assuming a single Python/JS statement like counter += 1 is atomic when it's actually.
2. Do not: adding locks so broadly that they serialize everything, eliminating the concurrency benefit entirely.

Example:
```bash
identify every shared mutable resource and its guard
```

Check: Do not: assuming a single Python/JS statement like counter.
