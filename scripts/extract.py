"""Turn a long SKILL.md into one teaching card under 150 tokens."""

from __future__ import annotations

import re

from skill_tokens import count_tokens

_FENCE = re.compile(r"```([a-zA-Z0-9_+-]*)\n(.*?)```", re.S)
_H1 = re.compile(r"^#\s+(.+)$", re.M)
_NUM = re.compile(r"^\d+\.\s+(.+)$", re.M)
_BULLET = re.compile(r"^[-*]\s+(.+)$", re.M)


def extract_card(text: str, name: str) -> str:
    title = _title(text, name)
    rule, steps, example, lang, check = _parts(text, title)
    description = _description(title, rule)
    return fit(name, description, _short_heading(title), rule, steps, example, lang, check)


def _parts(text: str, title: str) -> tuple[str, list[str], list[str], str, str]:
    if "## Core model" in text:
        rule = _section(text, "Core model")
        code, lang = _code_after(text, "Example 1")
        if not code:
            code, lang = _code_after(text, "Example")
        boundary, _ = _code_after(text, "Example 2")
        example = _clean_lines(code)[:3]
        if boundary:
            last = _clean_lines(boundary)[:1]
            if last and last[0] not in example:
                example = (example + last)[:3]
        steps = [
            "Write what the fixture should show before you run it.",
            "Run it on the installed runtime and compare the output.",
            "Keep the boundary case in its own run.",
        ]
        check = "Do not edit the assert to match a surprising result."
        return _one_sentence(rule, 22), steps, example or [rule], lang or "text", check

    if "**Technical focus:**" in text:
        rule = _after(text, "**Technical focus:**")
        steps = _workflow_steps(text)
        check = _challenge(text) or "Test the boundary and one step past it."
        example = [_one_sentence(steps[0], 16)]
        return _one_sentence(rule, 22), steps, example, "text", _one_sentence(check, 18)

    if "own pitfalls" in text:
        return _foundation_parts(text)
    return _procedural_parts(text)


