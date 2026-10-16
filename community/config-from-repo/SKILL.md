---
name: config-from-repo
description: "Use when \"environment variable\", \".env\", or \"config file\" and the code needs a setting. Not when api key is the leak."
---

# Read config from the repo

Use the setting the project already documents.

1. Search for the variable name.
2. Read the example env or config file.
3. Wire that name. Do not invent a second name.

Example:
```text
The repo uses DATABASE_URL. Read process.env.DATABASE_URL.
```

Check: A new variable name the app never reads does nothing.
