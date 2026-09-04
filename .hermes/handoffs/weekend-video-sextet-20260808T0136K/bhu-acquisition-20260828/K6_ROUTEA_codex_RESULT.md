K6_FLOOR_UNDERDETERMINED

# K6 Route A — codex seat result

Blind status: no sealed exploratory artifact or other route/result/check/reconciliation file was read. Standing wording: the printed floor is **unreproduced from the stated inputs**, not an error.

## Limb A

The held publisher text gives the electron Cartan density as `rho_Ce ~ m_e/r_Ce^3 ~ 10^51 kg m^-3` and calls it approximately the maximum-density order (VoR lines 625–635). It then states that black-hole mass density cannot exceed `rho_Ce` and “from which” the minimum ECKS black-hole mass is `~10^16 kg` (lines 662–664). The appended erratum changes only sentences around Eqs. (21), (26), the coordinates above Eq. (29), and Eq. (29)’s measure (lines 767–781), so it amends neither statement. Exhaustive targeted searches of the full publisher and arXiv-derived held texts found the assertion in their abstracts and discussions, but no connecting density–mass/horizon calculation. `K6_PREMISE_VOID` therefore does not apply.

## Symbolic Route A result

The source-derived chain is:

1. The ECKS action and local field equations are Eqs. (3)–(6) (VoR lines 102–203); spin conservation and its multipole expansion yield Eq. (17) (lines 204–406).
2. Eq. (33) is explicitly order-of-magnitude: `m/r_C^3 ~ (G/c^4)(hbar/r_C^3)^2` (lines 551–568). Hence `r_C^3 ~ G hbar^2/(m c^4)`, so `r_C proportional to m^(-1/3)` and `rho_C=m/r_C^3 proportional to m^2`.
3. The paper calls `rho_Ce` an expected approximate ceiling and expressly calls its extension to self-gravitating systems a conjecture (lines 625–653).
4. A ceiling `rho <= rho_Ce` alone cannot imply a mass floor: a global relation specifying a mass-dependent proper volume or size is required. No such relation follows in the held source.

The first unbound quantity is `V(M)`, equivalently a source-bound size/mass relation. Failed binding attempt 1: `rho_BH` is not defined as a local rest-frame scalar or as a proper-volume average. Failed binding attempt 2: no ADM/Misner–Sharp/Komar mass choice, event/apparent/trapping surface relation, interior profile, charge/angular-momentum domain, or matching conditions are supplied for this implication. Under preregistration section 10, two failures to bind this same load-bearing premise require `K6_FLOOR_UNDERDETERMINED` without importing an unstated model.

## Assumption ledger

| Premise | Status | Receipt or role |
|---|---|---|
| ECKS action, Einstein–Cartan equations, spin conservation | source-derived | VoR Eqs. (2)–(6), lines 102–203 |
| Dirac spin density and four-fermion term | source-derived | VoR Eqs. (19)–(20), lines 333–366 |
| Eq. (33) balance and scaling | source-derived, order-of-magnitude only | VoR lines 551–568 |
| Electron Cartan-density ceiling | source-derived expectation | VoR lines 625–635 |
| Extension to all self-gravitating fermionic systems | source-derived conjecture | VoR lines 649–653 |
| Defined invariant black-hole density | ABSENT | no local scalar/proper-average definition |
| Defined black-hole mass and bounding surface | ABSENT | no mass notion or horizon relation supplied |
| Interior profile, charge/spin domain, matching conditions | ABSENT | source says full coupled equations must be solved, lines 604–612 |
| Schwarzschild radius, Euclidean uniform mean volume | newly added control only | algebra benchmark; not an ECKS premise |
| Unit coefficient in Eq. (33) | newly added control normalization | never treated as source-derived |
| SI constants in the script | cited standard numerical inputs | inserted only after symbolic seal |

## Controls and check sheet

The executable prints and asserts the Cartan scaling, unit-normalized electron radius, GR benchmark, density-measure rejection, deletion probe, and completion split. Its GR completion is explicitly only a control. Deleting the source-pinned ECKS equations leaves that injected GR relation and its unique number intact, which identifies it as circular for the K6 implication and bars a derived-floor class. Changing the added radius coefficient changes the resulting floor, exposing completion dependence.

`C1_SOURCE_IDENTITY=PASS`  
`C2_EQ33_SCALING=PASS`  
`C3_GR_BENCHMARK=PASS`  
`C4_DENSITY_SEMANTICS=PASS`  
`C5_DELETION_PROBE=PASS`  
`C6_COMPLETION_SPLIT=PASS`

No tier, warrant token, standing, or stamp is changed.
