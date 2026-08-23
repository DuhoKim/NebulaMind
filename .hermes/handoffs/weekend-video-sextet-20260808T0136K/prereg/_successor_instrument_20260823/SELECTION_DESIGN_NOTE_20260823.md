# Successor selection design — the leverage table

Hwao, 2026-08-23 20:47 KST. Inputs are custody-verified lane artifacts (brick centres sidecar 863e5ded…, per-brick
Cut-6 counts 4e4ec45d…); axis is Longo's frozen (216.984434295527, +32.060611193471). Rerun:
`python3 selection_leverage.py` — output archived beside it.

## The table (count-weighted, brick centres; N_eq = 3·N·Var)

| strategy | bricks | N_cut6 | Var(c) | N_eq |
|---|---:|---:|---:|---:|
| FULL footprint | 270,577 | 832,393 | 0.4452 | 1,111,747 |
| DEAD-RULE brickid≤121000 | 55,297 | 171,737 | 0.0577 | 29,707 |
| POLAR top 10% of objects | 28,182 | 83,241 | 0.9204 | 229,849 |
| **POLAR top 25%** | **69,580** | **208,100** | **0.8209** | **512,481** |
| POLAR top 50% | 136,604 | 416,197 | 0.6886 | 859,725 |
| EQUATOR worst 25% | 68,474 | 208,099 | 0.0790 | 49,344 |

Three facts for the successor prereg:

1. **Same N, 17× the leverage.** Polar-|cosθ| selection of 208,100 objects yields N_eq 512,481;
   the dead rule's 208k yielded 29,707. Selection strategy, not sample size, was the failure.
2. **The dead rule is reproduced independently here** (Var 0.0577 at Cut-6 vs 0.0580 measured on
   the Cut-5 parent) — this table required nothing that was not in the lane in mid-August.
3. **A leverage-based successor is CHEAPER than the dead run**: at 45% acceptance, ~28,000 bricks
   (roughly half the current transfer's brick count) already clears the frozen 100,000-N_eq
   requirement; at 25% acceptance, ~52,000 bricks.

## Caveats, stated

Brick-centre approximation (±0.0124-class bracket per the variance receipt's own argument);
Cut-6 counts, not accepted counts — acceptance re-tilts weights (the audit's warning); DR10.1
geometry — DR11's footprint differs and its table needs its own sidecar once its parent exists.
Selection ON |cosθ| is selection on position only, which preserves label exchangeability
(sign-independent), per the re-gate's exchangeability ruling.
