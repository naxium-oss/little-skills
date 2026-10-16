---
name: networking-volumes-and-container-lifecycle
description: "Use when \"networking volumes and container lifecycle\" is the work. relying on default bridge networking instead of a user-defined network, losing DNS-based service name resolution between containers."
---

# Networking, Volumes, and Container Lifecycle

relying on default bridge networking instead of a.

1. Do not: relying on default bridge networking instead of a user-defined network, losing DNS-based service name.
2. Do not: assuming depends_on (without a healthcheck condition) guarantees the dependency is ready to accept connections.

Example:
```yaml
services:
```

Check: Do not: relying on default bridge networking instead of a user-defined network, losing DNS-based service name resolution between.
