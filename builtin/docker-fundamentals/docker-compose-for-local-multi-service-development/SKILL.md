---
name: docker-compose-for-local-multi-service-development
description: "Use when \"docker compose for local multi service development\" is the work. assuming Composes networking/volume behavior matches production Kubernetes exactly, missing environment-specific bugs only caught after deployment."
---

# Docker Compose for Local Multi-Service Development

assuming Compose's networking/volume behavior matches production Kubernetes.

1. Do not: assuming Compose's networking/volume behavior matches production Kubernetes exactly, missing environment-specific bugs only caught after.
2. Do not: layering multiple Compose override files without verifying the final merged config, causing unexpected setting.

Example:
```yaml
services:
```

Check: Do not: assuming Compose's networking/volume behavior matches production.
