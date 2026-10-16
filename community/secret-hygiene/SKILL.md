---
name: secret-hygiene
description: "Use when \"api key\", \"secret in code\", or \"password in the repo\". Not when security audit of the whole app."
---

# Keep secrets out

A key in a file will be committed. Move it out.

1. Search the diff for keys, tokens, and passwords.
2. Read them from the environment the project already uses.
3. Leave a name in the example env file, not a real value.

Example:
```text
process.env.API_KEY. .env.example has API_KEY= with an empty value.
```

Check: Do not print the secret you just found.
