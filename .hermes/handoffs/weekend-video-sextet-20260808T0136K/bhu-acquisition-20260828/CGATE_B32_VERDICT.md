CANDIDATE_NARROWED_ENTRY57_NOT_PROOF_OWNER

# B32 adversarial verdict

I read entry 57 **in full**, all 39 PDF pages, sequentially with PyMuPDF (`fitz`). The journal/volume/page resolution is correct: entry 38 reference [15] is entry 57, Smoller & Temple, *Arch. Rational Mech. Anal.* 138 (1997), 239–277. But entry 57 does **not** prove that a standard TOV metric cannot be continued into a black hole. It assumes the exterior domain `A>0`, repeatedly makes that restriction part of its hypotheses, and never proves noncontinuability across `A=0` or nonexistence for `A<0`.

The candidate therefore survives only in narrowed form: entry 38 contains important unrecorded limitation claims, but entry 57 is not their proof owner and should not be promoted to `THEORETICAL-OBSTRUCTION` on this attribution.

## 1. What entry 57 actually proves

Entry 57 is a constructive and admissibility paper. Its progression across the full text is:

- Sections 1–2 set up an FRW interior matched to a static Oppenheimer–Tolman exterior and review the Lipschitz matching and conservation constraint.
- The paper explicitly says, near the beginning, that it restricts attention to shocks **outside the Schwarzschild radius**, `A>0`.
- Theorem 1 assumes `A(r̄0)>0`; the text then says conditions (2.20)–(2.22), including `A>0`, are implicit for every shock discussed thereafter.
- Theorems 4–7 derive the conservation constraint, pressure branches, and an equivalent autonomous shock ODE system under those hypotheses.
- Theorems 8–12 derive subluminality, Lax-admissibility, existence domains, equation-of-state freedom, and the FRW sound-speed formula.
- Theorem 13 proves a real exclusion **within the exterior construction**: for `A>0`, the branch with outer density `q̄>q` has negative squared sound speed and is physically inadmissible. The paper also rules out its `p−` pressure branch because its shock speed exceeds light speed.

None of those results is the claimed TOV-continuation theorem. Most decisively, the paper does not analyze a continuation through `A=0`: it excludes that surface from its domain. Theorem 9's phrase “the only obstruction to existence” refers to the local shock ODEs under the already imposed exterior assumptions and identifies `H=1`; it is not a global theorem about extending a standard TOV spacetime into `A<0`.

An assumption that keeps the analysis outside the horizon is not a proof that continuation is impossible. Nor do the exterior branch exclusions prove it. Entry 57 therefore remains correctly described at paper level as `CONSISTENCY-ONLY`, with claim-level parameter/branch exclusions recorded if the bibliography is meant to preserve them.

**Ruling on the main ask: entry 57 does not prove the TOV-continuation result.**

## 2. Citation resolution and where the warrant actually appears

The brief's bibliographic resolution is not the failure. Entry 38 reference [15] gives the same authors, journal, volume 138, pages 239–277, and year 1997 as the pinned entry-57 PDF. The slightly different title does not change that identity.

The problem is the attribution. Entry 38 says both that the result was proved in [15] and, later, that a standard static-fluid TOV metric only exists for `2M/r̄<1`. Entry 57 supplies no such proof.

Entry 38 itself does, however, give the essential claim-level argument in Section 4. For the standard TOV ansatz,

`A = 1 − 2M/r̄`.

When `A<0`, `r̄` becomes timelike and the old static time coordinate becomes spacelike. A co-moving perfect fluid must consequently put its nonzero four-velocity component along `r̄`, not along the exterior TOV time coordinate. Entry 38 derives a different Einstein–fluid system, equations (4.16)–(4.18), and calls the resulting spacetime “TOV inside the Black Hole”; it is dynamical, not a continuation retaining the defining static/co-moving structure of a **standard** TOV fluid sphere.

That supports a narrow statement:

> A standard static, co-moving TOV fluid solution does not continue into `A<0` *as the same standard static TOV construction*; inside the horizon the causal roles of the coordinates switch and the co-moving perfect-fluid ansatz yields a different, dynamical system. The pressureless Schwarzschild/OS case is the special vacuum/contact-discontinuity limit.

It does not support the broader wording “no metric of TOV form or no matter solution can exist inside a black hole.” Entry 38 constructs precisely an analogue with radial dependence, but it is dynamical because radial position is timelike.

Accordingly, this claim is not ownerless in the corpus in the ordinary evidentiary sense: entry 38 supplies a derivation of the essential causal-signature distinction. It **is** falsely attributed to entry 57 as a previously proved theorem. The bibliography should not represent entry 57 as owning it.

## 3. Ownership-of-proof and entry 38's tier

The ownership-of-proof convention remains correct: merely citing a no-go does not transfer proof-tier status to the citing paper, and a citation does not confer proof ownership on a source that does not contain the proof.

But its mechanical application in the B32 proposal needs one correction. Entry 38 is not only a report. Its Section 4 independently derives why the interior case requires a different co-moving system. That is enough claim-level warrant for the narrow result, even though the backward attribution to [15] is unsupported.

