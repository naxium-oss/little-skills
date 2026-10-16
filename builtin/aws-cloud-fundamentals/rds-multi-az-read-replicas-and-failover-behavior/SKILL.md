---
name: rds-multi-az-read-replicas-and-failover-behavior
description: "Use when \"rds multi az read replicas and failover behavior\" is the work."
---

# RDS Multi-AZ, Read Replicas, and Failover

assuming a read replica provides.

1. Do not: assuming a read replica provides automatic failover/high-availability like Multi-AZ does, when it requires manual.
2. Do not: not testing application reconnection.

Example:
```bash
aws rds describe-db-instances --db-instance-identifier mydb --query "DBInstances[0].{MultiAZ:MultiAZ,ReadReplicaDBInstanceIdentifiers:ReadReplicaDBInstanceIdentifiers}"
```

Check: Do not: assuming a.
