---
name: horizontal-pod-autoscaling-and-resource-based-scaling-decisions
description: "Use when \"horizontal pod autoscaling and resource based scaling decisions\" is the work."
---

# Horizontal Pod Autoscaling and Resource-Based Scaling

omitting resource requests on the.

1. Do not: omitting resource requests on the target Deployment, causing HPA's percentage-based CPU target to be.
2. Do not: scaling on CPU alone for an I/O-bound or queue-depth-driven workload, missing the actual bottleneck.

Example:
```bash
kubectl autoscale deployment web --cpu-percent=60 --min=2 --max=10
```

Check: Do not: omitting resource.
