"""Rewrite every SKILL.md into a card under 150 tokens.

Originals are copied once to ../skills-original-backup and reread from there,
so a second run does not compress a card again.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKUP = ROOT.parent / "skills-original-backup"
sys.path.insert(0, str(ROOT / "scripts"))

from agent_cards import hand_cards  # noqa: E402
from extract import extract_card, fit  # noqa: E402
from skill_tokens import count_tokens  # noqa: E402

EXTRA_QUOTES: dict[str, list[str]] = {
    "product-truth": ["who is it for", "product truth"],
    "visual-direction": ["visual direction", "art direction"],
    "type-and-space": ["the spacing", "the type"],
    "color-and-contrast": ["the colors", "hard to read"],
    "motion-and-states": ["feels dead", "add motion"],
    "design-audit": ["review this design", "design audit"],
    "design-handoff": ["design handoff", "design system"],
    "framing-research-questions": ["research question", "what would falsify"],
    "surveying-prior-work": ["prior work", "already known"],
    "designing-the-analysis": ["how should we analyse"],
    "preregistering-analysis": ["pre-registration", "lock the analysis"],
    "setting-up-reproducible-analysis": ["so it reruns"],
    "executing-analysis": ["run the analysis"],
    "investigating-anomalous-results": ["numbers look wrong"],
    "verifying-results-before-claiming": ["can we claim"],
    "requesting-red-team-review": ["red team"],
    "reporting-and-archiving-findings": ["write it up"],
    "establishing-feasibility-first": ["will this even run"],
    "svg-authoring": ["svg icon", "author an svg"],
    "svg-debugging": ["svg is blank", "svg debugging"],
    "svg-editing": ["edit the svg"],
    "svg-examples": ["svg example"],
    "svg-visual-verification": ["check the svg"],
    "voxel-terrain": ["voxel terrain"],
    "voxel-objects": ["voxel object"],
    "voxel-editing": ["edit voxels"],
    "voxel-debugging": ["voxel bug"],
    "voxel-texturing": ["voxel texture"],
    "voxel-visual-verification": ["check the voxels"],
    "threejs-game-director": ["three.js game", "game director"],
    "threejs-gameplay-systems": ["gameplay systems"],
    "threejs-game-ui-designer": ["game ui", "hud"],
    "threejs-3d-generator": ["3d asset", "generate a model"],
    "threejs-image-generator": ["generate an image"],
    "threejs-audio-generator": ["game audio"],
    "threejs-voxel-games": ["voxel game"],
    "threejs-debug-profiler": ["three.js profiler", "frame time"],
    "threejs-qa-release": ["release the game"],
    "threejs-aaa-graphics-builder": ["aaa graphics"],
    "game-qa-threejs": ["playtest the game"],
    "visual-testing-playwright": ["visual test", "playwright screenshot"],
    "scroll-sites": ["scroll site"],
    "watch": ["youtube captions"],
    "video-vision": ["sample the frames"],
}


def main() -> None:
    originals = load_originals()
    hands = hand_cards()
    written: set[str] = set()
    problems: list[str] = []
    for rel, text in originals.items():
        name = Path(rel).parent.name
        if name in hands:
            card = hands[name]
        elif name.startswith("debug-"):
            card = debug_card(text, name)
        else:
            card = extract_card(text, name)
            card = with_quotes(card, EXTRA_QUOTES.get(name, []))
        problems.extend(check(card, name))
        dest = ROOT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(card, encoding="utf-8", newline="\n")
        written.add(name)
        if len(written) % 200 == 0:
            print(len(written), flush=True)
    for name, card in hands.items():
        if name in written:
            continue
        problems.extend(check(card, name))
        dest = ROOT / "community" / name / "SKILL.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(card, encoding="utf-8", newline="\n")
    if problems:
        print("\n".join(problems[:40]))
        raise SystemExit(f"{len(problems)} cards failed the cap or the slots")
    print(f"wrote {len(list((ROOT / 'builtin').rglob('SKILL.md')))} builtin + {len(list((ROOT / 'community').rglob('SKILL.md')))} community")


def load_originals() -> dict[str, str]:
    if not BACKUP.exists():
        for base in ("builtin", "community"):
            src = ROOT / base
            if not src.exists():
                continue
            for path in src.rglob("SKILL.md"):
                rel = path.relative_to(ROOT)
                dest = BACKUP / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, dest)
        print(f"backed up originals to {BACKUP}")
    found = {}
    for path in BACKUP.rglob("SKILL.md"):
        rel = path.relative_to(BACKUP).as_posix()
        found[rel] = path.read_text(encoding="utf-8")
    return found


def debug_card(text: str, name: str) -> str:
    lang = name.removeprefix("debug-")
    heads = re.findall(r"^### (.+)$", text, re.M)
    hints = _debug_hints(text)
    run = re.search(r"\*\*Run:\*\*\s*`([^`]+)`", text)
    first = heads[0].split("/")[0].strip() if heads else f"{lang} failure"
    quotes = [f"{lang} {first}", first]
    if name == "debug-python":
        quotes = ["pytest fails", "ModuleNotFoundError", f"{lang} {first}"]
    quoted = ", ".join(f'"{item}"' for item in quotes[:3])
    description = f'Use when {quoted}. Not when explaining working {lang} code.'
    steps = hints[:3] or [f"If you see {head.split('/')[0].strip()}, check that before a wide edit." for head in heads[:3]]
    if len(steps) < 2:
        steps = [f"Run the {lang} test command.", "Change one suspected line and rerun it."]
    example = run.group(1).strip() if run else f"Run the {lang} tests."
    return fit(
        name,
        description,
        f"Debug {lang}",
        f"Reproduce the {lang} failure with the project command, then change one thing.",
        steps,
        [example],
        "text",
        "The same command that failed has to pass.",
    )


def _debug_hints(text: str) -> list[str]:
    hints = []
    parts = re.split(r"(?m)^### ", text)[1:]
    for part in parts:
        title, _, body = part.partition("\n")
        label = title.split("/")[0].strip()
        sentence = ""
        for line in body.splitlines():
            stripped = line.strip().lstrip("-").strip()
            if stripped and not stripped.startswith("#"):
                sentence = stripped
                break
        if sentence:
            hints.append(f"{label}: {sentence}")
        else:
            hints.append(label)
        if len(hints) == 3:
            break
    return hints


def with_quotes(card: str, extras: list[str]) -> str:
    if not extras:
        return card
    match = re.search(r'^description: "(.*)"\s*$', card, re.M)
    if not match:
        return card
    desc = match.group(1).replace('\\"', '"').replace("\\\\", "\\")
    prefix = ", ".join(f'"{item}"' for item in extras)
    if desc.startswith("Use when "):
        desc = "Use when " + prefix + ", " + desc[len("Use when ") :]
    else:
        desc = f'Use when {prefix}. {desc}'
    updated = _swap_desc(card, desc)
    while count_tokens(updated) > 150 and " is the work. " in desc:
        desc = desc.split(" is the work. ", 1)[0] + " is the work."
        updated = _swap_desc(card, desc)
    while count_tokens(updated) > 150 and extras:
        extras = extras[:-1]
        prefix = ", ".join(f'"{item}"' for item in extras)
        base = match.group(1).replace('\\"', '"').replace("\\\\", "\\")
        desc = "Use when " + prefix + ", " + base[len("Use when ") :] if prefix else base
        if " is the work. " in desc:
            desc = desc.split(" is the work. ", 1)[0] + " is the work."
        updated = _swap_desc(card, desc)
    return updated


def _swap_desc(card: str, desc: str) -> str:
    escaped = desc.replace("\\", "\\\\").replace('"', '\\"')
    return re.sub(r'^description: ".*"\s*$', f'description: "{escaped}"', card, count=1, flags=re.M)


def check(card: str, name: str) -> list[str]:
    errors = []
    if count_tokens(card) > 150:
        errors.append(f"over {name} {count_tokens(card)}")
    if f"name: {name}\n" not in card:
        errors.append(f"name {name}")
    if "Example:" not in card or "\nCheck: " not in card or "\n1. " not in card:
        errors.append(f"slots {name}")
    if not re.search(r'^description: "Use when ', card, re.M):
        errors.append(f"desc {name}")
    return errors


if __name__ == "__main__":
    main()
