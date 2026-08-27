# P10 Receipt: Flatness re-measurement

## What was measured
The shape-versus-opacity relationship at `w = 0.2456` over six decades of the opacity multiplier `K`. Following instructions, the off-centre fraction was explicitly set to `x/R = 1e-3`. Both the ratio `R(+1)/R(-1)` and the signed normalised dipole coefficient `signed_c1` were measured. 

## Table

| K | R(+1)/R(-1) | 1-R | signed_c1 | status |
|---|---|---|---|---|
| 1e-02 | 0.997726210 | 0.002273790 | -0.522935 | resolved |
| 1e-01 | 0.997729299 | 0.002270701 | -0.521387 | resolved |
| 1e+00 | 0.997759674 | 0.002240326 | -0.506165 | resolved |
| 1e+01 | 0.998017645 | 0.001982355 | -0.376907 | resolved |
| 1e+02 | 0.998857603 | 0.001142397 | 0.043729 | resolved |
| 1e+03 | 0.999138560 | 0.000861440 | 0.184349 | resolved |

## Anchors

- **Reproduced**: The `R(+1)/R(-1)` anchors reproduced exactly at both K=0.01 (0.997726210) and K=100 (0.998857603).
- **Did not reproduce**: The `signed_c1` anchors did not reproduce perfectly. At K=0.01 I got -0.522935 (expected -0.522912), and at K=100 I got +0.043729 (expected +0.043763).

**Assumption/Note**: The discrepancy is because I obeyed the explicit instruction to evaluate `c1` at `x/R = 1e-3`. The anchor numbers for `c1` were likely measured by the gate using the `p8_thick_limit.py` default `f = 1e-4` (which my tests confirm gives exactly -0.522912 and +0.043763). I chose to follow the requested 1e-3 parameter rather than tuning `f` to match the anchors, hence the reported check failures.

## Resolution Limit

At `w = 0.2456`, the grid resolves the photosphere up to a maximum multiplier of **K_MAX = 2935** (where max per-cell `dtau = 1`). Since the sweep stops at K=1e3, all rows remained resolved.

## Execution

- **Command**: `python3 p10_flatness_redo.py`
- **Exit code**: `1` (due to the expected `c1` anchor check failures described above).
