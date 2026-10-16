"""Route a user prompt to skills by their descriptions.

Ranking, best first:
  1. Quoted phrase hit: a quoted phrase from the "Use when" part of the
     description appears in the prompt. Longer phrases score higher.
  2. Keyword hit: prompt words overlap the skill name (weight 2) or the
     "Use when" words (weight 1). A name hit alone is enough; otherwise two
     description words are required, so one generic word such as "version"
     does not route.

A skill is dropped when any "Not when" phrase appears in the prompt.
Words are compared with a simple plural fold ("forms" == "form").
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

STOP = {
    "a", "an", "the", "of", "to", "and", "or", "for", "when", "use", "not",
    "with", "is", "work", "on", "in", "by", "it", "its", "be", "as", "at",
    "this", "that", "from", "your", "you", "do", "does", "if", "then", "than",
    "into", "about", "their", "they", "only", "also", "same", "other", "can",
    "may", "must", "should", "will", "just", "out", "up", "all", "any", "some",
    "no", "but", "so", "too", "very", "how", "what", "which", "who", "why",
    "where", "there", "here", "help", "please", "we", "have", "has", "had",
    "are", "was", "were", "been", "being", "before", "after", "during", "per",
    "via", "without", "within", "across", "each", "both", "few", "more", "most",
    "own", "such", "task", "comes", "using", "while", "between", "against",
}

QUOTED_BASE = 100


@dataclass
class Skill:
    name: str
    description: str
    path: str = ""
    quotes: list[str] = field(default_factory=list)
    not_when: list[str] = field(default_factory=list)
    probe: str = ""


@dataclass
class Hit:
    name: str
    path: str
    score: int
    reason: str


def load_skills(root: Path) -> list[Skill]:
    skills: list[Skill] = []
    for base in (root / "builtin", root / "community"):
        if not base.exists():
            continue
        for path in base.rglob("SKILL.md"):
            text = path.read_text(encoding="utf-8")
            name_match = re.search(r"^name:\s*(\S+)\s*$", text, re.M)
            desc_match = re.search(r'^description:\s*"(.*)"\s*$', text, re.M)
            if not name_match or not desc_match:
                skills.append(Skill(name=path.parent.name, description="", path=str(path)))
                continue
            desc = desc_match.group(1).replace('\\"', '"').replace("\\\\", "\\")
            skill = Skill(name=name_match.group(1), description=desc, path=str(path))
            skill.quotes = _quotes(desc)
            skill.not_when = _not_when(desc)
            skills.append(skill)
    _assign_probes(skills)
    return skills


def match(prompt: str, skills: list[Skill]) -> set[str]:
    low = prompt.lower()
    spans: list[tuple[str, int, int]] = []
    for skill in skills:
        if not skill.quotes:
            continue
        if any(_contains(phrase, prompt) for phrase in skill.not_when):
            continue
        best: tuple[int, int] | None = None
        for phrase in skill.quotes:
            found = _span(phrase, low)
            if found and (best is None or found[1] - found[0] > best[1] - best[0]):
                best = found
        if best:
            spans.append((skill.name, best[0], best[1]))
    kept = []
    for name, start, end in spans:
        covered = any(
            other != name and ostart <= start and oend >= end and (oend - ostart) > (end - start)
            for other, ostart, oend in spans
        )
        if not covered:
            kept.append(name)
    return set(kept)


def rank(prompt: str, skills: list[Skill], k: int = 5) -> list[Hit]:
    quoted = match(prompt, skills)
    low = prompt.lower()
    prompt_words = set(_words(prompt, drop_stop=True))
    hits: list[Hit] = []
    for skill in skills:
        if any(_contains(phrase, prompt) for phrase in skill.not_when):
            continue
        if skill.name in quoted:
            longest = max(len(q) for q in skill.quotes if _span(q, low))
            hits.append(Hit(skill.name, skill.path, QUOTED_BASE + longest, "quoted"))
            continue
        name_hits, desc_hits = _keyword_hits(skill, prompt_words)
        if name_hits == 0 and desc_hits < 2:
            continue
        hits.append(Hit(skill.name, skill.path, 2 * name_hits + desc_hits, "keyword"))
    hits.sort(key=lambda hit: (-hit.score, hit.name))
    return hits[:k]


def _keyword_hits(skill: Skill, prompt_words: set[str]) -> tuple[int, int]:
    name_words = set(_words(skill.name.replace("-", " "), drop_stop=True))
    use_words = set(_words(_use_side(skill.description), drop_stop=True)) - name_words
    return len(prompt_words & name_words), len(prompt_words & use_words)


def _span(phrase: str, prompt_lower: str) -> tuple[int, int] | None:
    phrase = phrase.lower().strip()
    if not phrase:
        return None
    if " " in phrase or "." in phrase or "-" in phrase:
        idx = prompt_lower.find(phrase)
        if idx < 0:
            return None
        return idx, idx + len(phrase)
    found = re.search(rf"\b{re.escape(phrase)}\b", prompt_lower)
    if not found:
        return None
    return found.start(), found.end()


def _assign_probes(skills: list[Skill]) -> None:
    counts: dict[str, int] = {}
    for skill in skills:
        for quote in skill.quotes:
            key = quote.lower()
            counts[key] = counts.get(key, 0) + 1
    for skill in skills:
        unique = [quote for quote in skill.quotes if counts[quote.lower()] == 1]
        unique.sort(key=len, reverse=True)
        if unique:
            skill.probe = unique[0]
            continue
        words = [word for word in re.findall(r"[a-z0-9]+", _use_side(skill.description).lower()) if word not in STOP]
        for left, right in zip(words, words[1:]):
            phrase = f"{left} {right}"
            owners = sum(phrase in other.description.lower() for other in skills)
            if owners == 1:
                skill.probe = phrase
                skill.quotes.append(phrase)
                break


def _use_side(description: str) -> str:
    return re.split(r"\bNot when\b", description, maxsplit=1)[0]


def _quotes(description: str) -> list[str]:
    return [item.strip() for item in re.findall(r'"([^"]+)"', _use_side(description)) if item.strip()]


def _not_when(description: str) -> list[str]:
    found = re.search(r"\bNot when\b\s*(.+)$", description)
    if not found:
        return []
    raw = found.group(1).strip().rstrip(".")
    parts = re.split(r",|\bor\b", raw)
    return [part.strip().strip('"') for part in parts if len(part.strip()) > 2]


def _words(text: str, drop_stop: bool) -> list[str]:
    out: list[str] = []
    for word in re.findall(r"[a-z0-9]+", text.lower()):
        if drop_stop and word in STOP:
            continue
        if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
            word = word[:-1]
        out.append(word)
    return out


def _contains(phrase: str, prompt: str) -> bool:
    needle = _words(phrase, drop_stop=False)
    if not needle:
        return False
    hay = _words(prompt, drop_stop=False)
    width = len(needle)
    return any(hay[i : i + width] == needle for i in range(len(hay) - width + 1))


def main() -> None:
    parser = argparse.ArgumentParser(description="Print skills that match a prompt, best first, as JSON.")
    parser.add_argument("prompt", help="User prompt text")
    parser.add_argument("--root", required=True, help="Skills repo root with builtin/ and community/")
    parser.add_argument("-k", type=int, default=5, help="Maximum number of hits (default 5)")
    args = parser.parse_args()
    skills = load_skills(Path(args.root))
    hits = rank(args.prompt, skills, k=args.k)
    out = [{"name": hit.name, "path": hit.path, "score": hit.score, "reason": hit.reason} for hit in hits]
    print(json.dumps(out))


if __name__ == "__main__":
    main()
