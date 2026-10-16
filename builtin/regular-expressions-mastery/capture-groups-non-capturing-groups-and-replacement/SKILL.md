---
name: capture-groups-non-capturing-groups-and-replacement
description: "Use when \"capture groups non capturing groups and replacement\" is the work. adding a new capturing group to an existing pattern and breaking every downstream \\1/group(2) reference due to renumbering."
---

# Capture Groups, Non-Capturing Groups, and Replacement

adding a new capturing.

1. Do not: adding a new capturing group to an existing pattern and breaking every downstream \1/group(2).
2. Do not: forgetting (?:...) for a purely structural group, cluttering match results with unwanted captured substrings.

Example:
```bash
test the pattern against a positive and a negative fixture before using it
```

Check: Do not: adding a.
