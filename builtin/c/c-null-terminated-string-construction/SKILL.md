---
name: c-null-terminated-string-construction
description: "Use when \"c null terminated string construction\" is the work. A C string requires a terminating null within accessible storage."
---

# C Null-Terminated String Construction

A C string requires a terminating null within accessible storage.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```c
char buffer[8];
int written = snprintf(buffer, sizeof buffer, "%s", "hello");
assert(written >= 0 && (size_t)written < sizeof buffer);
```

Check: Do not edit the assert to match a surprising result.
