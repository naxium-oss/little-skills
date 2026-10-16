# Provenance for the NAXIUM Science skills

Fourteen skills, all Titan text. They are not copies of the upstream libraries,
and they are not a bundled agent runtime. What each one adapts is listed below,
so a reader can check the claim instead of trusting it. `LICENSE` in this
directory carries the three MIT notices in full.

Every skill carries `adapted-from` in its frontmatter. The two that say
`Titan original` adapt nothing and are listed at the end of this file.

| Upstream | License | What was adapted |
|---|---|---|
| [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) (K-Dense Inc.) | MIT, 2025 | The **domain coverage** under `scientific-*`, `omics-*`, `cheminformatics-*`, `molecular-*`, `publication-*` and `literature-*`: which public databases are worth naming, which package each analysis job belongs to, and the safety boundaries they attach to clinical, animal-welfare and regulatory work. |
| [science-superpowers](https://github.com/K-Dense-AI/science-superpowers) (K-Dense, Inc.) | MIT, 2026 | The **methodology order** under `framing-*`, `surveying-*`, `designing-*`, `preregistering-*`, `setting-up-*`, `executing-*`, `investigating-*`, `verifying-*`, `requesting-*`, `reporting-*`, `establishing-*` and `writing-*`: pre-registration before outcomes, the confirmatory/exploratory split, anomaly root-cause before adjustment, and evidence before claims. |
| [k-dense-byok](https://github.com/K-Dense-AI/k-dense-byok) (K-Dense) | MIT, 2026 | The **desktop-workspace shape** only: bring-your-own-key providers, a local-first project folder, compute chosen per task, and a notebook that records reasoning next to results. Titan already had each of those; the skill text says which Titan surface owns it. |

## What is original here

Every sentence in these skill bodies. The upstream repositories phrase their
methodology for their own harness, their own tool names, and their own file
layout; none of that applies to this one. Each skill below was written against
Titan's real surface: `todo_write`, `bash`, `read`, `write`, `edit`,
`web_search_multi`, `web_read_smart`, `papers_search`, `ml_preflight`,
`ml_run_pipeline`, `ml_wiki`, `present_artifact`, `spawn_subagent`,
`summon_review`, `ask_user_question`, and the `skills` tool.

Two of the fourteen are Titan's own, with no upstream lineage:

- `science-workflow` is the entry point for NAXIUM Science mode. It routes a
  request to the right skill in the order above, names the tools, and is the id
  the router shortlists for the mode.
- `running-science-on-a-local-model` is the piece the upstream sets do not have.
  They assume a frontier model with a large context. This one is written for the
  4B to 12B local models Titan is often run on: one step per turn, print rather
  than recall, fold long output, keep the plan in a file, check every step
  against its expectation, and hand off the steps that exceed the model.

The three blocks that repeat across these skills live once in
`packages/nx-titan-configs/skills/fragments/` and are inlined at read time:

- `${science-slm-contract}`: how the work is written down so a small model can
  finish it.
- `${science-evidence-record}`: what a claim has to carry.
- `${science-human-boundary}`: the line between an aid and a decision.

Keeping them as fragments is not tidiness. A body that carries the same three
paragraphs costs context on every turn, and the small-model budget classes cap a
skill body at 4,000 characters.

## Names this repository retains

The project names above appear in exactly three files: this notice, the `LICENSE`
next to it, and `docs/LICENSES.md`. No skill body carries one. Science mode and
its skills are Titan's.

## Getting more than this set

This directory is a curated subset chosen for what Titan's tool surface can
actually execute. The full libraries ship hundreds of skills, and the Extensions
view browses live third-party catalogues (`catalog.list`) with a quarantined
install (`extension.installRemote`) for anything published there.
