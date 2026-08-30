ENTRY50_NARROWED_MS_THRESHOLD_IS_SOURCE_DERIVED_AND_RECORD_IS_SELF_CONTRADICTORY

# CGATE B47 verdict

I read all 34 two-up sheets of the pinned MIT-CTP-1690 scan, using the OCR companion sequentially for prose and the scan itself as the authority. I rendered the pages containing the Section II threshold argument, equations (5.31)–(5.37), the simple-connectedness argument, equations (6.1)–(6.6), the conclusion, and footnotes 18 and 24. I also reran `b47_entry50_fullread.py` unchanged: it reports `10/10`.

The paper-level ruling survives: entry 50 is not an operative theoretical obstruction under the fixed b28 rule. Its operative contribution is a constructive, leading-WKB tunneling calculation from the type-(a) branch to the universe-producing type-(b) branch. The authors expressly lack a genuine Euclidean interpolating manifold, introduce a pseudomanifold prescription, and conjecture that its action supplies the semiclassical amplitude. `CONSISTENCY-ONLY` is therefore the appropriate paper-level census class, provided the record preserves that conjectural status.

The submitted record nevertheless needs two corrections, one substantive and one record-integrity correction.

## 1. The M_S result is not merely inherited

The statement that the Section II threshold is “inherited, not re-proven here” is false. Section II initially says that the classical bubble problem was analyzed in refs. [2]–[7] and that it will state results without deriving the junction equation. But after defining the potential and the masses in (2.19), this paper itself applies the Penrose condition to the displayed global geometries:

- for the expanding solutions above the relevant threshold it identifies a closed anti-trapped surface and applies Penrose plus the null-energy condition;
- for `M_S < M < M_cr`, it traces the null rays at the maximum-radius point and concludes that an initial singularity is necessary;
- it then observes that this surface would not exist when the Kruskal trajectory crosses to the right of the origin, which occurs for `M < M_S`, and concludes that expanding type-(a) bubbles in that range can in principle be produced classically without an initial singularity.

This is a source-owned geometric argument for the threshold, even though the paper says it is also summarizing ref. [9]. It is fair to call the result a rederivation, review proof, or local demonstration based on previously developed classical trajectories. It is not fair to say that the result is only inherited or not re-proven.

This correction does not create a paper-level obstruction. The `M > M_S` limb is genuine claim-level obstruction content inside a paper whose operative task is to tunnel past that classical restriction. The record should describe it that way.

## 2. The two proposed internal negatives are real but subsidiary

### Canonical formulation

Section VI proves a failure of the particular reduced canonical program. Equation (6.3) shows that `∂p/∂r-dot` can have either sign, so `p(r,r-dot)` is noninvertible and the authors cannot define the desired single-valued `H(r,p)`. They additionally derive the endpoint-momentum problem for `M_D < M < M_S` and find non-monotonic numerical behavior. The paper repeatedly scopes this to “our program,” its one-degree-of-freedom reduction, and its slicing prescription. It is a real methodological exclusion, not a theorem that canonical quantum gravity or tunneling in general is impossible. Claim-level treatment is correct.

### Nonsingular multi-sheeted covering

Section V really does exclude a nonsingular multi-sheeted covering because the underlying space is simply connected: every closed path contracts to a trivial path and therefore must return to its original sheet. The paper immediately bypasses this by allowing a singular coordinate covering for which the coordinate image can jump sheets and `sqrt(g)` can vanish and change sign. This is a narrowly specified topological exclusion and is accurately retained at claim level; it is not the operative paper verdict.

I found no further result in Sections II–VI or Appendices A–F that changes the paper-level class. The appendices support the coordinate construction, action variation, Euclidean geometry, and continuity corrections. They do not prove a broader no-member result.

## 3. Conjecture and pathology framing

The later full-read paragraph is substantially faithful. The source says all three possibilities explicitly: absence of a manifold may mean stationary phase failed, the thin-wall approximation cannot be extended into the Euclidean regime, or tunneling is forbidden. It then pursues a conjecture. After (5.34), it again says the action is based on conjecture rather than derivation and identifies the mismatch between wall and volume weighting and the continuous-field inconsistency. The singular covering repairs several of these problems only at the price of a metric whose determinant can vanish and change sign. The conclusion again says there is no definitive answer and calls the functional-integral result plausibly correct.

