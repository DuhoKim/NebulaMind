# Hwao coordination plan — remaining NebulaMind Lab navigation videos

Task: `nav-video-expansion-20260721`
Lane: Hwao/Fable coordinator
Status: PLAN_COMPLETE — planning only, no rendering performed
Source of truth read: `NebulaMind-origin-main-live/frontend/src/app/lab/{labTabStore.ts, stageData.ts, LabStages.tsx}` + V8 receipts under `HermesOps/scripts/clips/subnav_flow_female_voice_v8/`

---

## 0. What the user asked

> "generate videos for remained parts also. should we change the character for each Nav?"

Two questions: (a) how much to render for the parts not yet covered, and (b) whether the presenter identity should change per stage. This plan decides both and hands Tori a bounded, per-video render spec.

## 1. Ground truth — the actual top navigation

`STEPS` in `labTabStore.ts` is **four** stages, not fourteen flat items:

| key | nav label | heading | coverage |
|---|---|---|---|
| `topic` | Topic | How the research topics were picked | ✅ done (5 clips) |
| `data` | Data | The data sources | ⬜ remaining |
| `research` | **Methods** | The analysis methods | ⬜ remaining |
| `paper` | Paper | The outputs produced | ⬜ remaining |

Sub-items (`stageData.ts`): Data = SDSS · JWST · COSMOS2020 · IllustrisTNG (4). Methods = ms · mzr · smf · eff · simobs (5). Paper = progress · flagship · frontier · pipeline · how (5). Note the nav label for `research` is **"Methods"** — narration must say "Methods", never "Research".

Topic was already shipped as five clips (`oMA-H1m5yZQ`, `1vjXzWa9JAY`, `RbjFCiX2i3k`, `cp8-I5XRP9s`, `1tG5cuTcPXI`).

## 2. Decision 1 — Scope: **three stage-overview videos** (Data, Methods, Paper)

**Recommended: 3 videos, one per remaining stage, 60–75 s each, in the established V8 format.** Not fourteen per-sub-item clips.

Why this matches the real navigation:

- **Topic was per-sub-item for a reason that does not generalize.** Topic's five items are *sequential stages of one algorithm* (corpus → embedding → clustering → overlay → ranking); each has its own distinct visualization, its own numbers, and only makes sense after the previous one — so each earned a full explainer. Data / Methods / Paper are the opposite: each stage is a **catalog of parallel siblings** (four surveys; five scaling relations; five views of one output board). A viewer landing on the Data dropdown wants "what are the sources and why these four," answered once in 70 s — not four near-identical ~10 s talking-head clips.
- **One video per remaining dropdown = 1:1 with the top nav.** Three uploads fill the three empty stage embed slots and keep the series coherent (Topic covered in depth, each other stage covered once). Fourteen clips would be repetitive channel uploads with high fixed per-clip cost (render + manual SRT + QA + separate upload gate) and low marginal payoff.
- **Each sub-item still gets airtime** as one dedicated scene inside its stage video (see the six-beat maps in §5), so nothing is dropped — it is threaded, not multiplied.

Deferred, not rejected: if the user later wants per-survey deep dives (e.g. a standalone SDSS or JWST clip), that is a clean follow-on task — flag it, do not pre-build it now.

## 3. Decision 2 — Character: **keep the person, change the set**

Direct answer to "should we change the character for each Nav?": **No — do not change the presenter.** Keep the single recognizable female astronomer that anchors the Topic series.

- **Same face** — the exact `character/master_portrait.png` identity, no re-roll.
- **Same voice** — `en-US-EmmaNeural`, female, "Cheerful/Clear/Conversational", +38 % synthesis rate, as in every V8 clip.
- **What changes per stage** — wardrobe, background set, accent palette, framing, and on-screen specialty cues. Same host, three purpose-built sets.

Rationale: identity continuity is what makes this a *series* rather than three unrelated uploads; it compounds channel recognition and lets the palette (not a new person) signal "you are now in a different stage." Introducing new faces/voices would fracture the brand for zero explanatory gain. This is the standard "one host, different set" explainer pattern.

## 4. Decision 3 — Creative variants (continuity chosen)

Palettes are pinned to the site's own Lab tokens so the video matches the page it embeds in (`--lab-accent` ≈ `#7c86ff` indigo, `--lab-accent2` ≈ `#4ad6c4` teal, plus the amber/gold `#e0a458` used in the charts).

