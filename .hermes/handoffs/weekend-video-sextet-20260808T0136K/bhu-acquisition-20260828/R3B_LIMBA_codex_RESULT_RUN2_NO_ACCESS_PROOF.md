RIGIDITY_ABSENT

Seat: `codex`

Entry 56 does not force `M_T`, hence `r_S = 2GM_T`, to remain constant. Its wording—“If we want MT ... to be constant”—makes constancy a chosen condition, implemented with a time-dependent junction, rather than a consequence of the construction. The paper also explicitly permits the BHU exterior to be non-empty: accretion can increase `r_S` and produce an effective Lambda term that decreases with time (`w_DE > -1`). The isolated, empty-exterior case is therefore an assumption/specialization, not a derived necessity. Since `Lambda = 3/r_S^2`, the construction admits evolving effective dark energy. Limb B is not reached.

## Source identity

PDF-extracted source, printed with `repr()` by the executable and matched after normalization:

- L25: “A system with a finite mass M has a finite gravitational radius rS = 2GM.”
- L28: “Such boundary condition is equivalent to a [Lambda] term: [Lambda] = 3/rS2.”
- L138–L140 in the pinned-text numbering (L139–L141 under Python `splitlines()` because form feeds count as separators): the mass is a function of tau, and “If we want MT ... to be constant throughout the evolution, we need the junction chi* ... to be a function of time tau.”

`C1_SOURCE_IDENTITY=PASS`

## Evolution search

Exact search terms used:

`rS could increase`
`accretion from outside`
`function of time`
`function of τ`
`If we want MT`
`isolated`
`mass loss`
`non-static exterior`

Decisive resulting text (source L311–L318 in the pinned numbering; L315–L322 under Python `splitlines()`):

> The BHU exists within a larger background that may or may not be totally empty outside. In the latter case, rS could increase if there is accretion from outside. This case is more speculative and needs to be studied in more detail, but it could result in an effective [Lambda]e term that decreases with time (wDE > -1).

Additional resulting text says the mass inside fixed `chi` is constant for matter with `rho ~ a^-3`, is a function of tau for radiation or another equation of state, and “More generally, M could be a function of time.” No match was found for `mass loss` or `non-static exterior`.

`C2_EVOLUTION_SEARCH=PASS`

## Discrimination

LambdaCDM with a true cosmological constant makes the same fixed `w = -1` prediction as the isolated, fixed-`M_T` specialization. Class 4 would take precedence if rigidity held, but it does not apply because entry 56 admits evolving `r_S`.

`C3_DISCRIMINATION_STATED=PASS`

## Limb and harness controls

`C4_PUBLISHED_ONLY=NOT RUN`

No data, published constraints, likelihood, or network was accessed. No symbolic operation was performed, so the 120-second symbolic cap was not invoked.

Live harness output from the successful executable run:

```text
python3 -c "import sys;print(sys.version)" -> 3.9.6 (default, May 22 2026, 11:13:45)
[Clang 21.0.0 (clang-2100.1.1.101)]
python3 -c "import sympy;print(sympy.__version__)" -> 1.14.0
shasum -a 256 $(command -v python3) -> b8763cf250e607a778bb4603cecb5b90338814d0a3dfcba0d57b1de242f610e9  /usr/bin/python3
```

`C5_HARNESS_PINNED=PASS`

Every local file path opened or created during the study:

```text
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/R3B_LAMBDA_RIGIDITY_PREREG_20260904.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/R3B_LIMBA_SEAT_BRIEF_20260904.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/gaztanaga_mass_mnras_clean.txt
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/R3B_limbA_codex.py
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/R3B_LIMBA_codex_RESULT.md
```

The only path outside `bhu-acquisition-20260828/` is inside the expressly authorized `../bhu-reading-20260823/sources/` tree.

`C5b_NO_CROSS_LANE_ACCESS=PASS`
