# HC-1H acceptance record

**Accepted:** 2026-08-15 01:08 KST
**Authorised by:** Duho Kim, verbatim: *"accept it, and run autonomously for rest of tonight"*
**Accepted artifact:** `LANA_ONE_HUMAN_ATTENUATION_20260814.md`
SHA-256 `b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd`

## What is accepted

HC-1H replaces HC-1…HC-6: **one human checker (Duho), 850 blinded labels** — 500 real, 200 blind
synthetic ground-truth injections, 150 mirrored re-presentations. Nine strata = machine-committee
state x |chi| tertile, Neyman allocation, floor 30 real per stratum. The machine committee is
stratifier / allocator / diagnostic **only, never inside `a`**. Optional §2b pilot (150 labels) may
return only PASS-TO-FULL-HC1H or INCONCLUSIVE.

## Gate chain

| Gate | Result |
|---|---|
| `KUN_ONE_HUMAN_ADVERSARY_20260814.md` | sealed independent position, written before reading Lana |
| `KUN_HC1H_GATE_20260814.md` | PASS WITH REQUIRED REPAIRS (five) |
| `KUN_HC1H_RECONFIRM_20260814.md` | HOLD — two statistical repairs + HC-7 trigger |
| `KUN_HC1H_FINAL_20260814.md` | statistical repairs PASS; HC-7 still open |
| `KUN_HC1H_CLOSE_20260814.md` | **PASS_HC1H_CLOSE_ON_EXACT_HASH** |

Errors caught by that chain, for the record: a power break-even wrong by 0.08 in `a`; a variance
formula understating sigma threefold; a pilot carry-forward that was selection-then-reuse bias; an
unenforced blinding assumption. One relay failure was mine — Kun's re-gate listed three required
repairs and I passed on two.

## What this acceptance does NOT authorise

No sky run. No real image fetched. No publication. No push. **The STOP rule stands**: the moment the
next step would touch real galaxies, the lane stops and reports that as the successful outcome.
K-8 remains untripped — no real-sky statistic exists anywhere in this program.

Next: the frozen preregistration is amended to incorporate HC-1H, gated, and re-frozen. That
amendment is a separate act from this acceptance.
