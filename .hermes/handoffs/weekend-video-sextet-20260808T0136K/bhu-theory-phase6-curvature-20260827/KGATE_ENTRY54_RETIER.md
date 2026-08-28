**DEMOTE**

# Gate verdict — entry 54 testability re-tier

Seat: KIMI. Date: 2026-08-28 (KST). Gate: `BRIEF_ENTRY54_RETIER_GATE.md`.
Artifact under review: `../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md`, entry 54.
Primary source read in full: `../bhu-reading-20260823/sources/2505.23877_clean.txt` (921 lines).
Line numbers below refer to that pinned file. The bibliography was read, not edited.

## Quotation audit of the brief (finding in its own right)

Every quotation in the brief was checked against the source or the bibliography. All are accurate:

- Entry 54 text — verbatim match, bibliography lines 374–378.
- Tier definitions — verbatim match, bibliography lines 16–17.
- Batch-9 correction note — verbatim match, bibliography lines 26–28.
- Eq. 27 as `Ω_k = −(0.07 ± 0.02)(χ_*/χ_k)²` — accurate rendering of source line 331
  (the brief drops the leading identity `Ω_k ≡ −k(1/H_0)²`, which changes nothing).
- "The paper states `χ_k > χ_*`" — accurate for the body text (lines 140, 306, 335).
  Nuance: the abstract (line 39) states the weaker `χ_k ≥ χ_*`. The strictness
  discrepancy is internal to the paper; it does not affect any conclusion below,
  since `(χ_*/χ_k)² ≤ 1` suffices for the ceiling reading.

One inaccuracy in Tori's opening finding (not in the brief): the sentence
"Planck PR3 lensed power spectrum revealed a 3σ preference for positive
curvature … Ω_k ≃ −0.04 ± 0.01" is attributed to §VIII; it actually sits in §IX
(Discussion), source line 480. Cosmetic; the quote itself is verbatim.

## 1. Does the paper state `χ_k > χ_*`? — YES, three times in the body

- Line 140: "The case of interest here is k ≡ 1/χ_k² with χ_k > χ_* , which
  corresponds to an overdensity."
- Line 306 (opening of §VI): "Recall from Eq. 8 that χ_k needs to be larger than
  the cloud boundary: χ_k > χ_* ."
- Line 335 (immediately after Eq. 27): "which, for χ_k > χ_* , is consistent with
  a critical reanalysis of the Planck Legacy 2018 data Di Valentino et al. 2020."

The abstract (line 39) uses the non-strict form: "This lower bound follows from
the requirement of χ_k ≥ χ_* ≃ 15.9 Gpc to address the cosmic microwave
background low quadrupole anomaly."

## 2. Does Eq. 27 therefore bound the magnitude rather than predict a value? — YES

Eq. 27, line 331: "Ω_k ≡ −k(1/H_0)² = −(0.07 ± 0.02)(χ_*/χ_k)²".

With `χ_k > χ_*` (body) or even `χ_k ≥ χ_*` (abstract), the factor
`(χ_*/χ_k)² ≤ 1`, so Eq. 27 yields `|Ω_k| ≤ 0.07 ± 0.02` — a ceiling on the
magnitude, with the bracket edge reachable only at `χ_k = χ_*`. Nothing in the
model fixes where below that ceiling Ω_k lies: χ_k is required to be finite
(line 287: "the cloud is finite (that is, χ_k < ∞ and r_S < ∞)") but is
unbounded above, so Ω_k may approach 0 from below arbitrarily closely. The
paper's own abstract frames 0.07 ± 0.02 as a "lower bound" (line 39) — the
most negative value allowed — not as a predicted window with a central value.
Eq. 27 is a scaling relation with a free ratio, not a calibrated prediction.

## 3. Do the authors qualify or withdraw the numeric limits? — YES (qualify expressly)

Line 336, verbatim: "The limits for Ω_k above assume that the homogeneity scale
is the result of only χ_* . This also explains the low quadrupole C_2
Camacho-Quevedo and Gaztañaga 2022 . However, if the homogeneity scale or the
low value of C_2 has a different origin, then the value of Ω_k in the floating
FLRW cloud could be smaller."

Precision note: "withdraw" is Tori's word and is slightly strong. The authors do
not retract the ceiling; they expressly make the numeric limits conditional on
the χ_* ≃ 15.93 ± 2.22 Gpc identification (Eq. 26, line 325), which itself
descends from θ_cut ≃ 65.9 ± 9.2° (Eq. 25, line 319, Camacho-Quevedo &
Gaztañaga 2022 — same lead author as the paper). The effect on the falsifier is
the same: the number is not the model's unconditional content.

## 4. Is there a sentence stating the requirement as a sign? — YES

Line 336, verbatim: "Inflation preceded by a bounce requires Ω_k < 0 , and this
could be found in upcoming cosmic surveys, as indicated by the analysis in Di
Valentino et al. 2020."

Reinforcing statements of the same hard content:
- Line 286: "Note how it is critical that k > 0 (or χ_k² < ∞) to have a bounce
  before the singularity (a = 0) occurs."
