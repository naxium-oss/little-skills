---
name: time-series-handling-with-pandas-datetimeindex
description: "Use when \"time series handling with pandas datetimeindex\" is the work."
---

# Time Series Handling with Pandas DatetimeIndex

mixing timezone-naive and timezone-aware timestamps in the same.

1. Do not: mixing timezone-naive and timezone-aware timestamps in the same DataFrame, causing comparison/join errors or silent.
2. Do not: resampling a non-additive column (like a snapshot balance) with sum() instead of last()/mean(), producing.

Example:
```bash
print df.dtypes, df.shape, and df.head() before transforming
```

Check: Do not: mixing timezone-naive.
