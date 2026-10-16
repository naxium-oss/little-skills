---
name: package-management-across-distributions
description: "Use when \"package management across distributions\" is the work. forgetting apt-get update before install in a fresh container layer, installing a stale cached version."
---

# Package Management Across Distributions

forgetting apt-get update before install in a fresh container layer, installing a stale cached version.

1. Do not: forgetting apt-get update before install in a fresh container layer, installing a stale cached.
2. Do not: leaving apt cache files in container images, bloating size unnecessarily.

Example:
```bash
sh -n <script>
command -v <tool>
```

Check: Do not: forgetting apt-get update before install in a fresh container layer, installing a stale cached version.