| Stage | Persona | Accent palette | Wardrobe / framing | On-screen specialty cues |
|---|---|---|---|---|
| **Data** | Observational astronomer at the archive | Cool teal → blue (`#4ad6c4`/`#38bdf8`) | Field jacket; medium framing; observatory / server-archive backdrop | Telescope dome, sky-survey footprint, SQL/catalog rows, redshift ladder z≈0→10 |
| **Methods** | Computational astrophysicist | Violet → indigo (`#7c86ff`/`#8b93c9`) | Neat lab layer; slightly closer framing; whiteboard/plot backdrop | Equations, scaling-relation scatter plots, TNG simulation cube, "same recipe both sides" motif |
| **Paper** | Research editor / referee | Warm gold (`#e0a458`) | Editorial/desk styling; desk framing; manuscript-wall backdrop | AASTeX manuscript page, citation links, ACCEPT/MINOR/MAJOR/REJECT stamp, revise-loop arrow |

Common to all three: 1280×720 · 24 fps · ~73.5 s · six scene-aligned narration paragraphs · exact-audio talking presenter · manual scene-aligned SRT · light ambient bed (reuse `original_cosmic_ambient_73s.wav`, optionally tinted per palette).

## 5. Decision 4 — Acceptance matrices (one per planned video)

Fixed across all three (do not re-decide per video): **Voice** en-US-EmmaNeural / female / +38 %. **Captions** manual SRT, one cue per scene, timed to the exact TTS driver (V8 method). **Duration** 60–75 s target (~73.5 s reference). **Local QA** — replicate `qa_receipt.json`: 4× decode pass, ≥72 temporal frames reviewed, presenter identity stable, exact-audio lip-sync, female driver median f0 in 170–178 Hz (reject if ≤141 Hz), caption timing pass; log all timestamps in **KST**. **Publication gate** — see §7; every video is a local master only until the gate clears.

### 5A · DATA — "The data sources"
- **Purpose:** why these four surveys, arranged as a redshift ladder from the z≈0 anchor to the JWST frontier, plus the simulation they will be tested against.
- **Source claims (from `stageData.ts`, verify per §6):** SDSS ~10⁶ nearby galaxies, galSpecExtra + galSpecLine, SkyServer DR18 SQL, GSWLC-2 & MPA-JHU via VizieR TAP, z≈0 anchor for MZR/SFMS/FMR. JWST rest-frame optical z≈4–10 NIRSpec; Nakajima+23 (180), Lisiecki+25 (3743 MIRI/CEERS), Chworowsky+24. COSMOS2020 ~1.7M photometric galaxies, LePhare/EAZY masses + photo-z. IllustrisTNG TNG100-1 group catalogs via public API at z=0/4/5/6, h=0.6774, f_b=0.1575.
- **Six scene beats:** (1) intro — read whole surveys, not a cherry-picked sample; the ladder in redshift. (2) SDSS — the local z≈0 benchmark every relation is measured against. (3) JWST — the high-z frontier, first statistical early-Universe chemistry. (4) COSMOS2020 — ~1.7M photometric masses bridging the gap to z≈5. (5) IllustrisTNG — the flagship simulation held out as the thing to test. (6) how they combine + the honesty caveat.
- **Narration boundaries:** state the Tremonti O/H ~0.24 dex offset is *reconciled before cross-survey comparison* (do not imply raw scales are directly comparable). Call photometric masses "photometric" (photo-z scatter, no Vmax completeness correction). Do not call any of these a NebulaMind result — they are inputs.
- **Presenter:** Data persona, teal/blue set, archive/dome cues.

### 5B · METHODS — "The analysis methods"
- **Purpose:** the five scaling relations the pipeline measures, and the single idea that the *same relation is computed identically* in every dataset so comparisons are fair.
- **Source claims:** ms — median log SFR in mass bins (sSFR cut), fit slope + normalization across z; tests cosmic SFH. mzr — 12+log(O/H) vs M✱ + FMR on a matched abundance scale, aperture check; tests enrichment / FMR-vs-aperture. smf — comoving number density per dex of M✱; tests mass assembly + JWST "too many massive galaxies too early". eff — M★/(f_b·M_halo) vs halo mass (abundance matching); tests whether the baryon budget even allows the counts (Boylan-Kolchin). simobs — the same relations overlaid TNG-vs-data on a matched scale.
- **Six scene beats:** (1) the idea — one recipe, run identically everywhere, so any gap is physics not method. (2) star-forming main sequence. (3) mass–metallicity + FMR. (4) stellar mass function → SF-efficiency / baryon budget. (5) simulation vs observation — the sharpest test. (6) honesty floor — matched scales, medians not cherry-picks, results are descriptive.
- **Narration boundaries:** never assert a specific measured slope/normalization as a validated finding — these are *methods*, and any live number belongs to the Paper stage under the descriptive label. Say "on a matched abundance scale" wherever metallicity is mentioned. Frame simobs as a test, not a verdict.
- **Presenter:** Methods persona, violet/indigo set, equations/plots/sim-cube cues.

