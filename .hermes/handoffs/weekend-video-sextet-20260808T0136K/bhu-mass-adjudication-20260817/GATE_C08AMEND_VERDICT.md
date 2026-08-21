PASS_C08_AMENDMENT

# Gate — C08 amendment (2026-08-21) to `C08_MASS_ADJUDICATION_20260817.md`

Cross-engine review. Author lane: Tori/Lana (2026-08-17 original, 2026-08-21 amendment).
Original gate: Kun (`PASS_C08_ADJUDICATION`). This reviewer is a different model family from
both; all findings below were formed from the pinned sources and receipts, not from the
amendment's own summary. No network used. Nothing edited; findings only.

## 1. Does the amendment change the verdict? — NO. Claim verified.

Diffed the amended file against `.pre-amendment`. The total delta is:

- Three inline edits, each confined to a confidence figure, each preserving the old value
  inline with attribution:
  - §4 limb 2: "~21σ" → "~21σ on the preprint masses, **6.7σ on the published ones (amended
    2026-08-21)**". The ruling clause "**Met at the FALSIFIES standard**" is untouched.
  - §5 verdict sentence: the parenthetical "~21σ" → "**6.7σ** on published masses — amended
    2026-08-21". "Outcome 1 — the mass evidence FALSIFIES the chain as the source states it"
    is byte-identical.
  - §5 confidence paragraph: "21σ on the deciding limb" → "**6.7σ** ... was 21σ".
- The appended amendment section itself.

Nothing else moved. The per-link rulings (links (1)–(4) bullets), limb 1's serious-doubt
tier, the exclusions, and the scope label are untouched. The sealed criterion file is
byte-identical to what was gated: re-hashed `C08_CRITERION_PREREG_20260817.md` at
`69f274a38226d9728c850bf6382564d17bfb5ae7ca4cda5e4f2f9254d8daacbe`, matching the hash cited
in both the adjudication and the Kun gate. The amendment's own claim — "the verdict is
unchanged, only the confidence figure moves" — is exactly what the diff shows.

## 2. Is 6.7σ right? — YES, arithmetic and choice both check out.

Reran the receipts (`r2_four_percent.py`, `r3_channel_settled.py`, `r4_accreted_mass.py`),
all clean, and recomputed the four rows independently:

| row | amendment | rerun / independent recompute |
|---|---|---|
| Miao+ 2026 preprint, bare 4% | 22.8σ | 22.75σ (R2 prints 22.8) |
| Miao+ 2026 preprint, 4% + Tauris 0.0134 | 21.6σ | 21.57σ (R4 prints 21.6) |
| Ferdman+ 2020 published, bare 4% | 7.1σ | 7.05σ (R3 prints 7.1) |
| Ferdman+ 2020 published, 4% + Tauris 0.0134 | **6.7σ** | **6.74σ** |

