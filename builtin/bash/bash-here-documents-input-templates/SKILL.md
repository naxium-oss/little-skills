---
name: bash-here-documents-input-templates
description: "Use when \"bash here documents input templates\" is the work. A quoted here-document delimiter disables parameter and command expansion in its body."
---

# Bash Here-Documents & Input Templates

A quoted here-document delimiter disables parameter and command expansion in its body.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```bash
name="Ada"
cat <<EOF
Hello $name
```

Check: Do not edit the assert to match a surprising result.
