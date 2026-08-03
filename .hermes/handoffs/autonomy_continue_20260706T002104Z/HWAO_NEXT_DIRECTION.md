# Hwao next direction — 20260706T002104Z

Lane: Hwao/Fable (coordinator).
Inputs: continuation brief; wave2 dir (5 pins on evidence [26088, 26089, 28099, 28132, 28155],
Lana adequacy PASS-with-limitation, Goru repaired ledger, Tori independent validation PASS);
DB spec dir (2 specs + summary, markers present). `NO ACTIVE EXECUTION PHRASE` everywhere.

## 0. Wave2 completion ruling (the missing Kun artifacts)

**Not a hard blocker, but the first work item.** Tori's independent validation re-derived
everything Kun's checker would assert (offset→quote equality, hash recompute, 2929 exclusion,
no stance upgrade, no mutation artifacts), so the *facts* are verified. What's missing is the
*persisted, re-runnable* checker + boundary report that makes post-reset re-verification
possible. Ruling: Track A status = **PROVISIONAL_PASS (Tori-validated)**; it becomes COMPLETE
when Kun's artifacts land. Kun's closure runs first and in parallel with read-only starts of the
next slice — it must not serialize the whole night. Note satisfied: the pinned triplicate row is
28099, exactly the canonical-survivor rule from the dedupe spec.

## 1. Next recommended sequence (mission spine)

Pins are hardened → move up the spine. Two tracks in parallel:

- **Track C (primary autonomous artifact): debate-map refresh** — step6-style research-status /
  debate map rebuilt over the post-remap, post-recompute, post-pinning board, diffed against the
  2026-07-03 baseline (`docs/baseline_step6_status_debate_map_20260703T0954Z/`). This is the
  ledger→debate-map stage and the direct feeder of any future prose work. Docs-only, read-only
  inputs.
- **Track D (DB ripeness continuation):** finish what the specs need to become decidable —
  Lana's disposition route recommendations (now unblocked: `2604.15438` full text is fetched) —
  and prepare **one** exact packet (dedupe) under strict gates, execution withheld.

No UI/runtime/product work; operator visibility is served by cockpit text only.

## 2. Lane assignments (deliverables, paths, markers)

New run dir for Track C: `docs/hwao_debate_map_refresh_20260706T002104Z/`

- **Kun — wave2 boundary closure (first).** In `docs/hwao_overnight_pinning_wave2_20260705T1615Z/`:
  `pinning_wave2_checker.py` (deterministic: reparse `PINS_WAVE2.jsonl`, recompute sha256, assert
  `text[char_start:char_end] == quote`, assert no claim-2929 rows, assert role/stance verbatim
  vs read-only DB state, scan wave2+dbprep dirs for SQL/apply/rollback/migration artifacts),
  `CHECKER_RESULT.md`, `KUN_WAVE2_BOUNDARY.md`.
  Done marker: `KUN_WAVE2_BOUNDARY_CLOSED_20260706T002104Z`.
- **Lana — disposition route recommendations, then debate-map science pass.**
  (1) `docs/hwao_overnight_db_packet_prep_20260705T1615Z/LANA_DISPOSITION_ROUTE_RECS.md`:
  per-row route recommendation for all 14 rows of the 2929 spec — confirm/deny 28060→2942 from
  the fetched 2604.15438 text; relevance verdict on the 2512.21927v1 Perseus-Arm ×4 group;
  flag any Route-H rows. Also confirm dedupe survivor 28099 (payload check vs 28154/28161).
  Marker: `LANA_DISPOSITION_ROUTE_RECS_20260706T002104Z`.
  (2) Debate-map science layer: `LANA_DEBATE_MAP_SCIENCE.md` in the Track C dir — per affected
  section (AGN Feedback & Quenching; Star Formation, Quenching & Color Bimodality;
  Retrieval-Complete Evidence Claims): live disputes, stance balance quality, wording-contract
  risks, prose-readiness notes. Marker: `LANA_DEBATE_MAP_SCIENCE_20260706T002104Z`.
- **Goru — debate-map mechanical layer.** `GORU_DEBATE_MAP_COUNTS.md` + `debate_map_data.json`
  in the Track C dir: per-claim stance mix (support/counter/neutral), pin coverage, trust
  values, evidence counts, delta table vs the step6 baseline. Read-only extracts via Tori.
  Marker: `GORU_DEBATE_MAP_COUNTS_20260706T002104Z`.
- **Tori — dispatch, custody, gated packet generation.** (1) Write/dispatch the three saved
  briefs in §5. (2) Run read-only extracts for Goru/Lana. (3) After BOTH
  `KUN_WAVE2_BOUNDARY_CLOSED…` and Lana's survivor-28099 confirmation: generate the **dedupe
  exact packet** per its spec (backup, validator, checksums, drift guards, trigger tag,
  rollback spec gated separately) in a new `docs/galaxy_2931_dedupe_exact_packet_<ts>/` dir;
  run its validator; store packet id in the handoff dir only — **never in public cockpit**.
  Marker: `DEDUPE_PACKET_PREPARED_NOT_APPROVED_<ts>`. (4) Cockpit checkpoint per §6.
