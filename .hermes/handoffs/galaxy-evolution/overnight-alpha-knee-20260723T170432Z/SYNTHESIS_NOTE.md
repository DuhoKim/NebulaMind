# The age-resolved α-knee in the Milky Way disk: a systematics-limited candidate

**NebulaMind Lab · autonomous overnight run · synthesis note**
*Descriptive, not validated. Not a detection. No human has vouched for this result.*

---

## The question

The gas-phase α-element "knee" — the metallicity [Fe/H]ₖₙₑₑ at which [Mg/Fe] turns off its
high-α plateau — marks the epoch when Type-Ia iron caught up with the core-collapse α-elements.
Whether that turnover sat at the **same metallicity at all epochs**, or **shifted as the disk
aged**, is a real open question: prior work maps the age–[α/Fe] *sequence* (Mackereth+2017,
Lagarde+2021, Casali+2025), but **nobody has extracted the knee *vertex* per stellar-age bin**.
That per-age vertex — and its rate of change, **d[Fe/H]ₖₙₑₑ/d(age)** — is the datum this run
targeted, and it does not exist in the literature.

## What was measured

A capability built the same night (`nm_external_data`: VizieR + resilient SkyServer) assembled a
sample that the standard pipeline could not reach: **~330,000 APOGEE (DR18) giants** with C/N
spectroscopic ages and distances (`apogeeDistMass`) ⋈ Galactic coordinates (`apogeeStar`) ⋈
[Fe/H]–[Mg/Fe] chemistry (`aspcapStar`), joined in-process on `APOGEE_ID`. The knee vertex was
located by a broken-line ridge fit (bootstrap errors) in ~30–41 populated **(R_g × age)** cells.
The design is intrinsically non-circular: every cell sits on **one ASPCAP abundance scale**, so a
gradient is a pure *internal* differential, immune to the absolute-scale offset that sinks
cross-survey work. The measurement was repeated across a **25-corner systematic sweep**
(α-element Mg/O/Si × flag strictness × knee-definition `ridge_pct` × R₀ × SNR × binning).

## Result — a candidate, honestly bounded

- **Knee position is robust:** median [Fe/H]ₖₙₑₑ ≈ **−0.50**, stable (−0.44…−0.58) across all corners.
- **The age-gradient is present but method-sensitive.** d[Fe/H]ₖₙₑₑ/d(age) is **positive in 18 of 25
  corners at >2.5σ** (median **+0.027 dex/Gyr**, reaching 5–13σ for Si and the wide-age binning), and
  its sign **survives the abundance-scale swap in 23/25** corners (`noncircular_robust`). *But the
  sweep exposed a real systematic:* the signal **washes out at the extreme knee-definition setting
  (`ridge_pct = 80`)** — Mg/loose/r80 → +0.001, Mg/strict/r80 → −0.002 — and is weak in the O-based
  corners (+0.013 to −0.003). So the effect depends on **how the knee vertex is defined.**
- **The radial gradient is null.** d[Fe/H]ₖₙₑₑ/dR_g flips sign with binning (+0.048 to −0.061) — **not
  robust**, consistent with the spatial invariance of the high-α sequence (Nidever+2014). This
  matches the pre-run novelty gate, which flagged the *radial* framing as already-answered.

| systematic corner | d[Fe/H]ₖₙₑₑ/d(age) (dex/Gyr) | σ | non-circular |
|---|---|---|---|
| Mg · fiducial (r75) | +0.032 ± 0.006 | 5.4 | ✓ |
| Si · strict · r70 | +0.092 ± 0.015 | 6.2 | ✓ |
| age-coarse binning | +0.052 ± 0.004 | 13.1 | ✓ |
| Mg · loose · **r80** | +0.001 ± 0.008 | 0.2 | ✓ |
| O · loose · r75 | −0.003 ± 0.007 | −0.4 | ✗ |
| **across 25 corners** | **median +0.027** (range −0.003…+0.092) | — | 23/25 ✓ |

## Verdict

A **suggestive, systematics-limited candidate** — not a detection. The high-α knee shows a positive
age-trend that survives the α-element choice (Mg, Si), distance scale, SNR floor, and radial/age
binning, **but is sensitive to the knee-definition method** (`ridge_pct`), which is therefore the
limiting systematic. It must not be overclaimed as a measurement of when the disk's chemical
turnover shifted.

**The robustness sweep is the point.** Any single corner would have reported "+0.032 dex/Gyr at 5σ"
and called it a discovery; running 25 corners revealed the ridge-definition fragility that a single
run hides. This is the process working as designed — the honest bound is the result.

**Status:** descriptive · not validated · not deployed to the board. The next step to promote it from
candidate to result is a **more principled knee-finder** (a physical broken-power-law or changepoint
model, not a ridge percentile) to remove the `ridge_pct` sensitivity — not more data.

*Run: 25/25 corners, 22 review-cleared by the automated referee, 3 shelved, 92 min. Study module
`nm_alpha_knee.py` on main (PR #128). All numbers above are automated and unreviewed by a human.*
