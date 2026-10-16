---
name: caching-and-persisted-queries
description: "Use when \"caching and persisted queries\" is the work. assuming a CDN caches GraphQL POST responses like REST GETs without explicit persisted-query + GET-based configuration."
---

# Caching and Persisted Queries

assuming a CDN caches GraphQL POST responses like.

1. Do not: assuming a CDN caches GraphQL POST responses like REST GETs without explicit persisted-query +.
2. Do not: forgetting cache normalization requires consistent id/__typename fields across queries to merge correctly.

Example:
```bash
query __schema { types { name } } against the running endpoint
```

Check: Do not: assuming a CDN caches GraphQL POST responses like REST GETs without explicit persisted-query + GET-based configuration.
