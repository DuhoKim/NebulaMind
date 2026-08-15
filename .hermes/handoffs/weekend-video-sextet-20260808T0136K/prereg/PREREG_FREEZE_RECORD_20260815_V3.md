# PREREGISTRATION FREEZE RECORD v3 — PC-1 input contract repaired

**Frozen:** 2026-08-15 20:42:35 KST
**Authorised by:** Duho Kim, verbatim: *"freeze it"*
**Executed by:** Hwao (coordinator).

## What is frozen

`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
SHA-256 `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`, mode 444.
Byte-identical to the candidate Kun gated **PASS_V3_FREEZE_CLEAR_ON_EXACT_HASH**.

## What changed from v2

**PC-1's input contract was wrong.** The route binding froze `size=256`, `bands=grz`; the estimator
appendix froze a single-channel 128x128 ResNet-18. The route specified twelve times more pixel data
than the instrument consumes, and **the reduction from three 256² planes to one 128² tensor was
never frozen anywhere** — an undefined step sitting where the custody chain must be tightest.

v3 fixes the contract to **128x128, single band r, float32**, with band, FITS plane/HDU,
nanomaggy-to-tensor conversion, background treatment, invalid-pixel rule, clipping/scaling, byte
order, memory layout and mirror point all frozen on synthetics only.

**Why one band, and why r.** Chirality is parity-odd; pixelwise colour is parity-even — a mirror
reverses spatial index and preserves every per-pixel band value, so colour cannot carry the sign,
only sensitivity. Kun's ruling: *"It is not a separate parity-odd sign channel."* Band choice
therefore costs power, which HC-1H measures and HC-6 gates, never bias. r is chosen for sitting at
neither extreme of the position-correlated systematics — extinction sensitivity g > r > z, sky
variation z > r > g — while retaining arm contrast. The r-band guarantee rests on the study's own
frozen `flux_r > 0` and `dered_mag_r < 17.7` cuts, verified in three independent places.

## Supersession chain

| Document | SHA-256 | Status |
|---|---|---|
| `PREREG_LONGO_AMPLITUDE_TEST_20260812.md` | `ac43490054b159610385b8fa…` | superseded draft, preserved |
| `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260814.md` | `da2c6a21d994b9af7395347b…` | superseded, preserved, 444 |
| `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815.md` | `62dad44dd92acf2781d2c8cf…` | superseded, preserved, 444, verified intact at freeze |
| `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` | `b06901c8a0f3a0570af41262…` | **this freeze** |

## Gate chain

Tori acquisition strategy + Goru access facts (independent, no contact) → `KUN_STRATEGY_GATE`
(PASS_WITH_REPAIRS, HOLD EXECUTION) → Duho approves the amendment direction → Lana PC-1 amendment →
`KUN_PC1_AMENDMENT_GATE` (parity argument held; `[VERIFY]` fills a blocker) → fills from primary
sources, **one claim corrected** → v3 candidate → `KUN_V3_FREEZE_GATE` (HOLD, GZ DECaLS rationale
over-claimed) → repair → **`KUN_V3_REGATE` PASS on exact hash**.

The GZ DECaLS rationale took four passes: written from memory, factually wrong about the imagery,
over-claimed as "every parent", then bounded to our own frozen cuts. Recorded because the receipt
chain should show why, not just that.

## BS-1 remains FAILED

The licence limb failed and was rewritten, not marked passed. Nothing here reverses that.

## K-8 timing attestation

**No real-sky statistic exists anywhere in this program.** No cutout has been fetched; no transport
exists; `BUILD_ONLY_STOP` is intact. This amendment is made at the only safe point — before the run.

## What this freeze does NOT authorise

**It fixes the input contract, not the delivery route.** The acquisition channel is unresolved: the
survey discourages bulk automated cutout use and asks large jobs to use Globus, and an operator query
awaits Duho. `HOLD EXECUTION` stands. Binding prerequisites to any sky access, carried in v3:
Tori's successor route binding; Yui's hash-pinned input-function receipt **with the R1–R5 /
retention / calibration rerun through that exact function**; PC-3/PC-4 re-gated if cutting moves
local; and `nm_acquire_cutouts.py` forbidden from executing while it hardcodes `grz`, `256`,
`[3, 256, 256]`.

No sky run, publication, catalogue release, commit or push follows from this freeze.