Entry 38 should nevertheless remain `CONSISTENCY-ONLY` at paper level. Its operative contribution is constructive: it builds the inside-black-hole TOV analogue and matches it to FRW shock solutions beyond the Hubble length. The limitation motivates and delimits that construction; it is not the paper's dominant result. This is the same paper-level/claim-level distinction used for construction papers containing parameter exclusions.

Recommended record repair for entry 38:

- state that standard static/co-moving TOV cannot retain that character for `A<0`, because the radial coordinate becomes timelike and the co-moving Einstein–fluid equations change;
- state that entry 38 derives the replacement dynamical system in Section 4;
- do **not** say entry 57 proves the result;
- retain `CONSISTENCY-ONLY`.

## 4. The infinite-FRW/Schwarzschild statement

The sentence “the infinite FRW metric cannot be matched to the Schwarzschild metric” occurs in entry 38's discussion of its Oppenheimer–Snyder construction. It is not a coordinate-patch obstruction: the paper uses Eddington–Finkelstein coordinates specifically to regularize the Schwarzschild horizon and obtains a regular matching trajectory through it.

It is instead a global model/idealisation statement. A `k=0` FRW slice is all of Euclidean `R³`, with homogeneous matter and infinite extent/mass. The Schwarzschild exterior in the OS construction is the vacuum exterior of a **finite**, fixed enclosed mass. The junction therefore requires truncating FRW at a finite-radius interface; it cannot simultaneously retain the entire infinite FRW spatial slice and attach a Schwarzschild exterior “beyond” its edge. The source's nearby mass-continuity and finite-total-mass discussion makes that scope clear.

The defensible wording is:

> In the finite-mass, spherically symmetric OS/Schwarzschild junction construction considered here, the complete infinite `k=0` FRW spatial slice cannot be the bounded interior of a Schwarzschild exterior; only a finite FRW region can be matched across the interface.

This is not a class-wide no-go against every conceivable embedding, gluing, asymptotic construction, or local FRW/Schwarzschild matching. Entry 38 does not present a separately labelled general theorem proving such a universal claim.

## 5. Is hit-count ordering defensible, and what should be read next?

Hit count is defensible only as one queue-priority signal. It is not defensible as a completion rule or as evidence that low-count papers are clear. Entry 5 is a direct counterexample to any such use: a genuine operative obstruction scored zero under the earlier vocabulary.

After the three highest-count papers, I would not simply descend the count column. I would alternate strata:

1. read one high remaining count paper (entry 51);
2. read one from the minimum-count stratum (randomize among entries 8, 11, 12, and 43 rather than choosing by title);
3. continue alternating high/middle/low counts;
4. in every paper, inspect abstract, theorem/proposition statements, conclusion, and the derivation around model-domain assumptions even when the lexical count is zero;
5. finish all 20, because only a census—not a thresholded subset—supports a corpus-wide clearance.

If only one paper can be read next, choose by a recorded random draw from entries 8, 11, 12, and 43. That directly stress-tests the instrument's known failure mode. Entry 51 can follow immediately as the highest remaining lexical-priority item.

## 6. Predicate audit of `b32_entry38_candidate.py`

The script passes 4/4, but its predicates establish phrase presence and bibliographic identity, not the proposed adjudication.

1. **TOV claim predicate:** it checks that “cannot be continued into a Black Hole” and “we proved this in” occur somewhere in normalized entry-38 text. It does not establish that the phrases belong to the same assertion, occur twice as the description claims, define “standard TOV,” or verify any proof.
2. **Infinite-FRW predicate:** it confirms a substring only. It does not determine whether the limitation is local, global, coordinate-induced, mass-induced, or universal.
3. **Citation predicate:** this is the strongest check. Taking the last `[15]` and finding the exact journal/volume/pages nearby does resolve the reference-list item, and the independent PDF header confirms entry 57. But the predicate itself does not compare authors/title/year, inspect the cited paper, or show that the cited paper contains the attributed result.
4. **Record-absence predicate:** it searches only the two exact source phrasings in the entire bibliography. A paraphrase, narrower description, or claim-level note would pass unnoticed. The script's prose says the record was directly read, but that reading is not encoded in the predicate.

`BIB` is otherwise not used to verify entry numbers, current tiers, pinned-source status, or the proposed no-change disposition. No predicate reads entry 57 at all. Thus 4/4 validates the trigger for this gate, not its answer.

## Disposition

- **Entry 57:** no TOV-continuation proof; retain `CONSISTENCY-ONLY`; do not label it the obstruction owner.
- **Entry 38:** retain `CONSISTENCY-ONLY`, but repair its prose to include the narrow static/co-moving TOV limitation and the bounded-FRW/Schwarzschild junction limitation.
- **Attribution:** flag “proved in [15]” as unsupported by the cited entry-57 text. Entry 38's own Section 4 supplies the best in-corpus derivational warrant for the narrow causal-signature claim.
- **Infinite FRW:** treat as a finite-mass OS/Schwarzschild junction limitation, not a universal no-go and not a coordinate-patch artifact.
- **Census:** continue through every remaining paper with stratified/random low-count reads, not count-only descent.
