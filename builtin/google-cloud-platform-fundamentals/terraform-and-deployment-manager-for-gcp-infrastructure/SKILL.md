---
name: terraform-and-deployment-manager-for-gcp-infrastructure
description: "Use when \"terraform and deployment manager for gcp infrastructure\" is the work. upgrading the Google Terraform provider without reading its changelog, triggering unexpected resource replacement (and downtime) on the next."
---

# Terraform and Deployment Manager for GCP

upgrading the Google Terraform.

1. Do not: upgrading the Google Terraform provider without reading its changelog, triggering unexpected resource replacement (and.
2. Do not: mixing manually-created GCP resources with Terraform-managed ones in the same project without importing them.

Example:
```hcl
resource "google_cloud_run_v2_service" "api" {
```

Check: Do not: upgrading the Google Terraform provider without reading.
