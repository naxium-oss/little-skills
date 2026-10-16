---
name: secrets-management-in-infrastructure-code
description: "Use when \"secrets management in infrastructure code\" is the work. hardcoding a database password directly in a .tf file or committed .tfvars, exposing it in version control history."
---

# Secrets Management in Infrastructure Code

hardcoding a database password directly.

1. Do not: hardcoding a database password directly in a .tf file or committed .tfvars, exposing it.
2. Do not: leaving Terraform state readable by overly broad IAM permissions, exposing secrets embedded in resource.

Example:
```hcl
data "aws_secretsmanager_secret_version" "db_password" {
```

Check: Do not: hardcoding a database password directly in a .tf file or committed .tfvars, exposing it in version.
