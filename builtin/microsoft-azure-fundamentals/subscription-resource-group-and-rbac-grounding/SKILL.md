---
name: subscription-resource-group-and-rbac-grounding
description: "Use when \"subscription resource group and rbac grounding\" is the work. deploying to the wrong subscription because az account set wasnt called or verified after a context switch."
---

# Subscription, Resource Group, and RBAC Grounding

deploying to the wrong subscription because az account.

1. Do not: deploying to the wrong subscription because az account set wasn't called or verified after.
2. Do not: assuming a "Reader" role at the subscription level doesn't apply to a specific resource.

Example:
```bash
az account show
```

Check: Do not: deploying to the wrong subscription because az account set wasn't called or verified after a context.
