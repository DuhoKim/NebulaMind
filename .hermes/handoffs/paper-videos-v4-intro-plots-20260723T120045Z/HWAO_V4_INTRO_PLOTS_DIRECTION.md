# HWAO V4 DIRECTION — introductions and evidence plots (paper videos)

Author: Hwao (coordinator) · Written: 2026-07-23 ~14:00 KST (05:00Z)
Brief: `HWAO_BRIEF.md` in this lane · Mode: read-only inspection + this one report. No render, upload, visibility, website, DB, deploy, git, cron, or V3-artifact mutation occurred.

## 0. Evidence base (what was actually inspected)

- V3 publication receipt `paper-videos-v3-male-lipsync-20260723T050645Z/final_publication_handoff.json`: five public V3 videos (z9-metallicity `unxDehCBlqQ`, scaling-relations `03ckTQepNcc`, massive-abundance `op-1qwx9Pqk`, mzr-framework `Ip3QFVWWEP0`, tng-validation `__Zpj526DxE`), 2:40–2:48 each, manual English captions, local+API+watch-page QA PASS.
- V3 selection contract `selection_v3.json`: presenter C (fictional young Black male creator, master PNG sha `e6600e3e…`), voice Kokoro-82M ONNX `am_michael`, speed 1.0, 134.4 wpm, presenter box [1980,610,430,560] in 2560×1440, "presenter secondary to science"; any voice/wording/identity/speed change invalidates lip-sync + captions.
- V2 spec `paper_video_specs_v2.json` + `build_paper_videos_v2.py` + V3 `build_v3_audio_and_layouts.py`: 8 teaching scenes (+intro scene_00, +outro scene_09); V3 reuses V2 scene PNGs; **scene 1 pastes the manuscript first page as a large left panel** (`render_scene`, index==1, `first_page_path` — `build_paper_videos_v2.py:274`), which is exactly the failure Duho flagged.
- Source freeze `source_freeze.json` (marker `NEBULAMIND_FIVE_PAPER_V2_SOURCE_FREEZE`): five frozen PDFs with sha256 + frozen `.md` text extracts + first-page PNGs under `paper-videos-v2-20260723T034035Z/sources/`.
- Figure captions located in the frozen extracts (line numbers are `.md` lines): z9-metallicity:173 Fig 1; scaling-relations:385 Fig 2; massive-abundance:170 Fig 1; tng-validation:301 Fig 1 + :312 Fig 2; mzr-framework: **no figure caption found**.
- z9 abstract quantities (from frozen extract): −0.47±0.10 dex (Nakajima Te, lensed anchors), −0.69±0.03 dex unlensed (Pollock, N=5, z=9.3–9.9, logM⋆=8.2–8.6, leave-one-out spread 0.04), anchor swap −0.65 dex, Isobe ~1500-galaxy JADES −0.5 to −0.6 dex, Te-scale uncertainty 0.1–0.2 dex, explicitly not a detection.
- NOT yet inspected (stopped on direction): the papers' build lanes (`galaxy-evolution/overnight-*-20260720`) for raw figure data/`.tex` — so **data recoverability is unverified for every paper**; treated accordingly in §4.

## 1. Acceptance contract (user correction → testable criteria)

A V4 video passes only if all hold:

1. **No manuscript cover-page-as-explanation.** The first-page image appears in no teaching scene, at no size. (Automatable: no layout composites `*-first-page.png`.)
2. **Opening establishes the scientific question in plain language** within the first ~20 s: what is measured, why it is hard, what would count as an answer — before any jargon or branding.
3. **Plots are evidence-bearing and readable**: every plotted visual carries the claim being shown; minimum rendered axis/tick label height ≥ 22 px at 2560×1440 (≈ legible at 1440p and acceptable at 720p); no plot shown for under ~8 s.
4. **Every plotted visual is tied to (a) a frozen figure/data source and (b) exactly one allowed claim**, both recorded in the V4 spec (`figure_source` + `claim` + `source_lines` into the frozen `.md`). No visual may imply more than its recorded claim.
5. **Presenter C + `am_michael` + exact-audio lip-sync unchanged** (per `selection_v3.json` downstream rule) unless Duho changes them.
6. **Descriptive / not-validated boundaries stay prominent**: the status scene remains, and the "machine-generated, descriptive, not validated, not a formal detection" line stays in on-screen text and description metadata.

