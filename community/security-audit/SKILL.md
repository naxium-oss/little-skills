---
name: security-audit
description: "Use when \"security audit\", \"secrets scan\", or \"check for vulnerabilities\". Not when exploit, payload, or poc."
---

# Security audit

Report the hole and the fix. Do not write an attack.

1. Search for secrets, injection, XSS, SSRF, path traversal, and unsafe spawn.
2. Open each hit and keep it only if the code is really reachable.
3. State severity, file, impact, and the fix.

Example:
```text
src/run.ts passes user input to spawn. Pass an arg array.
```

Check: No payload and no proof-of-concept attack in the report.
