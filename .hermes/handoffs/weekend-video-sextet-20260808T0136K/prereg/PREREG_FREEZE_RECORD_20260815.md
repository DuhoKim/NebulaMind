# PREREGISTRATION FREEZE RECORD v2 — HC-1H incorporated

**Frozen:** 2026-08-15 03:21 KST
**Authorised by:** Duho Kim, verbatim: *"accept it, and run autonomously for rest of tonight"* (01:08 KST)
**Executed by:** Hwao (coordinator), under that standing authorisation, while Duho slept.

## What is frozen

`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815.md`
SHA-256 `62dad44dd92acf2781d2c8cf25161f7f344e3fe6f7fec35b7e04308bd1539c12`
Byte-identical to the candidate Kun gated; chmod 444 at freeze.

## What changed from v1

HC-1…HC-6 replaced by **HC-1H**: one human checker, 850 blinded labels (500 real, 200 blind synthetic
ground-truth injections, 150 mirrored re-presentations), nine strata = machine-committee state × |χ|
tertile, Neyman allocation, floor 30 real per stratum. The machine committee is stratifier /
allocator / diagnostic **only, never inside `a`**. HC-7 gains clause (v), synthetic/repeat identity
exposure, as a hard INCONCLUSIVE trigger. `a_gate = 0.7905`; the 0.85 quality floor binds separately.
Optional §2b pilot (150 labels) returns only PASS-TO-FULL-HC1H or INCONCLUSIVE.

## Supersession chain

| Document | SHA-256 | Status |
|---|---|---|
| `PREREG_LONGO_AMPLITUDE_TEST_20260812.md` | `ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590` | superseded draft, preserved |
| `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260814.md` | `da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308` | superseded freeze, preserved, mode 444, verified intact at freeze time |
| `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815.md` | `62dad44dd92acf2781d2c8cf25161f7f344e3fe6f7fec35b7e04308bd1539c12` | **this freeze** |

## Gate chain

`KUN_ONE_HUMAN_ADVERSARY` (sealed before reading Lana) → `KUN_HC1H_GATE` (five repairs) →
`KUN_HC1H_RECONFIRM` (two statistical repairs + HC-7) → `KUN_HC1H_FINAL` → `KUN_HC1H_CLOSE`
(PASS on exact hash) → Duho accepts → `KUN_V2_PREREG_GATE` (HOLD, two metadata repairs) →
`KUN_V2_PREREG_GATE2` (**PASS_V2_FREEZE_CLEAR_ON_EXACT_HASH**).

Also gated tonight: `KUN_ACQUISITION_GATE_20260814.md` — **PASS_ACQUISITION_BUILD_ONLY_GATE**.

## BS-1 remains FAILED

The licence limb failed and was **rewritten, not marked passed**. The permission was never obtained;
the output was redesigned so it is not required. Nothing in this freeze reverses that.

## K-8 timing attestation

**No real-sky statistic exists anywhere in this program at freeze time.** No real cutout has been
fetched. The amendment is therefore made at the only safe point — before the run.

## What this freeze does NOT authorise

No sky run · no publication · no derived-catalogue release · **no push**. The STOP rule stands. Every
future public release must pass the pinned linter against the cumulative registry.
