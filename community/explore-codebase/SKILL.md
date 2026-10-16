---
name: explore-codebase
description: "Use when \"unfamiliar codebase\", \"where is the entry\", or \"map the repo\". Not when how does a known feature."
---

# Map before editing

Name the entry, the test command, and the files on the path.

1. Read the manifest for scripts and the test command.
2. Open the entry the run script starts.
3. Follow one path from input to output.

Example:
```text
Entry src/main.ts. Test: npm test. Change belongs in src/auth.ts.
```

Check: If you cannot name those, keep reading. Do not edit yet.