Inputs verified against pinned sources, not taken on trust: Ferdman masses 1.62 ± 0.03 /
1.27 ± 0.03 are verbatim in `sources/ferdman2020_clean.txt`; Tauris 2017's per-phase maxima
(CE 0.01, wind < 4×10⁻⁴, Case BB 5×10⁻⁵–3×10⁻³ M⊙) are verbatim in
`sources/tauris2017_clean.txt`, and 0.0134 is R4's correctly-labelled sum of those maxima
(Tauris's own summary figure, "at most ~0.02 M⊙", also verified in the clean text). The
"overstated 7–15×" is 0.1/0.0134 = 7.5× and 0.2/0.0134 = 14.9× — correct.

The choice of 6.7σ as operative is the defensible one, and it is the most conservative row
in the amendment's own table. The lane's standing rule (and the sealed criterion's
measurement class) put published, refereed masses in the base layer; Ferdman 2020 is the
published measurement of record. The 4% + Tauris ceiling is the most source-generous ceiling
the in-lane literature supports, since it prices in the source's own He-giant proviso at its
modern-literature value. The alternative a referee might prefer — 7.1σ, the sealed
criterion's bare 4% on published masses — is disclosed in the table with an explicit
one-line decomposition of the two changes (source class vs ceiling). Either way limb 2 fires
by a wide margin; the choice is presentation, not verdict.

Robustness note I checked myself: the sealed prereg defines the fraction against
max(m₁,m₂), while the receipts build ceilings as 0.04 × m_lighter. Under the sealed
max-denominator convention the four rows become 21.7 / 20.5 / 6.7 / 6.4σ. Two consequences:
(a) the amendment's operative 6.7σ coincides exactly with what the sealed criterion, applied
as written, yields on the published record (6.72σ); (b) the full defensible band across both
conventions is 6.4–7.1σ, and every point in it leaves limb 2 met at the FALSIFIES standard.
The operative figure is not an artifact of a favourable convention.

## 3. The source-class claim — VERIFIED, with one non-material leg noted.

The amendment says arXiv:2606.19276 is a preprint, not the "accepted A&A" paper the original
called it. Checked against the pinned artifacts:

- `sources/ar5iv_2606.19276.html` re-hashes to `ad8fba272ad619971a3bb8dca7d257e5bbd66d17dc
  df097a87b00450d81539ce` — matches SOURCE_PIN. Abstract masses 1.599(8), 1.290(8),
  q = 0.807(8) verified verbatim in the HTML; authors confirmed as Miao, Freire, Wex, Meng,
  Tauris, Zhao.
- The pinned arXiv API record (`sources/_tmp_aa.xml`, fetched 2026-08-21) contains **no
  journal_ref and no DOI**. Its comment field reads "accepted by Astronomy & Astrophysics"
  — so the original's "accepted A&A" was not invented, but the amendment's operative claim
  ("it is not, today, a published paper") is correct on the metadata, and SOURCE_PIN's
  nuance (acceptance may be real but precedes indexing) is fairly carried by the amendment.
- "INSPIRE has no publication_info": no INSPIRE record is pinned in the lane, and this gate
  is no-network — UNVERIFIED-AT-GATE for that leg specifically. Non-material: the arXiv
  metadata alone substantiates the source-class fix under the lane's published-layer rule.

## 4. Laundering sweep — CLEAN. Every new assertion traces to a pinned source or receipt.

Factual assertions the amendment adds that were not in the gated original:

1. arXiv:2606.19276 is a preprint (no journal_ref/DOI; INSPIRE no publication_info) —
   SUPPORTED (arXiv leg verified; INSPIRE leg per §3 note).
2. Preprint authorship (Miao, Freire, Wex et al.) and pin hash — SUPPORTED, verified.
3. "Its values are exactly right" (1.599(8)/1.290(8)/0.807(8) verbatim) — SUPPORTED,
   verified in the pinned HTML.
4. Ferdman 2020 is the published record: 1.62 ± 0.03 / 1.27 ± 0.03 — SUPPORTED, verified in
   `ferdman2020_clean.txt`.
5. BLR's companion paper (Phys. Rept. 462 §3.2) quantifies the caveat at 0.1–0.2 M⊙ —
   SUPPORTED, verbatim in `sources/blr_physrept_clean.txt` ("an additional 0.1 to 0.2 M⊙ of
   helium during the helium shell burning"). Pinned file re-hashes to `fc3ed8cd…` as TRACK_B
   records.
6. Tauris et al. 2017 budgets total accretion at 0.0134 M⊙, 7–15× overstatement — SUPPORTED
   (verbatim per-phase values verified; sum and ratios recompute).
7. The four readings (22.8/21.6/7.1/6.7) — SUPPORTED (rerun + independent recompute, §2).
8. "Tracks gated PASS_P3A_AUDIT, PASS_P3B_TRACKB, PASS_P3C_TRACKC" — SUPPORTED: those exact
   tokens are the first lines of `REGATE_A_VERDICT.md`, `GATE_B_VERDICT.md`,
   `GATE_C_VERDICT.md`. Neutral observation: track A passed on re-gate after an initial
   `HOLD_P3A_LOADBEARING` and repair; the tokens the amendment cites are the current,
   operative ones.
9. "Limb 2 fires at every reading in the table" — TRUE (minimum row is 6.7σ ≫ the 95.4%
   bar).

No new claim entered under cover of the correction. The amendment lowers the headline
confidence and strengthens the footing (published masses, quantified caveat) — the opposite
of laundering.

## 5. The original's honesty — the self-characterisation is accurate.

`.pre-amendment` §4 contains "Disclosure — the caveat found after sealing": it raises the
He-giant qualifier unprompted, states it surfaced after the criterion was sealed, declines
to narrow the criterion post hoc, and argues the verdict is invariant to the caveat under
both readings. The amendment's description — "disclosed the He-giant caveat unprompted (§4)
rather than hiding it, and argued around it" — is a fair characterisation of the text being
corrected, not a self-serving one. TRACK_B §5 independently characterises it the same way.

## 6. Overclaim sweep — CLEAN.

"BHU is falsified" appears only inside the quoted prohibition ("would be false and is still
not said"), same construction as the gated original. Nothing states or implies CNS is
vindicated; the amendment reaffirms the chain is falsified as its source states it, which is
the anti-vindication direction. The per-link bounds (CNS not thereby refuted; links (1)–(2)
not individually falsified) survive untouched from the gated text.

## Non-blocking findings (recorded, none rises to a HOLD)

- (a) Cosmetic seam from the inline edit: the amended §5 verdict sentence now pairs
  "19.3 ± 0.7%" — a preprint-masses asymmetry — with "6.7σ on published masses". On the
  published masses the fractional asymmetry is 21.6% (which at the sealed max-denominator
  convention is exactly where 6.7σ comes from). The amendment's own table is internally
  clean; only the inline-edited sentence mixes the two mass sets. Worth a one-word touch if
  the document is ever revised; does not affect any verdict.
- (b) Denominator convention: receipts use 0.04 × m_lighter; the sealed criterion defines
  the fraction against max(m₁,m₂). Disclosed already in TRACK_B §6. Shifts individual rows
  by 0.3–0.7σ; verdict invariant across both conventions (band 6.4–7.1σ). The operative
  6.7σ equals the sealed convention's bare-4% figure on published masses.
- (c) INSPIRE publication_info absence: asserted via SOURCE_PIN without a pinned INSPIRE
  record — UNVERIFIED-AT-GATE under this no-network gate; non-material per §3.

## Verdict

The amendment does exactly and only what it declares: the verdict, per-link rulings, and
sealed criterion are untouched; the confidence figure moves from ~21σ to 6.7σ, the old value
is preserved inline with attribution, the arithmetic reproduces, the operative-figure choice
is the most conservative defensible one, the preprint reclassification is verified against
pinned metadata, and nothing new is laundered in.

PASS_C08_AMENDMENT.

— Kimi K3 (Moonshot AI), cross-engine reviewer, 2026-08-21 KST. Findings only; nothing
edited; no network used. Author lane (Tori/Lana) and original gate (Kun) are different
model families from this reviewer.
