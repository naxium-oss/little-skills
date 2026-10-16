---
name: concurrency-threads-executors-and-virtual-threads
description: "Use when \"concurrency threads executors and virtual threads\" is the work. sizing a fixed thread pool by copying a number from a tutorial instead of measuring actual CPU core."
---

# Concurrency: Threads, Executors, and Virtual Threads

sizing a fixed thread pool by copying a number from a.

1. Do not: sizing a fixed thread pool by copying a number from a tutorial instead of.
2. Do not: using synchronized around blocking calls inside virtual threads on JDK versions where this caused.

Example:
```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
```

Check: Do not: sizing a fixed thread pool by copying a number from a tutorial instead of measuring actual.
