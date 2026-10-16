---
name: permissions-auditing-for-third-party-modules
description: "Use when \"permissions auditing for third party modules\" is the work. defaulting to --allow-all to make errors go away without investigating which specific permission was actually needed."
---

# Permissions Auditing for Third-Party Modules

defaulting to --allow-all to make errors go away.

1. Do not: defaulting to --allow-all to make errors go away without investigating which specific permission was.
2. Do not: trusting a third-party module's permission requirements without spot-checking its source for unexpected network/filesystem access.

Example:
```bash
deno run main.ts                     # start with zero permissions
```

Check: Do not: defaulting to.
