# C08 adjudication — does the mass evidence create serious doubt, or falsify, the CNS chain?

**Lana (science / claim-boundary seat), 2026-08-17 KST. Scope label, per the brief:
black-hole-universe cosmology is Duho's personal side-interest, not a NebulaMind research
programme, and nothing here presents it otherwise.** This settles the one item
`bhu-closing-video-20260812T2322K` deliberately left open — ledger C08: *"The packet does not
adjudicate whether the mass evidence creates serious doubt or falsifies the CNS chain."* The
closed line's record stands; nothing else is reopened.

**Inputs and discipline.** Assembly is `CLAIM_LINE_LEDGER_V11.md` (authority packet
`b244ea0a…`, hash re-verified today) — C04–C07 are cited, not re-derived. The falsification
criterion was written and hashed **before** the evidence harvest:
`C08_CRITERION_PREREG_20260817.md`, SHA-256
`69f274a38226d9728c850bf6382564d17bfb5ae7ca4cda5e4f2f9254d8daacbe`, and is applied below
without edits. Ordering, exactly: ledger read → primary source fetched for verbatim wording →
criterion sealed → evidence harvest → application. One wrinkle disclosed in §4.

## 1. The primary source, verbatim

Brown, Lee & Rho, *"Kaon Condensation, Black Holes and Cosmological Natural Selection,"*
PRL 101, 091101 (2008); arXiv:0802.2997. The packet had reached this paper at abstract level;
the full text was fetched today. Abstract, complete and verbatim:

> "It is argued that a well measured double neutron star binary in which the two neutron stars
> are more than 4% different from each other in mass or a massive neutron star with mass
> M ∼> 2 M⊙ would put in serious doubt or simply falsify the following chain of predictions:
> (1) nearly vanishing vector meson mass at chiral restoration, (2) kaon condensation at a
> density n∼3n₀, (3) the Brown-Bethe maximum neutron star mass M_max≈1.5 M⊙ and (4) Smolin's
> 'Cosmological Natural Selection' hypothesis."

Supporting passages, verbatim with locations:

- Section I, prediction (c): *"Find a neutron star of mass ∼>2 M⊙, whether in binary or
  otherwise, then it falsifies the VM of HLS theory, which in turn falsifies the kaon
  condensation at ∼3n₀."*
- Section I, the binary limb: *"Find a well measured double neutron star binary in which the
  two neutron stars are more than 4% different from each other (modulo some small additional
  shift by He red giant) in mass."*
- Section V (conclusion): *"A firm observation of any type of a neutron star whose mass is
  greater than M^BB_max or to be safe ∼> 2 M⊙ would present a serious obstacle to the BB and
  CNS scenarios."*

**Framing, which determines what could falsify it:** the bound is stated with "∼" throughout —
approximate, and model-dependent by construction (it is the conclusion of links (1)–(2), not a
free-standing number). But the paper offers the chain *as a falsifiable conjunction with its
own two-limb falsifier set and its own thresholds*: ≈1.5 M⊙ is the predicted maximum, ∼2 M⊙ is
the paper's self-declared safety margin ("to be safe"), and >4% double-NS mass asymmetry is an
independent falsifier with one unquantified caveat ("modulo some small additional shift by He
red giant"). It exempts no formation channel and does not mention PSR J0737−3039 (already
known in 2008 with a ~6.7% mass difference).

## 2. The criterion (sealed before the harvest — full text in the prereg file)

Summary of `C08_CRITERION_PREREG_20260817.md` (`69f274a3…`): qualifying measurements are
dynamical (pulsar-timing) masses; light-curve/photometric masses and objects of unresolved
nature are context only. **Limb 1 FALSIFIES:** one qualifying star > 2.00 M⊙ at ≥ 95.4% plus an
independent corroborator at ≥ 68.3%, or one at ≥ 99.73%. **Limb 2 FALSIFIES:** an uncontested
double-NS binary, both masses from timing, whose 95.4% interval excludes ≤ 4% mass difference.
**SERIOUS DOUBT:** neither limb met, but ≥ 2 qualifying stars > 1.50 M⊙ at ≥ 99.73% each and
≥ 1 qualifying central value ≥ 2.00. **NEITHER / CANNOT BE SETTLED:** as defined there.
Verdict must speak per-link, and may never say "BHU is falsified" (C02: CNS is one of at least
five mutually disagreeing programmes).

