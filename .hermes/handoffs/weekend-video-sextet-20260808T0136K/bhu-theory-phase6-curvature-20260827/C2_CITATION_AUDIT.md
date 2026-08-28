# C2 — audit of the target paper's observational-support paragraph

Tori, 2026-08-28 ~00:1x KST. Every quotation below is from the cited source, read this session.
Nothing is asserted from memory.

**Target:** Gaztañaga, Kumar, Pradhan & Gabler, PRD 111, 103537 (2025), arXiv 2505.23877.

**The paragraph under audit** (§VIII, pinned text line 480), verbatim:

> "The smoking gun for our bouncing scenario is the presence of both a small spatial curvature
> and a small Λ term. […] The Planck PR3 lensed power spectrum revealed a 3σ preference for
> positive curvature [Planck Collaboration 2020b], with Ω_k ≃ −0.04 ± 0.01, in agreement with our
> Eq. 27. Recent results from ACT [ACT Collaboration 2025] similarly suggest a slight preference
> for positive curvature (**see their Fig. 9**), although the current uncertainties remain too
> large to decisively rule out a flat universe. **The latest DESI data [DESI Collaboration 2025]
> echo this trend, also hinting at a mild preference for positive curvature.**"

Its reference list resolves those to **ACT = arXiv:2503.14452** and **DESI = arXiv:2503.14738**.

---

## Finding 1 — the DESI claim is not supported by the paper cited

`arXiv:2503.14738` is *DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and
Cosmological Constraints*. It **assumes flatness and derives no Ω_K constraint.** Verbatim:

> "Through most of this paper we will assume a flat universe and thus Ω_K = 0 in equation 6,
> motivated by the tight constraints obtained on Ω_K when it is allowed to vary freely."

It defers curvature to a companion paper. Its abstract states only that "the results are well
described by a flat ΛCDM model".

**Three independent reads** (arXiv abstract, arXiv HTML v2, ar5iv HTML) found no Ω_K constraint.
The cited paper cannot "hint at a mild preference for positive curvature"; it fixes curvature to
zero by assumption.

**Worse for the claim, the actual DESI+CMB curvature analyses run the other way.** Both current
ones find Ω_k > 0 — *open*, the sign this model forbids (see `c1_curvature_constraints.py`, 7/7):

| analysis | Ω_k | from flat |
|---|---|---|
| Chen & Zaldarriaga, `2505.00659`, DESI DR2+CMB | **+0.00227** (from their `R_k = 21 H_0⁻¹`) | 2.06σ |
| DESI DR1 FS + DR2 BAO + CMB, `2602.18761` | **+0.0028 ± 0.0011** | 2.55σ |

---

## Finding 2 — the ACT characterisation is contradicted by the ACT paper's own summary

`arXiv:2503.14452` is *ACT DR6: Power Spectra, Likelihoods and ΛCDM Parameters* (Louis et al.).
Its curvature result, verbatim (Eq. 46 and surrounding text):

> "**the ACT power spectra prefer a flat geometry**, with the curvature parameter measured from
> the lensing in the power spectrum to be
>
>     Ω_K = −0.004 ± 0.010 (68%, ACT)
>         = −0.010 ± 0.009 (68%, W-ACT)"

Its Figure 19 caption: *"Constraints on Ω_K from the CMB power spectrum for different data
combinations: **the ACT data are consistent with a flat universe.**"*
Its Figure 20 caption: results *"are **consistent with ΛCDM (zero curvature)**."*

Ω_K = −0.004 ± 0.010 is **0.4σ from zero**. The central value is negative, so "a slight
preference" is not fabricated — but the source it is drawn from describes its own result as
preferring flat, twice, in figure captions written for that purpose.

**On the figure pointer — caveated.** In the version available to me (draft dated 25 June 2025),
**Figure 9 is the ACT EB/TB power spectra and polarization-angle rotation ψ** — cosmic
birefringence, not curvature. Curvature is Eq. 46 and Figures 19–20. *However*, the BHU paper was
posted in May 2025 and would have cited an earlier version, and figure numbering can shift
between arXiv versions. **I have not checked v1, so I do not claim the pointer was wrong when
written.** The substantive mischaracterisation in Finding 2 does not depend on it.

---

## Finding 3 — the cited ACT paper explicitly undercuts the BHU paper's primary support

This is the strongest of the three, and it needs no version caveat. The BHU paragraph's lead
evidence is Planck PR3's 3σ closed preference. The very next source it cites says, verbatim:

> "The Planck PR3 lensed power spectrum shows a 3σ preference for non-zero curvature
> [Planck Collaboration 2020d], **although this is disfavored with the inclusion of large-scale
> structure data.**"

and diagnoses where that preference comes from:

> "**The high fluctuation in A_lens also manifested itself in the Planck analyses as a preference
> for positive spatial curvature, with Ω_K < 0** […] It cannot be measured using the primary CMB
> power spectra alone since different combination of other cosmological parameters can absorb the
> changes caused by non-zero flatness […] This geometric degeneracy is effectively broken when
> using the lensed CMB spectrum, or combining the CMB with lensing and/or BAO"

So the paper cited in support of the trend attributes the headline number to the lensing-amplitude
fluctuation and states that adding large-scale structure disfavours it.

---

## What this does and does not establish

