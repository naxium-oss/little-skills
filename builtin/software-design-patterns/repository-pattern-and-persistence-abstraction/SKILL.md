---
name: repository-pattern-and-persistence-abstraction
description: "Use when \"repository pattern and persistence abstraction\" is the work. leaking ORM-specific query builder objects or SQL fragments through the repository interface, coupling business logic to the underlying."
---

# Repository Pattern and Persistence Abstraction

leaking ORM-specific query builder objects.

1. Do not: leaking ORM-specific query builder objects or SQL fragments through the repository interface, coupling business.
2. Do not: creating an overly generic repository interface (query(criteria: any)) that just re-exposes raw query capability.

Example:
```bash
map the callers and the concrete types actually constructed
```

Check: Do not: leaking ORM-specific query builder objects or SQL.
