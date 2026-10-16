---
name: untrusted-pull-request-workflow-isolation
description: "Use when \"untrusted pull request workflow isolation\" is the work. Keep untrusted pull-request code away from write tokens, privileged runners, and deployment secrets."
---

# Untrusted Pull Request Workflow Isolation

Keep untrusted pull-request code away from write tokens, privileged runners, and deployment secrets.

1. Verify workflow syntax and event semantics against current official documentation.
2. Pin third-party actions to reviewed commit identifiers.
3. Isolate untrusted inputs and grant only necessary token permissions.

Example:
```text
Verify workflow syntax and event semantics against current official documentation.
```

Check: Review cache keys, artifact integrity, secret exposure, OIDC audience and subject conditions, required checks, and local reproduction.
