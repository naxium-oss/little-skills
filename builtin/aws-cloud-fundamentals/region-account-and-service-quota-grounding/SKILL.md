---
name: region-account-and-service-quota-grounding
description: "Use when \"region account and service quota grounding\" is the work. assuming a resource created in us-east-1 is visible/usable in us-west-2 without explicit replication."
---

# Region, Account, and Service Quota Grounding

assuming a resource created in us-east-1.

1. Do not: assuming a resource created in us-east-1 is visible/usable in us-west-2 without explicit replication.
2. Do not: hitting an undocumented-to-the-team default quota limit in production because it was never verified in.

Example:
```bash
aws sts get-caller-identity
```

Check: Do not: assuming.
