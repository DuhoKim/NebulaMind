# PREREGISTRATION FREEZE RECORD — Longo amplitude test

**Frozen:** 2026-08-14 19:26:34 KST (2026-08-14T10:26:34Z)
**Authorised by:** Duho Kim, verbatim: *"accept it and freeze"*
**Executed by:** Hwao (coordinator), on that instruction.

## What is frozen

`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260814.md`
SHA-256 `da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308`
Byte-identical to the candidate Kun gated; set read-only (`444`) at freeze time.

## Authority chain

| Step | Document | Result |
|---|---|---|
| Slot gate | `KUN_FINAL_GATE_20260814.md` | HOLD FREEZE — BS-1 licence FAIL, 9 slots pass |
| Redesign re-gate | `KUN_REDESIGN_REGATE_20260814.md` | PASS as direction; BS-1 must be rewritten, not marked passed |
| Amendment gate | `KUN_AMENDMENT_GATE_20260814.md` | PASS with three required text repairs |
| Final confirmation | `KUN_FINAL_CONFIRM_20260814.md` | **PASS_FINAL_CONFIRM_ON_EXACT_HASH** |
| Acceptance | this record | **Duho accepted** |

## Artifacts pinned at freeze (all verified on disk at freeze time)

| Artifact | SHA-256 |
|---|---|
| frozen preregistration | `da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308` |
| gated candidate (identical bytes) | `da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308` |
| superseded 2026-08-12 draft (preserved) | `ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590` |
| `release_linter/nm_release_lint.py` | `7ff18bfc9272bcbb924b77cb81f2b37c45a130c2b1c5ba1fbc9b95baaab323ac` |
| `release_linter/SELFTEST.md` | `c23bed0d42865961bba1240dbcb52fb496281d044afa766a64c6a07253f66706` |
| `release_linter/test_nm_release_lint.py` | `4316567c26b68296fcc870534dea66b56f34cf5167bc78e16b11576d8bf309cb` |
| `release_linter/YUI_RELEASE_LINTER_20260814.md` | `1c47e8d9c4b4c1ff1af0ebb29d97c2b39c8a22d8e45b2342df32ecd67e07b29b` |

Linter state at freeze: `PASS_SYNTHETIC_SELFTEST fixtures=22/22`; unit suite 36/36 OK.
Independently reverified by Kun before his final confirmation.

## Binding-slot outcome at freeze

BS-1 **licence limb FAILED as originally written** and was **rewritten**, not marked passed. The
original phrase `licence permits derived-catalogue publication` remains failed; the redesign removed
derived-catalogue publication from the output package rather than obtaining the permission.
BS-2 PASS (9/10 covariates; arm contrast dropped and published) · BS-3 PASS (identity 1,000/1,000
bit-exact) · BS-4 PASS with required near-total-abstention notice (production acceptance 16/12,000)
· BS-5 PASS (Longo sign quoted and mapped; synthetic sign anchor required before any real image) ·
BS-6 PASS · BS-7 PASS (FAIL_CLOSED branch) · BS-8 PASS with declared analytical-evaluation deviation
· BS-9 PASS (σ_ours 0.004805 ≤ 0.008; floor 0.014848 ≤ 0.025; holds at a = 0.85) · BS-10
informational · BS-11 FILLED (release linter).

## K-8 timing attestation

**No real-sky statistic has been computed anywhere in this program at freeze time.** The freeze is
therefore made at the only safe point: before any sky value exists. Any parameter change after a
real-sky statistic voids the run under K-8.

## What this freeze does NOT authorise

No sky run · no publication · no derived-catalogue release · no commit · no push · no acceptance of
any future artifact. The **STOP rule** stands: if work reaches the point where the next step is
touching real galaxies, the lane stops and reports that as the successful outcome.
Every future public release must pass the pinned linter against the **cumulative** release-history
registry (F-10.f); an isolated-package ACCEPT is insufficient for publication.

## Custody assigned at freeze (F-10.i)

Manifest truth — release steward. Historical freeze-attestation truth — freeze steward, with Kun
confirming at release gates. Scientific and legal claim scope — science/claim seat.
This record is the freeze attestation those roles refer back to.
