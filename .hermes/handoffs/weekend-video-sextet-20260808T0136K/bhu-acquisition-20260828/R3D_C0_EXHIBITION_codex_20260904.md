ACCESS_SHA=b7883c25784cdbc2617ac7f17ae9accf90f75785866b8849cec4a272111387d2
C0_REACHABILITY=FAIL

# C0 REACHABILITY EXHIBITION

Scope: this is a reachability test of the frozen document's machinery only. The constructions below are hypothetical printed-result configurations; they are not claims about Dymnikova physics. No Dymnikova source was read.

| verdict | concrete input | clause path | reachable yes/no |
|---|---|---|---|
| §4.1 `DYM_FLOOR_DERIVED` | Completed §2c census prints a relation whose solution is the unique allowed mass `M = 1.000e15 kg`; the completion ledger contains no admissible completion that changes it or permits masses approaching zero; all reached C1–C5b controls pass. | §2 completion-free derivation adds nothing → §3 Limb A reproduces a size–mass/bounding relation, so proceeds to Limb B → §4.1 unique positive completion-free floor, no differing admissible floor, no zero-approaching family → C6 is run; under §4.1 the class is filed whether C6 passes or a breaker condition fails. | yes |
| §4.2 `DYM_FLOOR_UNDERDETERMINED` | Completed census gives completion-free floor `M_min = 10 kg`. One admissible, exactly-one-assumption completion `A: M_min = 2L` with the printed result fixing `L = 10 kg` gives `20 kg`. These are the only admitted floors and neither branch permits masses approaching zero; controls pass. | §2 defines `A` as admissible (one named assumption, consistent with every printed relation) and counts the completion-free derivation → §3 reproduces a bounding relation and enters Limb B → §4.2 has two positive unequal floors, `10 kg` and `20 kg`, with no zero-approaching branch → class 2. | yes |
| §4.3 `DYM_NO_SIZE_MASS_RELATION` | Every manifest source is readable; the exhaustive §2c census and equation list complete with equal reconciliation counts, but no included printed item binds size to mass or bounds mass; all reached controls pass. | §2c complete census → §3 Limb A cannot reproduce a size–mass relation or mass bound → §3 directs “file `DYM_NO_SIZE_MASS_RELATION` and stop” → §4.3. C6 is not reached. | yes |
| §4.4 `DYM_NO_POSITIVE_FLOOR` | Census prints `M = r kg/m` with `r > 0 m` otherwise unrestricted. Thus `r_n = 1/n m` gives `M_n = 1/n kg → 0`; all reached controls pass. | Printed relation binds size and mass, so §3 enters Limb B → §4.4's explicit definition is met: no positive lower bound follows and masses approach zero → class 4, which also has precedence over class 2. | yes |
| §4.5 `DYM_FLOOR_COMPLETION_DEPENDENT` | Printed relations allow exactly `M_n = (10 + 1/n) kg`, `n = 1,2,…`: they have positive lower bound 10 kg but no attained minimum. Hence no positive minimum/floor follows and masses cannot approach zero. One admissible named completion, `A: n = 1`, yields the unique attained minimum `11 kg`; no other admissible completion exists. | A mass-bounding relation is reproduced, so §3 enters Limb B → §4.4 does not apply because a positive lower bound exists (its definition of “permit” is not met) → §4.5: no positive attained minimum follows from printed relations alone, an admissible completion gives `11 kg`, and no branch approaches zero → class 5; its own clause makes C6 `NOT_RUN`. | yes |
| §4.6 `DYM_SOURCE_BLOCKED` | Configure manifest entry 18 as unreadable (permission denied) when C1 computes its digest; no scientific class is selected. | §2a/C1: a pinned source the branch needs cannot be read → C1 explicitly files `DYM_SOURCE_BLOCKED` → §4.6 says the study waits and this is not a scientific verdict. | yes |
| §4.7 `R3D_NO_CLASS` | All four sources are readable and every candidate relation is resolved. In blind seat A, the required C2 reconciliation count is `100 non-blank lines / 99 assigned dispositions` on attempt 1 and again on attempt 2; seat B is control-clean. A third seat re-runs that failed reconciliation and also obtains `100/99`. | §4.7 first rules out source blocking because nothing is unread or unresolved → a required control fails after two attempts in seat A → the one-clean-seat exception is defeated because the third seat re-runs the failed control and also fails → §4.7 files `R3D_NO_CLASS`. | yes |
| C6 condition 1 PASS | Derived floor `M_min = 1.000e15 kg`; dimensional analysis prints `[M_min] = kg`. | C6 applies after §4.1 → condition-1 procedure classifies dimension → mass in kg meets its pass criterion. | yes |
| C6 condition 1 FAIL | Candidate input: the dimensionless ratio `M_min/m_P = 4.594e22`. | The candidate would fail condition 1, but it cannot reach C6: §4.1 requires a positive minimum black-hole mass and C6 applies only after §4.1. A dimensionless ratio is expressly not the required mass magnitude, so §4.1 cannot legitimately be reached. | **no — UNREACHABLE** |
| C6 condition 2 PASS | Floor `M_min = sqrt(hbar*c/G) = 2.176434e-8 kg`; constants are only `hbar`, `c`, and `G`. | §4.1 → C6 condition 2 → each constant terminates in §2b, satisfying every row of the provenance table. | yes |
| C6 condition 2 FAIL | Floor `M_min = alpha*sqrt(hbar*c/G)` with `alpha = 2` introduced as “we choose alpha=2,” with no manifest derivation. | §4.1 → condition-2 scope includes `alpha` because it is in the derived magnitude → its chain terminates neither in a §2a equation nor §2b and is a `we choose` terminus → condition 2 fails. | yes |
| C6 condition 3 PASS | Final expression `sqrt(hbar*c/G)`; replacing all non-§2b parameters by independent symbols leaves no such symbols. | §4.1 → condition-3 SymPy simplification once → printed free-symbol set outside §2b is `{}` → exact PASS criterion is met. | yes |
| C6 condition 3 FAIL | Candidate input: final expression `a*sqrt(hbar*c/G)`, where `a` is a free core normalisation. | The candidate would print free-symbol set `{a}` and fail condition 3, but it cannot reach C6: with `a` unchosen, no unique numerical completion-free floor follows, contrary to §4.1; choosing `a` is an added completion and also defeats §4.1. Because C6 applies only after §4.1, every condition-3 FAIL candidate is blocked before the condition is run. | **no — UNREACHABLE** |
| C6 condition 4 PASS | Fixity table for `M_min = sqrt(hbar*c/G)` lists held constants `hbar`, `c`, and `G`, and gives their §2b deriving entries (with no additional held-fixed quantity). | §4.1 → condition-4 procedure lists every held constant → every row has the allowed deriving passage/list entry → condition 4 passes. | yes |
| C6 condition 4 FAIL | Derivation holds core density `rho0 = 1.000e18 kg/m^3` fixed, but the C2 artefact contains no manifest passage deriving that constancy. | §4.1 → condition-4 fixity table contains `rho0` → no reproduced C2 manifest passage supports its constancy → condition 4 fails. | yes |
| C6 condition 5 PASS | Floor interval `[1.000e15, 1.000e15] kg`; complete four-row comparison table, including ΛCDM. | It intersects neither `[2.176434e-8, 2.176434e-8]`, `[1.729e11, 5.190e11]`, nor `[4.375e30, 5.768e30]` kg; ΛCDM has no interval and can never match → by the iff overlap rule, condition 5 passes. Comparator overlap: none. | yes |
| C6 condition 5 FAIL | Floor interval `[2.000e11, 2.000e11] kg`; complete four-row comparison table, including ΛCDM. | `max(2.000e11,1.729e11) = 2.000e11 <= min(2.000e11,5.190e11) = 2.000e11`, so it overlaps comparator 2, Hawking evaporation `[1.729e11, 5.190e11] kg`; it overlaps neither Planck nor stellar interval → the iff overlap rule makes condition 5 fail, naming comparator 2. | yes |
| `C6_BREAKER_TEST=PASS` | A §4.1 floor `[1.000e15,1.000e15] kg`; complete four-row condition-5 table; C1–C5b pass; condition 1 reports kg; condition 2 traces every derived-floor constant to §2a/§2b; condition 3 prints no surviving non-§2b symbol; condition 4 gives a deriving passage for every fixed quantity; condition 5 has no comparator overlap. | §4.1 reaches C6 → every condition 1–5 satisfies its own decision rule and the table is complete → C6's stated aggregate PASS clause. | yes |
| `C6_BREAKER_TEST=FAIL` | A §4.1 floor `[2.000e11,2.000e11] kg`; conditions 1–4 pass and the four-row table is complete, but condition 5 overlaps Hawking comparator `[1.729e11,5.190e11] kg`. | §4.1 reaches C6 → condition 5 fails its iff overlap rule → C6's aggregate FAIL clause (“any condition fails”) → §4.1 nevertheless remains filed and the failed artefact is reported. | yes |
| `C6_BREAKER_TEST=NOT_RUN` | The §4.3 construction above: completed census reproduces no size–mass relation or mass bound. | §3 Limb A stops at `DYM_NO_SIZE_MASS_RELATION` → §5 C6 applies only if §4.1 is reached → C6's stated `NOT_RUN` clause. The same aggregate outcome is also forced by §4.5. | yes |