## 3. The mass evidence, brought up to date (2026-08-17)

**Qualifying (timing) measurements:**

| System | Mass (68.3%) | Source | Status vs ledger |
|---|---|---|---|
| PSR J0740+6620 | 2.08 ± 0.07 | Fonseca et al. 2021 (arXiv:2104.00880) | As ledgered (C07): clears 2.00 at 68.3%, not 95.4%. No later revision found. |
| PSR J1614−2230 | **1.928 ± 0.017** | NANOGrav 9-yr, Fonseca et al. 2016 (arXiv:1603.00545) | **Revised down** from Demorest's 1.97 ± 0.04 (C06). Reported per the brief's lighter-values-equally rule. |
| PSR J1913+1102 A/B | **1.599(8) / 1.290(8)**, q = 0.807(8) | 2026 update, accepted A&A (arXiv:2606.19276); discovery masses 1.62/1.27 ± 0.03, Ferdman et al. 2020, Nature 583, 211 | **New to this line** — the ledger carried only limb 1. DNS nature confirmed, not questioned, in the 2026 paper. |
| PSR J0737−3039 A/B | 1.338 / 1.249 (both radio pulsars) | Kramer et al. 2021, PRX 11, 041050 | Double-pulsar; nature beyond contest by construction. 6.7% mass difference at ~10⁻⁴ precision. |

**Context only (excluded from the verdict by the pre-registered measurement class):**

- PSR J0952−0607: 2.35 ± 0.17 (Romani et al. 2022, ApJL 934 L17), tightened to 2.35 ± 0.34 at
  95% credibility in a 2026 follow-up — light-curve-model mass; the ledger's `[VERIFY]` flag is
  now resolved (the measurement is real and unretracted) but the class is excluded, and even
  taken at face value its 95% lower bound (~2.01) only brushes 2.00.
- PSR J0514−4002E companion: 2.09–2.71 M⊙ (95%; Barr et al. 2024, Science) — NS-vs-BH nature
  unresolved; excluded.
- PSR J0453+1559: 1.559/1.174, a 24.7% asymmetry — but Tauris & Janka 2019 (ApJL 886, L20)
  propose the companion is a white dwarf from a thermonuclear electron-capture supernova, so
  its double-NS nature **is contested** and the criterion's own clause excludes it. Context
  only; the verdict does not use it.

No qualifying measurement newer than the table was found; searches to today surfaced none.

## 4. Application

**Limb 1 (maximum mass).** FALSIFIES standard **not met**: no qualifying star exceeds 2.00 M⊙
at ≥ 95.4% (J0740+6620 is the strongest and fails exactly there, per ledger C07). SERIOUS
DOUBT conditions **met with room to spare**: J1614−2230 exceeds 1.50 M⊙ by 25σ, J0740+6620 by
8.3σ, J1913+1102 A by 12.4σ — three independent qualifying systems each ≥ 99.73% above the
chain's stated maximum — and J0740+6620's central value (2.08) sits above 2.00. Stated
plainly: link (3) *as literally written* (M_max ≈ 1.5 M⊙) is contradicted at ≥ 8σ by every
heavy qualifying system; only the source's own "to be safe" ∼2 threshold keeps limb 1 in the
serious-doubt tier rather than the falsifies tier.

**Limb 2 (double-NS asymmetry).** **Met at the FALSIFIES standard.** PSR J1913+1102:
Δm = 0.309 ± 0.011 M⊙, a fractional difference of 19.3 ± 0.7% — the 95.4% interval excludes
≤ 4% at ~21σ on the preprint masses, **6.7σ on the published ones (amended 2026-08-21)**. Both masses are from radio timing; the double-NS nature is uncontested in the
refereed literature (assumed without question in the 2026 accepted update, which models the
companion's formation as the second NS's supernova). PSR J0737−3039 (6.7% ± ~0.01%) formally
meets the criterion as a second, nature-beyond-contest system.

