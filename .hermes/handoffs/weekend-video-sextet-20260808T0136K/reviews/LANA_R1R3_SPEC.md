# LANA_R1R3_SPEC — screen/furniture/plot spec from the scientific-presentation consult

Owner: **Lana** (`lana-overhaul` seat). Filed **2026-08-08 14:07 KST** from
`reviews/SCIPRES_CONSULT_SYNTHESIS_R1R3.md` (my R1–R3 numbering).

## Authority — read first

- **Advisory, under a frozen order.** `HWAO_OVERHAUL_ORDER.md` supersedes this wherever they differ.
  This is implementation detail the order does not fix in renderer terms, not a competing order.
- **Single-writer preserved.** The `integrator` seat owns `tools/nm_paper_*.py` and the candidate
  `build.py`. **I do not edit those.** This file is an integrator-executable spec: field names, draw
  order, failure conditions, acceptance checks. I SPEC; the integrator EXECUTES.
- **Claim boundary unchanged.** `video_reportable_now: false`, `BLOCK_SUBSTANTIVE_RESULT_RENDER`.
  Nothing here authorizes a result claim. "handedness", never "parity", in any audience-facing text.

## Grounding — what the built candidate already implements

I read the candidate renderer (`integrator/canaries/spin-method-overhaul-canary-20260808T1312K/build.py`)
before speccing. **The 1312K build already implements the substance of all three items** — this spec
therefore (a) records accept/amend/reject, (b) formalizes the field/gate contract so the behaviour is
reproducible and the gates are permanent rather than incidental, (c) adds two forward extensions. Where
the build chose a different-but-stronger route than the synthesis proposed, I accept the built route and
say so.

---

## R1 — Split screen text from narration — **ACCEPT, with amendment (the `screen` field is moot)**

**Synthesis proposal:** add an optional per-card `screen` field rendered *instead of* `body`.

**What the build did instead (and why it is stronger):** the paragraph-`body` card kind is **gone**.
There is no `body` any more. `render(...)` (build.py 607–629) dispatches on the per-card `section` and
draws a **bespoke scientific diagram** for each; the full narration sentence is rendered **only** as a
bottom subtitle (`caption()`, build.py 239–245: a box at y 940–1055, one neutral style, fontsize 31).
So "screen == voiceover as the dominant visual" — the exact failure mode R1 names — is eliminated
architecturally: the dominant visual is the diagram, and the sentence is demoted to a subtitle.

**Amendment — spec the contract, drop the field:**
1. **Do not reintroduce a paragraph body.** The `screen` field is unnecessary for this build and must
   not become a back door to full-sentence cards. Each card's dominant text is the diagram's terse
   headline + labels.
2. **Headlines and diagram labels are terse noun phrases, stats, or marks** — never a full sentence
   (e.g. `PREDECLARED ASYMMETRY ESTIMATOR`, `VALUE WITHHELD`, `MIRROR DISCRIMINANT`). ≤ ~6 words.
3. **The narration sentence appears once, only as the subtitle**, ≤ 2 lines (enforced — see R3).
4. **Acceptance check:** for every card, the single largest text block must not be a narration
   sentence. Verifiable by the existing encoded-frame OCR pass (`encoded_qa.json`).

Disposition: **R1 accepted in substance; the `screen`-field mechanism is superseded by the
no-body architecture and should not be built.**

---

## R2 — Slide furniture — **ACCEPT as built; drop one sub-requirement**

**Built:** `global_chrome(draw, t, section)` (build.py 210–236) draws, on every frame:
- footer left `NEBULAMIND · SPIN METHOD`, top rule under it;
- **top-right `METHOD DESIGN · NO MEASURED VALUE` in amber** — a persistent claim-boundary reminder on
  every single frame. I **endorse this specifically**: it satisfies, at the furniture level, my standing
  requirement that the withholding be visible, not buried in one card;
- a **6-node section progress rail** (`QUESTION · MIRROR TEST · FROZEN DESIGN · ESTIMATOR · CONTROLS ·
  SCIENTIFIC GATE`), the active node driven by the per-card `section`;
