---
name: component-extraction-versus-utility-duplication
description: "Use when \"component extraction versus utility duplication\" is the work. extracting a component too early with only one real use case, guessing at a variant API that doesnt."
---

# Component Extraction versus Utility Duplication

extracting a component too early with only one real use case.

1. Do not: extracting a component too early with only one real use case, guessing at a.
2. Do not: copy-pasting long utility strings across a dozen components instead of extracting a shared one.

Example:
```bash
npx tailwindcss --help | head -3
```

Check: Do not: extracting a component too early with only one real use case, guessing at a variant API.
