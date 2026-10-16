---
name: environment-variables-and-shell-configuration-files
description: "Use when \"environment variables and shell configuration files\" is the work. setting PATH/env vars only in .bashrc, then wondering why a cron job or systemd service (non-interactive, non-login) cant."
---

# Environment Variables and Shell Configuration Files

setting PATH/env vars only in.

1. Do not: setting PATH/env vars only in .bashrc, then wondering why a cron job or systemd.
2. Do not: assuming .bash_profile sources on every new terminal tab (it often doesn't for non-login shells).

Example:
```bash
echo $PATH
```

Check: Do not: setting PATH/env.