def fit(
    name: str,
    description: str,
    heading: str,
    rule: str,
    steps: list[str],
    example: list[str],
    lang: str,
    check: str,
) -> str:
    steps = [_clip(step, 16) for step in steps][:3]
    example = [_clip(line, 18) for line in example if line.strip()][:3] or ["See the invariant above."]
    rule = _clip(rule, 22)
    check = _clip(check, 18)

    def render() -> str:
        body_steps = "\n".join(f"{i}. {step}" for i, step in enumerate(steps, 1))
        fence_lang = lang if re.fullmatch(r"[a-z0-9_+-]+", lang or "") else "text"
        example_block = "\n".join(example)
        desc = description.replace("\\", "\\\\").replace('"', '\\"')
        return (
            f"---\n"
            f"name: {name}\n"
            f'description: "{desc}"\n'
            f"---\n\n"
            f"# {heading}\n\n"
            f"{rule}\n\n"
            f"{body_steps}\n\n"
            f"Example:\n"
            f"```{fence_lang}\n"
            f"{example_block}\n"
            f"```\n\n"
            f"Check: {check}\n"
        )

    text = render()
    seen = 0
    while count_tokens(text) > 150 and seen < 12:
        seen += 1
        before = text
        if len(example) > 1:
            example.pop()
        elif len(steps) > 2:
            steps.pop()
        elif len(rule.split()) > 8:
            rule = _clip(rule, max(4, len(rule.split()) // 2))
        elif len(check.split()) > 6:
            check = _clip(check, max(3, len(check.split()) // 2))
        elif " is the work. " in description:
            description = description.split(" is the work. ", 1)[0] + " is the work."
        elif len(steps) > 2 or (steps and len(steps[-1].split()) > 8):
            steps[-1] = _clip(steps[-1], 6)
        else:
            heading = " ".join(heading.split()[:3]) or heading
            example = ["Run the boundary once."]
            steps = [_clip(step, 6) for step in steps[:2]] or ["State the invariant.", "Run it."]
            rule = _clip(rule, 6)
            check = _clip(check, 6)
            description = f'Use when "{_quote_title(name)}" is the work.'
        text = render()
        if text == before:
            break
    return text


def _description(title: str, rule: str) -> str:
    quoted = _quote_title(title)
    focus = _one_sentence(rule, 18).replace('"', "").replace("'", "")
    if focus.lower().startswith(quoted.lower()):
        return f'Use when "{quoted}" is the work.'
    return f'Use when "{quoted}" is the work. {focus}'


def _quote_title(title: str) -> str:
    words = re.sub(r"[^A-Za-z0-9 ]+", " ", title).split()
    return " ".join(words).lower()


def _title(text: str, name: str) -> str:
    match = _H1.search(text)
    if match:
        return match.group(1).strip()
    return name.replace("-", " ")


def _short_heading(title: str) -> str:
    words = title.split()
    if len(words) <= 6:
        return title
    return " ".join(words[:6])


def _section(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*\n(.*?)(?:\n##\s|\Z)", text, re.S | re.M)
    if not match:
        return ""
    return match.group(1).strip()


def _after(text: str, marker: str) -> str:
    idx = text.find(marker)
    if idx < 0:
        return ""
    line = text[idx + len(marker) :].strip().splitlines()[0]
    return _plain(line)


def _workflow_steps(text: str) -> list[str]:
    chunk = text
    for marker in ("Apply the domain workflow", "Step 3"):
        idx = text.find(marker)
        if idx >= 0:
            chunk = text[idx:]
            break
    steps = []
    for raw in _NUM.findall(chunk):
        sentence = raw.split("Record the artifact")[0].strip()
        sentence = _plain(sentence).rstrip(".")
        if len(sentence) < 8:
            continue
        steps.append(sentence + ".")
        if len(steps) == 3:
            break
    if len(steps) < 2:
        steps = [
            "Write the invariant and the smallest failing input.",
            "Run that fixture and keep the raw output.",
        ]
    return steps


def _challenge(text: str) -> str:
    match = re.search(r"Challenge the conclusion\s*\n+(.+)", text)
    if not match:
        return ""
    line = match.group(1).strip()
    if line.startswith("#"):
        return ""
    return _one_sentence(_plain(line), 18)


def _foundation_parts(text: str) -> tuple[str, list[str], list[str], str, str]:
    code, lang = _library_example(text)
    pitfalls = _pitfalls(text)
    rule = pitfalls[0] if pitfalls else _first_prose(text)
    steps = [f"Do not: {item.rstrip('.')}." for item in pitfalls[:2]]
    if len(steps) < 2:
        steps = [
            "Reproduce the snippet on the installed runtime before trusting it.",
            "Change one input and rerun the same command.",
        ]
    check = f"Do not: {pitfalls[0].rstrip('.')}." if pitfalls else "Say unverified if it was not run."
    example = _clean_lines(code)[:3] or [_one_sentence(rule, 16)]
    return _one_sentence(rule, 22), steps[:3], example, lang or "text", _one_sentence(check, 18)


def _procedural_parts(text: str) -> tuple[str, list[str], list[str], str, str]:
    do_this = _section(text, "Do this")
    numbered = _numbered(do_this) if do_this else _numbered(text)
    if do_this and len(numbered) >= 2:
        steps = numbered
    elif numbered and len(numbered[0].split()) > 8:
        steps = numbered
    else:
        steps = _h2_steps(text) or numbered
    if len(steps) < 2:
        steps = [
            "Read the file the user named before changing it.",
            "Run the check the task names.",
        ]
    rule = _first_prose(text) or "Do the named task and keep the evidence."
    check = _stop_bullet(text) or "Say not run when the check did not run."
    code, lang = _library_example(text)
    example = _clean_lines(code)[:3] or [_clip(steps[0], 14)]
    return _one_sentence(rule, 22), steps[:3], example, lang or "text", _one_sentence(check, 18)


def _numbered(text: str) -> list[str]:
    steps = []
    for raw in _NUM.findall(text or ""):
        sentence = _one_sentence(raw, 18)
        if len(sentence) < 8 or sentence.lower().startswith("credit"):
            continue
        steps.append(sentence)
        if len(steps) == 3:
            break
    return steps


_SKIP_H2 = re.compile(
    r"purpose|when to use|overview|keep$|guardrails|working tools|evidence|boundaries|stop conditions|do this|final response|philosophy",
    re.I,
)


def _h2_steps(text: str) -> list[str]:
    steps = []
    for part in re.split(r"(?m)^##\s+", text)[1:]:
        title, _, body = part.partition("\n")
        title = title.strip()
        if not title or _SKIP_H2.search(title):
            continue
        sentence = _one_sentence(body, 14) if body.strip() else ""
        if sentence and not sentence.startswith("#") and sentence.lower() not in title.lower():
            step = f"{title}. {sentence}"
        else:
            step = title.rstrip(".") + "."
        steps.append(_one_sentence(step, 18))
        if len(steps) == 3:
            break
    return steps


def _first_prose(text: str) -> str:
    body = text.split("---", 2)[-1]
    lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if (
            not stripped
            or stripped.startswith("#")
            or stripped.startswith("---")
            or stripped.startswith("|")
            or stripped.startswith("```")
            or stripped.startswith("Credit")
        ):
            if lines:
                break
            continue
        lines.append(stripped)
        if stripped.endswith("."):
            break
    return _plain(" ".join(lines))


def _stop_bullet(text: str) -> str:
    for heading in ("Stop conditions", "Guardrails", "Common failures", "Common Failure Modes"):
        match = re.search(rf"^##\s+{re.escape(heading)}\s*\n(.*?)(?:\n##\s|\Z)", text, re.S | re.M)
        if not match:
            continue
        bullets = _BULLET.findall(match.group(1))
        if bullets:
            return _plain(bullets[0])
    return ""


def _library_example(text: str) -> tuple[str, str]:
    for lang, body in _FENCE.findall(text):
        if "has been executed" in body or body.strip().startswith("# 1."):
            continue
        if lang.lower() in {"bash", "sh", "text", "json"} and "version" in body and "print" not in body:
            continue
        if body.strip():
            return body, lang or "text"
    return "", "text"


def _code_after(text: str, heading: str) -> tuple[str, str]:
    idx = text.find(heading)
    chunk = text[idx:] if idx >= 0 else text
    match = _FENCE.search(chunk)
    if not match:
        return "", "text"
    return match.group(2), match.group(1) or "text"


def _pitfalls(text: str) -> list[str]:
    idx = text.find("own pitfalls")
    chunk = text[idx:] if idx >= 0 else text
    end = chunk.find("\n## ")
    if end >= 0:
        chunk = chunk[:end]
    items = []
    for item in _BULLET.findall(chunk):
        plain = _plain(item)
        if "Writing syntax from memory" in plain or "Treating a tutorial" in plain:
            continue
        if len(plain) < 8:
            continue
        items.append(plain)
        if len(items) == 3:
            break
    return items


def _body(text: str) -> str:
    parts = text.split("---", 2)
    body = parts[-1] if len(parts) == 3 else text
    return _plain(body)


def _plain(text: str) -> str:
    text = re.sub(r"`{1,3}([^`]*)`{1,3}", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("*", "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _one_sentence(text: str, max_words: int) -> str:
    text = _plain(text)
    if not text:
        return "State the invariant, then run it."
    sentence = re.split(r"(?<=[.!?])\s+", text)[0]
    return _clip(sentence, max_words)


def _clip(text: str, max_words: int) -> str:
    words = text.split()
    if len(words) <= max_words:
        return text.strip()
    clipped = " ".join(words[:max_words]).rstrip(",;:")
    if clipped[-1] not in ".!?":
        clipped += "."
    return clipped


def _clean_lines(code: str) -> list[str]:
    lines = []
    for raw in code.splitlines():
        line = raw.strip()
        if not line or line.startswith("# ") and "always" not in line:
            if line.startswith("#") and "always" in line:
                lines.append(line)
            continue
        if line.startswith("#") and "always" not in line and not line.startswith("#!"):
            continue
        lines.append(line)
    return lines
