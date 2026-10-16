---
name: cost-visibility-and-dated-pricing-verification
description: "Use when \"cost visibility and dated pricing verification\" is the work. quoting an EC2/S3 price from memory or an old blog post as current."
---

# Cost Visibility and Dated Pricing Verification

quoting an EC2/S3 price from memory.

1. Do not: quoting an EC2/S3 price from memory or an old blog post as current.
2. Do not: forgetting spot price volatility means a "cheap" instance type can spike or be reclaimed.

Example:
```bash
aws ce get-cost-and-usage --time-period Start=2025-01-01,End=2025-02-01 \
```

Check: Do not: quoting.
