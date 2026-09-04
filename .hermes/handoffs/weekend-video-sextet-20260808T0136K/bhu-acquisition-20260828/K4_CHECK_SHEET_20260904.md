# K4 — one-page check sheet

**Tori, 2026-09-04 13:30 KST.** For a human checking this without redoing it. Every line carries a source line or an
executed-output line. Run any script below with `python3` from this directory.

## The question
Does a genuine causal boundary — K2's derived comoving junction — change the large-angle CMB when imposed on the
**perturbations**, not just the background?

## The answer in one line
**We cannot tell, and the reason is the model's, not ours: the junction does not determine the interior modes.**

## Why, in four steps

| step | what | receipt |
|---|---|---|
| 1 | the junction is **not** F1 (monopole-only) and **not** F2 (kills the spectrum) — all four seats agree | `K4_limb2_claude.out` `FINDING_NOT_F1=True`/`FINDING_NOT_F2=True`; `K4_limb2_codex.out` `F1_COMPARISON=NO`/`F2_COMPARISON=NO`; `K4_route2_agy.out` §4 |
| 2 | so the a-priori kill (prereg §4 limb 2) **does not fire** | same |
| 3 | but for every `ℓ ≥ 2`, `m`, the Schwarzschild exterior keeps **free Zerilli data** — one free function of time per `(ℓ,m)` — that the junction does not fix | `K4_limb2_codex.out` `FREE_MODE=…`; `K4_route2_agy.out` §3; third seat §4 |
| 4 | so there is **no derived `C_ℓ`** to score, and no reason to open the map | third seat §5 |

## The one assumption that would close it
"**No incoming radiation from past null infinity**" makes the exterior response unique. It is the standard
astrophysical choice — **and it is an added physical assumption, not something the Darmois conditions give**
(third seat §1). The prereg forbids manufacturing it (§5 class 4, §9), so it was not made. That is the whole result.

## What did NOT happen, and must not be read as having happened
- **No Planck pixel was touched.** `K4_limb2_claude.out` prints `PLANCK_DATA_OPENED=no`; `K4_limb2_codex.out` prints
  `NO_PIXEL_INPUT=TRUE`.
- **Four of the six controls were NOT RUN** — `C1_NO_BOUNDARY_LCDM_ROW`, `C3_WINDOW_ROW_REPRODUCED`, `C4_SEATS_AGREE`,
  `C5_ESTIMATOR_C2_REPRODUCED` all belong to the half that was never reached. They are recorded as NOT RUN, not as
  passes. Only `C2_BACKGROUND_JUNCTION_K2` (satisfied by construction in every seat) and `C6_PREDICTION_BEFORE_DATA`
  (satisfied trivially: no map was opened) are claimed.
- **No tier, warrant token, standing or stamp moved.**

## Tori's own seat was wrong — read this before trusting the claude column
The claude seat filed `LIMB2_NOT_F1_F2`, arguing that "regularity at infinity and no incoming radiation fix the
exterior response uniquely". **That imported the very assumption the prereg forbids.** codex caught it blind, route 2
caught it blind by a third method, and the third seat ruled it an added assumption. The token is withdrawn; the filed
class is `K4_UNDETERMINED`. The seat's F1/F2 comparison stands.

## What it costs and what it buys
Ordered at 13:15, filed at 13:30 — about one seat-day of the ten to fourteen estimated, because the prereg put the
cheap limb first. The freedom map's structural residual (its L174–177) **does not close**, but it is sharper: the
obstruction is an underdetermination in the model, not an unfinished calculation.

## Receipts (sha256)
```
K4_BOUNDARY_TRANSFER_PREREG_20260904.md  7a5ad550f3044bbd0584b09e51595989deb121d2b20093bc50b36a8ef77f066c
K4_limb2_claude.py                       68a597b3cec148de573a8947120fb4368da1be7426bdce32ccb162494c7191a8
K4_limb2_claude.out                      9208b8fda18f7b92299996ca5bc16a88d77a3df80ee10453c315148947cee34a
K4_limb2_codex.py                        daba86f1809d422227befc07ec210b4655303ecc90102b8253e1029734a35af3
K4_limb2_codex.out                       aa8bb4e77f1a4473efa99be39941e3bff147e48e1594411a7afcbef55df4bb28
K4_route2_agy.py                         2b7343f4bb68cda45b58e8a981ca54da3c59a2fdbba12eebd550e10fc2a81d1c
K4_route2_agy.out                        05d222b3a1f157d581ad14c0515ef64d46b49a07a331b4ba264b26709a3b7fe2
```
Gate `K4_PREREG_GATE_20260904_agy.md`; seats `K4_LIMB2_codex_RESULT.md`, `K4_ROUTE2_20260904_agy.md`,
`K4_THIRD_SEAT_20260904_agy.md`. All dispatched through `nm_referee_dispatch.sh` with ACCESS_SHA proof.

K4_CHECK_SHEET_COMPLETE
