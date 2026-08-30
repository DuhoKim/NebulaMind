# STANDING ORDER — produce the BHU lane morning report (then delete this file)

**Order:** Duho, typed ~00:44 KST, relayed by Blanc 02:46 KST 2026-08-31, verbatim: *"give me the
morning report."* Blanc's timing ruling: **produce it at the MORNING tick, NOT overnight.** Blanc
collects all lanes into the **07:00 KST handover** and Duho is pinged then.

## WHEN
On the first tick that fires at **≥ ~06:00 KST** (check `date` every tick; before 06:00 = keep the
quiet loop, do NOT produce it yet — Blanc said not overnight). Aim to have it done before 07:00 so
Blanc can collect it.

## WHAT — per `[[feedback_morning_report_routine]]` + `[[feedback_read_status_aloud_by_default]]`
1. **Plain-English big-picture** written status of the BHU lane (the routine: everyday words, lead
   with the question, jargon stays in receipts).
2. **One audio reading in Tori's voice** — `~/HermesOps/scripts/nm_fable_say.sh tori --deck <deck>.json`
   (nova voice; NEVER `say`). Deck uses the podcast schema; **every on-screen number spoken aloud**.
3. **Route per tmux client width** (`[[reference_audio_routing_and_listen_page]]`): 171=MacBook →
   hand over the listen.html link (never leave the reading undelivered); 227=Studio → plays locally.

## CONTENT TO COVER (the lane's final state as of 2026-08-31 ~02:47)
- **The BHU published-bibliography audit is essentially complete.** 58 papers, all tiered + double-
  gated. **55 read; entries 1 & 3 abstract-confirmed; 3 paywalled holdouts (2, 42, 47) left gated
  by Duho's own call.** Battery `check.py` = 77 green.
- **Tiers:** 4 calibrated falsifiers (7, 44 FIRED · 31, 51 LIVE), 3 theoretical-obstructions
  (5, 22, 48), 7 qualitative-directional, ~32 consistency-only, plus 7 support instruments now
  content-bound.
- **Overnight, two seat gates both ran clean:** **B59** — entry 54's source OVERSTATES its ACT/DESI
  curvature support (both seats; citation fix, tier unchanged). **B61** — the curvature falsifier is
  **LIVE but NOT FIRED**; DESI+CMB Ω_k = +0.0023±0.0011 (~2.1σ OPEN, adverse to the family's closed
  prediction but not a detection). Wired a standing battery tripwire **b63** that re-fires at ≥3σ.
- **Foundations receipted overnight:** every entry's publication bound to a pinned Crossref record
  (b57, 58/58 published journal-articles), pin hash-custody (b58), entry-22 publication receipt (b56).
- **Cockpit** `bhu-lane2-status`: fixed 4 things Duho flagged — within-branch ordering, the four
  calibrated falsifiers were showing "—", folded in entry 16 + the 7 support papers, and pulled
  their formal citations. All 58 now shown.
- **Handoff to Hwao:** her prereg V124 (Longo-amplitude test) anchors on Longo 2011 = BHU **entry
  58**, which I content-verified in **b54** (pinned arXiv abstract, exact numbers) — an independent
  receipt for her citation pass. Brief: `TORI_TO_HWAO_BHU_STUDY_20260831T0046K.md`.
- **Open items:** none. (Browser route for 2/42/47 resolved: leave gated.)

## AFTER
Delete this file (`git rm`) once the report + audio are delivered, so it doesn't re-fire.
