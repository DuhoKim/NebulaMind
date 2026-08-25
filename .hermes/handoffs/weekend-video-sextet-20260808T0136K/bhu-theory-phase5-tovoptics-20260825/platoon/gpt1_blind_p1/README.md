# Blind Phase 5b P1 result (gpt1)

## Scope and custody

This is an independent calculation from `BRIEF_GPT1_BLIND_P1.md`. I used only the equations in that brief and the explicitly named Phase-4 `a1_results.csv`. I did not read any prior Phase-5 optical-depth script, receipt, `S0_*`, or earlier optical-depth file.

Artifacts:

- `DERIVATION.md`: invariant element, ODE reduction, endpoint proof, unit conversion
- `compute_blind_p1.py`: executable calculation
- `p1_optical_depth.csv`: requested scan
- `p1_convergence.csv`: explicit cutoff-settlement check
- `GPT1_P1_DONE.md`: completion marker

Run with:

`python3 compute_blind_p1.py`

Dependencies: Python 3, NumPy, SciPy.

## Selected crossing and normalization

The prescribed minimization selects Phase-4 CSV line 36750:

- residual `|2-2 sqrt(t)(1+sqrtN)| = 7.76500376878e-05`
- `N_s = 6.5012969034`
- `sqrtN = 2.5497640878`
- `u = 0.10561554607`
- `v = 0.42996501982`
- `u/v = 0.245637531430`
- `t_s/t_crit = 0.079366045102`

For `t_crit=4.35e17 s`, `t_s=3.45242296194e16 s` and `rhobar_s rbar_s=1.89522391340e-18 s^-1`.

The pinned crossing gives both `pbar_s=u rho_FRW` and `rhobar_s=v rho_FRW`; these are simultaneously compatible with constant `w` only at `w=u/v=0.2456375`. For the requested `w` sensitivity scan I hold the pinned density and geometry (`rhobar_s`, `rbar_s`, `N_s`) fixed and set `pbar_s=w rhobar_s`. Thus the `w=0.2456` row is the crossing-consistent case; other rows are explicit closure sensitivity assumptions, not claims that both original `u` and `v` remain satisfied.

## Assumptions

- `f_b` is scanned exactly over `{1,0.1,0.01}` as requested.
- `Y_e` is carried over `[0.5,1]`: one electron per two baryon masses to fully ionized hydrogen. Results scale exactly linearly with `Y_e`; the CSV gives both endpoints.
- Electrons are free and scattering is in the Thomson regime. Ionization history, pairs, Klein-Nishina corrections, absorption, and post-shock microphysical evolution are not modeled.
- CODATA constants used: `sigma_T=6.6524587321e-29 m^2`, `m_p=1.67262192595e-27 kg`, `c=299792458 m/s`, `G=6.67430e-11 SI`.
- Because optical depth is dimensionless, “geometric and physical units” are exposed as `tcrit_times_Irho` (geometry-only), `Irho_s^-1`, `Ne_m^-2`, and `tau`.

## Results

`Ne` below is for `Y_e=1`; halve it at `Y_e=0.5`. The tau interval is `[tau(Y_e=0.5), tau(Y_e=1)]`.

| w | f_b | tcrit I_rho | I_rho [s^-1] | Ne(Y_e=1) [m^-2] | tau range |
|---:|---:|---:|---:|---:|---:|
| 0.001 | 1 | 5.9529587e-4 | 1.3684963e-21 | 3.6750293e24 | 1.2223990e-4 .. 2.4447981e-4 |
| 0.001 | 0.1 | 5.9529587e-4 | 1.3684963e-21 | 3.6750293e23 | 1.2223990e-5 .. 2.4447981e-5 |
| 0.001 | 0.01 | 5.9529587e-4 | 1.3684963e-21 | 3.6750293e22 | 1.2223990e-6 .. 2.4447981e-6 |
| 0.05 | 1 | 3.0703241e-2 | 7.0582163e-20 | 1.8954492e26 | 6.3046989e-3 .. 1.2609398e-2 |
| 0.05 | 0.1 | 3.0703241e-2 | 7.0582163e-20 | 1.8954492e25 | 6.3046989e-4 .. 1.2609398e-3 |
| 0.05 | 0.01 | 3.0703241e-2 | 7.0582163e-20 | 1.8954492e24 | 6.3046989e-5 .. 1.2609398e-4 |
| 0.2456 | 1 | 1.4218838e-1 | 3.2686985e-19 | 8.7779289e26 | 2.9197405e-2 .. 5.8394810e-2 |
| 0.2456 | 0.1 | 1.4218838e-1 | 3.2686985e-19 | 8.7779289e25 | 2.9197405e-3 .. 5.8394810e-3 |
| 0.2456 | 0.01 | 1.4218838e-1 | 3.2686985e-19 | 8.7779289e24 | 2.9197405e-4 .. 5.8394810e-4 |
| 0.30 | 1 | 1.6178830e-1 | 3.7192714e-19 | 9.9879201e26 | 3.3222113e-2 .. 6.6444227e-2 |
| 0.30 | 0.1 | 1.6178830e-1 | 3.7192714e-19 | 9.9879201e25 | 3.3222113e-3 .. 6.6444227e-3 |
| 0.30 | 0.01 | 1.6178830e-1 | 3.7192714e-19 | 9.9879201e24 | 3.3222113e-4 .. 6.6444227e-4 |

All requested cases are optically thin (`tau<1`) under the stated `f_b,Y_e` ranges. The largest is `tau=0.0664442` at `w=0.30, f_b=Y_e=1`. The crossing-consistent row has `tau=0.0583948 f_b Y_e`.

## Convergence and limiting-case checks

1. Analytic endpoint: `rho ~ (N-1)^alpha`, so the integrand in `N` is `~(N-1)^(alpha-1/2)` and integrates to a finite `epsilon^(alpha+1/2)/(alpha+1/2)`. See `DERIVATION.md`.
2. Cutoff settlement: all values stabilize by `N-1=10^-6`; full data are in `p1_convergence.csv`.
3. Independent coordinate check: direct integration in `y=r/r_s` down to `N-1=10^-6` reproduced endpoint `K=I_rho/(rho_s r_s)` with relative discrepancies `1.6e-12, 4.5e-13, -5.2e-13, -2.8e-13` for increasing `w`.
4. Near-dust geometry: if pressure is negligible, `N'=-N/r` gives `N r=constant` and hence `r_h/r_s=N_s=6.5012969`. At `w=0.001`, the numerical value is `6.5012827`, as expected.
5. Scaling: CSV rows verify exact linearity in `f_b` and `Y_e`; geometry columns do not change with either.
6. Dimensional check: `sigma_T c I_rho/(G m_p)` is dimensionless, while `c I_rho/(G m_p)` is `m^-2`.
7. Re-running the script regenerates both CSV files deterministically and exits successfully.