## Cross-acceptance findings

- The §4.4 zero-approaching construction cannot also be filed as §4.2 because §4.4 expressly takes precedence.
- The §4.5 construction has a positive lower bound but no attained minimum. It is therefore outside §4.4 under §4.4's definition of “permit” (“no positive lower bound on the mass follows”), while satisfying §4.5's “no positive floor” in the document's minimum-mass sense. If “floor” were instead read everywhere as any lower bound, §4.5 would be unreachable; the class's own required report category “no attained minimum” and the study's stated question about a minimum license the attained-minimum reading used here. This is a terminology ambiguity, not dual acceptance under that reading.
- A §4.1 input can accept either aggregate C6 PASS or aggregate C6 FAIL; §4.1 explicitly remains filed after a breaker failure. Those are C6 outcomes, not competing §4 outcome classes.
- `C6_BREAKER_TEST=NOT_RUN` can be produced by every terminal route other than §4.1, including the exhibited §4.3 and §4.5 routes.

## Unreachable verdicts and blocking clauses

### C6 condition 1 FAIL

Blocking clauses (verbatim):

> **DYM_FLOOR_DERIVED** — a unique positive floor follows from the printed relations **with no added completion**, **no admissible completion yields a different floor, and none permits masses approaching zero.**

> **C6 — breaker test.** Applies **only if `DYM_FLOOR_DERIVED` is reached**; otherwise `NOT_RUN`, never a pass.

> dimension is mass (kg or M☉), not dimensionless and not a shape/scale/ratio

A dimensionless/shape/scale/ratio candidate can fail condition 1 only after C6 is reached, but it cannot supply the minimum-black-hole-mass floor required to reach §4.1 and hence C6. A legitimate §4.1 result is a mass magnitude, which necessarily passes condition 1's dimensional criterion.

### C6 condition 3 FAIL

Blocking clauses (verbatim):

> **DYM_FLOOR_DERIVED** — a unique positive floor follows from the printed relations **with no added completion**, **no admissible completion yields a different floor, and none permits masses approaching zero.**

> **C6 — breaker test.** Applies **only if `DYM_FLOOR_DERIVED` is reached**; otherwise `NOT_RUN`, never a pass.

> **PASS exactly when the simplified expression contains none of those symbols** — i.e. the printed number is recovered with no non-§2b parameter chosen.

For condition 3 to fail, a non-§2b free symbol must survive, meaning the printed numerical floor is not recovered without choosing that parameter. Then a unique completion-free floor does not follow, so §4.1—and therefore C6—cannot be reached. Choosing the parameter is an added completion and is blocked by the same §4.1 clause.

R3D_C0_EXHIBITION_COMPLETE
