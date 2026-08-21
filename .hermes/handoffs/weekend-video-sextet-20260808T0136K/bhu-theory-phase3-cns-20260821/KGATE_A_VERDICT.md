PASS_P3A

# K-Gate A — third-engine review of Track A (Brown, Lee & Rho 2008 audit), post-both-repairs

**Verdict: PASS.** I re-derived my own view from `sources/blr_clean.txt` and the artifacts, not
from the two prior verdicts. The current state is correct on every check I could run: quote
fidelity holds (including the rewritten H1), the receipt reproduces and I confirm both numbers
independently, the load-bearing set of 5 is anchored in the paper's own abstract rather than in
its critics, the overclaim sweep is clean, and B-18 is nowhere leaned on as verified. Four minor
non-blocking items are recorded at the end. None rises to a HOLD.

I am a third model family: the author (Tori) and the first gate share one family, the
cross-engine gate was OpenAI (GPT-5.6/Codex), and I am Moonshot AI's Kimi K3. Where I agree with
an earlier verdict below, it is because the source agrees, and I say what I checked myself.

---

## Check 1 — QUOTE FIDELITY: PASS

**(a) No M_max derivation exists in the paper — B-5 (NOT-DERIVED-HERE) is correct.** I grepped
`blr_clean.txt` for `Tolman|integrat|we obtain|our calculation|dM_max|sensitivity` and read every
occurrence of the 1.5 M⊙ figure:
- Line 46: an EOS with kaon condensation near 3n₀ "when put in Tolman-Oppenheimer-Volkov equation,
  leads to" ≈1.5 M⊙ "**has been predicted** in several different ways" — reported, not performed.
  This is the paper's only TOV mention.
- Line 118: "Positing that it takes place at n∼3n₀, **BB obtain** the maximum upper mass to be
  M_max≈1.5 M⊙" — explicitly Brown & Bethe's result.
- Line 172–173: "This happens at near n≈3n₀ [BLR-kaon07] giving the BB maximum mass" — cited out.
No EOS function is written, no TOV integration is done, no mass-radius sequence, no dM_max/dn_c.
H1's "imported, cited to Brown & Bethe, ApJ 423 (1994) 659 and BLR, Phys. Rept. 462 (2008) 1"
matches the reference list (lines 210, 219). No HOLD from (a).

**(b) CNS citations confirmed.** Ref (5), line 222: "L. Smolin, The Life of The Cosmos, Oxford
University Press, New York and Oxford, 1997" — a general-audience book = Smo97. Ref (6), line 225:
"L. Smolin, Physica A 340 (2004) 705" = Smo04. I read all 24 reference entries (lines 209–291);
the only "1992" in the file is Schaller et al., A&AS 96 (1992) 269. **Smolin 1992, CQG 9, 173 is
nowhere cited.** H2 and the audit's "does not run through the CNS paper of record" are accurate.

**(c) §III inference, verbatim.** Line 69: "Now a fundamental law of nature is that a system moves
toward equilibrium in such a way as to maximize the entropy. Therefore, the maximum number of
black holes does the best, so far, in moving towards equilibrium." The audit's H3 quotation stops
at "does the best" — a truncation of the trailing adverbial, no change of meaning. Faithful.

**(c′) H1's rewritten wording — re-checked for over-correction, as instructed.** Current H1 quotes
BLR as saying the ≳2 M⊙ limb "would put in serious doubt or simply falsify" the chain. That is a
verbatim substring of line 24 ("would put in serious doubt or simply falsify the following chain
of predictions"). The repair did not overshoot in either direction: it neither strengthens the
modality (the old "the chain dies" pseudo-quote, now disclosed as an error in H1 and §6) nor
softens BLR's own words. One narrowing remains and is harmless: H1 calls the ≳2 M⊙ star "the
falsifier" where the abstract (lines 21–28) states a two-limb set (>4% DNS asymmetry **or**
≳2 M⊙). B-1 records both limbs, and I confirmed B-1 against the adjudication's verbatim abstract
(`C08_MASS_ADJUDICATION_20260817.md` §1) — they match. No distortion propagates.

## Check 2 — H3 FAIRNESS (the harshest check): the current H3 is fair; no HOLD

I argued the pro-BLR side from the source, as strongly as it can be argued:
- §III's own title flags analogy, not entailment: "Maximization of Black Holes **≈** Maximization
  of the Entropy" (line 54).