- Line 75: "The flat case k = 0 used previously is a good approximation all the
  way to the point where we approach the singularity but does not allow for a
  bounce to occur."
- Line 40 (abstract): "its key observational signature being the presence of
  small but nonzero spatial curvature, a testable prediction for upcoming
  cosmological surveys."

## 5. Does a confirmed flat universe refute this model? — NO

The model's allowed range reaches 0 from below with no lower gap: Ω_k ∈
(−0.09 ≲, 0) at the 1σ edge of the conditional ceiling, and arbitrarily close
to 0 as χ_k grows. Any operationally achievable "confirmed flat" result — a
measurement interval containing 0 at finite precision — is fully consistent
with the model, since some sufficiently small |Ω_k| < 0 satisfies both the
measurement and the model. The paper itself concedes current data cannot
exclude this (line 480: "the current uncertainties remain too large to
decisively rule out a flat universe").

An exactly-zero universe would contradict the model (lines 75, 286: the bounce
requires k > 0), but exact flatness is not confirmable by any finite-precision
observation, so that reading is operationally empty.

What actually refutes the model:
- Unconditionally: a confirmed OPEN universe, Ω_k > 0 — the hard content is the
  sign (Q4), so the kill condition lives on the open side of zero.
- Conditionally (only if the χ_* identification is insisted upon, which the
  authors expressly do not insist on — Q3): a confirmed too-closed universe,
  Ω_k ≲ −0.09, violating the ceiling.

The entry's sentence "a confirmed flat universe refutes it" is therefore false
in every operationally meaningful sense: it places the kill condition on the
wrong side of zero. Flatness is where this model is most comfortable. Tori's
central claim is verified against the source.

## 6. Does the entry meet "number + threshold"? If not, which tier fits? — NO; QUALITATIVE-DIRECTIONAL

It does not meet the tier's meaning. The bibliography's worked example of
CALIBRATED-FALSIFIER is entry 7 (lines 121–126): a calibrated number
(M_max ≈ 1.5 M☉) plus a threshold (≳ 2 M☉) such that crossing the threshold
refutes — and it fired. Entry 54 has no equivalent: its number is a conditional
ceiling the authors qualify away (Q3), and its unconditional content is a sign
(Q4). No numeric threshold in this paper can fire on the near side of zero at
any finite precision. The entry also states the falsification condition
backwards (Q5), so as written it is wrong independent of the tier question.

Tier that fits, from the four existing classes: **QUALITATIVE-DIRECTIONAL** —
the surviving hard prediction is a direction (closed curvature, Ω_k < 0). This
follows the bibliography's own precedent (batch-9, lines 26–28: entry 6 demoted
CALIBRATED-FALSIFIER → QUALITATIVE-DIRECTIONAL when the numeric threshold was
found absent from the text; here the threshold is present but conditional and
misdirected). The reclassed entry MUST carry the operational annotation, or the
demotion repeats the original error in a new form: *falsifiable only from the
open side — a confirmed Ω_k > 0 refutes; flatness at any finite precision does
not; a confirmed Ω_k ≲ −0.09 refutes only under the authors' own conditional
χ_* identification.* The DESI curvature watch should watch for a confirmed open
result, not a flat one.

Considered and not chosen: minting a fifth class (e.g., "SIGN-FALSIFIER —
one-sided: a hard sign/inequality prediction with an explicit boundary value,
refuted only by confirmed results on the excluded side, consistent with values
arbitrarily close to the boundary on the allowed side"). It describes this
paper precisely, but taxonomy parsimony and the batch-9 precedent favor the
existing class with the annotation above; the gate's applying step may adopt the
new class instead without re-adjudication if the maintainers want
falsifiability granularity preserved in the class name itself.

## 7. Testimony — what I could NOT verify (not findings)

- The publication record (PRD 111, 103537, 2025). The pinned text is the
  arXiv-derived clean text; the bibliography asserts Crossref verification
  (line 375). I did not re-check Crossref.
- The paper's characterizations of external datasets (Planck PR3's 3σ
  preference and Ω_k ≃ −0.04 ± 0.01, ACT 2025, DESI 2025, Di Valentino et al.
  2020) — reported here as the paper's claims, not independently confirmed.
  Whether that support survives dataset selection (Tori's question 2) is a real
  open question outside this gate's scope.
- The claim that entry 54 is "the family's only LIVE numeric falsifier" — a
  claim about all other entries, outside this gate.
- The DEMOTE verdict rests solely on the pinned source text and the
  bibliography's own tier definitions and precedent, all quoted above.

## Bottom line for the applying step

Verdict: **DEMOTE** entry 54 from CALIBRATED-FALSIFIER to QUALITATIVE-DIRECTIONAL,
with the falsification direction corrected: the model's hard content is the sign
Ω_k < 0; it is refuted by a confirmed open universe (Ω_k > 0), conditionally by
a confirmed Ω_k ≲ −0.09, and NOT by any finite-precision flat result. This gate
decides only the classification; per the brief, a separate step applies it.
