---
name: engine-and-specification-version-grounding
description: "Use when \"engine and specification version grounding\" is the work. assuming a Baseline widely available feature works in all target browsers without checking the actual support table date."
---

# Engine and Specification Version Grounding

assuming a Baseline "widely available" feature works in all target browsers without checking the actual support table date.

1. Do not: assuming a Baseline "widely available" feature works in all target browsers without checking the.
2. Do not: testing only in one engine and shipping to others.

Example:
```bash
node --check <file>
node --test
```

Check: Do not: assuming a Baseline "widely available" feature works in all target browsers without checking the actual support.
