B2_REVIEW=AMENDMENT_STANDS

# KIMI B2 CHALLENGE — adversarial review of AMENDMENT A, B2 closure, and the scope qualification
**Referee: Kimi (k3), 2026-09-07. Target: `B1_RESULT_V2_20260907.md` AMENDMENT A, `B2_CLOSURE_20260907.md`,
`b2_closure.py`, `B1_SCOPE_QUALIFICATION_20260907.md`. I did not produce this algebra. I re-derived what I checked.**

## 0. What I inspected and ran

- Source paper: N. J. Popławski, *Gen. Relativ. Gravit.* **53**, 18 (2021) — peer-reviewed journal article.
  Equation claims here are bound to **arXiv:2007.11556v2 HTML (v2 dated 23 Jun 2026), read by me 2026-09-07** —
  an author-posted hosted copy self-identifying as the published version. I read that **extraction**, and separately
  reached the **Springer publisher page** (link.springer.com/article/10.1007/s10714-021-02790-7): it confirms only the
  metadata (journal, volume, article number, 07 Feb 2021, title, abstract); the full text is subscription-walled, so
  **equation-level identity with the version of record is NOT established** — same binding as the filing itself.
  Bounded errata search: none found; absence of a later correction is NOT inferred.
- `b2_closure.py`: re-run from `bounce/` with /usr/bin/python3 + SymPy, exit 0, all residuals zero, tokens as filed.
- My own independent script `kimi_b2_independent_check.py` (same directory, no imports from theirs): exit 0.
  It re-derives the (14) expansion from the printed form, the factorisation, the compatibility residual, both branch
  realisations including (11) with derivative terms, the β tunings, constraint-propagation identities with an
  UNSUBSTITUTED ῥ (see §2), the case (b)/(c) matter systems, and the full count table.
- Prior art cited for the no-production structure (Kopczyński PLA 43, 63 (1973); Tafel PLA 45, 341 (1973);
  Kuchowicz J. Phys. A 8, L29 (1975); Hehl et al. RMP 48, 393 (1976)) is peer-reviewed; I did not re-read those
  for this challenge — the attacks below are algebraic and do not rely on them.

## 1. ATTACK: "The special branch carries no bounce" — the gluing question. Survives; stated reason is incomplete.

I tried to break this four ways.

**(a) Is H really forced constant on the branch?** Yes. On an interval with Ψ≠0: N=0 with ṅ=0 gives Ψ=3Hn_*;
the prescription Ψ=βH⁴ then gives H(βH³−3n_*)=0. H=0 forces Ψ=0 (contradiction with production), so
H³=3n_*/β>0 — a unique real positive root, constant because β and n_* are constants. **H=0 is excluded on the
branch** precisely because Ψ=3Hn_* would then vanish. Re-derived (PART 1 of my script).

**(b) Could a solution LEAVE or JOIN the branch at finite time, so a bouncing solution touches it?** This is the
attack that matters, and the amendment's stated reason — "H is constant and non-zero on that branch, so it never
crosses zero" — does **not** answer it; read strictly, that sentence is a non-sequitur against gluing (a branch with
no turning point can still be visited by a bouncing trajectory that departs it). Neither B2 nor the amendment proves
non-gluing. I therefore proved it myself from the filed assumptions (smooth functions on a connected open interval I,
T>0, Ψ=βH⁴ with fixed β>0), and the attack FAILS:

- On U={A(T)≠0} (open), E=0 gives Ṫ=−HT and (37) then gives βH⁴=0, so H≡0 on U.
- On W=int{T=T_*}, (37) gives βH³=3n_*, so H≡H_*>0 on W.
- Hence {H≠0}⊆W, is open, and H≡H_* on each component. A component with an endpoint τ interior to I would have
  H(τ)=0 (definition of a component boundary) yet H→H_*≠0 along the component — contradicting continuity.
  So {H≠0} is ∅ or all of I.
