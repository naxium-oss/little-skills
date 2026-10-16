---
name: cost-management-reserved-instances-and-right-sizing
description: "Use when \"cost management reserved instances and right sizing\" is the work."
---

# Cost Management: Reserved Instances and Right-Sizing

purchasing a multi-year Reserved Instance.

1. Do not: purchasing a multi-year Reserved Instance commitment based on a short observation window that doesn't.
2. Do not: downsizing a resource based on average utilization alone without checking peak-load windows, causing performance.

Example:
```bash
az consumption usage list --start-date 2025-01-01 --end-date 2025-02-01 --query "[].{resource:instanceName, cost:pretaxCost}"
```

Check: Do not: purchasing a.
