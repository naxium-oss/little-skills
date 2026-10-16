---
name: bun-as-package-manager-install-and-lockfile
description: "Use when \"bun as package manager install and lockfile\" is the work. running npm install in a Bun project and overwriting bun.lockb implicitly via a stray package-lock.json."
---

# Bun as Package Manager: Install and

running npm install in a Bun project.

1. Do not: running npm install in a Bun project and overwriting bun.lockb implicitly via a stray.
2. Do not: assuming bunfig.toml registry overrides apply retroactively to an existing lockfile without reinstalling.

Example:
```bash
bun install
```

Check: Do not: running npm install in a Bun project and overwriting bun.lockb implicitly via a stray package-lock.json.