- BLR explicitly decline the mechanism: "We are not in a position, nor is it our objective, to
  address the basic questions associated with the scenario … What we can address is one of the
  falsifiable predictions" (line 52).
- The actual CNS requirement is sourced to Smolin, not to the second law: "the upper mass limit
  of neutron stars be as low as possible" (line 50, Smo04) and the falsifiable prediction
  (line 44, Smo97;Smo04).
- §III ends by *posing* the question ("One, what is the lowest upper mass of neutron star?; two,
  what is the maximum upper mass?", line 71) — BLR treat entropy as motivation for asking, not as
  the derivation of the answer.

So §III is a motivating remark, and the current H3 says exactly that: it keeps the non-sequitur
criticism only under an explicit condition ("Read as parameter selection … the second law governs
how a system evolves, not which Standard Model parameters obtain"), states "BLR do not offer it as
a derivation," routes the CNS link through B-17/B-18, and withdraws the old "does not do the work
the chain needs." I also probed the opposite failure — did the repair make H3 too *soft*? It did
not: the withdrawn claim is precisely the one the source refutes, and the defensible criticism of
the one sentence survives. A reasonable referee would not call the current H3 overstated. B-9's
demotion to secondary stands.

## Check 3 + the added attack — THE LOAD-BEARING SET OF 5: correct, and anchored in the paper

The trajectory 7 → 4 → 5 invites the suspicion that the set was tuned to fit its critics. It was
not, and the reason is checkable: the 5 rows are the abstract's own enumerated chain (lines
24–28), one row per link with link (4) split into its two distinct textual moments:
- link (1) "nearly vanishing vector meson mass at chiral restoration" → **B-2** (lines 150–154);
- link (2) "kaon condensation at a density n∼3n₀" → **B-4** (the number, line 172, cited to
  BLR-kaon07; the mechanism B-3 is standard physics and correctly not load-bearing);
- link (3) "the Brown-Bethe maximum neutron star mass M_max≈1.5 M⊙" → **B-5**;
- link (4) "Smolin's CNS hypothesis" → **B-17** (the requirement, line 50) + **B-18** (the quoted
  prediction, line 44).

That mapping is the paper's table of contents, not a critic's construction. The two error
directions that produced 7 and then 4 are also now correctly understood and disclosed in the
audit itself: 7 over-included a heuristic (B-9), a lower-bound side argument (B-12), and
miscounted an unread citation (B-18) as failing; 4 over-corrected by erasing B-18's structural
role. 5 separates the axes properly: B-18 is load-bearing (it is BLR's *direct* CNS falsifier,
line 44) **and** unverified (Smo97/Smo04 unopened). I attacked the boundaries for completeness:
B-1 is the test, not a link (duplicative of the four); B-10 is an observational floor, not a
chain step; B-21 is a separate, author-flagged-untrustworthy route ("the models used are not
quantitatively trustworthy," line 200), not the fired falsifier's path. Nothing is missing and
nothing is extra. The old 7/7 echo of Phase 2 is gone from the register of record; what remains —
"falsifiable content and derived content are disjoint" — is verified against the source (B-5 is
genuinely NOT-DERIVED-HERE), so the surviving parallel to Phase 2 is real, not shaped.

## Check 4 — NORMAL-PRACTICE FAIRNESS: PASS

H1 (lines 16–18): "This is normal practice for a 4-page note — but it means the *falsifiable*
content and the *derived* content of this paper are disjoint sets." The JSON contract (line 7)
adds: "There is no failing count. An imported citation is not a defect in a 4-page note…"
Ordinary citation practice is acknowledged, not indicted.

## Check 5 — RECEIPT: PASS, independently recomputed

`python3 receipts/r1_entropy.py` → `1.0494e+77 k_B` (dev 0.05%), ratio `1.049e+20`, `R1 PASS`,
exit 0. My own 50-digit Decimal recomputation from G, ħ, c, M⊙, two independent routes:
- direct: `4πG M⊙²/(ħc) = 1.0494297066288976505372915741…×10⁷⁷`;
- via the horizon: `r_s=2GM/c²`, `A=4πr_s²`, `ℓ_P²=ℏG/c³`, `A/(4ℓ_P²)` = identical to all 50 digits.
Against the printed 1.05×10⁷⁷ (line 63): 0.054% with the receipt's M⊙=1.98892×10³⁰; 0.0995% with
the modern IAU nominal 1.98847×10³⁰ — H4's "robust to the modern M⊙" holds. Ratio to the ~10⁵⁷
k_B Fe-core figure (line 55): 1.0494×10²⁰ vs the printed 10²⁰ (line 67). B-7, B-8, H4 stand.

## Check 6 — OVERCLAIM SWEEP: PASS (clean)

Grepped the audit for `falsified|BHU|generalis|generaliz|disprov|refut|chain dies|7 of 7|7/7`.
Every live hit is either about *the chain as the source states it* (§2, line 84, immediately
qualified by "narrower and sharper"), a source report (B-21), or inside the §5/§6 gate records
narrating what was removed. **No sentence claims CNS itself is falsified, and nothing generalises
to black-hole-universe cosmology.** The standing rule ("BHU is falsified" is false and never said)
is not violated. Track C is left explicitly open (lines 92–95).

## Check 7 — B-18 NOT LEANED ON: PASS

B-18 is UNVERIFIED-AT-GATE in both prose and JSON; §2 (lines 92–95) states the Smolin sources are
unopened and the CNS entailment "is therefore still an open question after this audit, not a
settled one. That is Track C's job." Nothing downstream treats the quote as established. The
silent typo correction of BLR's "scnario" → "scenario" (line 44) does not change meaning.

## Machine-state verification (beyond the assigned checks)

- `verdicts.json`'s `source_sha256` (`d191ff01…7e0d`) equals `shasum -a 256 TRACK_A_AUDIT.md` —
  the tally is pinned to the current prose, not a stale draft.
- I reran `extract_verdicts.py` on copied inputs in a scratch dir outside the lane: the
  regenerated JSON is byte-identical to the committed file; self-report "22 rows | load-bearing 5,
  of which imported-not-derived: 4 | unverified: 1"; tally sums to 22; per-row verdicts match the
  audit table cell-for-cell on my read.

## Minor findings — recorded, non-blocking

1. **B-17's evidence cell over-attributes by one citation.** The specific sentence "the upper mass
   limit of neutron stars be as low as possible" is cited in the source to **Smo04 only**
   (line 50); Smo97 attaches to the theory statement (line 49) and to the prediction quote
   (line 44, "Smo97 ; Smo04"). The cell "Smo97 (popular book) + Smo04 (Physica A)" and H2's "half
   of that support is inadmissible" are true of link (4) as a whole, but strictly the
   *requirement* sentence rests on the peer-reviewed half alone. This slightly weakens the
   popular-book punch for B-17 while leaving it intact for B-18; it changes no verdict.
2. **Per-row `passing:false` booleans persist** on the imported/unverified rows, in residual
   tension with the contract's "an imported citation is not a defect." Both prior reviewers
   flagged this as non-blocking; I independently agree — the aggregate pejorative count is gone
   and the contract forbids deriving one. A schema-level smell, not an overclaim.
3. **H5's "The revision is real and now uncontroversial"** is a present-day claim not established
   by the 2008 text. UNVERIFIED-AT-GATE here (no network), as the cross-engine gate also marked
   it. A side remark; nothing load-bearing rests on it.
4. **Cosmetic:** section numbering runs 0,1,2,3,5,6,4 (gate records appended before the
   constraints receipt). No content impact.

## UNVERIFIED-AT-GATE at this review

- The substance of Smolin 1997/2004 (does Smolin actually say the quoted prediction) — primary
  sources not in the lane; correctly tagged B-18 UNVERIFIED-AT-GATE and nothing leans on it.
- H5's present-day clause (finding 3 above).
- External scientific correctness of rows graded "standard"/"published values" (B-6, B-13, B-14,
  B-16) — I verified fidelity to BLR's text, not the primary literature behind them.
- The 2026-08-17 adjudication was consulted, not re-litigated, per instruction.

## Boundaries receipt

Reads only within the lane plus the permitted adjudication context. No network; `portal.nersc.gov`
untouched. Exactly one file written: this verdict (scratch regeneration ran in /tmp outside the
lane and was removed). `GATE_A_VERDICT.md`, `REGATE_A_VERDICT.md`, `XGATE_A_VERDICT.md` read only.
Nothing committed, published, or uploaded. "BHU is falsified" is false and is not said here.

— Third-engine reviewer: **Kimi K3 (Moonshot AI)**, via Hermes, 2026-08-21 KST.
Signed. Findings only; nothing fixed. Engine distinct from the author's family and from the
cross-engine gate's (OpenAI).
