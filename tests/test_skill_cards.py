"""Skill card contract and trigger routing.

Tree checks fail until scripts/compress_skills.py rewrites builtin/ and community/.
"""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from skill_tokens import count_tokens  # noqa: E402
from extract import extract_card  # noqa: E402
from trigger_router import load_skills, match  # noqa: E402

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
BOILER = (
    "NOT RETRIEVED",
    "illustrative-unverified",
    "Evidence report template",
    "${scope-and-triggers",
    "${design-slm",
    "${science-",
    "This is an instruction document, not an assertion",
)


def skill_files() -> list[Path]:
    found = []
    for base in (ROOT / "builtin", ROOT / "community"):
        if not base.exists():
            continue
        for path in base.rglob("SKILL.md"):
            found.append(path)
    return found


class ExtractorTests(unittest.TestCase):
    def test_core_model_keeps_the_real_assert(self) -> None:
        text = """---
name: javascript-equality-coercion
description: Make comparisons explicit.
---
# JavaScript Equality

## Core model

Prefer strict equality. Object.is distinguishes signed zero and NaN.

## Example 1: Core behavior

```javascript
console.assert(0 !== "0");
console.assert(Object.is(NaN, NaN));
```

## Example 2: Boundary or counterexample

```javascript
console.assert(!Object.is(0, -0));
```
"""
        card = extract_card(text, "javascript-equality-coercion")
        self.assertLessEqual(count_tokens(card), 150)
        self.assertIn('0 !== "0"', card)
        self.assertIn("Use when", card)
        self.assertNotIn("NOT RETRIEVED", card)

    def test_skillstack_ignores_mismatched_scenario(self) -> None:
        text = """---
name: jump-buffering-and-coyote-time
description: Use when performing jump buffering and coyote time.
---
# Jump Buffering and Coyote Time

**Technical focus:** Measure buffer and grace windows in simulation time and test exact threshold boundaries.

### Step 3: Apply the domain workflow

1. Define simulation units and input buffering windows. Record the artifact or observation produced by this step.
2. Replay fixtures at the boundary tick. Record the artifact or observation produced by this step.

### Step 6: Challenge the conclusion

Test the boundary tick and one tick past it.

## 5. Worked example

A fast-moving player passes through a thin wall.
```text
# No command or output in this example has been executed.
```
"""
        card = extract_card(text, "jump-buffering-and-coyote-time")
        self.assertLessEqual(count_tokens(card), 150)
        self.assertIn("grace windows", card)
        self.assertNotIn("thin wall", card)
        self.assertNotIn("has been executed", card)

    def test_foundations_keeps_pitfall(self) -> None:
        text = """---
name: iterators-generators-and-laziness
description: Generators run once.
---
# Iterators, Generators, and Laziness

## 5. Examples

### A. From the library

```python
second_pass = [l for l in lines if l]   # always []
```

## 6. Failure modes

The library's own pitfalls for this skill:

- passing a generator to a function that iterates it more than once.
- assuming generator expressions support indexing or len().
"""
        card = extract_card(text, "iterators-generators-and-laziness")
        self.assertLessEqual(count_tokens(card), 150)
        self.assertIn("iterates it more than once", card)
        self.assertIn("always []", card)


