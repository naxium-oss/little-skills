---
name: secrets-management-in-ci-pipelines
description: "Use when \"secrets management in ci pipelines\" is the work. printing an environment variable for debugging that happens to contain a secret, leaking it into build logs retained."
---

# Secrets Management in CI Pipelines

printing an environment variable for debugging that happens to contain.

1. Do not: printing an environment variable for debugging that happens to contain a secret, leaking it.
2. Do not: exposing repository secrets to pipeline runs triggered by untrusted fork pull requests.

Example:
```bash
read the workflow triggers, permissions, and runner labels
```

Check: Do not: printing an environment variable for debugging that happens to contain a secret, leaking it into build.
