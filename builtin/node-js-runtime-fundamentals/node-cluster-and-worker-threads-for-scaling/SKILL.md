---
name: node-cluster-and-worker-threads-for-scaling
description: "Use when \"node cluster and worker threads for scaling\" is the work. reaching for cluster to solve a CPU-bound bottleneck when worker_threads is the correct tool, since cluster only multiplies."
---

# Node Cluster and Worker Threads for

reaching for cluster to solve.

1. Do not: reaching for cluster to solve a CPU-bound bottleneck when worker_threads is the correct tool.
2. Do not: forgetting worker threads have separate memory by default, requiring explicit message passing or SharedArrayBuffer.

Example:
```javascript
import { Worker, isMainThread, parentPort } from "node:worker_threads";
```

Check: Do not: reaching for cluster to solve a CPU-bound.
