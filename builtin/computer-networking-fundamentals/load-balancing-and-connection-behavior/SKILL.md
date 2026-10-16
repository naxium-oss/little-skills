---
name: load-balancing-and-connection-behavior
description: "Use when \"load balancing and connection behavior\" is the work. using a shallow liveness check as the load balancers health endpoint, routing traffic to instances that are alive."
---

# Load Balancing and Connection Behavior

using a shallow liveness check.

1. Do not: using a shallow liveness check as the load balancer's health endpoint, routing traffic to.
2. Do not: assuming zero-downtime deploys work without testing actual in-flight request behavior during a real rollout.

Example:
```bash
resolve the name and confirm the address actually used
```

Check: Do not: using a shallow liveness check as the load balancer's health endpoint, routing traffic to instances that.
