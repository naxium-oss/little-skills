---
name: pods-deployments-and-desired-state-reconciliation
description: "Use when \"pods deployments and desired state reconciliation\" is the work. manually kubectl edit-ing a Pod managed by a Deployment and being confused when it reverts."
---

# Pods, Deployments, and Desired-State Reconciliation

manually kubectl edit-ing a Pod managed by.

1. Do not: manually kubectl edit-ing a Pod managed by a Deployment and being confused when it.
2. Do not: not checking kubectl describe pod events, missing the actual scheduling/image-pull/crash reason shown there.

Example:
```bash
kubectl get deploy web -o yaml
```

Check: Do not: manually kubectl edit-ing a Pod managed.
