---
name: dependency-injection-and-service-lifetimes
description: "Use when \"dependency injection and service lifetimes\" is the work. injecting a Scoped DbContext into a Singleton service, causing the same database context instance (and its state/connection) to."
---

# Dependency Injection and Service Lifetimes

injecting a Scoped DbContext into a Singleton service, causing the same.

1. Do not: injecting a Scoped DbContext into a Singleton service, causing the same database context instance.
2. Do not: registering a stateful service as Singleton when it actually holds per-request mutable state, causing.

Example:
```bash
dotnet --info
```

Check: Do not: injecting a Scoped DbContext into a Singleton service, causing the same database context instance (and its.