**Disclosure — the caveat found after sealing.** The criterion was sealed after the first two
source fetches; a third fetch (checking the paper body for formation-channel exemptions)
surfaced the "(modulo some small additional shift by He red giant)" qualifier on limb 2. The
criterion is not narrowed post hoc. Handled both ways: under the criterion as written, limb 2
is met by two systems; under a maximally source-generous reading in which the unquantified
caveat absorbs J0737−3039's 2.7-point exceedance, J1913+1102's 19.3% — nearly five times the
threshold itself — cannot be a "small additional shift" on any reading, and limb 2 is still
met. The verdict is invariant to the caveat.

**Outcome-4 check:** the verdict does not hinge on any excluded-class measurement; outcome 4
does not apply.

## 5. Verdict

**Outcome 1 — the mass evidence FALSIFIES the chain as the source states it**, via the
source's own second falsifier limb: a well-measured double neutron star binary more than 4%
different in mass exists (PSR J1913+1102; 19.3 ± 0.7% asymmetry on the preprint masses, 21.6% on the published ones; ≤4% excluded at **6.7σ** against the published record — amended 2026-08-21), formally
seconded by the double pulsar. Independently, limb 1 sits at the pre-registered SERIOUS-DOUBT
tier: three qualifying systems exceed the chain's stated 1.5 M⊙ maximum at ≥ 8σ each and the
heaviest well-measured star's central value is above 2.00, without clearing 2.00 at 95.4%.

**Per-link, as the reporting rule requires:**

- **Link (3), the Brown–Bethe maximum ≈ 1.5 M⊙:** contradicted directly, ≥ 8σ per system,
  three systems. Dead as a literal prediction irrespective of which limb one prefers.
- **Links (1)–(2), vector-meson/HLS and kaon condensation at ∼3n₀:** the source's own
  unconditional falsifier for these ("Find a neutron star of mass ∼>2 M⊙ … then it
  falsifies…") is *not* met at the pre-registered credibility — these links are under serious
  doubt via the chain, not individually adjudicated falsified by the mass limb.
- **Link (4), Smolin's CNS:** the chain *including* CNS is falsified as stated. What that
  means, said carefully: CNS's flagship falsifiable prediction — the one clean falsifiable
  number in the family surveyed (C04) — is gone. CNS as a hypothesis is not thereby refuted;
  it can retreat from the Brown–Bethe EOS route, at the price of no longer being tested by
  this channel. And per C02, CNS is one of at least five mutually disagreeing BHU programmes:
  **"BHU is falsified" would be false and is not said.**

**Confidence:** high. The statistical component is not close (**6.7σ** on the deciding limb against the published record — amended 2026-08-21, was 21σ; 8–25σ
on the supporting one). The residual risk is interpretive, and it is stated rather than
hidden: the source's unquantified He-giant caveat (verdict invariant, §4) and the choice to
read the source's two-limb abstract sentence as the falsifier set it plainly is. A referee
could dispute whether limb 2 "should" carry the chain given that the paper's body emphasizes
the mass ceiling; the abstract's own wording says either observation suffices, and the
criterion committed to that reading before the evidence was gathered.

## 6. Note, not a study — said plainly

This is a **note**. The measurements are the pulsar community's, the threshold is the
source's, and the analysis is arithmetic on published posteriors. What it adds — a
pre-registered criterion, the limb the ledger never carried (the DNS-asymmetry falsifier,
already met in the published literature since 2020 and tightened in 2026), and a per-link
verdict — is exactly enough to settle C08, and not enough to clear the flagship bar for a
paper. It should be filed as the closing annex to the BHU line, not grown into a manuscript.

## 7. Constraints receipt

Literature hosts only (arXiv, ar5iv, ADS-indexed pages via search); `portal.nersc.gov` not
touched — the checksum harvest was left alone. No new observations, no sky run, no survey
data. No commit, no push, no publication, no accepted status. Files written:
`C08_CRITERION_PREREG_20260817.md` (sealed pre-harvest, `69f274a3…`) and this adjudication.
Kun gates this output; Duho decides what happens to it.

## Sources

- Brown, Lee & Rho 2008, PRL 101, 091101 — arXiv:0802.2997 (full text via ar5iv)
- Demorest et al. 2010, Nature 467, 1081 — arXiv:1010.5788 (superseded value, cited via ledger)
- Fonseca et al. 2016 (NANOGrav 9-yr), ApJ 832, 167 — arXiv:1603.00545
- Fonseca et al. 2021, ApJL 915, L12 — arXiv:2104.00880
- Ferdman et al. 2020, Nature 583, 211
- arXiv:2606.19276 (2026, accepted A&A) — J1913+1102 update
- Kramer et al. 2021, PRX 11, 041050 — double pulsar
- Romani et al. 2022, ApJL 934, L17; 2026 follow-up (ApJ, DOI 10.3847/1538-4357/ae28c5) — J0952−0607 (context)
- Barr et al. 2024, Science 383, 275 — J0514−4002E (context)
- Tauris & Janka 2019, ApJL 886, L20 — arXiv:1909.12318 — J0453+1559 companion contest (context)

— Lana, 2026-08-17 KST.


---

# AMENDMENT — 2026-08-21: the deciding-limb margin, corrected from ~21σ to 6.7σ

Duho: *"fix the C08 headline to say 6.7 sigma"*. **The verdict is unchanged. Only the confidence
figure moves.** Limb 2 still fires; the chain is still falsified as its source states it.

## Why

Two things surfaced in Phase 3 (`bhu-theory-phase3-cns-20260821/`, tracks gated
`PASS_P3A_AUDIT`, `PASS_P3B_TRACKB`, `PASS_P3C_TRACKC`):

1. **The masses this document headlined are from a preprint.** The "2026 update, accepted A&A
   (arXiv:2606.19276)" is Miao, Freire, Wex et al., now pinned at
   `bhu-theory-phase3-cns-20260821/sources/ar5iv_2606.19276.html`, sha256 `ad8fba27…`. **Its values
   are exactly right** — m_p = 1.599(8), m_c = 1.290(8), q = 0.807(8), verbatim from the abstract.
   But arXiv shows no journal_ref and no DOI, and INSPIRE has no publication_info. It is not, today,
   a published paper. The published measurement of record remains Ferdman et al. 2020, Nature 583,
   211: 1.62 ± 0.03 and 1.27 ± 0.03.
2. **The source's own caveat is quantified.** §4 above treated "(modulo some small additional shift
   by He red giant)" as unquantifiable. Brown, Lee & Rho's companion paper (Phys. Rept. 462 §3.2)
   puts it at 0.1–0.2 M⊙ — but Tauris et al. 2017 budget total accretion onto the first-born NS at
   **0.0134 M⊙**, overstating it 7–15×. The generous ceiling is therefore 4% + 0.0134 M⊙, not a bare
   4%, and not the proviso's figure.