- moving scan-lines that keep even long static states alive — satisfies HWAO §4 "no unchanged state
  > ~8 s" **without** decorative zoom or divider cards.

This **answers Kun's dead-air objection**: a persistent roadmap cue with **zero** full-screen section
cards. Yui's and Goru's independent "restore no divider cards" conclusions are honoured.

**Amendment — drop the `n / N` counter and linear top bar.** The synthesis asked for a card-index
`n / N` and a thin progress bar proportional to `idx/N`. The build uses a **discrete stage rail** keyed
to the *argument phase*, not the raw card count. That is better for this cut — it tells the viewer where
they are in the *reasoning*, not in a slide deck — so **do not also add** the numeric counter and linear
bar; two progress indicators would clutter. Stage rail stands as the single roadmap cue.

**Keep:** title-card structured credit. Confirmed present as `GALAXY ZOO 1 · DATA RELEASE · Table 2`
(no internal filename). If a human-readable author credit is wanted, add `data: Galaxy Zoo 1 —
Land et al. 2008` as a structured line, never a paragraph.

Disposition: **R2 accepted as built; `n/N` + linear bar dropped in favour of the stage rail.**

---

## R3 — Restyle plots for video + fail the build on overflow — **ACCEPT as built; the gate is LIVE; extend it**

**Built:**
- Figures are **bespoke vector-style diagrams** (per-`section` draw code), not matplotlib defaults. No
  internal plot `title` duplicating the card heading (the heading *is* the diagram title). Type is large
  and legible at 1080p (headlines/labels ≫ the old ~20px ticks).
- **The caption-overflow build gate exists and is live.** `validate_caption_layout()` (build.py 637)
  is called at build time (build.py 801) and **raises `RuntimeError` if any caption wraps to > 2 lines**
  — exactly R3's demand that "clipped text is a rendering bug promoted to a review gate." The f15-style
  clip cannot ship silently.
- `encoded_qa.json` on the actual encoded frames: `encoded_true_peak_no_clipping = True`,
  `no_forbidden_or_internal_filename_ocr_hits = True` — no repo paths, no truncated tokens on screen.

**Extensions — carry the same fail-hard discipline further:**
1. **Diagram-internal overflow gate.** The live gate guards only the subtitle caption. Extend the same
   raise-on-overflow check to any text baked into a diagram that exceeds its bounding box (the 1903 cut's
   clipped `REVERSES` bar annotation was *inside* a figure, not in the caption). Fail the build, don't clip.
2. **OCR forbidden-term gate → build-failing, not QA-advisory.** `no_forbidden_or_internal_filename_ocr_hits`
   is currently a post-hoc QA field. Because the claim boundary is **absolute**, promote it to a
   **build-failing gate**: any on-frame OCR hit of a forbidden term (`parity`, a result value, significance,
   dipole/cosmology, DESI/Ganalyzer, an internal `*.json`/repo path) fails the build exactly as the numeric
   guard does. Boundary enforcement must not depend on a reviewer noticing.

Disposition: **R3 accepted as built; the overflow gate confirmed live; two extensions specified.**

---

## Out of scope (per the synthesis brief — do not expand without Hwao)

R4–R9 (equation/table/stats card kinds, funnel schematic, character demotion, per-line builds,
sibling regeneration) and Yui's hash-bound build receipt. Several are already met by the 1312K build or
the HWAO order; none are opened here.

## Cross-reference to the frozen order

| This spec | HWAO order | Relationship |
|---|---|---|
| R1 no-body architecture | §3 "no paragraph/status/quote card as dominant visual" | R1 *implements* the ban positively (what to draw instead) |
| R2 stage rail + amber boundary footer | §4 "no unchanged state > ~8 s"; §5 withholding visible | R2 supplies the persistent cue the order requires |
| R3 bespoke plots + overflow/OCR gates | §3 "no internal filenames as citations"; §5 forbidden list | R3 makes the boundary a *build gate*, not a review hope |

All three sit inside the single-writer rule and the frozen claim boundary. Integrator executes.