- H≡0 on I is impossible in **both** geometries (PART 2): in KS, H≡0 ⇒ u=−2v, matter constant (Ṅ=0, ρ̇=−3H(ρ+P)=0),
  and H-preservation plus the constraint force κP₀=−3v²−K/3, κρ₀=K−3v²; constancy of ρ₀,P₀ then forces v=0, after
  which the v-equation reads v̇=−K/3≠0 since K=1/Y²>0 — contradiction. In flat BI, H≡0 ⇒ Ḣ_i=κ(ρ−P)/2=0, and
  ρ−P=ε−p=2ε/3, so ε=0, i.e. T=0 — excluded.
- Therefore **every smooth interval solution has H≡H_*>0 and T≡T_***: no solution ever crosses H=0, no bouncing
  solution exists at all (in either geometry), and there is nothing to glue the branch to. Junctions would also
  violate the smoothness the system is posed in.

So the CONCLUSION is correct and in fact stronger than claimed — but the one-sentence justification in the amendment
is insufficient as written; the non-gluing lemma is unstated in both documents. Reported, not repaired.

**(c) Scope dependence.** The entire exclusion rests on smoothness and on the fixed-β prescription. With a free
Ψ(t) that can vanish on an interval, the evolving branch Ṫ=−HT exists and a C⁰-gluing at a tuned instant (kink in Ṫ)
is not excluded by the matter equations. B2 discloses this exactly ("A free Ψ(t) or a variable β(t) would change the
answer"); **the amendment text does not restate it** — a reader of V2+Amendment alone could over-read "every bouncing
one is excluded" as prescription-independent. Wording gap, not an error.

**(d) Terminology nit.** "de Sitter-like": the KS realisation has constant NONZERO shear S=Λ_*/3 (disclosed in B2)
and Y=Λ_*^{−1/2} constant; it is not constant-curvature de Sitter. Hedged with "-like"; nit only.

## 2. ATTACK: the counting. Verified independently; one caveat.

- **All eight table rows reproduce** (PART 6): KS 8 unknowns/6 evolution (a: excess +1; b,c: 0; d: −1 with 7 unknowns);
  flat BI 10 unknowns/8 evolution (a: +1; b,c: 0; d: −1 with 9).
- **Are there uncounted independent equations?** No. I checked each candidate against the printed text:
  (11) is exactly (10)₃−(10)₂ (paper says so; verified algebraically including derivative terms);
  (36) is the (10)₁ constraint after thermal substitution; (37) is (34) with n=h_nT³ (paper: "follows from the first
  equation in (34)"); (38) is a rewrite of (37); (17) is (14) restated via (1). None is an independent addition.
- **Is E=0 legitimately counted as an evolution equation?** Yes, and this was worth checking because (14) is derived
  from (10). With ῥ left symbolic I get the exact identities (PART 4):
  Ċ_K+3HC_K = −κ(ρ̇+3H(ρ+P)) = −κE (KS, modulo the spatial equations), and Ċ_B+6HC_B = −κE (BI).
  So E is precisely the propagator of the constraint: without imposing E, C=0 on initial data would not propagate.
  B2's warning not to double-count (14) alongside the field system AND the differentiated constraint is exactly right.
- **K=1/Y², H=(u+2v)/3, Ψ=βH⁴** are definitions/specified functions, not unknowns. Correct.
- **Case (a): exactly one compatibility condition?** At function level, yes — the excess is one, and the residual
  −2ΨT(3αh_n²T²−2h*)/(3h_n) is a single functional condition. CAVEAT: after it is imposed (T=T_*), existence of the
  steady state additionally requires the constant-level tuning β=81n_*/Λ_*^{3/2} (KS) or β=9√3 n_*/Λ_*^{3/2} (BI)
  (my PART 3; ratio 3√3). That is a second, parameter-level condition — disclosed in the amendment ("βH³=3n_*",
  "tuned β") and in B2, but "exactly ONE compatibility condition" alone would mislead if read in isolation.
- **Case (b): does dropping n=h_nT³ leave n unsourced?** No. N=0 sources n (ṅ=βH⁴−3Hn); E sources T;
  the derivative matrix has determinant F′=4h*T³>0; my independent residual is zero and
  Ṫ=αβnH⁴/(2h*T³)−HT matches B2. Determined, as filed.

## 3. ATTACK: the narrowing to "the bouncing sector". Loopholes closed — and the exclusion is BROADER than filed.

- **Evolving-temperature solutions with Ψ≠0 only somewhere:** wherever Ψ≠0, T=T_* is forced (§1b), so no evolving
  production interval exists. "Production switches on and off": under Ψ=βH⁴, Ψ(t)=0 ⟺ H(t)=0, and since H≡H_*>0 on
  every solution, switching never occurs. "Ψ≠0 only on a measure-zero set": {Ψ≠0}={H≠0} is open (H continuous), so
  measure-zero ⟺ empty; then H≡0, excluded per §1b in both geometries. All three loopholes are closed — by the
  assumptions, which B2 states and the amendment incorporates by reference but does not restate.
- **The narrowing sentence understates the result.** The algebra excludes EVERY evolving interval solution of the
  printed thermal specialisation at fixed β>0 — bouncing or not, static included (§1b) — and at any β off the single
  tuned value the printed KS system has NO smooth interval solutions at all. The amendment's own sentence "the only
  solutions satisfying it are the tuned steady state above" says this; the next sentence ("`B1_ILL_POSED` ... holds for
  the bouncing sector") then weakens it inconsistently. The imprecision favors the filing (underclaim, not overclaim).

## 4. ATTACK: does the scope qualification over-correct? No.

The a⁻⁶ degeneracy supports: (i) the dynamical-unattainability statement — kept by the qualification, correctly;
(ii) the critical surface ρ=1 being invariant and codimension-1 — a genericity-adjacent fact about the BOUNDARY, not
about bounces; (iii) the bounce region being an OPEN subset of initial-data space — which under any smooth measure has
positive measure, so the degeneracy does not even weakly support bounce "improbability". I find no sense in which the
degeneracy licenses a genericity claim the qualification wrongly disclaims; if anything, (iii) reinforces the
disclaimer's direction. Keeping the pre-registered class NAME while disclaiming the measure reading is defensible
pre-registration hygiene.

## 5. Claimed-loosely and shown-but-not-claimed

- Claimed, justification incomplete in text: the no-bounce conclusion (non-sequitur re gluing; gap closable from filed
  assumptions — §1b — but not closed in either document).
- Claimed loosely (all disclosed nearby or in B2): "exactly ONE compatibility condition" (function-level only; the β
  tuning is a second, parameter-level condition); "narrowed ... to the bouncing sector" (understates; §3);
  "de Sitter-like" (KS realisation has constant nonzero shear).
- Shown by the algebra (mine, re-derived; consistent with B2's residuals) but NOT claimed anywhere in the filing:
  (i) no H≡0 interval can exist in either geometry under the printed thermal specialisation (KS: K>0 contradiction;
  BI: ε=0); (ii) consequently, at fixed β>0 off the single tuned value the printed system has no interval solutions
  at all — the paper's §9 evolutionary narrative (collapse → bounce → cycles → inflation) has no smooth solution on
  any open interval as printed, a statement strictly stronger than "ill-posed for the bouncing sector";
  (iii) the propagation identities Ċ_K+3HC_K=−κE and Ċ_B+6HC_B=−κE hold with UNSUBSTITUTED ῥ, i.e. the first law is
  exactly the constraint propagator (B2 asserts propagation; the exact equivalence is not stated).

## 6. Why not WRONG or UNSUPPORTED

WRONG requires a false claim. I found none within the declared assumptions: branch existence, both realisations, both
β tunings, the exclusion of evolving/bouncing production solutions, all eight count rows, and CLOSURE_SUFFICIENT=b,c
all reproduce independently, and the script tokens match a fresh run (exit 0). UNSUPPORTED requires the algebra not to
back the claims; it backs them — the defects are an unstated lemma (gluing), an unrestated scope dependence
(fixed-β, smoothness), and three disclosed-or-understated wording issues. None is fatal. I attempted to break the
amendment hardest at the gluing point and the attempt instead strengthened it.

**B2_REVIEW=AMENDMENT_STANDS**
