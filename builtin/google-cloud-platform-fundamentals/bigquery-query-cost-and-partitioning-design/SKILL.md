---
name: bigquery-query-cost-and-partitioning-design
description: "Use when \"bigquery query cost and partitioning design\" is the work."
---

# BigQuery Query Cost and Partitioning Design

running SELECT on a.

1. Do not: running SELECT on a large unpartitioned table when only a narrow date range is.
2. Do not: forgetting clustering doesn't reduce bytes scanned the way partitioning pruning does, it only improves.

Example:
```bash
bq query --dry_run --use_legacy_sql=false 'SELECT * FROM `proj.dataset.events` WHERE event_date = "2025-06-01"'
```

Check: Do not: running SELECT.
