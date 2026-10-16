---
name: container-logging-and-log-driver-configuration
description: "Use when \"container logging and log driver configuration\" is the work. leaving default unbounded json-file logging on a verbose long-running container, eventually filling host disk and causing unrelated container."
---

# Container Logging and Log Driver Configuration

leaving default unbounded json-file.

1. Do not: leaving default unbounded json-file logging on a verbose long-running container, eventually filling host disk.
2. Do not: configuring a remote log driver without verifying actual delivery, discovering the gap only during.

Example:
```bash
docker inspect --format='{{.HostConfig.LogConfig}}' my-container
```

Check: Do not: leaving default unbounded json-file logging on a.