**Establishes:** the observational-support paragraph does not survive checking. One citation
points at a flatness-assuming analysis; one is contradicted by its source's own summary; and the
source cited second undercuts the evidence cited first. On current data the model's required sign
is the *disfavoured* one at roughly 2–2.5σ.

**Does not establish:** that the model is refuted. It is not. Ω_k < 0 is disfavoured, not
excluded — the 2.6σ lower edge still crosses zero — and per `OPENING_FINDING_FALSIFIER_MISREAD.md`
the model can retreat toward Ω_k → 0⁻ indefinitely, where no measurement reaches it.

**Not yet done, and needed before this is a result rather than a lead:**

1. ~~Read the DESI companion paper the DR2 II text defers curvature to~~ — **PARTIAL.** I did
   *not* obtain `DESI Collaboration et al. 2025c` itself. I read three other DESI-based curvature
   analyses instead (Chen & Zaldarriaga `2505.00659`; DESI FS+DR2 `2602.18761`; wCDM+Ω_k
   `2512.09486`, the last pinned locally). All give Ω_k > 0. The named companion remains unread.
2. ~~Read Planck 2018 VI's own Ω_k table~~ — **DONE 2026-08-28**, §7.3 extracted from the PDF.
   See the revision below; it changes a finding.
3. Check ACT `2503.14452v1` for the Figure 9 numbering. **STILL OPEN.**
4. Confront the χ_* identification — whether the model's only number rests on the same lead
   author's prior homogeneity-scale measurement. **STILL OPEN**, and still the attack I would
   make first.

**Standing caution against myself.** This is the kind of finding I have twice today promoted past
what it could carry. It is a citation audit with three quoted sources, not a refutation of a
published paper, and it should be gated before it is described as anything more.

---

# REVISION, 2026-08-28 — the Planck gap is closed, and it EXONERATES the target on that citation

Planck 2018 VI §7.3 retrieved as PDF and extracted locally. Ledger rebuilt: all eleven entries
first-hand, `c2_constraint_ledger.py` 6/6, exit 0.

## The correction, stated before anything else

The target quotes Planck as `Ω_k ≃ −0.04 ± 0.01`. Planck's own Eq. 46b is:

> `Ω_K = −0.044 (+0.018/−0.015)   (68 %, Planck TT,TE,EE+lowE)`

**The target's rendering is accurate.** My first pass could not verify it, recorded it as
second-hand, and flagged it as the one strongly-closed number I could not stand behind. It
stands. The description of the paragraph as one where citations "do not survive checking" was
too broad: **one of the three survives checking intact.**

Planck also supports the target's "3σ" characterisation — §7.3 calls it "an apparent detection
of curvature at well over 2 σ", with a 99% region of `−0.095 < Ω_K < −0.007` and "only about
1/10000 samples at Ω_K ≥ 0".

## What the target does omit — Planck's reading of its own number, same section

- **Cause.** "The reasons for the pull towards negative values of Ω_K … are essentially the same
  as those that lead to the preference for A_L > 1, although slightly exacerbated in the case of
  curvature."
- **Fragility.** "not robust at the approximately 0.5 σ level to modelling of the polarization
  likelihoods, with the CamSpec TT,TE,EE+lowE likelihood giving Ω_K = −0.037 (+0.019/−0.014)."
- **Lensing reverses it.** "Closed models predict substantially higher lensing amplitudes than in
  ΛCDM, so combining with the lensing reconstruction … pulls parameters back into consistency
  with a spatially flat universe to well within 2 σ" → `Ω_K = −0.0106 ± 0.0065` (Eq. 47a).
- **BAO reverses it further, and flips the sign.** `Ω_K = 0.0007 ± 0.0019` (Eq. 47b),
  "spatially flat to a 1 σ accuracy of 0.2 %."

**So the charge on the Planck citation is OMISSION, not misquotation.** That is a weaker claim
than my first pass implied, and it is the one the evidence supports.

## The three citations, restated

| citation | verdict after full verification |
|---|---|
| Planck `1807.06209` | **Number accurate.** Omits the source's own attribution to A_L, its likelihood-fragility, and its reversal under lensing and BAO. |
| ACT `2503.14452` | **Mischaracterised.** Source states "the ACT power spectra prefer a flat geometry"; `Ω_K = −0.004 ± 0.010` is 0.4σ. Figure pointer unverified against v1. |
| DESI `2503.14738` | **Unsupported.** Cited paper assumes `Ω_K = 0` and derives no curvature constraint. |

## The pattern across the eleven constraints

Every closed value in the ledger is CMB-alone (3.11σ, 2.93σ, 2.64σ) — and Planck itself disowns
those as A_L-driven and likelihood-fragile. **Every combination that breaks the geometric
degeneracy** — Planck+lensing, Planck+lensing+BAO, and all five DESI-based entries — sits at or
across zero, four of them on the open side. With the CMB-alone rows set aside, nothing in the
ledger detects curvature at all (max 2.55σ).

This is the honest shape of it: the model's required sign survives only in the dataset
combination that its own collaboration attributes to a known anomaly.

**Still not a refutation**, for the reason in `OPENING_FINDING_FALSIFIER_MISREAD.md`: the hard
prediction is `Ω_k < 0` with no floor, so the model retreats toward `0⁻` where no measurement
reaches it.
