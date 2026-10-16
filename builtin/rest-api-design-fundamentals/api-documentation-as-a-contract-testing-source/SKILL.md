---
name: api-documentation-as-a-contract-testing-source
description: "Use when \"api documentation as a contract testing source\" is the work. hand-writing an OpenAPI spec once and never validating it against the running API again, letting it silently drift."
---

# API Documentation as a Contract Testing

hand-writing an OpenAPI spec once.

1. Do not: hand-writing an OpenAPI spec once and never validating it against the running API again.
2. Do not: generating client SDKs from a stale spec, shipping clients that don't match actual server.

Example:
```bash
curl -sS -D - <endpoint> -o /dev/null
```

Check: Do not: hand-writing an.
