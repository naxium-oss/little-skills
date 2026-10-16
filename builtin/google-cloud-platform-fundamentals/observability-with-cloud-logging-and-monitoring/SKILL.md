---
name: observability-with-cloud-logging-and-monitoring
description: "Use when \"observability with cloud logging and monitoring\" is the work. assuming default log retention is indefinite when its time-bounded per bucket configuration."
---

# Observability with Cloud Logging and Monitoring

assuming default log retention is indefinite.

1. Do not: assuming default log retention is indefinite when it's time-bounded per bucket configuration.
2. Do not: writing an alert policy and never validating it fires by testing an actual threshold.

Example:
```bash
gcloud logging read 'resource.type="cloud_run_revision" AND severity>=ERROR' --limit 20 --format=json
```

Check: Do not: assuming default log retention is indefinite when it's time-bounded per bucket configuration.
