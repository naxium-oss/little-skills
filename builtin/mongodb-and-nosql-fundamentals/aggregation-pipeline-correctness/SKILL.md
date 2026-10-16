---
name: aggregation-pipeline-correctness
description: "Use when \"aggregation pipeline correctness\" is the work. placing $match after an expensive $lookup/$group instead of before, processing far more documents than necessary."
---

# Aggregation Pipeline Correctness

placing $match after an expensive $lookup/$group instead.

1. Do not: placing $match after an expensive $lookup/$group instead of before, processing far more documents than.
2. Do not: forgetting $unwind turns an array field into one document per element, multiplying downstream counts.

Example:
```javascript
db.orders.aggregate([
```

Check: Do not: placing $match after an expensive $lookup/$group instead of before, processing far more documents than necessary.