### 5C · PAPER — "The outputs produced"
- **Purpose:** what the pipeline emits — the draft board, hand-guided flagship vs pipeline frontier drafts, the live automated run board — and honestly how a paper is actually made and gated.
- **Source claims:** boards = Draft board (every draft + status), Flagship (hand-guided), Frontier (pipeline), Pipeline runs (automated live board). "How papers are made": Draft = real numbers into an AASTeX (`aastex631`) manuscript, compiled to PDF with tectonic; Referee = automated `astrosage-70b`, verdict ACCEPT/MINOR/MAJOR/REJECT, author revises (soften overclaims, add caveats, never invent numbers) and re-reviews; Gates = novelty gate + citation-entailment gate; Honest label = bounded automated results are **descriptive, not validated measurements** until human review; MINOR ≠ acceptance.
- **Six scene beats:** (1) what the outputs are — the draft board and where each stands. (2) flagship (hand-guided) vs frontier (pipeline) drafts. (3) pipeline runs — the automated live board. (4) how one is made — real numbers → AASTeX → tectonic PDF. (5) the referee loop + the two gates (novelty, citation-entailment). (6) the honest label — descriptive until a human clears it.
- **Narration boundaries:** speak board *counts* only qualitatively or re-read them at render time (the boards are live and drift — see §6); never present a pipeline draft as a peer-reviewed or validated result; keep the "descriptive, not validated" wording verbatim; do not name the referee as a human process.
- **Presenter:** Paper persona, warm-gold editorial set, manuscript/citation/review-loop cues.

## 6. Decision 5 — Claims requiring live-source inspection before narration is final

Tori must re-read these against the live page/source at render time; do not lock final narration until confirmed:

1. **Live/dynamic boards (Paper stage):** flagship / frontier / pipeline counts and statuses change — keep qualitative or re-read at render; never bake a stale count into audio.
2. **Model/tool names:** referee = `astrosage-70b`, embedding = qwen3-embedding-4b, AASTeX `aastex631`, tectonic — confirm none have been renamed since these files (memory notes a separate broken `atom-astronomy-7b`; do not cite it — `stageData.ts` is authority).
3. **COSMOS2020 "~1.7M"** and the JWST sample sizes (180 / 3743) — confirm against the served `stageData.ts` before speaking exact figures.
4. **TNG constants** h=0.6774, f_b=0.1575 and snapshots z=0/4/5/6 — confirm unchanged.
5. **Metallicity scale caveat** — the Tremonti +0.24 dex reconciliation is load-bearing for the Data + Methods honesty boundary; keep it (memory: metallicity-calibration-scale gotcha).
6. **Embed/upload state:** `subnavVideos.ts` is stale and **out of scope** — do not read it as truth for what is public, and do not narrate "watch the next clip" against an unconfirmed slot.

## 7. Execution notes for Tori (bounded local render) + publication gate

**Reuse, do not rebuild** — parameterize the existing V8 pipeline per stage:
- `generate_female_narration_v8.py` → TTS (en-US-EmmaNeural, +38 %, six scenes, exact-audio driver).
- `run_female_talking_heads_v8.py` + `build_flow_female_voice_v8.py` → talking-head + composite + SRT.
- `character/master_portrait.png` → identity (unchanged). `original_cosmic_ambient_73s.wav` → ambient bed.
- Per-stage deltas are only: narration text (§5), palette/wardrobe/backdrop/cues (§4), SRT cues. Output three local masters named `NEBULAMIND_SUBNAV_{DATA,METHODS,PAPER}_V8_FEMALE_VOICE_EXACT_LIPSYNC.mp4` with a `qa_receipt.json` per §5.

**Publication gate (hard stop — separate from rendering):**
- Local masters + QA receipts only. **No upload, no visibility change** without explicit per-video user approval.
- When approved, default **UNLISTED** review copies only (public requires a separate explicit OK per video).
- **No cron / no automated upload job** without per-step approval (memory: no-cron, quintet /credits + cron ban).
- **No edits** to `subnavVideos.ts` or any delivery manifest, no DB/API writes, no deploy/restart, no git writes — those are out of this task entirely.

## 8. Safety & ownership recap

Planning-only Hwao task. This step: read the four live Lab sources + V8 receipts, wrote this one plan file. Performed **no** rendering, image/video generation, upload, visibility change, source/manifest edit, DB/API write, deploy, git write, cockpit edit, or secret access. All deferred actions above are gated on explicit user approval.

---

HWAO_NAV_VIDEO_EXPANSION_PLAN_COMPLETE_20260721
