# Handover — night of 2026-08-14

## State

The preregistration is **FROZEN, accepted by Duho, committed, pushed, and merged to main**.
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260814.md` — SHA-256
  `da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308` (read-only, 444)
- Freeze record: `PREREG_FREEZE_RECORD_20260814.md`
- Merged as `dc85980460ce` via PR #144; branch `feat/paper-workflow-v2`.

Ten binding slots: nine pass, **BS-1's licence limb failed and stays failed**. The output was
redesigned to need no derived catalogue rather than the permission being obtained. BS-11 (release
linter) added and filled.

**BS-5 synthetic absolute-sign anchor: PASS**, 32/32 both directions, no correction, convention
unchanged. Gated by Kun (`KUN_BS5_ANCHOR_GATE_20260814.md`).

## Built tonight, not yet gated

- `acquisition/` — cutout pipeline. **Build only; it has no network client at all** (AST-audited;
  `MockTransport` is the only `fetch` implementation). 14/14 tests, all three negative fixtures fire.
- `handcheck/` — blinded hand-check harness. 29/29 self-test checks on a full synthetic 500,
  plus an independent verifier at 33/33 that never imports the production module.

## Next steps, in order

1. Yui's `YUI_HANDCHECK_HARNESS_20260814.md` design doc (was in progress at 23:11).
2. Kun gates both builds. **Do not dispatch him until Yui's doc lands** — gating a moving target
   produces a receipt for a version that no longer exists.
3. Then the run, which is blocked on people, not code: HC-1..HC-5 needs **two independent checkers
   plus a third adjudicator** hand-classifying 500 blinded galaxies. `a < 0.85` overall or any
   stratum < 0.70 → INCONCLUSIVE-BY-POWER, no run.

## The line that still holds

The STOP rule is absolute and unlifted in practice: no real cutout has been fetched, no sky
statistic computed, K-8 not tripped. Duho authorised "run it"; the run could not start because the
tools did not exist. They exist now — running them is still his call.

## Morning video (built 2026-08-15 ~01:00)

`/Users/duhokim/HermesOps/cockpit/videos/status_20260815_prereg/where_the_work_stands_20260815.mp4`
3m 06s, narrated, 12 cards, every number verified against a cited receipt. Not uploaded.
Covers: the claim being tested, why it was frozen first, the licence failure and the output
redesign, the 32/32 sign anchor, and that the remaining step needs a human. Ends on the STOP rule.

---

## Overnight, 01:00–01:30

**HC-1H is CLEAN and ACCEPTED.**
- Kun: `PASS_HC1H_CLOSE_ON_EXACT_HASH` (`KUN_HC1H_CLOSE_20260814.md`, 01:05)
- Duho accepted 01:08, verbatim *"accept it, and run autonomously for rest of tonight"*
  → `HC1H_ACCEPTANCE_20260815.md`
- accepted artifact: `LANA_ONE_HUMAN_ATTENUATION_20260814.md`
  `b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd`

It took four revisions. Errors the gate chain caught: a power break-even wrong by 0.08 in `a`; a
variance formula understating sigma 3x; a pilot carry-forward that was selection-then-reuse bias; an
unenforced blinding assumption. **One relay failure was mine** — Kun's re-gate listed three required
repairs and I passed on two, having read only part of that document.

**Also gated:** Tori's acquisition pipeline — `PASS_ACQUISITION_BUILD_ONLY_GATE`
(`KUN_ACQUISITION_GATE_20260814.md`). Kun verified the no-network claim from the source himself:
the module imports no HTTP library at all; the single URL constant only builds a request record.

**In flight at 01:30**
- v2 preregistration candidate `PREREG_LONGO_AMPLITUDE_TEST_20260815_CANDIDATE.md`
  (`6ae6a58cd6d29511…`, 406 lines) — with Kun for gating
- Yui reworking the hand-check harness for HC-1H (it was built to the superseded HC-1 spec:
  wrong strata, no synthetic injections, no mirrored repeats, no HC-7 UI)

**Integrity:** the 08-14 frozen preregistration is untouched — `da2c6a21d994b9af…`, perms `444`.

**Waiting on Duho, in order**
1. Nothing yet — v2 is still gating. If it passes, it is frozen overnight per his authorisation.
2. **Pilot (150 labels) or full (850)** — §2b of the HC-1H document; this is his choice and nothing
   proceeds without it.
3. Authorising the acquisition run. Still the STOP-rule crossing.

**Not done, deliberately:** nothing pushed, published, or run against sky. No real galaxy touched.
K-8 untripped. Morning video: `/Users/duhokim/HermesOps/cockpit/videos/status_20260815_prereg/`.
