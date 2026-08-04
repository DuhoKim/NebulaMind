# MERIT PANEL — ANCHOR_GAP_PAPER.tex (anchor-gap census)

Lane: `c41-trackb-shape2-mzr-20260804T1452K`
Convener: Hwao (merit-panel convening seat), 2026-08-04 21:39 KST (stamped via `date`)
Manuscript: `ANCHOR_GAP_PAPER.tex` — post referee fixes; referee verdict **MINOR**
(`KUN_ANCHORGAP_REFEREE.md`: four minor errata F-R1…F-R4, none touching a number, a
verdict, the null, or a contract rule).
Grounding artifacts read this session: the full .tex, `KUN_ANCHORGAP_REFEREE.md`,
`T3_REAL_RESULTS.json` (5 anchors, 2/1/0 bins + 2 below-floor, both frozen forecasts,
licensed §6 null), `T5_RECEIPTS.md` (11 sha-receipted artifacts, seven-run log,
C1+C2 applied, gate-to-T5 timeline 14:52→18:29 KST).
Rubric: `frontend/src/app/lab/paperScores.ts` — originality × significance, 1–10 per
seat, grounded note per seat. Four scoring personas (hwao / tori / kun / goru); the
DR seat **abstains** with a note.

## Panel scores

| Seat | Lens | Originality | Significance | 
|---|---|---|---|
| DR | literature precedent | — (abstain) | — (abstain) |
| Hwao | synthesis & field impact | 7 | 6 |
| Tori | framing & motivation | 8 | 6 |
| Kun | adversarial | 5 | 4 |
| Goru | rigor & result-solidity | 6 | 6 |

**Four-seat panel means: originality 6.50, significance 5.50 → merit 6.00** (mean
over both axes, scoring seats only). The DR abstention is recorded mean-neutral in
the TS snippet below so it does not move the merit number.

## Seat notes (grounded)

**DR — ABSTAIN.** The DR lens scores literature precedent, and no Deep Research /
literature sweep was executed for this lane; the precedent question that would decide
originality here — has anyone published a pre-registered, contract-grade census of
*public-archive quotability* of z>3 direct-Te anchors, as distinct from compiling the
detections themselves? — cannot be answered from lane artifacts alone. Per crew
protocol, DR output enters as a filed reference artifact, not an on-demand seat;
inventing a precedent judgment without one would be exactly the kind of un-receipted
number this lane's protocol exists to prevent. Abstention is recorded mean-neutral.

**Hwao (synthesis & field impact) — 7 / 6.** Measuring the settle-line's own
statistics is a genuinely new move for this program: the prior papers measured
metallicities, this one measures the gap (a global VizieR TAP enumeration → 95
candidate rows → exactly 5 contract-grade anchors against a pre-fetch frozen forecast
of ~25). Its exclusion taxonomy converts "more data needed" into four named, cheap
publication acts (machine-readable fluxes with uncertainties, archived Hβ, ID-linked
masses, per-object magnifications) — the finding that JADES contributes 85/95
candidate rows and zero anchors purely for want of usable Hβ columns and linked masses
is the kind of result that can actually change survey archiving practice. Significance
capped at 6 because a census-and-null steers behavior but settles nothing on axis A3
itself: the matched-mass re-test remains unexecutable, by the paper's own headline.

**Tori (framing & motivation) — 8 / 6.** The strongest framing in the portfolio:
freeze the entire measurement contract — declared Te scale, uniform S/N(λ4363)≥5
floor, one derivation pipeline, yield forecast — *before the first science row is
fetched*, then report only what the archives supply. The pre-committed v1=25 forecast
is precisely what turns "we found 5" from an anecdote into a measured
order-of-magnitude shortfall, and the supersession of the flagged v2=87 forecast is
disclosed rather than buried. The modality discipline (a census and a null; no deficit
verdict of any size or direction) holds in every sentence per the referee's
occurrence-by-occurrence scan, and the motivation is ledger-mapped to axis A3's
explicit settle-line rather than paraphrased. Significance capped because the
well-posed question it answers is about archives, not galaxies.

**Kun (adversarial) — 5 / 4.** Rigor is not the issue — every published number was
independently reproduced to the printed digit, 10/10 shas re-verified, all 64 S/N-floor
exclusions re-derived with zero mismatches. The caps are substantive. First, the
headline shortfall is measured against the crew's own pre-fetch forecast, so it partly
quantifies forecast quality rather than archive thinness (v2's 0.12 dex claim was
already flagged arithmetically impossible pre-result, F-T4-1; v1's ~25 rests on an
assumed ~1% auroral detection rate). Second, the census total is an explicitly
single-epoch, VizieR-only floor with 12/23 candidate tables unreachable at run time
and the λ1666/λ5755 anchor channels un-enumerated — the "5" has wide one-sided slack.
Third, the JADES zero-anchor result is largely an archival-formatting artifact (no
usable Hβ columns), and the five surviving anchors themselves sit on SMACS J0723 /
Abell 2744 sightlines with no per-object μ, so even they need a magnification audit
before any populated-bin use. The paper concedes every one of these openly — which is
why this seat scores 5/4 rather than lower — but a null about one archive's holdings
at one epoch is a modest scientific object however honestly it is stated.

