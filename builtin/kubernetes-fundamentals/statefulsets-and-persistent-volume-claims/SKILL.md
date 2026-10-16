---
name: statefulsets-and-persistent-volume-claims
description: "Use when \"statefulsets and persistent volume claims\" is the work. assuming a Deployments ephemeral Pods are appropriate for a stateful database, losing data on every rescheduling event."
---

# StatefulSets and Persistent Volume Claims

assuming a Deployment's ephemeral Pods are appropriate for.

1. Do not: assuming a Deployment's ephemeral Pods are appropriate for a stateful database, losing data on.
2. Do not: using a Delete reclaim policy on a StorageClass for critical data, unexpectedly losing volumes.

Example:
```bash
kubectl get pvc -o wide
```

Check: Do not: assuming a Deployment's ephemeral Pods are appropriate for a stateful database, losing data on every rescheduling.
