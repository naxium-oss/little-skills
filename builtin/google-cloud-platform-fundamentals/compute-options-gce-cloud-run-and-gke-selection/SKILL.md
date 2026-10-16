---
name: compute-options-gce-cloud-run-and-gke-selection
description: "Use when \"compute options gce cloud run and gke selection\" is the work."
---

# Compute Options: GCE, Cloud Run, and

choosing GKE for a.

1. Do not: choosing GKE for a simple stateless API that Cloud Run would serve more cheaply.
2. Do not: assuming Cloud Run's min-instances=0 has no cold-start latency impact on the first request after.

Example:
```bash
gcloud run deploy my-api --image gcr.io/my-project/my-api:1.4.0 --region us-central1 \
```

Check: Do not: choosing GKE.
