---
name: vpc-networking-fundamentals
description: "Use when \"vpc networking fundamentals\" is the work. assuming a private subnet has zero outbound internet access when a NAT gateway is attached."
---

# VPC Networking Fundamentals

assuming a "private" subnet has zero outbound.

1. Do not: assuming a "private" subnet has zero outbound internet access when a NAT gateway is.
2. Do not: leaving a security group rule open to 0.0.0.0/0 on a database port from an.

Example:
```bash
aws ec2 describe-route-tables --filters "Name=association.subnet-id,Values=subnet-0123abcd"
```

Check: Do not: assuming a "private" subnet has zero.
