# Track A — equation-by-equation audit of Brown, Lee & Rho (2008)

**Source of record:** Brown, Lee & Rho, *"Kaon Condensation, Black Holes and Cosmological Natural
Selection,"* PRL **101**, 091101 (2008); arXiv:0802.2997**v2**, full text in `sources/`
(`blr_clean.txt`, extracted from the ar5iv render of the v2 source).
**Scope:** the derivations, not the claims — the claims were adjudicated on 2026-08-17 and that
verdict is not reopened here.

## 0. Headline findings

**H1 — The paper contains no derivation of the number its own falsifier tests.** The falsifier is a
neutron star ≳ 2 M⊙, which BLR say "would put in serious doubt or simply falsify" the chain — graded
wording I earlier compressed to "the chain dies" inside quotation marks, which overstated their
modality. *(Corrected after the cross-engine gate.)* The chain's quantitative core is
M_max^BB ≈ 1.5 M⊙. That number is **imported**, cited to Brown & Bethe, ApJ **423** (1994) 659 and
BLR, Phys. Rept. **462** (2008) 1. There is no TOV integration in this paper, no equation of state
written down, and no sensitivity of M_max to n_c. Links (1) and (2) are likewise asserted by
citation (Harada–Yamawaki for the vector manifestation; BLR-kaon07 for n ≈ 3n₀). This is normal
practice for a 4-page note — but it means the *falsifiable* content and the *derived* content of
this paper are disjoint sets.

**H2 — The CNS link rests on a popular book.** Link (4) — that CNS requires the neutron-star upper
mass limit to be "as low as possible" — is sourced to `Smo97` = Smolin, *The Life of the Cosmos*
(Oxford University Press, 1997), a general-audience book, and `Smo04` = Smolin, Physica A **340**
(2004) 705. Under our own standing rule (peer-reviewed journal articles are the base layer;
popular-science works are context, never a base source) half of that support is inadmissible.
**Note also: this paper never cites Smolin 1992, CQG 9, 173** — our bibliography's entry 6, and the
paper we came here to audit alongside it. The CNS attribution in the falsifying paper does not run
through the CNS paper of record.