## 2. Reusable V4 scene grammar (drop-in for the existing 10-slot pipeline)

Keep the proven mechanics (per-scene Michael audio → SRT → layouts → lip-synced presenter composite); replace scene *content* roles:

| Slot | Role | Content rule |
|---|---|---|
| 00 | Title hook (~8 s) | One-sentence question hook + series branding. No cover page. |
| 01 | Problem / introduction | Plain-language question + why it matters; 2–3 concept cards (reuse V2 card grammar). Replaces the cover-page scene. |
| 02 | Method / sample | What data, what sample, what is computed; one small schematic or sample-count card. |
| 03–05 | Evidence plots (2–3 scenes) | One plot per scene, full-width panel where the cover page used to sit is NOT reused — plot occupies the primary ~1900 px panel, presenter box untouched; each with 1-line plain-English axis caption + 1-line claim annotation. |
| 06 | Interpretation / cross-check | What the plots jointly support; the paper's own robustness/cross-check numbers. |
| 07 | Limitation / status recap | Dominant systematic + "descriptive, not validated" boundary (keeps V2's warning-scene styling). |
| 08 | (optional spare) | Extra evidence plot for figure-rich papers, else merge and shorten. |
| 09 | Outro | Read-the-paper URL + status line. Unchanged. |

Narration budget unchanged: ~134 wpm ⇒ keep each scene 20–40 words to hold ≤ ~3 min.

## 3. Paper-by-paper plot candidate map

Page numbers and per-figure pixel quality are deliberately left to the Goru inventory (G1 below); caption anchors are exact.

| Paper (frozen PDF under `paper-videos-v2-20260723T034035Z/sources/`) | Candidate visual | Axes in plain English | Exact claim it supports | Risks |
|---|---|---|---|---|
| `z9-metallicity.pdf` (sha `7b12f8af…`) | **Fig 1** (caption `.md:173`): unlensed z≃7–10 mass–metallicity plane | x: galaxy stellar mass; y: gas oxygen abundance; points: the 5 unlensed galaxies vs the local relation | "The five unlensed z≈9–10 galaxies sit ~0.69±0.03 dex below the local relation" | Small N labels may be tiny; deficit depends on Te scale (0.1–0.2 dex) — annotation must say so; per-galaxy values likely in a table → best redraw candidate **if** Kun verifies |
| `scaling-relations.pdf` (sha `8a45fe2a…`) | **Fig 2** (caption `.md:385`): offsets from z≈0 relations vs redshift | x: cosmic time (redshift); y: how far high-z galaxies deviate from today's relations | "Deviations from local scaling relations grow/evolve systematically with redshift" | Fig 1 not yet located in extract — inventory must confirm figure count; multi-panel figures may need per-panel crops; calibration-scale caveat (memory: O/H scales don't cancel) |
| `massive-abundance.pdf` (sha `1b2de6f7…`) | **Fig 1** (caption `.md:170`): cumulative number density of massive galaxies vs mass | x: galaxy stellar mass; y: how many such galaxies per volume exist above that mass | "Whether 'too massive, too early' survives depends on the counted abundance vs TNG expectation" | Log axes need plain-English framing; caption truncated in extract — verify full caption before annotating |
| `mzr-framework.pdf` (sha `bb0869aa…`) | **No figure found in extract.** Fallback: deterministic framework diagram built ONLY from the paper's own stated steps/table text, clearly labeled "diagram of the paper's procedure, not data" | n/a (workflow panel, not axes) | "Comparing metallicities requires matching aperture + calibration scale before claiming evolution" | Highest design risk: nothing to crop; any diagram must quote the paper's own wording (no invented quantities); if Goru's inventory finds a real figure/table, prefer it |
| `tng-validation.pdf` (sha `f037d89d…`) | **Fig 1** (caption `.md:301`): TNG median relations (coloured) vs SDSS z≈0 observations (black); **Fig 2** (caption `.md:312`): offsets vs redshift | Fig 1 — x: galaxy mass; y: relation quantity; curves: simulation vs real survey. Fig 2 — x: redshift; y: sim-minus-data offset | "TNG runs ~0.3 dex low vs SDSS on [relation per caption]; calibration ≠ validation" | Two-figure scene budget (use slots 03+04); coloured curves must survive crop contrast; the "~0.3 dex low" annotation must quote only the caption's own relation |

