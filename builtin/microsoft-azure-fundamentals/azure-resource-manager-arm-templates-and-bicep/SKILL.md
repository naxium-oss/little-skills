---
name: azure-resource-manager-arm-templates-and-bicep
description: "Use when \"azure resource manager arm templates and bicep\" is the work."
---

# Azure Resource Manager (ARM) Templates and

applying a Bicep deployment without what-if review, missing.

1. Do not: applying a Bicep deployment without what-if review, missing an unexpected resource replacement flagged only.
2. Do not: making manual portal changes to a Bicep-managed resource, causing silent drift that the next.

Example:
```bicep
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
```

Check: Do not: applying a.
