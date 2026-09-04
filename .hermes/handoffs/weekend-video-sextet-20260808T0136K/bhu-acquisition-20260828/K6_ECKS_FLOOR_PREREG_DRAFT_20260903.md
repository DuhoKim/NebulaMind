# DRAFT — NOT ORDERED — K6 pre-registration: does the ECKS density ceiling derive a minimum-black-hole-mass floor? (entry 51) (Tori, 2026-09-03 23:25 KST)

**Status:** drafted on Duho's overnight non-decision-work order. Gated as a draft 2026-09-03 23:31 KST (agy via
`nm_referee_dispatch.sh`, ACCESS PROVEN, `K6_DRAFT_GATE_agy.md`: PREREG_SOUND_WITH_REPAIRS, one repair applied). No K6 derivation
or study seat has started. If Duho orders K6, the text is re-gated and committed before any new derivation.

## 0. Why this would exist

Entry 51 states in the published paper that the electron Cartan density is approximately the maximum density of ordinary fermionic matter and then says a black hole's mass density cannot exceed it, "from which" a minimum mass of about 10^16 kg follows (`../bhu-reading-20260823/sources/poplawski_plb690_vor_clean.txt` L625–669). The version-of-record check found the same density and mass statements in the arXiv-derived text and the publisher version; the 2013 erratum changes other equations (`VOR_CHECK_51_59_codex.md` §1). The connecting density-to-black-hole-mass calculation is absent from both held texts. The record therefore carries `W_UNDERIVED`, and Duho's standing wording is "unreproduced from the stated inputs," not "error."

K6 asks the missing mathematical question without presuming the answer: do the paper's ECKS equations and its proved nonsingularity result bind a black-hole mass, density measure, horizon radius and interior geometry tightly enough to imply a positive mass floor? If so, what floor follows?

## 1. Prior-information disclosure and freeze boundary

This is not a first-look problem. The lane already has an exploratory six-route calculation (`b13_floor_routes.py`) and two adversarial readings (`AGATE_Q2_VERDICT.md`, `CGATE_Q2_VERDICT.md`). Those artifacts are prior information, not a K6 result. A future ordered run must:

1. hash and archive those artifacts before dispatch;
2. give both derivation seats the same disclosure that exploratory work exists, but bar them from reading its values or methods until each has sealed its own symbolic chain, assumptions and predicted class;
3. use only the publisher paper, its erratum and pinned peer-reviewed sources during the blind phase;
4. open the exploratory artifacts only for the post-derivation reconciliation.

The draft itself makes no claim that the ordered seats can be blind to the existence of the record's `W_UNDERIVED` status.

## 2. Objects and definitions to bind before arithmetic

At step 1, before evaluating a mass, each seat must pin from the source or mark absent:

- the ECKS field equations and Dirac spin-density conservation result used by entry 51;
- the Cartan-radius relation in Eq. (33), including every suppressed dimensionless coefficient and its order-of-magnitude status;
- the density symbol in the claimed ceiling: local rest-frame density, proper-volume mean density, coordinate-volume density, or another invariant;
- the black-hole mass: ADM, Misner–Sharp, Komar or another source-defined mass;
- the surface that binds size to mass: event horizon, apparent horizon, trapping horizon or another source-defined surface;
- the interior matter profile, charge and angular momentum domain, and matching conditions needed to connect the density ceiling to that mass and surface.

No GR exterior, Euclidean volume, uniform-density interior, Kerr/Kerr–Newman limit or order-unity coefficient may enter silently. Any such item is an added completion and must be named and tested separately from what the paper itself derives.

## 3. The question, exactly

From the publisher version of entry 51, its erratum and the peer-reviewed equations it explicitly imports, does there exist a source-bound theorem of the form

`rho <= rho_Ce  =>  M >= M_min > 0`

for every black hole in the paper's stated ECKS domain? If yes, is the unique derived `M_min` within one decade of `10^16 kg` (the pre-declared match interval is `10^15 <= M_min <= 10^17 kg`)? If the implication is not source-bound, identify exactly which free definition, coefficient, geometry or matching condition prevents it.

The one-decade interval operationalises the paper's order-of-magnitude `~10^16 kg`; it is an audit criterion, not an uncertainty claimed by the paper.

## 4. Methods — two independent routes

### Route A: theorem/inequality route

Starting from the pinned ECKS action, field equations and conservation identities, derive every inequality between the density scalar, a quasilocal or asymptotic mass, and a trapped surface. List each premise. Prove the universal lower bound, prove that no positive universal bound follows, or stop at the first unbound quantity. Only after the symbolic result is sealed may constants be inserted.

### Route B: admissible-completion/countermodel route