**Goru (rigor & result-solidity) — 6 / 6.** The most solid artifact chain of any lane
paper to date: a reviewed-script protocol under which a stencilled mock result was
caught by forensics and rejected; a seven-run log with three honest failures preserved;
per-row exclusion provenance whose taxonomy sums exactly to 95; independent PyNeb
re-derivation of all five anchors' E(B−V)/Te/O-H to the printed digit; flux rows
verified character-for-character against the source archive; and a below-bin-floor
correction (C1) so the accounting closes exactly (3 binned + 2 below-floor = 5). The
result is non-circular by construction — the yield could not have been steered because
the floor, pipeline, and forecast were frozen pre-fetch — and the referee pass found
zero numeric defects. Docked on both axes because what it establishes so solidly is
deliberately modest (N=5, zero populated bins, no metallicity claim), per-object MC
uncertainties remain untabulated (disclosed §6.4), and two documentation seams
(PyNeb version, Hγ/Hβ vs the frozen doc's Hα/Hβ branch) survive as disclosed defects.

## Ready-to-paste TS snippet

Key: `"/studies/c41-highz-mzr-calibration-anchored.pdf"`. Matches the
`PAPER_SCORES` entry format of `frontend/src/app/lab/paperScores.ts`. The `dr` seat
is an **abstention**: `Record<Evaluator, EvalScore>` requires all five keys, so its
numbers are the four-seat panel means (mean-neutral placeholders, leaving merit at
6.00) and its note states the abstention explicitly.

```ts
  "/studies/c41-highz-mzr-calibration-anchored.pdf": { scores: {
    dr: { originality: 6.5, significance: 5.5, note: "ABSTAIN — the DR lens requires a literature-precedent sweep and no Deep Research run was executed for this lane; whether a pre-registered census of public-archive Te-anchor quotability at z>3 has precedent cannot be judged from lane artifacts. Numbers are mean-neutral placeholders (four-seat panel means) so the abstention does not move the merit." },
    hwao: { originality: 7, significance: 6, note: "Measuring the settle-line's own statistics is a new move for the program: a global archive census (95 candidate rows -> exactly 5 contract-grade anchors vs a frozen forecast of ~25) whose exclusion taxonomy converts 'more data needed' into four named publication acts — JADES contributing 85/95 rows and zero anchors purely for missing Hbeta columns and linked masses is a result that can change survey archiving practice; capped at 6 because a census-and-null steers behavior but settles nothing on axis A3 itself." },
    tori: { originality: 8, significance: 6, note: "Strongest framing in the portfolio: the whole measurement contract (declared Te scale, S/N>=5 floor, one pipeline, yield forecast) frozen BEFORE the first science row, so 'we found 5' becomes a measured order-of-magnitude shortfall rather than an anecdote; modality discipline (census and null, no deficit verdict of any size or direction) holds in every sentence per the referee scan. Capped because the well-posed question it answers is about archives, not galaxies." },
    kun: { originality: 5, significance: 4, note: "Rigor is not the issue (every number reproduced to the printed digit; 64 exclusions re-derived, zero mismatches). Caps: the shortfall is measured against the crew's own forecast, so it partly quantifies forecast quality (v2's 0.12 dex was flagged impossible pre-result); the total is a single-epoch VizieR-only floor with 12/23 tables unreachable and lambda1666/5755 channels un-enumerated; the JADES zero is largely an archival-formatting artifact, and the five anchors themselves lack per-object magnifications on cluster sightlines. All conceded openly — but a null about one archive's holdings at one epoch is a modest scientific object." },
    goru: { originality: 6, significance: 6, note: "The most solid artifact chain of any lane paper: reviewed-script protocol that caught and rejected a stencilled mock, seven-run log with honest failures preserved, per-row provenance summing exactly to 95, independent PyNeb re-derivation of all five anchors to the printed digit, and closed 3+2=5 accounting; non-circular by construction (floor, pipeline, forecast all frozen pre-fetch) with referee verdict MINOR and zero numeric defects. Docked because what it establishes solidly is deliberately modest (N=5, zero populated bins) and per-object MC uncertainties remain untabulated." },
  } },
```

Panel merit (as `meritOf` will compute over the pasted entry): **6.00**
(originality mean 6.50, significance mean 5.50).

## Convener's closing statement

The panel's spread is itself informative: the seats that score *how the question is
posed and secured* (Tori 8/6, Goru 6/6, Hwao 7/6) sit well above the seat that scores
*what was learned about galaxies* (Kun 5/4). That is the correct shape for this paper —
it is the best-executed and most honestly-framed artifact the lane has produced, and
its deliverable is a census and a null. Merit 6.00 places it mid-pack numerically, but
unlike the rejected-cohort papers its number is limited by chosen modality, not by
defect: no seat found a circularity, an unreceipted number, or an over-claim.
Advisory only; no promotion, publication, or DB action is implied.

MERIT_ANCHORGAP_COMPLETE_20260804