The negative-action characterization is also accurate. On the rendered page, (5.34) is a sum of three nonpositive terms under the stated branch choices and the range `2GM < r < 1/chi`; the authors explicitly call it negative definite. They do not treat the sign as exponential enhancement: Section IV retains the growing/decaying WKB branch ambiguity and chooses the decaying solution for tunneling. The GUT-scale estimate is indeed of order `10^(-10^11)` for the probability, not an empirical falsifier.

## 4. Cross-links

All four cross-links are source-supported:

- ref. [9] is Farhi–Guth, Phys. Lett. 183B, 149 (entry 48);
- ref. [6] is Blau–Guendelman–Guth, Phys. Rev. D35, 1747 (entry 49), and footnote 18 explicitly corrects the sign in its equation (4.25a), saying upward motion on the left de Sitter diagram has negative `t-dot_D` but positive `beta_D`;
- ref. [11] is Frolov–Markov–Mukhanov, Phys. Lett. 216B, 272 (entry 13);
- ref. [2] is the six-item Sato/Kodama/Sasaki/Maeda chain associated with entry 47.

Footnote 24 separately supports the Fischler–Morgan–Polchinski agreement: it maps their expression to (5.34), notes an early-preprint sign misprint, and reports extension beyond their initially restricted mass range.

## 5. Tier and falsifier

`CONSISTENCY-ONLY` is the correct primary tier under the corpus's operative-contribution convention. The paper computes a proposal-dependent amplitude and argues for a quantum escape; it does not supply a calibrated observational discriminator. The final external-signature discussion weakens rather than creates testability: disappearance of reflected photons need not uniquely signal universe creation, the competing probability is not estimated, and the paper ends by saying verification is unknown.

The tier should therefore remain `CONSISTENCY-ONLY`. The classical `M > M_S` result, canonical failure, and topological covering exclusion should remain explicitly scoped claim-level results.

## 6. Bibliography record defect

Entry 50 currently contains both:

- `NOT YET READ — census read queued`, and
- `READ IN FULL 2026-08-30` followed by the full-read adjudication.

Those states cannot simultaneously be true. The stale unread sentence must be removed or marked superseded. The adjacent acquisition sentence saying content identity remains testimony until comparison can remain if it is intended only to distinguish the preprint scan from the journal version of record; it must not be allowed to imply that the pinned preprint itself remains unread.

The full-read scope is otherwise honest: the PDF has 34 two-up scan sheets and the OCR text runs through Sections I–VII, references, and Appendices A–F. My rendered sheets confirm that the important equations and prose correspond to the OCR companion.

## 7. Predicate audit

The script's `10/10` is not an adjudication test and is materially underpowered:

1. The pin check verifies PDF magic and a hash prefix, but not the asserted 34-sheet count, page pairing, or presence of all scan images.
2. The OCR predicate checks a self-authored header, not correspondence between OCR and rendered source pages.
3. Identity and structure checks are keyword-presence tests. They do not establish a full read or mathematical correctness.
4. The first cross-link predicate checks only the PLB 183B string despite naming four links. Its `replace("183B. 149", "1836. 149")` normalization is opaque and makes the OCR's `B/6` ambiguity look like a substantive verification.
5. The second cross-link predicate checks three loose tokens anywhere in the source. Neither cross-link predicate binds reference numbers to bibliography entry numbers, checks footnote 18's correction, or checks footnote 24's comparison.
6. The record predicate checks a handful of phrases but misses the direct `NOT YET READ`/`READ IN FULL` contradiction.
7. No predicate tests the actual `M_S` reasoning. Consequently the script passes the false “inherited, not re-proven” characterization.
8. No predicate tests the hypotheses and sign argument behind (5.34), the WKB branch choice, the scope of (6.3), the simple-connectedness proof, the three “perhaps” alternatives, the pathology admissions, or the unverifiability conclusion.
9. The tier check merely parses the already-written label, and the obstruction-set check merely confirms that this label leaves a hard-coded paper-level set unchanged. Neither applies the b28 rule.

Accordingly, `10/10` means that the expected files and selected strings are present. It does not validate the proposed attribution, classification reasoning, full-read act, or internal consistency of the live record.

## Required disposition

Retain entry 50 as `CONSISTENCY-ONLY` and not a paper-level obstruction. Amend the record to (a) remove the stale `NOT YET READ` state and (b) say that Section II locally demonstrates the `M_S` Penrose threshold while reviewing and crediting ref. [9], rather than saying the threshold is merely inherited and not re-proven.
