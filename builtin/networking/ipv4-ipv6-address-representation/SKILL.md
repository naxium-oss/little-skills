---
name: ipv4-ipv6-address-representation
description: "Use when \"ipv4 ipv6 address representation\" is the work. IPv6 has multiple valid textual forms."
---

# IPv4 & IPv6 Address Representation

IPv6 has multiple valid textual forms.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import ipaddress
a = ipaddress.ip_address("2001:0db8:0:0:0:0:0:1")
b = ipaddress.ip_address("2001:db8::1")
```

Check: Do not edit the assert to match a surprising result.
