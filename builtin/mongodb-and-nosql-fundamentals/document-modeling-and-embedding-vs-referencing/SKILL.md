---
name: document-modeling-and-embedding-vs-referencing
description: "Use when \"document modeling and embedding vs referencing\" is the work. embedding an unbounded array (e.g., all comments ever made) that eventually hits the 16MB document limit."
---

# Document Modeling and Embedding vs. Referencing

embedding an unbounded array (e.g., all comments ever.

1. Do not: embedding an unbounded array (e.g., all comments ever made) that eventually hits the 16MB.
2. Do not: over-normalizing into many collections requiring $lookup joins for every simple read, hurting performance.

Example:
```javascript
// Embedded: order + line items read/written together, bounded count
```

Check: Do not: embedding an.
