---
name: content-negotiation-and-media-type-versioning
description: "Use when \"content negotiation and media type versioning\" is the work. silently defaulting to one format when an unsupported Accept header is sent instead of returning 406, hiding client."
---

# Content Negotiation and Media Type Versioning

silently defaulting to one format.

1. Do not: silently defaulting to one format when an unsupported Accept header is sent instead of.
2. Do not: forgetting Vary: Accept on cached negotiated responses, causing cross-format cache poisoning.

Example:
```bash
curl -sS -D - <endpoint> -o /dev/null
```

Check: Do not: silently defaulting to one format when an unsupported Accept header is sent instead of returning 406.
