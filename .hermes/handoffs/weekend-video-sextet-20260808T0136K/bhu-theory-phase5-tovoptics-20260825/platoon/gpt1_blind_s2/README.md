# GPT1 blind S2: kinematic shock-crossing temperature pattern

## Scope and blindness

This is an independent calculation from `BRIEF_GPT1_BLIND_S2.md` and the gated Phase-4 orbit only. I did not read or use `s2_transfer.py`, `S2_RECEIPT.md`, `S1_RECEIPT.md`, or `s1_crossing_shift.py`.

Files:

- `compute_blind_s2.py`: calculation and checks
- `s2_kinematic_pattern.csv`: requested numerical results

Run with:

```bash
python3 compute_blind_s2.py
```

## Assumptions and conventions

1. Units are those of the brief: `t_crit=1`, `eta=2 sqrt(t)`, and the observer epoch is `eta_obs=2`.
2. The final gated orbit row is at `t/t_crit=0.999999985`, only `1.5e-8` below the requested epoch. I use its `sqrtN=1.000000005` as the endpoint value, giving `r_*(t_obs)=2.00000001`.
3. `sqrtN(t)` is linearly interpolated in `log(t)`. Every reported crossing lies well inside the gated time interval.
4. The sight direction `n` points from the observer into the past/out toward the viewed sky. The photon propagates inward along `-n` after crossing.
5. The shock normal is the outward radial unit vector

   `m = (x_off e_z + chi n) / r_*`,

   so the projection used in the Doppler factor is

   `q = n dot m = (chi + x_off mu) / r_*`.

6. I take the exterior/TOV fluid to be static relative to the centre while the FRW fluid expands outward. Thus, in the local FRW frame, the TOV fluid velocity is `v_TOV=-beta m`, where `beta=1/sqrtN` at crossing. For temperature/frequency transferred from TOV to FRW,

   `D = T_FRW/T_TOV = nu_FRW/nu_TOV = 1/[gamma (1-beta q)]`,

   and the reported kinematic shift is `Delta T/T = D-1`. This fixes the otherwise sign-ambiguous phrase “relative speed” in the brief. Reversing which fluid is assigned the outward velocity reverses the leading (order-beta) sign and is a different frame convention.
7. Only the local special-relativistic kinematic jump is included. No intrinsic, gravitational, integrated, optical-depth, or scattering contribution is included.

## Crossing-region geometry

For all four requested offsets, every sky direction has exactly one shock crossing on the gated past light cone. At the observer, the ray is inside the shock, so the crossing function is negative. At the earliest gated conformal time it is positive even in the least favorable direction. The smallest endpoint margins are listed in the CSV and remain positive; the smallest is `0.74843617275` for `x_off/r_*=0.1`.

Therefore the crossing region is the entire sky (`4 pi` steradians). Expressed as a cap centered on the outward offset axis, its angular radius is 180 degrees. “Centre” below means `theta=0` (`mu=+1`, outward offset direction), and “edge” means the antipode `theta=180 degrees` (`mu=-1`).

## Results

| x_off/r_* | angular radius | Delta T/T range | centre | edge |
|---:|---:|---:|---:|---:|
| 0.001 | 180 deg (full sky) | [0.512100174, 0.514692690] | 0.514692690 | 0.512100174 |
| 0.01 | 180 deg (full sky) | [0.500503067, 0.526429577] | 0.526429577 | 0.500503067 |
| 0.05 | 180 deg (full sky) | [0.450261589, 0.580066110] | 0.580066110 | 0.450261589 |
| 0.1 | 180 deg (full sky) | [0.390162979, 0.650854770] | 0.650854770 | 0.390162979 |

The pattern is axisymmetric and monotone across each of these cases: maximum at the outward-axis centre and minimum at the antipodal edge. The different centre/edge values arise primarily because those rays cross at different epochs and hence different `beta`; the CSV records the crossing times and speeds.

The maximum requested magnitude is

`max |Delta T/T| = 0.650854770294`.

Compared with the observed CMB anisotropy amplitude `~1e-5`, this is larger by a factor

`6.50855e4`,

or about 4.81 orders of magnitude (roughly five orders). Thus the unattenuated local kinematic step is not a `1e-5`-scale effect.

## Limiting-case and numerical checks

- **Centered observer / isotropy:** setting `x_off=0` at `mu=-1,-0.5,0,0.5,1` gives exactly zero numerical spread in `Delta T/T`; all have `q=1`. The common value is `0.513395725020`.
- **Radial geometry:** at both requested radial axes the crossing normal and sight direction are parallel (`q=1`) after the inward-axis ray has passed the centre, as expected.
- **Root existence and uniqueness:** a 2,001-point conformal-time scan for five representative `mu` values in each of the four offset cases found exactly one sign change in every ray.
- **Equation residual:** the maximum absolute residual of `|x_off+chi n|-r_*(eta)` over those representative solved crossings is `6.66e-16`.
- **Doppler small-speed limit:** direct evaluation at `beta=1e-8` gives `Delta T/T -> beta q` for `q=-1,0,+1`, as required by the adopted velocity convention.
- **Angular-extremum check:** each pattern was sampled at 20,001 angles; candidate extrema were then refined by golden-section search. All extrema landed at the endpoints (`0` and `180` degrees).