**H3 — Section III's entropy argument is a loose sentence, not a load-bearing step.**
BLR motivate maximizing black holes thermodynamically: black-hole entropy exceeds Fe-core entropy by
~10²⁰ per particle, and then — "a fundamental law of nature is that a system moves toward
equilibrium in such a way as to maximize the entropy. Therefore, the maximum number of black holes
does the best". Read as parameter selection that inference is a non-sequitur: the second law governs
how a system evolves, not which Standard Model parameters obtain. **But BLR do not offer it as a
derivation, and this audit originally said they did.** The section is titled with an approximation
sign ("Maximization of Black Holes ≈ Maximization of the Entropy"), and §II states plainly that they
will not address CNS's mechanism at all — "We are not in a position, nor is it our objective…". The
CNS link runs through B-17/B-18 (Smolin's own stated requirement), not through §III. The
non-sequitur stands as a criticism of one sentence; the claim that it "does not do the work the
chain needs" was overstated and is withdrawn. *(Corrected after Gate A — see §5.)*

**H4 — The numbers this paper does derive are correct.** Eq. (2) recomputes to 1.0494×10⁷⁷ k_B
against the printed 1.05×10⁷⁷ (0.05%, robust to the modern M⊙), and the stated 10²⁰ entropy ratio
recomputes to 1.049×10²⁰. Where BLR compute, they are right; the chain's weight simply does not
rest there.

**H5 — The strongest counterexample of its day is dismissed via a conference talk.** PSR
J0751+1807 at 2.1 ± 0.2 M⊙ — which the paper concedes "would have been a clean falsification of the
BB theory as well as the CNS idea" — is set aside on a revision to 1.26 M⊙ sourced to a talk at a
2007 meeting, cited by URL. The revision is real and now uncontroversial, but at the time of
publication the paper's survival rested on unrefereed material.

## 1. Claim-by-claim verdicts

| # | Step | Verdict | Evidence |
|---|---|---|---|
| B-1 | Abstract: two-limb falsifier set (>4% DNS asymmetry **or** M ≳ 2 M⊙) | CHECK | Verbatim; matches the 2026-08-17 adjudication's quotation |
| B-2 | Link (1): vector manifestation — hidden gauge coupling → 0 near chiral restoration | ASSUMED-FROM-CITATION | Harada–Yamawaki PRL 86, 757; Phys. Rept. 381, 1. Not derived here. **Load-bearing** |
| B-3 | Link (2): kaons condense when μ_e reaches the in-medium kaon mass, via e⁻ → K⁻ + ν_e | CHECK-AS-MECHANISM | The mechanism is stated correctly and is standard; the *density* is not derived |
| B-4 | Link (2), the number: n_c ≈ 3n₀ | CITED-NUMERICS | Cited to BLR-kaon07. No calculation in this paper. **Load-bearing** |
| B-5 | Link (3): M_max^BB ≈ 1.5 M⊙ from TOV with the kaon-condensed EOS | NOT-DERIVED-HERE | Imported from Brown & Bethe 1994. No EOS, no TOV, no dM_max/dn_c. **Load-bearing** |
| B-6 | Eq. (1) Bekenstein entropy S_H = (k_B/4)·A/ℓ_P² | CHECK | Standard |
| B-7 | Eq. (2) S_H = 1.05×10⁷⁷ k_B (M/M⊙)² | CHECK | Recomputed 1.0494×10⁷⁷ (receipt R1); 0.05% |
| B-8 | "entropy increased by a factor of 10²⁰ per particle" | CHECK | Recomputed 1.049×10²⁰ (receipt R1) |
| B-9 | §III: second law ⇒ black-hole number is maximized | UNSUPPORTED | Non-sequitur if read as parameter selection — but authors flag §III with "≈" and disclaim the mechanism in §II. **Secondary, not chain-critical** (Gate A) |
| B-10 | §IV: M_max cannot be much below ~1.44 M⊙ because the Hulse–Taylor pulsar exists | CHECK | Valid observational floor |
| B-11 | §IV: lowering M_max moves BH onset below ZAMS 18 M⊙ ⇒ less galactic ¹²C | CHECK-AS-ASTROPHYSICS | The astrophysics is defensible |
| B-12 | …and that therefore M_max should not be lower | UNSUPPORTED | BLR do give a qualitative bridge — massive-star production "must be extremized, in order to produce the maximum number of black holes", and that production depends on carbon/oxygen cooling — but it is never quantified or its direction established, so the step remains unsupported rather than absent. Bounds M_max from *below*, which neither fired limb tests. **Secondary** (Gate A; wording corrected at the cross-engine gate) |
| B-13 | Eqs. (3)–(5): 3α → ¹²C, ¹²C(α,γ)¹⁶O, ¹²C+¹²C → ²⁴Mg; 20 keV vs 80 keV | CHECK | Standard nuclear astrophysics |
| B-14 | ν-pair emission cross-section ∝ T¹¹ | CITED | Bethe 1979 |
| B-15 | 3-body rate ∝ ρ², ¹²C removal ∝ ρ; equality at ZAMS ~18 M⊙ | CITED-NUMERICS | Bro01; not recomputed here |
| B-16 | Kunz et al. 165 ± 50 keV·b vs Caughlan–Fowler 100 keV·b | CHECK | Published values |
| B-17 | Link (4): CNS requires the NS upper mass limit "as low as possible" | ASSUMED-FROM-CITATION | Smo97 (*popular book*) + Smo04 (Physica A). **Load-bearing** |
| B-18 | Quoted Smolin prediction: a star appreciably above M_max^BB "will count against the CNS scenario" | UNVERIFIED-AT-GATE | Attributed to Smo97/Smo04; neither read by us. **Load-bearing AND unverified** — it is BLR's direct CNS falsifier, so it carries the link structurally; not having read it is a verification state, not a demotion. Demoting it conflated the two. (cross-engine gate) |
| B-19 | PSR J0751+1807 revised 2.1 ± 0.2 → 1.26 M⊙ | CHECK-AS-REPORTED | Sourced to a conference talk URL, not a refereed paper (H5) |
| B-20 | "no smoking-gun evidence against the BB scenario" | CHECK-AS-OF-2008 | Superseded by the 2026-08-17 adjudication |
| B-21 | CCS/LIGO route: stiff EOS ⇒ kaon condensation pushed to ≳ 7n₀ ⇒ BB falsified | CITED / AUTHOR-FLAGGED | Authors state "the models used are not quantitatively trustworthy" |
| B-22 | Closing "web of falsifiable connections" summary | CHECK | Fair summary of what precedes it |

## 2. What this does to the chain

The 2026-08-17 adjudication falsified the chain **as the source states it**, on the source's own
limb 2. This audit says something narrower and sharper about *why that was so easy*: links (1)→(3)
were never load-bearing derivations in this paper to begin with. The paper's contribution is the
*falsifier set*, not the physics behind it — and the falsifier set is the part that has now fired.

The consequence for Track B is concrete: **re-deriving M_max must go to Brown & Bethe 1994 and
Phys. Rept. 462, not to this paper.** There is nothing here to re-derive.

The consequence for Track C is sharper still. B-17 and B-18 are the entire link from a
neutron-star mass to Smolin's hypothesis, and both are citations we have not yet opened — one of
them to a popular book, and neither to Smolin 1992. **Whether CNS actually entails a low M_max is
therefore still an open question after this audit, not a settled one.** That is Track C's job.

## 3. Receipts

- **R1** (`receipts/r1_entropy.py`): Eq. (2) and the 10²⁰ ratio, recomputed from G, ħ, c, M⊙.

## 5. Gate record — HOLD, and what I accepted

Gate A returned **HOLD_P3A_LOADBEARING** (`GATE_A_VERDICT.md`). It confirmed quote fidelity, the
receipt (recomputed two independent ways, agreeing to machine precision), H1, H2, and a clean
overclaim sweep — and then found that the headline number was not honestly earned:

> "I find the set was shaped, whether deliberately or by motivated construction, to reproduce the
> earlier 7/7 finding."

I accept that. Every one of the four repairs is the gate's, not mine:

1. **B-18 removed from the failing count.** UNVERIFIED-AT-GATE is an unread citation, not a failure.
   Counting it was the tally leaning on B-18 in exactly the way this prose refuses to.
2. **B-9 demoted.** §III's entropy remark is a motivating gloss; the authors' own "≈" and their §II
   disclaimer say so. Calling it load-bearing attributed to BLR a derivation they declined to make.
3. **B-12 demoted.** The carbon/LUM argument bounds M_max from below, and neither limb of the
   falsifier that actually fired tests a lower bound.
4. **`n_load_bearing_failing` retired.** The prose called citation-import normal practice for a
   4-page note while the tally called the same rows failures; both cannot be the register of record.
   The field is now `n_load_bearing_imported`, which is true and carries no pejorative.

**After repair: 4 load-bearing rows (B-2, B-4, B-5, B-17), all imported rather than derived, and
1 unverified.** No "7 of 7". The spine the gate upheld — H1, the receipt, the narrower-and-sharper
framing, and Track C left open — is untouched, and it is the part worth having.

## 6. Cross-engine gate — the same-family gates were not enough

Re-gated on a different engine (OpenAI Codex) after all three Phase 3 gates turned out to be
fresh-context readers from the author's own model family. Tracks B and C passed cross-engine
unchanged. **Track A held again**, on three findings the same-family re-gate had approved:

1. **The B-18 repair overshot, in the opposite direction from the original error.** I had demoted it
   from load-bearing because it was unverified. Structural importance and verification status are
   different axes: B-18 is BLR's *direct* CNS falsifier and carries the entire link, whether or not
   we have read the source. Restored to load-bearing **and** unverified. Load-bearing is now 5, of
   which 4 are imported-not-derived and 1 unverified.
2. **A quote-fidelity defect in my own headline.** I compressed BLR's "would put in serious doubt or
   simply falsify" into "the chain dies" — and put it in quotation marks. That strengthens their
   modality into unconditional falsification. Corrected in H1.
3. **B-12 was too absolute.** BLR do give a qualitative bridge from carbon to black-hole count
   (massive-star production "must be extremized"; that production depends on carbon/oxygen cooling).
   It is unquantified, so the step is unsupported — but not absent, which is what I wrote.

Worth recording why this matters beyond the three fixes: the same-family re-gate explicitly checked
whether I had over-corrected and concluded I had not. A different engine found that I had, on B-18,
in the same pass where it caught a quotation I had strengthened. One model family checking its own
work missed both.

## 4. Constraints receipt

Literature hosts only; `portal.nersc.gov` untouched. No new observations. Source text was already
on disk from the 2026-08-11 re-verification; nothing re-fetched. Writes confined to this lane.
Nothing committed, published or uploaded.

— Tori, 2026-08-21 KST. Audit only; nothing derived beyond verification arithmetic.
