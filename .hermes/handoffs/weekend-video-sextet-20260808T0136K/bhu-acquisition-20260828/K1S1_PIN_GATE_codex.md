ACCESS_SHA_CLAUDE=6056c13393dcfa9d1a749fcc7fce131de3a6c97850440924a1ad25095d3aa57f
ACCESS_SHA_AGY=0bb6fd67692328dd9916ade547a2827e30e1a66dbcb80e8cf883304f7bdad5dd
PIN_GATE=FAIL

# MASTER PIN SHEET for phase 2

This sheet does **not** release phase 2: row 2 lacks the receipt required by the frozen preregistration. Repairs below replace stale/invalid line receipts but cannot repair that preregistration failure.

| row | phase-2 pin | receipts that held / repair |
|---|---|---|
| 1 | `ln(10^10 A_s)=3.044 +/- 0.014`; `n_s=0.9649 +/- 0.0042`; `k_0=0.05 Mpc^-1`; `P_R(k)=A_s(k/k_0)^{n(k)}` | `1807.06209_clean.txt:L1526-L1537, L1780, L1827, L3047-L3055` (Claude); agy's independent values hold at `L1413, L1419`. |
| 2 | **NOT CLEARED:** proposed `sigma(M) proportional to A_s^(1/2)` at fixed shape | `1807.06209_clean.txt:L1780, L3047-L3050` establishes power proportional to `A_s`; `2002.12778_clean.txt:L1683-L1687` identifies `sigma` as the rms/dispersion and relates limits to power; `1405.7023_clean.txt:L2308, L2382` says power is variance. None explicitly states the pinned exponent `1/2`. A satisfactory receipt must explicitly give `sigma^2(M)=integral ... P_R ...` (or explicitly `sigma proportional to sqrt(A_s)`) under fixed transfer/window/shape. A definitional derivation is scientifically sound but is not acceptable under the prereg's “exponent pinned with a receipt” wording. |
| 3 | Kroupa high-mass IMF `xi(m) proportional to m^(-alpha_3)`, `alpha_3=2.3 +/- 0.7` for `m>=1 M_sun`, hence nuisance range `[1.6,3.0]` | `astro-ph_0009005_clean.txt:L329-L338`; reference slopes at `L213, L288-L289`; alternate-model context at `L474-L475, L490`; revision at `L886-L889` (Claude). Agy's `L826` receipt is invalid and its `alpha_1/alpha_2` pair is not the required high-mass nuisance. |
| 4 | Fryer delayed/rapid prescriptions, metallicity corners, and source bar `M_NS,max=2.5 M_sun`; invert at phase 2 | **Repaired to current source lines:** Eq. 5 and definitions `1110.1726_clean.txt:L631-L688`; Eq. 6 `L690-L805`; Eqs. 7-8 `L845-L925`; Eq. 9 `L928-L989`; gap comparison `L1005-L1012`; bar `L1041-L1063`. Agy's `L1051, L1073` hold. The PDF is `1110.1726.pdf`, pp. 11-12. |
| 5 | `delta_c` nuisance envelope `[0.3,2/3]` (centre `0.4-0.45`); Gaussian `beta approximately Erfc[delta_c/(sqrt(2)sigma)]`; Carr beta-to-present-abundance conversions | `2002.12778_clean.txt:L187-L196, L301, L307, L1683-L1687`. Agy's `1405.7023_clean.txt:L553, L1593` validly pins only the representative `0.41` and equivalent Press-Schechter formula, not Claude's envelope. |
| 6 | C1: local stellar-BH relic mass density about `5x10^7 M_sun Mpc^-3`; z=0 mass-function fits `log N=5.623` (field) and `6.078` (field+cluster), with roughly flat `5-50 M_sun` behavior | `2110.15607_clean.txt:L44-L46, L347-L348, L356-L362, L381-L383, L590-L600, L908-L918` (Claude). This validly repairs agy's UNPINNED row. |
| 7 | C2 mass window `1-100 M_sun`: mandatory `f<1` coverage; optional/potential O1 line `f<0.01` over `10-300 M_sun` must be declared before computation | `2002.12778_clean.txt:L1004-L1008, L1066, L1451, L1461, L1596-L1597, L1604`; conversions `L301, L307`. Secondary QCD/constraint context: `2026_PBH_constraints_evidence_prospects_arXiv_2601.06024.clean.txt:L265-L275, L1104-L1108, L1136`. This validly repairs agy's UNPINNED numeric bound; agy's `2002.12778_clean.txt:L1691` is only a figure caption. |

## Row-by-row agreement