## 4. Crop vs redraw decision

**Default = deterministic high-DPI crop of the frozen PDF figure + plain-English annotation overlay.** Redraw is allowed **only** per-figure after Kun verifies the full plotted series/values are recoverable from a frozen source (paper table, or the 20260720 build-lane data once inventoried) — the z9 N=5 sample is the only likely qualifier today. Never invent geometry, smooth, extrapolate, or add synthetic points; annotations may quote only numbers present in the frozen `.md`. Every crop/redraw records: source sha256, page/bbox or data table + script hash, and the one allowed claim (contract §1.4).

## 5. Highest-risk local canary + QA before any batch rebuild

**Canary = z9-metallicity, full single-video local build** (flagship track; densest quantitative claims; the one likely redraw; tests the new intro replacing the cover-page scene). Local only — no upload, no publication.

QA criteria (all must pass, receipts sha-stamped in this lane):
1. No frame contains the first-page image (layout audit + spot frames).
2. Fig-1 scene: axis labels ≥ 22 px, claim annotation exactly matches spec `claim`, source sha recorded.
3. Narration text == spec text == SRT (existing deterministic check), duration ≤ 3:00, scene count per grammar §2.
4. Presenter box, identity master sha, voice id/speed unchanged vs `selection_v3.json`; lip-sync regenerated only from new audio.
5. Boundary text present in scene 07 and outro; "not a formal statistical detection" appears verbatim.
6. Duho watches the canary and approves before any of the remaining four are built.

## 6. Ordered gates and lanes

- **G1 — Inventory (Goru, mechanical, read-only):** per paper — figure/page list with pixel sizes, full captions, tables, and any build-lane data files under `galaxy-evolution/overnight-*-20260720`; output one JSON inventory in this lane.
- **G2 — Reproducibility check (Kun, read-only):** for each proposed redraw, confirm every plotted value is recoverable from frozen sources; verdict crop|redraw per figure.
- **G3 — V4 spec draft (Hwao coordinates, Lana reviews scientific/visual semantics):** scene-by-scene spec per grammar §2 + contract §1; Lana signs claims/axes wording against the frozen `.md`.
- **G4 — Canary build + QA (Tori executes bounded build; Tori verifies receipts):** §5 only, local.
- **G5 — User approval of canary (Duho).**
- **G6 — Batch rebuild of remaining four (Tori, bounded), same QA.**
- **G7 — Publication decision:** separate explicit user gate; nothing in this direction authorizes upload, visibility, or metadata changes.

Hard exclusions from the brief remain in force at every gate: no video rendering or media generation (until G4's explicitly gated local build), no YouTube upload/privacy/deletion/metadata mutation, no V1/V2/V3 visibility change, no website/embed/cockpit mutation, no DB write, deploy, restart, cron, git write, branch/worktree change, or public publication, and no overwrite of any V3 artifact/checkpoint/receipt.

HWAO_V4_INTRO_PLOTS_DIRECTION_COMPLETE