- **Hwao — synthesis.** `DEBATE_MAP_REFRESH.md` final synthesis review + the morning decision
  menu appended to `docs/hwao_overnight_pinning_atlas_20260705T153533Z/OVERNIGHT_RESULT.md`.
  Marker: `DEBATE_MAP_REFRESH_COMPLETE_20260706T002104Z`.

## 3. DB ripeness decision

- **(a) Read-only verification: YES**, ongoing for all lanes.
- **(b) Exact packet preparation: YES — for the dedupe packet only**, and only after two gates
  pass (Kun wave2 closure; Lana survivor-28099 confirmation). Grounds: the spec is complete, the
  route question collapsed once the wave-2 pin landed on 28099 (both live routes keep 28099; the
  only open sub-choice, plain-keep vs merge-notes, is recorded in the packet as a flagged
  option), and generation is reversible paperwork. The **disposition packet is NOT ripe for
  generation**: it awaits Lana's per-row route recommendations and then the user's route
  choices — it advances tonight only to recommendation-complete.
- **(c) Execution: NO — nothing executes tonight.** The user's standing sentence is not a
  packet phrase. Execution requires the generated packet's validator + drift + lane reviews all
  PASS and the user's literal `APPROVE EXECUTE <packet_id>` in the operator channel, exactly
  once, by Tori. This report executes no DB writes.

## 4. Kun brief (for Tori to dispatch verbatim)

> KUN WAVE2 BOUNDARY CLOSURE — 20260706T002104Z. Read
> `docs/hwao_overnight_pinning_wave2_20260705T1615Z/` (PINS_WAVE2.jsonl, FETCH_LOG, manifest,
> LANA_WAVE2_ADEQUACY.md, GORU_WAVE2_COUNTS.md). Deliver into that dir:
> (1) `pinning_wave2_checker.py` — deterministic, read-only: reparse ledger, recompute source
> sha256s, assert text[char_start:char_end]==quote for all 5 pins, assert no claim-2929 rows,
> assert role/stance copied verbatim (no neutral/none→support), scan wave2 + dbprep dirs for
> SQL/apply/rollback/migration artifacts (expect 0);
> (2) `CHECKER_RESULT.md` with PASS/FAIL and counts;
> (3) `KUN_WAVE2_BOUNDARY.md` — boundary verdict incl. fetch cap compliance (exactly 3 fetched +
> 2 copied), git read-only custody, zero mutation artifacts.
> Locks: docs-only/read-only; no DB writes; no git mutation; no fetching. If any assertion
> fails: write DIVERGENCE_REPORT.md, freeze the failing item, do not self-heal.
> Marker: `KUN_WAVE2_BOUNDARY_CLOSED_20260706T002104Z`.

## 5. Saved briefs for Tori to write/dispatch

1. `.hermes/handoffs/autonomy_continue_20260706T002104Z/KUN_WAVE2_BOUNDARY_BRIEF.md` — §4 text.
2. `.hermes/handoffs/autonomy_continue_20260706T002104Z/LANA_DISPOSITION_ROUTES_BRIEF.md` —
   Lana item (1) from §2, with the 14-row table copied in and pointers to the fetched
   `2604.15438` text and the disposition spec.
3. `.hermes/handoffs/autonomy_continue_20260706T002104Z/DEBATE_MAP_REFRESH_BRIEF.md` — Track C:
   Goru mechanical layer first (read-only extracts via Tori), Lana science layer on top, Kun
   checker replication over the map data, Hwao synthesis; run dir
   `docs/hwao_debate_map_refresh_20260706T002104Z/`; baseline diff against
   `docs/baseline_step6_status_debate_map_20260703T0954Z/`; docs-only locks restated.
4. `.hermes/handoffs/autonomy_continue_20260706T002104Z/TORI_DEDUPE_PACKET_GEN_BRIEF.md` —
   gated generation task per §2/§3(b): prerequisites, spec path, packet dir pattern, validator
   requirement, packet id kept out of public cockpit, marker
   `DEDUPE_PACKET_PREPARED_NOT_APPROVED_<ts>`.

## 6. Cockpit/status wording for Tori

> Night shift, part 3: the five new source pins passed independent validation (Kun's re-runnable
> check is being added now). Next up while you sleep: refreshing the research-status/debate map
> against the July-3 baseline, completing science recommendations for the 14 leftover rows on
> retired claim 2929, and preparing — on paper, validator-checked, **not** approved and **not**
> executable without your explicit phrase — the small duplicate-evidence cleanup packet for
> claim 2931. Nothing in the database, wiki, git, or services is being changed. Active execution
> phrase: NONE.

## 7. Marker

HWAO_NEXT_DIRECTION_20260706T002104Z
