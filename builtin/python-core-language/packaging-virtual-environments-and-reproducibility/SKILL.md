---
name: packaging-virtual-environments-and-reproducibility
description: "Use when \"packaging virtual environments and reproducibility\" is the work. installing globally with sudo pip install."
---

# Packaging, Virtual Environments, and Reproducibility

installing globally with sudo pip install.

1. Do not: installing globally with sudo pip install.
2. Do not: assuming requirements.txt without hashes is reproducible across machines with different available wheels.

Example:
```bash
python3 --version
python3 -c "import sys; print(sys.version_info, sys.implementation.name)"
```

Check: Do not: installing globally with sudo pip install.