Independently characterize the paper's allowed stationary or collapsing configurations. Either construct two source-admissible completions that obey the same density ceiling but yield different mass floors, which establishes underdetermination, or prove that the ECKS equations and matching conditions remove that freedom. A Schwarzschild mean-density estimate may be run as a control, but it is not the ECKS result unless the source-bound derivation licenses that interior and density definition.

The two routes must use separate scripts or notebooks and separate assumption ledgers. Agreement of two numerical substitutions into the same unstated density-volume formula is one method, not two.

## 5. Outcome classes — closed decision order

Apply these in order and file exactly one:

1. **K6_SOURCE_INCONSISTENT:** the source-bound premises needed for the claimed implication have no common solution. State the minimal inconsistent set; no mass floor is reported.
2. **K6_NO_POSITIVE_FLOOR:** a proof or explicit one-parameter family shows that black-hole masses approach zero while all source-bound ECKS premises and the density ceiling remain satisfied.
3. **K6_FLOOR_UNDERDETERMINED:** the source leaves at least one load-bearing definition, coefficient, interior geometry or matching condition free, and two admissible completions yield different mass floors. Report the freedom; do not choose a preferred completion.
4. **K6_PRINTED_ORDER_DERIVED:** the source-bound chain yields a unique positive floor in `10^15–10^17 kg` without an added completion. Report the formula and value.
5. **K6_ALTERNATIVE_FLOOR_DERIVED:** the source-bound chain yields a unique positive floor outside `10^15–10^17 kg`. Report the formula, value and logarithmic separation from `10^16 kg`.

These classes describe the study result only. No class changes a tier, standing or warrant token without a separate Duho ruling.

## 6. What counts as a verdict

A verdict requires:

- a symbolic implication proof, no-floor proof, inconsistency proof, or two explicit admissible completions for underdetermination;
- an assumption ledger marking every premise as source-derived, cited, or newly added;
- a reproducible numerical script only after the symbolic chain is fixed;
- controls C1–C6 below passing in both derivation seats;
- a one-page check sheet and an independent second-route reconciliation.

Merely rerunning `b13_floor_routes.py`, reproducing one Schwarzschild estimate, or observing that the paper omits a displayed equation does not count as a K6 verdict.

## 7. Controls

- **C1 — source identity:** reproduce the held publisher text's Cartan-density ceiling and `~10^16 kg` sentence, and verify that the pinned erratum does not amend either. Failure = stop; no class.
- **C2 — Eq. (33) scaling:** derive `r_C proportional to m^(-1/3)` and `rho_C proportional to m^2` from the paper's order-of-magnitude relation; with a unit coefficient, reproduce the electron Cartan radius within 0.5 decade of `10^-27 m`. The unit coefficient must remain labelled a control normalisation, not a source result. Failure = stop.
- **C3 — GR benchmark:** independently derive the Schwarzschild uniform-mean-density identity `rho_bar = 3 c^6 / (32 pi G^3 M^2)` and reproduce it numerically. This validates algebra only and cannot supply the ECKS interior premise. Failure = stop.
- **C4 — density semantics:** show that every density used is a scalar or a specified hypersurface average with a proper-volume measure. Substituting a coordinate volume must be caught. Failure = stop.
- **C5 — deletion probe:** delete the load-bearing size/mass/interior relation from each proposed unique-floor proof. The proof must then lose uniqueness or the seat must show that the relation is independently forced by another pinned equation. Failure = the proof is circular; no derived-floor class.
- **C6 — completion split:** if an added completion is used, changing at least one allowed completion (profile, charge/spin sector, horizon or matching condition) must either leave the theorem invariant by proof or expose the result as completion-dependent. Failure = K6_FLOOR_UNDERDETERMINED, not a preferred-number verdict.

## 8. Seat plan, cost and stopping rule

Two fresh gpt-5.6-sol derivation contexts, blind to each other and to the exploratory values, one on Route A and one on Route B. A split goes to a fresh referee only through `/Users/duhokim/HermesOps/scripts/nm_referee_dispatch.sh` with ACCESS PROVEN. A second method is mandatory even if the first route lands on the printed order. Estimated cost: about three seat-days, pure theory, no observational data (`TOPIC_agy_report.md` Topic 2).

Stop after two failed attempts to bind the same missing source premise. File K6_FLOOR_UNDERDETERMINED rather than importing an unstated model. If the publisher text or erratum cannot be read, wait; do not substitute metadata or an abstract.

## 9. Non-circularity and scope

The printed `10^16 kg` value fixes only the pre-declared order-of-magnitude match interval; it may not be used to select a geometry, coefficient, density definition or matching condition. Existing exploratory values are opened only after both independent chains are sealed. The paper's Papapetrou/nonsingularity result and its mass-floor corollary remain separate claims. K6 is housekeeping on entry 51's warrant; it does not start K3 step 2, K4 or K5 and does not alter the paper record by itself.
