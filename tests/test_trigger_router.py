"""Ranked routing: quoted phrases, keyword overlap, and Not-when suppression."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from trigger_router import load_skills, match, rank  # noqa: E402

SKILLS = {
    "svg-icons": (
        'Use when the user asks for "svg icon", "svg logo", or vector graphics. '
        "Not when raster images, png or jpeg export."
    ),
    "tdd": (
        'Use when the user says "test first", "failing test", or "tdd". '
        "Not when explain or how many."
    ),
    "pdf-forms": (
        'Use when filling a PDF form or extracting fields from a PDF document. '
        "Not when plain text files."
    ),
    "release-notes": (
        "Use when writing release notes or a changelog from git history for a version."
    ),
    "generic-helper": (
        "Use when the user needs general help with a plain task."
    ),
}


def write_tree(root: Path) -> None:
    for name, desc in SKILLS.items():
        folder = root / "community" / name
        folder.mkdir(parents=True)
        (folder / "SKILL.md").write_text(
            f'---\nname: {name}\ndescription: "{desc.replace(chr(34), chr(92) + chr(34))}"\n---\n\n# {name}\n',
            encoding="utf-8",
        )


class RankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls._tmp.name)
        write_tree(cls.root)
        cls.skills = load_skills(cls.root)

    @classmethod
    def tearDownClass(cls) -> None:
        cls._tmp.cleanup()

    def names(self, prompt: str, k: int = 2) -> list[str]:
        return [hit.name for hit in rank(prompt, self.skills, k=k)]

    def test_quoted_phrase_routes_to_skill(self) -> None:
        self.assertEqual(self.names("can you write a failing test for slugify")[:1], ["tdd"])

    def test_quoted_hit_outranks_keyword_hit(self) -> None:
        hits = rank("write a failing test about the pdf form", self.skills, k=2)
        self.assertEqual(hits[0].name, "tdd")
        self.assertEqual(hits[0].reason, "quoted")
        self.assertEqual(hits[1].name, "pdf-forms")

    def test_longer_quoted_phrase_wins(self) -> None:
        hits = rank("make an svg icon and write a failing test", self.skills, k=2)
        self.assertEqual({hit.name for hit in hits}, {"svg-icons", "tdd"})
        self.assertTrue(all(hit.reason == "quoted" for hit in hits))

    def test_keyword_overlap_routes_without_quotes(self) -> None:
        self.assertEqual(self.names("extract the fields from this pdf form")[0], "pdf-forms")

    def test_name_tokens_count_as_keywords(self) -> None:
        self.assertEqual(self.names("write release notes for version 2")[0], "release-notes")

    def test_not_when_suppresses_quoted_hit(self) -> None:
        self.assertNotIn("svg-icons", self.names("export this png image to svg icon"))
        self.assertEqual(match("export this png image to svg icon", self.skills), set())

    def test_not_when_suppresses_keyword_hit(self) -> None:
        self.assertNotIn("pdf-forms", self.names("the pdf document is a plain text file"))

    def test_generic_prompt_routes_nothing(self) -> None:
        self.assertEqual(self.names("hello, how are you today"), [])

    def test_lone_word_must_be_in_skill_name(self) -> None:
        self.assertEqual(self.names("pdf")[:1], ["pdf-forms"])
        self.assertNotIn("css-grid-layout-model", self.names("fill in this pdf form"))

    def test_single_common_token_is_not_enough(self) -> None:
        # "release" appears in release-notes only, but "version" alone is too generic here.
        self.assertEqual(self.names("bump the version number"), [])

    def test_k_limits_results(self) -> None:
        self.assertLessEqual(len(rank("svg icon and failing test and pdf form", self.skills, k=1)), 1)

    def test_ranking_is_deterministic(self) -> None:
        prompt = "svg icon, failing test, pdf form"
        self.assertEqual(self.names(prompt, k=3), self.names(prompt, k=3))

    def test_match_behaviour_unchanged(self) -> None:
        self.assertEqual(match("write a failing test", self.skills), {"tdd"})


if __name__ == "__main__":
    unittest.main()
