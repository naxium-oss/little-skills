---
name: debug-csharp
description: "Use when \"csharp NullReferenceException\", \"NullReferenceException\". Not when explaining working csharp code."
---

# Debug csharp

Reproduce the csharp failure with the project command, then change one thing.

1. NullReferenceException: The stack names the line; check DI registrations, async gaps, and `!`/nullable suppression hiding a.
2. Deadlock on .Result: Async code calling `.Result` on a captured SynchronizationContext blocks; use `await` all the.
3. EF Core N+1 or missing data: Enable query logging (`LogTo`); check `Include`/`ThenInclude`, lazy loading proxies, and.

Example:
```text
dotnet build
```

Check: The same command that failed has to pass.
