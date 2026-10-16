---
name: rbac-roles-rolebindings-and-service-account-scoping
description: "Use when \"rbac roles rolebindings and service account scoping\" is the work."
---

# RBAC Roles, RoleBindings, and Service Account

granting cluster-admin broadly as a.

1. Do not: granting cluster-admin broadly as a shortcut during initial setup and never revisiting it, leaving.
2. Do not: leaving automountServiceAccountToken: true (the default) on Pods that don't need API server access at.

Example:
```bash
kubectl auth can-i delete pods --as=system:serviceaccount:default:web-sa -n default
```

Check: Do not: granting cluster-admin.
