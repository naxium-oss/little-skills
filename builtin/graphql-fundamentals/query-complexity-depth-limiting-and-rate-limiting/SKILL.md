---
name: query-complexity-depth-limiting-and-rate-limiting
description: "Use when \"query complexity depth limiting and rate limiting\" is the work. deploying a GraphQL API with no query cost analysis, allowing a single client request to fan out into."
---

# Query Complexity, Depth Limiting, and Rate

deploying a GraphQL API with.

1. Do not: deploying a GraphQL API with no query cost analysis, allowing a single client request.
2. Do not: rate-limiting only by request count, missing that GraphQL requests vary enormously in actual server.

Example:
```bash
query __schema { types { name } } against the running endpoint
```

Check: Do not: deploying a GraphQL API with no query.
