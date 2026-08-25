# TRIO OVERNIGHT REPORT — DESI HALF (Hwao draft, for Goru cross-check)

Hwao, 2026-08-25 10:55 KST. Every number below carries its evidence class and receipt path.
Goru: check each MEASURED number against its named receipt; anything you cannot reproduce is
a CATCH, and catches go in the published report.

## Plain-language lead (for the merged report's opening)

The night settled two things on the DESI side: the sky-image download finished and every one
of its 60,308 files is verified against the producer's own checksum list; and the successor
test's rulebook survived four adversarial review rounds by becoming executable code, leaving
a thirteen-item build list rather than any open design question. One seam surfaced this
morning: two galaxies of the 208,407 sit so far south that a brick their cutouts need was
never in the download plan — diagnosed, documented, not a data loss.

## 1. Transfer completion (MEASURED)

- Final receipt of stream A: 2026-08-24T11:30:13Z = **20:30:13 KST**; first completion check
  ran **20:35 KST** (`prereg/_sharded_20260823/COMPLETION_CHECK_20260824T2035K.out`, 444).
- Shards: **A 44,135 + B 8,086 + C 8,087 = 60,308** bricks
  (TRANSFER_COMPLETE.json in each root: dr10_south_image_r, dr10_shardB, dr10_shardC).
- Bytes: **541,807,623,468 + 97,845,831,360 + 96,208,853,760 = 735,862,308,588**
  (~735.9 GB) under the combined ceiling **922,388,644,983** (same three files).
- Quarantine: **0** in all three roots (completion check line "quarantine empty: 0").
- Merge 20:31–20:34 KST: pairwise path-collision counts **0/0/0**; merged receipts.jsonl =
  **60,314 lines, 60,308 ACCEPTED, 6 non-ACCEPTED provenance lines**
  (`prereg/_sharded_20260823/MERGE_RECORD_20260824.out`, 18 print-and-eval claims, 444).
- Reboot 2026-08-24 ~17:50 KST at 97.2%: ~50 min lost, **6 debris items archived
  digest-first** (`prereg/_sharded_20260823/REBOOT_DEBRIS_20260824.json`), 0 bytes lost.

## 2. Producer cross-check (MEASURED)

**accepted 60,308 · match 60,308 · problem 0** against Dustin Lang's 330,618-entry r-band
checksum list (task #26 final run inside completion_check.py 20:35 KST; re-run 10:42 KST this
morning, same result — `_dustin_list_20260822/crosscheck.py`, exit 0).

## 3. Cutter / chi drain — where it stands NOW (MEASURED; heartbeat stamps corrected per Goru)

- `cutouts_dr10_south/wrapper_heartbeat.json` (stamp 01:44:25Z = 10:44 KST): ready
  **208,405**, resolved **208,405**, batch **0**. `chi_dr10_south/chi_heartbeat.json`
  (stamp 02:00:16Z = 11:00 KST): measured **208,405** == tensors **208,405**. The drain
  leveled at 208,405 by ~10:30 KST and the wrappers' periodic heartbeats have re-stamped
  the same numbers since (Goru catch: my draft's "10:30 KST heartbeats" label was stale;
  the counts were and are exact).
- Completion check 10:42 KST: **4 of 5 legs PASS** (acquisition, quarantine, producer
  cross-check, chi==tensors). The failing leg wants cutter receipts ≥ 208,407.
- **The 2-object gap, diagnosed this morning (MEASURED end to end):**
  ls_id **10997315463551936** (ra 341.7456, dec **−88.5916**) plans bricks
  {3385m885, **3471m885**}; ls_id **10995116744378804** (ra 288.4480, dec **−87.1321**)
  plans {2857m870, 2894m872, 2902m870} — planner replay via
  `_objmanifest_20260820/build_object_manifest.py` this morning. The bolded bricks
  **3471m885 and 2857m870 are in the DR10 release** (both present in Dustin's dr10-r.txt,
  grep count 2) but were **never in the frozen 60,308-brick image manifest** — the parent
  needs 60,310 bricks. The cutter held both objects WAITING (fail-closed, by design), so no
  receipt of any kind exists for them. Not a transfer failure (transfer delivered its
  manifest 100.000%), not a cutter failure. Options recorded: documented shortfall
  (recommended while the decline decision is open) or a gated 2-brick manifest amendment
  (~30 MB).

## 4. Successor build (gate-state discipline: verdict lines quoted, nothing stronger)

- Five draft versions (V1–V5) and **ten adversarial gate reports** overnight, two engines
  (gpt-5.6-sol, codex). Every verdict line reads **REFUSED** — no PASS is claimed for any
  version. What each report's own "attacks that held" sections affirm (ASSERTED by the gate
  reports, files in `prereg/_successor_build_20260824/gates/`): axis vector correct to
  ≤4.4e-16 per component; quotation fidelity against the frozen predecessor; the decision
  partition exhaustive; the Clopper–Pearson pass integer x ≥ 962 of 1,000 correct; and —
  round 4, both gates — the pinned fixture output of the reference implementation
  **reproduced byte-for-byte** on their independent runs.
- Defects the rounds killed (each from a gate report's numbered finding): comparing the
  attenuated slope (×0.7 at the 0.85 labelling floor) against the undiluted 0.0408 target; a
  p < 0.001 threshold mathematically unreachable at 999 permutations (our old validator had
  been passing on that impossibility); two "blind-double" implementations using axes
  **3.72 arcminutes apart**; three brute-force selector counterexamples (worst ratio
  22,201×); a raw-vs-retained leverage seam that could admit a below-threshold sample.
- Structure now: constitution `PREREG_SUCCESSOR_DRAFT_V5_20260824.md` (sha 1c283bbf…) +
  reference implementation `ref/successor_ref.py` (sha 67bc4876…) declared THE definition,
  fixtures `ref/FIXTURES_20260824.out` (sha c82b2a25…, ALL FIXTURES PASS, contains all five
  gate counterexamples). Remaining work: **13-item build list**
  (`BUILD_LIST_V6_20260825.md`), every item carrying a gate-stated acceptance test; then V6,
  one more gate round, then the freeze candidate goes to Duho.
- Also MEASURED tonight: DR11 photo-z still absent from the public DR11 pages → the Sep 5
  DR10.1 fallback rule stands.

## Open on Duho's desk (unchanged)

Decline memo Rev 6 (DRAFT, unsigned — its banner line 5 is the gate-state truth); DR11 vs
DR10.1 by Sep 5; successor freeze signature comes only after a V6 PASS, which has not
happened.
