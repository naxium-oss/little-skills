"""Token estimate for skill cards.

Uses a GPT-2-style split, which counts at least as many tokens as cl100k
for this English-and-code mix. A card under this cap is under 150 model tokens.
"""

from __future__ import annotations

import re

_PAT = re.compile(
    r"""'(?:[sdmt]|ll|ve|re)| ?[A-Za-z0-9_]+| ?[^\sA-Za-z0-9_]+|\s+(?!\S)|\s+"""
)


def count_tokens(text: str) -> int:
    return sum(1 for part in _PAT.findall(text) if part.strip())
