# G3/G4 — z9 SIGN-OFF RECORD + BOUNDED CANARY-BUILD INSTRUCTION FOR TORI

Coordinator: Hwao · Written: 2026-07-23 ~14:55 KST (05:55Z) · Lane-only receipt.
Role note (honest record): per Duho's explicit "proceed", the Kun and Lana rulings below were executed by Hwao wearing those hats inside this lane this turn — no separate agent sessions. Every ruling is falsifiable via the cited anchors, so a later independent re-check can overturn any line item without unwinding the lane.

## Kun ruling — crop vs redraw for z9 Figure 1: **CROP**

- The evidence content of Figure 1 is the five per-galaxy (stellar mass, O/H) points. The G0 freeze extract contains **no recoverable per-galaxy value table** — only axis-tick bleed (`sources-v4/z9-metallicity.md:71-86`) and the qualitative "points lie ≈0.5–0.7 dex below" (`:96`). Redrawing the points would require inventing coordinates → prohibited by the direction (§4).
- Partially recoverable elements exist (Curti curve functional form `:96-100`; Isobe Z8=7.62±0.10, slope 0.34 `:92-94`) but a curves-only redraw would omit the actual evidence, so it fails "evidence-bearing".
- Therefore: use the G0 vector crop `sources-v4/figures/z9-metallicity-figure-1-vector-crop.png` (sha256 `8d1575a7…`, 1482×1080, 6× vector render, page 2, caption sha `c87ab296…`) in all three evidence slots, with per-slot single-claim overlays. Upscale cap 1.15×.
- Standing re-evaluation trigger: if a verified per-galaxy table lands in a future freeze, redraw may be reconsidered for the batch — not for this canary.

## Lana sign-off — semantic and visual: **PASS**

Semantic (claims vs current freeze):
- Slot 4 claim −0.69±0.03 / spread 0.04 = `:34`; "one fifth" = 10^−0.69 ≈ 0.20 ✓.
- Slot 5 claim 0.04-dex anchor shift to ≈−0.65 = `:37` (precise −0.645/0.042 at `:115` — rounded form matches the abstract) ✓.
- Slot 6 claim ~1500-gal stack, z=4–10, −0.5…−0.6 dex, Z8=7.62±0.10 = `:38-39`, `:92-94` ✓.
- Slot 7 GN-z11 z=10.6, direction-only framing, population −0.64…−0.68 = `:139-142` ✓ (does not overstate GN-z11's own uncertainty, 7.82±0.35 not narrated as precise).
- Slot 8 Te-scale 0.1–0.2 dex dominant = `:43`, `:113`, `:135`; detection disclaimer verbatim ✓.
- Axis plain-English ("Across: stellar mass. Up: gas oxygen abundance.") matches the figure caption's axes ✓.
- G2 rewrites (massive-abundance 3–6, scaling-relations 4–5 [+6/8 recommended], tng-validation 5) reviewed against their anchors — approved as written in `G2_NARRATION_REWRITES.md`.

Visual:
- No slot uses any cover/first-page asset; `forbidden_assets` enforced in spec ✓.
- Evidence panel region (110,250)-(1940,1330) does not intersect the presenter box [1980,610,430,560] ✓.
- Crop is a 6× vector render reviewed on G0's `V4_VECTOR_FIGURE_CROP_SHEET.png`; tick-label legibility to be measured at QA (≥22 px rule) rather than assumed ✓.
- Warning styling retained on slot 8; three-evidence-beat pacing (≥8 s each) within the ≤3:00 budget ✓.

Sign-off scope: `V4_Z9_CANARY_SPEC.json` (sha at build time to be recorded by Tori) + `G2_NARRATION_REWRITES.md`.

## Exact bounded canary-build instruction for Tori (G5 — runs only on Duho's release phrase "proceed z9 canary")

**Goal:** one local z9-metallicity V4 video implementing `V4_Z9_CANARY_SPEC.json` exactly. Local only.

**Allowed:**
1. Write everything under `canary-v4-z9/` inside this lane (build scripts, audio, layouts, lip-sync frames, composite, QA outputs). Model the builder on V3's `build_v3_audio_and_layouts.py` → `render_v3_musetalk_presenters.py` → `composite_v3_batch.py` chain, but reading `V4_Z9_CANARY_SPEC.json` as the sole narration/layout source (10 slots: 0 hook, 1–8 teaching, 9 outro).
2. Generate am_michael audio (Kokoro-82M, speed 1.0), SRT from spec narration, layouts (fig1_crop per spec, sha-verified before compositing), MuseTalk exact-audio lip-sync with presenter C master, final 2560×1440 composite.
3. Run deterministic QA + visual QA implementing the spec's `acceptance_checks` verbatim (including the 22 px label measurement and forbidden-asset scan), writing `canary-v4-z9/qa/` receipts and a final `canary-v4-z9/CANARY_LOCAL_HANDOFF.json` with shas of spec, audio, layouts, video.

**Prohibited (unchanged):** any YouTube/upload/visibility/metadata action, website/embed/cockpit change, DB, git, runtime/deploy/restart/cron, any write outside this lane, any edit to V2/V3 artifacts or to the frozen sources, any change to identity/voice/speed/wording (downstream rule: such a change invalidates lip-sync and captions and voids this sign-off).

**Stop condition:** after QA receipts are written, stop and report PASS/FAIL per acceptance check to Hwao/Duho. Duho watches the canary (G6) before any batch work (G7) — batch will additionally consume `G2_NARRATION_REWRITES.md` for the three changed papers and the mzr-framework visual plan.

## Gate state after this receipt

- G2 ✅ (rewrites drafted + Lana-approved) · G3 ✅ for z9 (inventory from G0 + Kun CROP ruling) · G4 ✅ for z9 (signed spec).
- **Exact next gate: G5 — Tori executes the bounded canary build above, only on Duho's explicit release.**

HWAO_V4_G2_G3_G4_Z9_SIGNED_COMPLETE
