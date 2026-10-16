---
name: retrieval-augmented-generation-pipeline-design
description: "Use when \"retrieval augmented generation pipeline design\" is the work. evaluating only end-to-end answer quality without isolating whether retrieval or generation is the actual failure point, making it."
---

# Retrieval-Augmented Generation Pipeline Design

evaluating only end-to-end answer quality.

1. Do not: evaluating only end-to-end answer quality without isolating whether retrieval or generation is the actual.
2. Do not: chunking documents by a fixed token count without regard to semantic boundaries (mid-sentence splits).

Example:
```bash
confirm the tokenizer revision matches the model checkpoint
```

Check: Do not: evaluating only end-to-end answer quality without isolating.
