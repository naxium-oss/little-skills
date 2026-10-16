---
name: memory-efficiency-and-dtype-optimization
description: "Use when \"memory efficiency and dtype optimization\" is the work. downcasting a numeric column to a smaller dtype without checking its actual value range, causing silent overflow/wraparound."
---

# Memory Efficiency and Dtype Optimization

downcasting a numeric column to a smaller dtype.

1. Do not: downcasting a numeric column to a smaller dtype without checking its actual value range.
2. Do not: leaving high-cardinality-looking-but-actually-repetitive string columns as object dtype, wasting significant memory versus category.

Example:
```bash
print df.dtypes, df.shape, and df.head() before transforming
```

Check: Do not: downcasting a numeric column to a smaller.
