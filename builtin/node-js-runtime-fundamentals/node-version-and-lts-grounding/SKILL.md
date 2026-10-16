---
name: node-version-and-lts-grounding
description: "Use when \"node version and lts grounding\" is the work. assuming a feature landed in a version because it exists in the latest Node docs, without checking when."
---

# Node Version and LTS Grounding

assuming a feature landed in a version because it exists in the latest Node docs, without checking when it was introduced relative.

1. Do not: assuming a feature landed in a version because it exists in the latest Node.
2. Do not: Mixing ESM and CJS assumptions in one file.

Example:
```bash
node --test
npm test
```

Check: Do not: assuming a feature landed in a version because it exists in the latest Node docs, without.
