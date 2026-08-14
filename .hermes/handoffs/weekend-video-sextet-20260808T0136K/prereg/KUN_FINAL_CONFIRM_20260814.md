# KUN_FINAL_CONFIRM_20260814

Timestamp: 2026-08-14 KST

Brief: `prereg/_tmp_KUN_FINAL_CONFIRM_BRIEF.md`

Boundary: documentation/gate only. I did not inspect sky data, rows, positions, images,
chirality labels, or sky statistics. I did not freeze, publish, accept, commit, or push anything.
Duho owns acceptance.

## Exact Hashes Confirmed

- `prereg/PREREG_LONGO_AMPLITUDE_TEST_20260814_CANDIDATE.md` —
  `da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308`
- preserved 08-12 draft, `prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md` —
  `ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590`
- `prereg/release_linter/nm_release_lint.py` —
  `7ff18bfc9272bcbb924b77cb81f2b37c45a130c2b1c5ba1fbc9b95baaab323ac`
- `prereg/release_linter/SELFTEST.md` —
  `c23bed0d42865961bba1240dbcb52fb496281d044afa766a64c6a07253f66706`
- `prereg/release_linter/test_nm_release_lint.py` —
  `4316567c26b68296fcc870534dea66b56f34cf5167bc78e16b11576d8bf309cb`
- `prereg/release_linter/YUI_RELEASE_LINTER_20260814.md` —
  `1c47e8d9c4b4c1ff1af0ebb29d97c2b39c8a22d8e45b2342df32ecd67e07b29b`

## Verification

I reran:

- `python3 prereg/release_linter/nm_release_lint.py --self-test`
  - `PASS_SYNTHETIC_SELFTEST`
  - `fixtures=22/22`
- from `prereg/release_linter`: `python3 -m unittest test_nm_release_lint.py`
  - `36` tests run
  - `OK`

## Verdict

**PASS_FINAL_CONFIRM_ON_EXACT_HASH.**

The three text repairs I required in `KUN_AMENDMENT_GATE_20260814.md` have landed in substance, not
only in wording:

1. **BS-11 is filled.** It is no longer marked OPEN. The binding-slot row carries the pinned linter
   hash, self-test requirement, 36-unit-test requirement, failure rule, and the four validity-range
   limits, including cumulative-context-only.
2. **The cumulative-release policy is binding in the preregistration.** F-10.f now states that every
   future public release, correction, supplement, figure-data package, video data appendix, or
   replacement package must be linted against the cumulative release-history registry, and that an
   isolated-package ACCEPT is insufficient for publication. A missing, stale, or unconsulted
   registry is a release HOLD.
3. **Machine limits are assigned to human custody.** F-10.i assigns manifest truth to the release
   steward/custody seat, historical freeze-attestation truth to the freeze steward with Kun
   confirmation at release gates, and scientific/legal claim scope to the science/claim seat. F-10.f
   also carries the honest ACCEPT semantics: linter ACCEPT means only that no implemented
   deterministic release rule fired on the exact hash-pinned cumulative package supplied to it.

The stale phrases I found are not live defects: old HOLD language appears only in the provenance
chain, and the old "licence permits derived-catalogue publication" phrase appears only inside the
explicit record that old BS-1 failed and stays failed as written.

## Freeze Blocker Status

I see **no remaining blocker from my amendment gate** on the exact candidate hash
`da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308`.

Safe statement to Duho:

> Kun passes the amended preregistration candidate on exact hash. The rewritten aggregate-only
> output boundary and BS-11 linter gate are now internally consistent and ready for Duho's
> acceptance decision. This PASS is not itself a freeze, run, publication, or acceptance.