| row | agreement |
|---|---|
| 1 | Yes: values agree. |
| 2 | Yes on the proposed value, but neither sheet has a receipt that explicitly pins the exponent. |
| 3 | No: agy gives lower-mass `alpha_1/alpha_2` values and no high-mass range; Claude pins `alpha_3` and `[1.6,3.0]`. |
| 4 | Partial: both give `2.5 M_sun`; agy does not pin the equation/range nuisance and Claude's line numbers became stale. |
| 5 | No: agy pins only `delta_c=0.41`; Claude pins the nuisance envelope `[0.3,2/3]`. Formulas agree. |
| 6 | No sheet-to-sheet value comparison: agy says UNPINNED; Claude's receipts hold. |
| 7 | No sheet-to-sheet numeric comparison: agy supplies only a figure-caption receipt; Claude's receipts hold. |

## Fryer PDF exponent check

`/opt/homebrew/bin/pdftotext -f 11 -l 12 -layout 1110.1726.pdf -` confirms that Eq. 6 has **four affected superscript 2 occurrences**: `(M_star-23.5)^2` and `(1+Z_metal)^2` in each of its two branches. In the layout extraction the four `2`s are detached above the baseline; the current clean text preserves them in its LaTeX render at `1110.1726_clean.txt:L738, L798`. Eq. 7's `Z_metal^(1/2)` is also visibly superscripted in the PDF but is not one of the “squared exponents” in the note.

## Failed receipts

- Claude row 4: `1110.1726_clean.txt:L83`, `L452`, `L456-L469`, `L489`, `L491`, `L494`, `L501-L502`, `L540-L551`, `L542`, and `L619-L621` do not state the claimed Fryer values in the source tree now present. The row-4 composite summary receipt consequently fails. Current-line repairs are in master row 4.
- Claude row 4 source-integrity receipt: recorded clean-text SHA `99893109925af7b66ec52b7498c39d3ac8657b7f0aaf53015a061424d19736d7` does not match the fetched file now present, whose SHA is `8f49418708594992cc8f9da284fb8f5fb5b2ce074c3b1932fa8b1fa58b1340f2`.
- Claude/agy row 2: the cited lines do not themselves state exponent `1/2`; the claimed exponent receipt therefore fails the preregistration standard.
- Agy row 3: `astro-ph_0009005_clean.txt:L826` says the alpha-plot parts are disjoint; it does not give `alpha_1=1.3 +/- 0.5` or `alpha_2=2.3 +/- 0.3`.
- Agy row 7: `2002.12778_clean.txt:L1691` is only “Figure 18: Combined constraints on beta(M)”; it supplies no `O(1) M_sun` value or exclusion.
- Agy's statements that fetched-source SHA256 values were recorded fail: its sheet records none. In particular `1405.7023_clean.txt` has no SHA receipt there.

## Fetched-source SHA256 check (actual files)

```text
0aa2174396080f6ea51f88b9270088931a242a13e3f5174ab3e55a350222e8ae  astro-ph_0009005_clean.txt
63441542f13a8588d9b5ac7d5fe3a542c8d8c300f1f7fc4030711cb3dde0e43d  astro-ph_0009005.pdf
8f49418708594992cc8f9da284fb8f5fb5b2ce074c3b1932fa8b1fa58b1340f2  1110.1726_clean.txt
2d99ea4252d293d8bed4c80673e5425f70d1ff6a3763626ed8e27ed931942839  1110.1726.pdf
cb90d58cdbbe9884e1ed1c4c4e9f1be9502c749e24aab0a76813a6857aab20d8  2110.15607_clean.txt
8006190e260e96065580b6c769d4e94bd189420fe8b428f70efc4f6edd95c9f3  2110.15607.pdf
2ad25933ea8b537d3e08f50af8c4bd7c9b5c30b60b90e6d73b5e61162b876327  1405.7023_clean.txt
```

## Gate note (104 words)

Rows 1 and 3-7 can be assembled from receipts that hold, after repairing Fryer's stale line numbers and using Claude's valid controls for agy's UNPINNED rows. The gate nevertheless fails because the frozen preregistration requires the amplitude exponent itself to be pinned with a receipt. The sheets derive `1/2` from power proportional to `A_s` plus the rms/variance definition; no cited line explicitly supplies that exponent or the full variance integral under the fixed-shape assumptions. Agy also omitted its claimed SHA records, and Claude's recorded Fryer clean-text hash no longer matches the file in the sources tree. Phase 2 must wait for an explicit exponent receipt and a frozen, hash-matched Fryer text receipt.