class TreeContractTests(unittest.TestCase):
    def test_every_skill_is_a_short_card(self) -> None:
        files = skill_files()
        self.assertGreater(len(files), 1000)
        errors = []
        names = []
        for path in files:
            text = path.read_text(encoding="utf-8")
            tokens = count_tokens(text)
            if tokens > 150:
                errors.append(f"{tokens}t {path.relative_to(ROOT)}")
            if not text.startswith("---\n"):
                errors.append(f"frontmatter {path.relative_to(ROOT)}")
            match = re.search(r"^name:\s*(.+)$", text, re.M)
            desc = re.search(r'^description:\s*"(.*)"\s*$', text, re.M)
            if not match or not desc:
                errors.append(f"yaml {path.relative_to(ROOT)}")
                continue
            name = match.group(1).strip().strip('"')
            if not NAME_RE.match(name):
                errors.append(f"name {name}")
            if path.parent.name != name:
                errors.append(f"dir {path.parent.name} != {name}")
            if not desc.group(1).startswith("Use when"):
                errors.append(f"desc {name}")
            if "Example:" not in text or "\n1. " not in text or "\nCheck: " not in text:
                errors.append(f"slots {name}")
            for bad in BOILER:
                if bad in text:
                    errors.append(f"boiler {name} {bad}")
            names.append(name)
        dupes = {n for n in names if names.count(n) > 1}
        if dupes:
            errors.append(f"dupes {sorted(dupes)[:8]}")
        self.assertFalse(errors, "\n".join(errors[:30]))

    def test_image_and_neighbor_prompts(self) -> None:
        skills = load_skills(ROOT)
        cases = [
            ("how many SKILL.md files do we have?", {"count-with-tools"}, {"explain-codebase", "clean-dry-code", "clone-from-reference"}),
            ("count the API routes", {"count-with-tools"}, {"explain-codebase"}),
            ("what is the total number of seed users?", {"count-with-tools"}, set()),
            ("do we have any retry logic?", {"count-with-tools"}, {"clean-dry-code"}),
            ("implement a countdown timer", set(), {"count-with-tools"}),
            ("write a function that returns the total", set(), {"count-with-tools"}),
            ("how many functions should this module export?", set(), {"count-with-tools"}),
            ("explain how the login feature works", {"explain-codebase"}, {"count-with-tools", "systematic-debugging"}),
            ("describe the billing module", {"explain-codebase"}, {"clone-from-reference"}),
            ("tell me how the parser works", {"explain-codebase"}, {"clean-dry-code"}),
            ("show me the upload flow", {"explain-codebase"}, {"count-with-tools"}),
            ("how does auth work?", {"explain-codebase"}, {"systematic-debugging"}),
            ("explain your plan", set(), {"explain-codebase"}),
            ("how does this bug happen?", {"systematic-debugging"}, {"explain-codebase"}),
            ("clone Wordle, recreate it based off their game", {"clone-from-reference"}, {"count-with-tools", "explain-codebase"}),
            ("inspired by their dashboard, see their layout", {"clone-from-reference"}, {"suggest-features"}),
            ("git clone the repo", set(), {"clone-from-reference"}),
            ("clone this helper function", set(), {"clone-from-reference"}),
            ("suggest a feature for search", {"suggest-features"}, {"suggest-improvements", "clean-dry-code"}),
            ("brainstorm feature ideas", {"suggest-features"}, {"clean-dry-code"}),
            ("think of a feature for comments", {"suggest-features"}, {"suggest-improvements"}),
            ("think of improvements to the existing parser", {"suggest-improvements"}, {"suggest-features", "clean-dry-code"}),
            ("what improvements would you make to checkout", {"suggest-improvements"}, {"suggest-features"}),
            ("DRY this parser and clean up dead code", {"clean-dry-code"}, {"suggest-features", "writing-plans"}),
            ("refactor parse and split it into smaller functions", {"clean-dry-code"}, {"writing-plans"}),
            ("split my component and break it into hooks", {"clean-dry-code"}, {"writing-plans"}),
            ("split the pull request", set(), {"clean-dry-code"}),
            ("break down the plan into steps", {"writing-plans"}, {"clean-dry-code"}),
            ("add slugify. tests after, ship the function now", {"tdd"}, set()),
            ("pytest fails with ModuleNotFoundError", {"debug-python", "systematic-debugging"}, {"explain-codebase"}),
            ("review the diff before merge", {"code-review"}, {"design-audit"}),
            ("security audit for secrets", {"security-audit"}, {"clone-from-reference"}),
            ("write an exploit payload for the login form", set(), {"security-audit"}),
        ]
        errors = []
        for prompt, required, forbidden in cases:
            got = match(prompt, skills)
            missing = required - got
            extra = forbidden & got
            if missing or extra:
                errors.append(f"{prompt!r} got={sorted(got)} missing={sorted(missing)} forbidden={sorted(extra)}")
        self.assertFalse(errors, "\n".join(errors))

    def test_each_skill_has_a_distinctive_hit_and_misses_generics(self) -> None:
        skills = load_skills(ROOT)
        errors = []
        for skill in skills:
            probe = skill.probe
            if not probe:
                errors.append(f"no probe {skill.name}")
                continue
            prompt = f"help with {probe}"
            got = match(prompt, skills)
            if skill.name not in got:
                errors.append(f"miss {skill.name} on {prompt!r} -> {sorted(got)[:6]}")
            strangers = [name for name in got if name != skill.name]
            if strangers:
                errors.append(f"fp {skill.name} also {strangers[:4]} on {prompt!r}")
        for generic in ("javascript", "python", "error", "function", "test", "file", "user", "data", "code", "update"):
            got = match(generic, skills)
            if got:
                errors.append(f"generic {generic!r} -> {sorted(got)[:6]}")
        self.assertFalse(errors, "\n".join(errors[:25]))

    def test_tdd_counters_the_baseline_excuse(self) -> None:
        text = (ROOT / "community" / "tdd" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("tests after", text)
        self.assertIn("skip", text.lower())


if __name__ == "__main__":
    unittest.main()
