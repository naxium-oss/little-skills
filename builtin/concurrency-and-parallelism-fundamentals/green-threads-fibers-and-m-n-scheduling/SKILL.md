---
name: green-threads-fibers-and-m-n-scheduling
description: "Use when \"green threads fibers and m n scheduling\" is the work. assuming all lightweight-thread runtimes transparently handle blocking syscalls without stalling the underlying OS thread, when this varies significantly."
---

# Green Threads, Fibers, and M:N Scheduling

assuming all lightweight-thread runtimes transparently.

1. Do not: assuming all lightweight-thread runtimes transparently handle blocking syscalls without stalling the underlying OS thread.
2. Do not: spawning an extremely large number of lightweight threads without verifying the scheduler's actual overhead.

Example:
```bash
identify every shared mutable resource and its guard
```

Check: Do not: assuming all lightweight-thread runtimes transparently handle blocking.