## The four readings

| masses | ceiling | exceedance |
|---|---|---|
| Miao+ 2026 (preprint) | bare 4% — *as originally computed here* | 22.8σ |
| Miao+ 2026 (preprint) | 4% + Tauris budget | 21.6σ |
| Ferdman+ 2020 (published) | bare 4% — this document's own criterion | 7.1σ |
| **Ferdman+ 2020 (published)** | **4% + Tauris budget** | **6.7σ** |

**6.7σ is the operative figure**: the published measurement, against the most source-generous ceiling
the literature supports. 7.1σ is the same correction with this document's original bare-4% criterion,
recorded so the two changes are not conflated — one is a source-class fix, the other a ceiling that
Phase 3 established after this document was written.

## What is NOT amended

- The verdict: **Outcome 1, the mass evidence falsifies the chain as the source states it.** Limb 2
  fires at every reading in the table.
- The pre-registered criterion, which was sealed before the harvest and is not retrofitted here.
- Limb 1's serious-doubt tier, and the per-link verdicts.
- The reading rule from C02: "BHU is falsified" would be false and is still not said.

## One thing this document got right that Phase 3 confirms

It disclosed the He-giant caveat unprompted (§4) rather than hiding it, and argued around it. The gap
was not diligence — the caveat's quantification lives in a companion paper that was not in the lane.

— Tori, 2026-08-21 KST. Amendment only; the 2026-08-17 gate (`PASS_C08_ADJUDICATION`) stands over
the original text, and this amendment was gated 2026-08-21 on a third model family — **`PASS_C08_AMENDMENT`**, `GATE_C08AMEND_VERDICT.md`. The gate confirmed no verdict, per-link ruling or sealed criterion moved; recomputed all four sigma rows independently (6.74σ against the stated 6.7σ); verified the Ferdman masses and Tauris per-phase maxima verbatim against the pinned sources; and found nothing laundered in under cover of the correction.
