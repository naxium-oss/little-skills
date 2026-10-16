---
name: evaluation-metrics-for-nlp-tasks
description: "Use when \"evaluation metrics for nlp tasks\" is the work. relying solely on BLEU/ROUGE for open-ended generation quality, missing valid paraphrases or coherence issues these metrics dont capture."
---

# Evaluation Metrics for NLP Tasks

relying solely on BLEU/ROUGE.

1. Do not: relying solely on BLEU/ROUGE for open-ended generation quality, missing valid paraphrases or coherence issues.
2. Do not: comparing perplexity scores across models using different tokenizers, which are not directly comparable.

Example:
```bash
confirm the tokenizer revision matches the model checkpoint
```

Check: Do not: relying solely on BLEU/ROUGE for open-ended generation.
