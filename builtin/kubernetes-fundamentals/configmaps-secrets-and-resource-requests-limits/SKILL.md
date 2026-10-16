---
name: configmaps-secrets-and-resource-requests-limits
description: "Use when \"configmaps secrets and resource requests limits\" is the work. treating base64-encoded Secrets as encrypted and storing them in plaintext version control."
---

# ConfigMaps, Secrets, and Resource Requests/Limits

treating base64-encoded Secrets as encrypted and storing them in plaintext version control.

1. Do not: treating base64-encoded Secrets as encrypted and storing them in plaintext version control.
2. Do not: setting memory limits far below actual peak usage observed via kubectl top, causing avoidable.

Example:
```yaml
resources:
```

Check: Do not: treating base64-encoded Secrets as encrypted and storing them in plaintext version control.
