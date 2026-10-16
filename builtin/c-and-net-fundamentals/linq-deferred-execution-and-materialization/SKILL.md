---
name: linq-deferred-execution-and-materialization
description: "Use when \"linq deferred execution and materialization\" is the work. enumerating an IQueryable multiple times, unknowingly re-executing a database query each time."
---

# LINQ Deferred Execution and Materialization

enumerating an IQueryable multiple times, unknowingly re-executing a database query each time.

1. Do not: enumerating an IQueryable multiple times, unknowingly re-executing a database query each time.
2. Do not: capturing a LINQ query with side-effecting Select projections without realizing deferred execution delays when.

Example:
```bash
dotnet --info
```

Check: Do not: enumerating an IQueryable multiple times, unknowingly re-executing a database query each time.
