---
name: utility-first-composition-and-class-ordering
description: "Use when \"utility first composition and class ordering\" is the work. assuming the last class in the class string always wins for conflicting utilities."
---

# Utility-First Composition and Class Ordering

assuming the last class in the class string always wins for conflicting utilities.

1. Do not: assuming the last class in the class string always wins for conflicting utilities.
2. Do not: hand-writing custom CSS for something a utility already covers, causing specificity fights with Tailwind's.

Example:
```bash
npx tailwindcss --help | head -3
```

Check: Do not: assuming the last class in the class string always wins for conflicting utilities.
