# T1 CENSUS — FINDINGS (enumeration stage; no eligibility ruling is made here)

Executed 2026-08-05 22:14–22:16 KST under `t1_mzr_enumerate.py` at Kun's APPROVED micro-delta
(sha 5f6d5e04d14e20f3...), against the frozen chain (contract 84e1d9b6ed147dd0..., appendix
b76c14ce40749720..., re-clear 8a2e8f4f5e2d0a5f...). Metadata only; no science rows fetched.

## 1. The instrument passed its pre-registered recall test

- **7/7 recall members returned** (R1–R7), read from the sha-pinned appendix, never retyped.
- **0/3 controls appeared** (C1–C3), including the decoy.
- **0 channel failures** — status `DONE`, not `PARTIAL_`. Every channel's delivered row count
  equalled its `COUNT(*)` pre-probe, so no channel was silently server-capped.

## 2. Reach: the UCD channel carries the census, as Shape-1 predicted

| axis | UCD channel | + name channel | name-channel gain |
|---|---|---|---|
| abundance | 5,393 | 5,568 | +175 (3.1%) |
| mass | 6,118 | 6,206 | +88 (1.4%) |
| redshift | 6,667 | 6,687 | +20 (0.3%) |

Three-axis intersection: **178** candidates; 21 dropped by the modifier filter (19 emptied on
redshift, 2 on abundance — all recorded per S2, all re-addable); **157** in the manifest.

## 3. The finding that matters for T2: `src.redshift` is tagged on the SYMBOL Z, not the concept

The UCD channel's reach comes at a cost the recall test cannot see. Recall measures misses; it
does not measure false positives except through the three controls, and the controls did not
cover the dominant contamination mode. Four semantically distinct quantities enter candidacy
under `src.redshift`, each verifiable from the manifest's own recorded evidence:

| table | column | recorded UCD | what it actually is |
|---|---|---|---|
| `I/349/starhorse` | `ZGal` | `src.redshift;pos.galactocentric;pos.cartesian` | Cartesian height above the Galactic plane |
| `I/355/paramp` | `z-Flame` | `src.redshift` | **gravitational** redshift of a star |
| `J/A+A/453/769/grid` | `Z` | `src.redshift;phys.composition` | initial metal mass fraction in a stellar model grid |
| `J/MNRAS/514/1071/primary` | `vGR1` | `src.redshift;pos.heliocentric;arith` | gravitational redshift velocity |

The `J/A+A/453/769/grid` case is the sharpest: a **stellar evolution model grid** whose X
(hydrogen fraction), M (initial mass) and Z (metal fraction) satisfy all three axes. It contains
no galaxies, no observations, and no redshift.

Scale, from recorded evidence only and **stated as a characterization, not a ruling**: for
**28 of 157** candidates every redshift-axis column is disqualified by its own UCD qualifier or
its own verbatim description; 5 more are mixed. T2 makes the actual rulings under E1–E4.

## 4. What this validates, and what it costs

**Validated:** the evidence-recording design works. Every disqualification above is visible in
the manifest's own `ucd` + verbatim `description` fields — T2 can rule without re-fetching
anything, which is exactly what §5/F8 required.

**Cost, to be fixed in T2's contract:** the control set tested the wrong failure mode. C1–C3
correctly stayed out, yet obvious non-galaxy contaminants sit in the manifest. A control set
that certifies precision must include a **stellar-catalog decoy** and a **model-grid decoy** —
tables that pass all three axes on symbol matching and must be excluded on species/phase. Recall
controls and precision controls are different instruments and this lane only froze the first.

## 5. Carried forward

- Kun advisory A1 (LOW): `recall_misses_are_instrument_failure` is type-unstable — a string
  under degradation, a list otherwise. T2 must branch on type, or the field gets restructured
  at T2's contract touch.
- Kun advisory S8 (wording): "case-complete" overstates the three-case name variants; mixed-case
  forms (`LogOH`, `ZPhot`) are unreachable by that channel. Belongs to §2b at the next contract
  touch — NOT a script change, since the frozen channel maps were computed on the same basis and
  switching to `LOWER()` would de-calibrate them.
- 24 descriptions were clipped at 160 chars, all itemized in `descriptions_clipped`, so T2 never
  quotes a silently truncated description.
