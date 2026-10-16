---
name: web-vitals-perf
description: "Use when \"LCP\", \"CLS\", \"INP\", or \"web vitals\". Not when the page has not been loaded."
---

# Web vitals

Measure after paint. Do not guess the score.

1. Load the page and read LCP, CLS, and INP.
2. Fix the largest image, layout shift, or long handler first.
3. Reload and compare the numbers.

Example:
```text
LCP was the hero image at 4.2s. Compress it and remeasure.
```

Check: A score you did not read from the page is a guess.
