---
name: cloud-storage-and-iam-uniform-bucket-level-access
description: "Use when \"cloud storage and iam uniform bucket level access\" is the work. leaving a bucket with legacy ACLs where an object-level ACL unexpectedly grants broader access than the bucket policy."
---

# Cloud Storage and IAM Uniform Bucket-Level

leaving a bucket with.

1. Do not: leaving a bucket with legacy ACLs where an object-level ACL unexpectedly grants broader access.
2. Do not: granting allUsers read access for a "quick public link" and forgetting to revoke it.

Example:
```bash
gsutil uniformbucketlevelaccess get gs://my-app-bucket
```

Check: Do not: leaving a bucket with legacy ACLs where.
