# Provenance for the NAXIUM Design skills

Ten skills, all Titan text. They are not copies of the upstream libraries, and
they are not a bundled agent runtime. `LICENSE` in this directory carries the
notices the two MIT sources require and states the terms of the Apache-2.0 one.

| Upstream | License | What was adapted |
|---|---|---|
| [impeccable](https://github.com/pbakaus/impeccable) (Paul Bakaus) | Apache-2.0 | The two-document setup (`PRODUCT.md` for durable product truth, `DESIGN.md` for visual direction and its separation from the product's facts), the audit and self-critique pass, the tinted-neutral and gray-on-color rules, the motion guidance, and the anti-pattern vocabulary. No files were copied: no code, no rule data, no command text. |
| [hallmark](https://github.com/Nutlope/hallmark) (Nutlope, made by Together AI) | MIT | The macrostructure idea (name the page shape before styling it), the audit as a punch list with severity rather than a rewrite, and the study-a-reference flow that extracts structure, type and color instead of reproducing pixels. |
| [taste-skill](https://github.com/Leonxlnx/taste-skill) (Leonxlnx) | MIT | The anti-slop frontend framing: one direction per brief, a display face with character rather than one neutral sans everywhere, one spacing scale, and the rule that two pages for two briefs must not be color-swaps of the same template. |

## What is original here

Every sentence in these skill bodies, and the two skills whose frontmatter says
`Titan original` because they adapt nothing:

- `design-workflow` is the entry point for Design mode. It routes a request to
  the step it is actually at, names the tools this repository really has, and is
  the id the router shortlists for the mode.
- `frontend-on-a-small-model` is the piece none of the upstream sets carry. They
  assume a large context and a frontier model. This one is written for the 4B to
  12B local models Titan is often run on: read a stylesheet in a window rather
  than whole, one section per turn, tokens before components, render and look at
  two widths, measure what can be measured, and hand off what exceeds the model.

`anti-slop-tells` distills the three sources above into the tells this
repository's own design review checks for: a tell the product bans cannot be a
tell the design library recommends.

The block that repeats across these skills lives once in
`packages/nx-titan-configs/skills/fragments/design-slm-contract.md` and is inlined
at read time as `${design-slm-contract}`, so the same seven rules cost one copy
instead of ten.

## Names this repository retains

The upstream names above appear in this notice, in the `LICENSE` next to it, in
`docs/LICENSES.md`, and in the source comment of the `design_studio` tool, which
is where the art-direction board it writes came from. No skill body carries one.
Design mode, its skills and its surface are Titan's.
