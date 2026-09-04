ACCESS_SHA=17dec02b20e65e57d8f5a9d1a6ea8644ad8ee6f58ac73051e7f1f1458735c2a4
RIGIDITY_ABSENT

Seat: `codex`

## Verdict

Entry 56 does **not** force `w = -1` across its admitted construction. It defines `r_S = 2GM_T` and `Λ_e = 3/r_S²`, so a fixed `M_T` gives a fixed `r_S` and hence `w = -1`. But the source presents fixed mass as a chosen setup, not a general consequence: “If we want `M_T` ... to be constant throughout the evolution,” the junction `χ*` must vary with `τ`. More decisively, it expressly admits a nonempty exterior with accretion: “`rS` could increase if there is accretion from outside,” yielding “an effective `Λe` term that decreases with time (`ωDE > −1`).” The isolated-black-hole conservation argument therefore applies only after imposing the empty-exterior/isolated condition; the construction does not derive that condition as mandatory.

Limb B is not reached.

## C1 — source identity

Source extraction, printed with `repr()` by the executable:

```text
'Such boundary condition is equivalent to a \x02 term: \x02 = 3/rS2 . We can therefore interpret cosmic acceleration as a measurement'
'The non-flat case, or more sophisticated global topologies, could             of τ . If we want MT in equation (7) to be constant throughout the'
'also be reproduced if we consider the more general case, but there            evolution, we need the junction χ ∗ in equation (6) to be a function'
```

After whitespace/symbol normalization: `Λ = 3/r_S²`; `r_S = 2GM_T`; and “If we want `M_T` to be constant throughout the evolution, the junction `χ*` must depend on `τ`.”

`C1_SOURCE_IDENTITY=PASS`

## C2 — evolution search

Exact search terms:

```text
'rS could increase'
'accretion from outside'
'function of time'
'If we want MT'
'isolated universe'
'fixed total relativistic mass'
```

Decisive resulting source text (PDF-extraction whitespace normalized):

> “For the case in equations (4) and (5), the mass inside χ is constant for matter-dominated fluid when ρ ∼ a−3. But in the early stages of the expansion, when the energy density is dominated by radiation or a fluid with a different equation of state, the mass inside χ is a function of τ. If we want MT in equation (7) to be constant throughout the evolution, we need the junction χ ∗ in equation (6) to be a function of time τ ... More generally, M could be a function of time.”

> “The BHU exists within a larger background that may or may not be totally empty outside. In the latter case, rS could increase if there is accretion from outside. This case is more speculative and needs to be studied in more detail, but it could result in an effective Λe term that decreases with time (ωDE > −1).”

`C2_EVOLUTION_SEARCH=PASS`

## C3 — discrimination

ΛCDM with a cosmological constant makes the same `w = -1` prediction. However, preregistered class 4 precedence is not reached because rigidity is absent.

`C3_DISCRIMINATION_STATED=PASS`

## C4 — no reanalysis

No data, likelihood, published constraint, network resource, or Limb B analysis was used.

`C4_PUBLISHED_ONLY=NOT RUN`

## C5 — live harness

```text
python3 -c "import sys;print(sys.version)"
3.9.6 (default, May 22 2026, 11:13:45)
[Clang 21.0.0 (clang-2100.1.1.101)]

python3 -c "import sympy;print(sympy.__version__)"
1.14.0

shasum -a 256 $(command -v python3)
b8763cf250e607a778bb4603cecb5b90338814d0a3dfcba0d57b1de242f610e9  /usr/bin/python3
```

`C5_HARNESS_PINNED=PASS`

No symbolic operation was required; therefore no symbolic timeout occurred.

## C5b — opened paths

```text
R3B_LAMBDA_RIGIDITY_PREREG_20260904.md
R3B_LIMBA_SEAT_BRIEF_20260904.md
../bhu-reading-20260823/sources/gaztanaga_mass_mnras_clean.txt
```

No path under `prereg/`, `_successor_build_`, or any spin-parity path was opened.

`C5b_NO_CROSS_LANE_ACCESS=PASS`
