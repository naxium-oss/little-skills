---
name: compiler-version-and-tsconfig-strictness-grounding
description: "Use when \"compiler version and tsconfig strictness grounding\" is the work. assuming strict: true implies every strictness flag is on in older TS versions where a newer flag was."
---

# Compiler Version and tsconfig Strictness Grounding

assuming strict: true implies every.

1. Do not: assuming strict: true implies every strictness flag is on in older TS versions where.
2. Do not: trusting editor type-checking (which may use a different TS version) over the CI compiler.

Example:
```json
{ "compilerOptions": { "strict": true, "noUncheckedIndexedAccess": true } }
```

Check: Do not: assuming strict: true implies every strictness flag.
