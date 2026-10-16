---
name: docker-security-image-scanning-and-least-privilege-runtime
description: "Use when \"docker security image scanning and least privilege runtime\" is the work. running vulnerability scans that only produce a report nobody reviews, without a CI gate that blocks builds on."
---

# Docker Security: Image Scanning and Least-Privilege

running vulnerability scans that only.

1. Do not: running vulnerability scans that only produce a report nobody reviews, without a CI gate.
2. Do not: running containers as root by default when the application never needs elevated privileges, unnecessarily.

Example:
```bash
trivy image my-app:1.4.0 --severity HIGH,CRITICAL
```

Check: Do not: running vulnerability scans that only produce a.
