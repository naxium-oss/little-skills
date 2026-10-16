---
name: azure-storage-and-blob-access-control
description: "Use when \"azure storage and blob access control\" is the work. assuming revoking a users RBAC role immediately invalidates SAS tokens they previously generated."
---

# Azure Storage and Blob Access Control

assuming revoking a user's RBAC role immediately invalidates SAS tokens they previously generated.

1. Do not: assuming revoking a user's RBAC role immediately invalidates SAS tokens they previously generated.
2. Do not: leaving allowBlobPublicAccess enabled account-wide when only one specific container needs public read access.

Example:
```bash
az storage account show --name mystorageacct --query "allowBlobPublicAccess"
```

Check: Do not: assuming revoking a user's RBAC role immediately invalidates SAS tokens they previously generated.
