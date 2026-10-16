---
name: s3-storage-classes-lifecycle-rules-and-consistency-model
description: "Use when \"s3 storage classes lifecycle rules and consistency model\" is the work."
---

# S3 Storage Classes, Lifecycle Rules, and

applying an aggressive lifecycle rule that transitions frequently-accessed.

1. Do not: applying an aggressive lifecycle rule that transitions frequently-accessed objects to Glacier, causing unexpected retrieval.
2. Do not: assuming outdated eventual-consistency caveats from old blog posts still apply to modern S3 behavior.

Example:
```bash
aws s3api put-bucket-lifecycle-configuration --bucket my-bucket --lifecycle-configuration file://lifecycle.json
```

Check: Do not: applying an.
