---
name: sharding-for-horizontal-scale
description: "Use when \"sharding for horizontal scale\" is the work. choosing a low-cardinality or monotonically increasing shard key (like a timestamp), causing uneven write distribution and hotspotting on."
---

# Sharding for Horizontal Scale

choosing a low-cardinality or monotonically.

1. Do not: choosing a low-cardinality or monotonically increasing shard key (like a timestamp), causing uneven write.
2. Do not: querying without the shard key in the filter, forcing an expensive scatter-gather across every.

Example:
```javascript
sh.shardCollection("app.orders", { customerId: "hashed" });
```

Check: Do not: choosing a low-cardinality or monotonically increasing shard.
