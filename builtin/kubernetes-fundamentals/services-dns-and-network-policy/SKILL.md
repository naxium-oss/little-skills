---
name: services-dns-and-network-policy
description: "Use when \"services dns and network policy\" is the work. mismatched selector labels between a Service and its target Pods, resulting in zero endpoints with no obvious error."
---

# Services, DNS, and Network Policy

mismatched selector labels between a Service and its target.

1. Do not: mismatched selector labels between a Service and its target Pods, resulting in zero endpoints.
2. Do not: assuming NetworkPolicy is enforced without confirming the cluster's CNI actually supports it.

Example:
```bash
kubectl get endpoints web-service     # empty means selector matches no pods
```

Check: Do not: mismatched selector labels between a Service and its target Pods, resulting in zero endpoints with no.
