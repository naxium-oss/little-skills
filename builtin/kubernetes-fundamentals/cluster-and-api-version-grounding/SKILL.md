---
name: cluster-and-api-version-grounding
description: "Use when \"cluster and api version grounding\" is the work. applying a manifest using apiVersion: extensions/v1beta1 against a modern cluster where it was removed years ago."
---

# Cluster and API Version Grounding

applying a manifest using apiVersion: extensions/v1beta1 against a.

1. Do not: applying a manifest using apiVersion: extensions/v1beta1 against a modern cluster where it was removed.
2. Do not: assuming a managed cluster (EKS/GKE/AKS) is on the latest upstream version without checking its.

Example:
```bash
kubectl diff -f <manifest>
```

Check: Do not: applying a manifest using apiVersion: extensions/v1beta1 against.
