---
name: status-codes-and-error-response-design
description: "Use when \"status codes and error response design\" is the work. returning 200 OK with an {error: ...} body instead of a proper 4xx/5xx status, breaking HTTP-level error handling."
---

# Status Codes and Error Response Design

returning 200 OK with an.

1. Do not: returning 200 OK with an {"error": ...} body instead of a proper 4xx/5xx status.
2. Do not: conflating 401 Unauthorized (missing/invalid credentials) with 403 Forbidden (authenticated but not permitted).

Example:
```bash
curl -sS -D - <endpoint> -o /dev/null
```

Check: Do not: returning 200.
