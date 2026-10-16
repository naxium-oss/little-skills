---
name: cidr-subnets-prefix-membership
description: "Use when \"cidr subnets prefix membership\" is the work. CIDR membership is a bit-prefix operation."
---

# CIDR Subnets & Prefix Membership

CIDR membership is a bit-prefix operation.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import ipaddress
network = ipaddress.ip_network("192.0.2.0/24")
assert ipaddress.ip_address("192.0.2.42") in network
```

Check: Do not edit the assert to match a surprising result.
