ACCESS_SHA=5cd4e6da543d2c0dd4b301a9ebdbed17336257cd6ed731ae615d97230f14832e
C0_REACHABILITY=PASS

# R3C2 — C0 REACHABILITY EXHIBITION on V22 (author seat: kimi, 2026-09-05)

Exhibited against: `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md`, Version 22 as it stands on disk
(sha256 above, computed by this seat with `shasum -a 256` before any other step). No other file in
this directory was opened. This is an exhibition of reachability only: it does not gate the study,
does not judge its physics or design quality, and runs no derivation. Each exhibit below is a
constructed, minimal, concrete input — a specific claim with specific inputs in a pinned-enumerable-
text scenario — traced through the document's own clauses to the declared verdict. Prior rounds did
the same (e.g. §10.2's "entry 59's `β`"). No exhibit is claimed to be a real corpus entry.

## 0. Dependence on the settled §1/§3 definition — recorded as a result

The brief notes that §1's core definition is marked rather than to be read assuming an interpretation,
and that this dependence is itself a result worth having. Stated precisely against V22:

- §1 as it stands embeds the settled option-(c) reading (ruled 2026-09-05 14:08 KST, §10.4; HELD marker
  removed at V10): the reproduction verdict answers "does the paper's own number follow from the
  paper's own recipe applied to the inputs it states"; the arithmetic consumes every ledger record
  with status `PRINTED` or `STANDARD` regardless of `origin` (§2 step 4, §3's inputs rule); provenance
  is recorded separately and `rests_on` is computed by script (`r3c2_lane_tools.py compute`, C3 lane
  side), never by a seat and never an input to the verdict. `REPRO_AFTER_CHOICE` is retired (§10.4);
  the arithmetic group is exactly `REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED` (§3).
- Every exhibition below assumes exactly this text and no other. The dependence is material and is
  recorded: under the retired derivation-only wording, two blind C0 seats found one class
  (`REPRO_AFTER_CHOICE`) unreachable (§10.3, both seats, same clause); the ruling retired the class
  rather than repairing it. Under the settled (c) wording exhibited here, no §3 outcome and no §4
  class is unreachable — see the tables. There is no held clause in V22; nothing below is contingent
  on an open ruling.

## 1. (A) Per-claim outcomes of §3 — six tokens, all reachable

§3's per-claim precedence (quoted): "Where more than one terminal condition holds, file the first in
this order: `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`,
then the arithmetic group."

| verdict | concrete input (exhibit) | clause path | reachable |
|---|---|---|---|
| `REPRO_WITHIN_STATED_PRECISION` | E1: `p1.tex:41` prints "ΩΛ = 0.685" as its own result; stated recipe ΩΛ = 1 − Ωm; Ωm = 0.3153 printed at `p1.tex:39`, verbatim on C3's closed list | §1 include → §2.1 extract → §2.2 inputs {Ωm} → §2.3 `STANDARD` (printed, closed-list verbatim) → §2.4 consume → 1 − 0.3153 = 0.6847 → no stated uncertainty → §3 rounding rule: rounds to 0.685 at printed 3-dp precision = printed numeral → §3 `REPRO_WITHIN_STATED_PRECISION`; precedence: no terminal condition holds → arithmetic group | yes |
| `REPRO_FAILED` | E2: `p2.tex:87` prints "t_H = 14.0 Gyr" as its own result; stated recipe t_H = 1/H0; H0 = 67.36 printed at `p2.tex:80`, verbatim on the closed list | §1 → §2.3 `STANDARD` → §2.4 consume → 1/H0 = 14.5159 Gyr → rounds to 14.5 at printed 1-dp precision ≠ 14.0, and no stated uncertainty → §3 `REPRO_FAILED` ("unreproduced from the stated inputs"; both numbers reported); precedence: no terminal condition → arithmetic group | yes |
| `REPRO_BLOCKED` | E3: `p3.tex:55` prints "r_d = 147.1 Mpc"; stated recipe needs c_s(z_d), not printed; `p3.tex:56` names a source: "we adopt the sound-speed fit of Smith (2019)", which is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md` | §1 → §2.3: value not printed, named source → §2 IMPORTED rule: "a cited value that does not machine-match at the named source's cited line, **or whose named source is not an enumerable text of the manifest, files `REPRO_BLOCKED` under §3**" → C3: status `BLOCKED`, `origin` `IMPORTED`, `ORIG_CITATION` to `p3.tex:56`, no value → §2: "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." → §3 `REPRO_BLOCKED`, input and source named; precedence: recipe stated (not NO_DERIVATION) → BLOCKED files first | yes |
| `REPRO_NOT_EVALUABLE` | E4: `p4.tex:203` prints "χ²_min = 112.4"; stated recipe is a 40-dimensional grid minimisation needing ~10⁶ model evaluations; all inputs printed | §1 → §2.3 all `PRINTED`/`STANDARD` → §2.4 attempt launched via §9's wrapper `/usr/bin/python3 r3c2_timeout.py 120.0 -- <command>` → monotonic 120.0 s deadline exceeded → wrapper prints `SYMBOLIC_TIMEOUT`, exits 124 → §3 `REPRO_NOT_EVALUABLE`, `SYMBOLIC_TIMEOUT` printed with the point reached; precedence: recipe stated, no blocked/absent input → NOT_EVALUABLE. (Machinery limb: a stated Boltzmann-hierarchy integration the lane has no machinery for → `MACHINERY_UNAVAILABLE`, same class.) | yes |
| `REPRO_NO_DERIVATION_STATED` | E5: `p5.tex:17` prints "the fit yields β = 0.93" as its own result; the only provenance sentence is "obtained with the pipeline described in §4.1" — where it came from, no operations a seat could attempt | §1 satisfied (printed numeral asserted as own result) → §2.1 finds no equation or computational procedure → §3: "A procedure named but not specified … states no computational procedure that could produce it; file this class and name the passage." → `REPRO_NO_DERIVATION_STATED`, passage named; precedence: first in the §3 order — files even though its would-be inputs are also absent | yes |
| `REPRO_INPUT_ABSENT` | E6: `p6.tex:66` prints "v_c = 210 km/s"; stated recipe v_c = √(GM/r); r = 8.0 kpc printed at `p6.tex:60` (`PRINTED`); G on the closed list (`STANDARD`); M neither printed anywhere nor traced to any named source | §1 → §2.2 inputs {G, M, r} → §2.3: M is `ABSENT` (C3) → §2: a seat may not supply a value; the attempt ends there → §3 `REPRO_INPUT_ABSENT`, input named; precedence: not NO_DERIVATION (recipe stated), not BLOCKED (no named source) → INPUT_ABSENT | yes |

All six §3 outcomes: REACHABLE. (The retired seventh, `REPRO_AFTER_CHOICE`, is not a §3 token in V22
— §10.4; it is exhibited as retired, not as a live outcome.)

## 2. (B) Study-level classes of §4 — eight classes, all reachable

§4's filing precedence (quoted): "Where more than one condition holds, file the first in this order:
`R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_OUTCOME_DISPUTED`,
`CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`, `CENSUS_COMPLETE`. **Once a stop
class applies, later limbs are unreached and their controls are `NOT_RUN`.**"

| class | concrete input (scenario) | clause path | reachable |
|---|---|---|---|
| `CENSUS_COMPLETE` | S1: corpus {p1, p2, p7}; three included claims file E1 (`WITHIN`), E2 (`FAILED`), and E7 (`p7.tex:9` prints "f = 0.48" from f = Ωm^0.55, Ωm `STANDARD`; 0.3153^0.55 = 0.53 ≠ 0.48 → `FAILED`). Controls C1–C5b PASS in both seats; C6: custodian seed supplied with receipt T; auditor re-derives all three arithmetic-group claims, all `MATCH`, ledgers complete → `C6_AUDIT_SAMPLE=PASS`; denominator 3 ≥ 1 | every included claim carries exactly one arithmetic-group outcome + `C6_AUDIT_SAMPLE=PASS` → §4.1; precedence: no stop class above holds (controls pass identically, enumerations agree, outcomes agree, origins agree within 10%, audit passes, no non-arithmetic outcome, denominator > 0) → `CENSUS_COMPLETE` | yes |
| `CENSUS_PARTIAL` | S2: corpus {p1, p3} → E1 files `WITHIN`, E3 files `REPRO_BLOCKED`; audit passes (auditor independently reaches the same `BLOCKED` on the named-source test). Zero-denominator route: corpus whose every candidate numeral is an equation number, reference number, page/line number, date, or attributed-not-derived → exclusion ledger full, included set empty | "at least one included claim carries a non-arithmetic outcome" (§4.2) after the §2 attempt (one repeat permitted, meaningful only for `REPRO_NOT_EVALUABLE`) → "INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`"; §4 precedence places PARTIAL directly above COMPLETE. Zero denominator: §4.1's own clause — "A denominator of zero files `CENSUS_PARTIAL` with the empty enumeration named; no census is complete over nothing" — and §4.2's "or the denominator is zero" (the V22 cosmetic) | yes |
| `CENSUS_AUDIT_FAILED` | S3: corpus {p1, p2}; seats file E2 as `WITHIN` with reproduced 14.0 (seat arithmetic error). Third-seat audit (C6, no sight of earlier work) re-derives E2 → 14.5159 → 14.5 ≠ 14.0 → auditor's outcome `REPRO_FAILED` vs sealed `WITHIN` → `MISMATCH` in `C6_AUDIT.json`. Seed route: custodian seed never supplied/recorded with receipt T. Receipt route: Blanc's post-opening re-hash of the tally mismatches receipt T | §4.3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger" → no tally filed, cause named. Seed route, C6 quoted: "If the seed is not supplied and recorded with the receipt, the audit does not run, `C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named." Receipt route, §7 quoted: "Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED`". Precedence: above PARTIAL/COMPLETE; §4.4's carve-out keeps it out of `R3C2_NO_CLASS` | yes |
| `R3C2_NO_CLASS` | S4: C5 harness — both seats run `/usr/bin/python3 -c "import sympy; print(sympy.__version__)"`; `ImportError`, exit 1; two attempts each; fails in every seat that attempted it. Pre-dispatch route: the builder's forbidden-list assertion finds a surviving forbidden string → `C4_PACKET_REDACTED=FAIL` | §4.4: "a control among C0 through C5b fails **in every seat that attempted it** after two attempts; a packet or seat-isolation failure before dispatch files this class." Precedence: first in the §4 order; later limbs `NOT_RUN`. Boundary honoured: the failing control (C5 / C4-packet) is inside C0–C5b, not C6 or the seal | yes |
| `CENSUS_DENOMINATOR_DISPUTED` | S5: candidate `p8.tex:12` prints "13.8"; seat A includes it (paper asserts it as its own result); seat B excludes it as `ATTRIBUTED_NOT_DERIVED`; two reconciliation attempts fail. Input-list route: agreed claim; seat A's ledger lists inputs {H0}, seat B's {H0, Ωm}; `merge` exits 1; the one C3 reconciliation against the stated equation fails | §1/§6: "disagreement on any candidate that survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED`" — disputed candidates listed, both ledgers reported. Input-list route, C3 quoted: "an input-set difference surviving that reconciliation stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4), the disputed inputs listed with both seats' quotations". Precedence: controls passed identically (no NO_CLASS, no SPLIT) → this class | yes |
| `CENSUS_OUTCOME_DISPUTED` | S6: agreed included claim `p9.tex:33` prints "σ8 = 0.811 ± 0.006" with stated recipe and all inputs `PRINTED`/`STANDARD`; seat A's mechanical attempt gives 0.8111 → |0.8111 − 0.811| = 0.0001 ≤ 0.006 → `REPRO_WITHIN_STATED_PRECISION`; seat B's gives 0.818 → |0.818 − 0.811| = 0.007 > 0.006 → `REPRO_FAILED`; the one reconciliation against the printed numeral and the stated-precision rule does not resolve the split (the difference is in the reproduced values, not the rule) | §2 step 5 / §4.6: "a disagreement surviving that reconciliation files `CENSUS_OUTCOME_DISPUTED` (§4)" — "The census does not proceed; the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached." Precedence: after DENOMINATOR_DISPUTED, before ORIGIN_DISPUTED — enumeration and input lists agree, so nothing above fires | yes |
| `CENSUS_ORIGIN_DISPUTED` | S7: 10 included claims; on 2 of them (20%) the seats' independent `origin` classifications disagree — input β at `p10.tex:44`: seat A files `CHOSEN` (`ORIG_CHOICE_STATED`, verbatim "we take β = 1/929.25"), seat B files `IMPORTED` (`ORIG_CITATION`, verbatim "β = 1/929.25 (Jones 2017)"), having matched different sentences; the disagreement is carried, never reconciled | §4.7: "the two seats' independent `origin` classifications disagree on inputs affecting **more than 10% of included claims**" → "The census does not proceed; every disputed input is listed with both seats' classification and both quotations." 2/10 = 20% > 10%. (At ≤ 10%: `ORIGIN_DISPUTED` inputs are carried and `rests_on` computed as a `DISPUTED` pair; the study continues — C6.) Precedence: after OUTCOME_DISPUTED, before AUDIT_FAILED — matches chronology (origin classification precedes audit) | yes |
| `CENSUS_CONTROL_SPLIT` | S8: C2 validate — seat A's ledger validates (exit 0); seat B's ledger fails validation (a `PRINTED` value 67.36 that does not machine-match its cited source line, which prints "67.4"); two attempts; the split persists | §4.8: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; **do not adopt the passing seat's result.**" Precedence: second, directly under `R3C2_NO_CLASS`, whose "in every seat" condition this scenario deliberately fails — exactly one seat fails, so SPLIT, not NO_CLASS | yes |

All eight §4 classes: REACHABLE.

## 3. (C) Explicit reachability statements

- §3: `REPRO_WITHIN_STATED_PRECISION` reachable; `REPRO_FAILED` reachable; `REPRO_BLOCKED` reachable;
  `REPRO_NOT_EVALUABLE` reachable; `REPRO_NO_DERIVATION_STATED` reachable; `REPRO_INPUT_ABSENT` reachable.
- §4: `CENSUS_COMPLETE` reachable; `CENSUS_PARTIAL` reachable; `CENSUS_AUDIT_FAILED` reachable;
  `R3C2_NO_CLASS` reachable; `CENSUS_DENOMINATOR_DISPUTED` reachable; `CENSUS_OUTCOME_DISPUTED` reachable;
  `CENSUS_ORIGIN_DISPUTED` reachable; `CENSUS_CONTROL_SPLIT` reachable.

## 4. The suspicion, answered directly: is `CENSUS_COMPLETE` reachable in practice?

**Answer: REACHABLE.**

The suspicion is correct about the mechanism and wrong about the conclusion. The mechanism, exactly as
the text routes it:

- `CENSUS_COMPLETE` (§4.1) requires "every included claim carries exactly one outcome from the
  arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`", and the arithmetic group is exactly
  `REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED` (§3).
- `CENSUS_PARTIAL` (§4.2) fires when "at least one included claim carries a non-arithmetic outcome, or
  the denominator is zero" and is declared "INCONCLUSIVE, and **it takes precedence over
  `CENSUS_COMPLETE`**"; the §4 precedence order lists `CENSUS_PARTIAL` immediately before
  `CENSUS_COMPLETE`.

So the forced routing is real: a single claim anywhere in the corpus that files `REPRO_BLOCKED`,
`REPRO_INPUT_ABSENT`, `REPRO_NO_DERIVATION_STATED`, or `REPRO_NOT_EVALUABLE` routes
claim → §3 non-arithmetic outcome → §4.2 condition true → precedence → `CENSUS_PARTIAL`, and
`CENSUS_COMPLETE` is then unreachable **for that corpus**. S2 exhibits exactly this with one blocked
claim in a two-claim corpus.

But unreachable-for-that-corpus is not unreachable. Reachability is existential, and the exhibiting
input is S1: a corpus in which every included claim states an equation or computational procedure, and
every input each recipe needs is printed in the claiming paper, printed verbatim on C3's closed list,
or machine-matched at the cited line of a pinned enumerable text — and every attempt finishes inside
the 120-second cap. Every claim then lands in the arithmetic group; with `C6_AUDIT_SAMPLE=PASS` and a
nonzero denominator, §4.1's condition holds and no class above it in the precedence fires. No clause
in the document forbids this conjunction; the definition quantifies over the corpus's content, not
over a property no corpus can have. Two sharpenings:

- `REPRO_FAILED` is in the arithmetic group. `CENSUS_COMPLETE` does not require the papers to be right;
  it requires them to be evaluable. A corpus of honest arithmetic failures completes (S1 contains one).
- The zero-denominator case is routed away from COMPLETE by §4.1's own guard ("no census is complete
  over nothing") — a guard against vacuous truth, not a block on the class.

Whether the real 89-text pinned corpus has the S1 property is the empirical question the census exists
to answer; this exhibition does not pre-judge it. The class CAN OCCUR; if the real corpus contains even
one unevaluable claim, the study files `CENSUS_PARTIAL` and reports each such claim and why — the
asymmetry is the census's intended behaviour, stated here as the routing, not as a defect.

## 5. Supplementary — declared conditions in §3 that are not per-claim outcomes

C0 asks for "every declared condition"; the five exclusion-ledger kinds are declared in §3 and are
explicitly "not per-claim outcomes". Each is exhibitable; none blocks anything above.

| condition | concrete candidate passage | clause path | reachable |
|---|---|---|---|
| `EQUATION_NUMBER` | `q1.tex:30` "…as shown in (14)." — numeral 14 | fails §1 (numeral is an equation number) → exclusion ledger, kind `EQUATION_NUMBER`, file/line/numeral recorded | yes |
| `REFERENCE_NUMBER` | `q2.tex:51` "…see [23]." — numeral 23 | fails §1 (reference number) → exclusion ledger | yes |
| `PAGE_OR_LINE_NUMBER` | `q3.tex:8` "see p. 412" — numeral 412 | fails §1 (page/line number) → exclusion ledger | yes |
| `DATE` | `q4.tex:19` "Planck 2018 results" — numeral 2018 | fails §1 (date) → exclusion ledger | yes |
| `ATTRIBUTED_NOT_DERIVED` | `q5.tex:72` "H0 = 67.4 km/s/Mpc (Planck Collaboration 2020)" — attributed, not derived | fails §1 ("values the paper attributes to another work without deriving") → exclusion ledger | yes |

Denominator consequence: a corpus whose candidates all fail §1 this way has denominator zero and files
`CENSUS_PARTIAL` via §4.1's guard — exhibited in S2's second route.

## 6. UNREACHABLE verdicts and their blocking clauses

None. Every §3 per-claim outcome (six of six) and every §4 study-level class (eight of eight) is
exhibited in §1–§2 above with a concrete input and a clause path through the V22 text. There is no
unreachable verdict, so there is no blocking clause to quote.

## 7. Method note for the verifying seat

One file was read (`shasum -a 256` printed above, first, before any other step); no other file in the
directory was opened. Every numeric claim in an exhibit was machine-checked by this seat
(1 − 0.3153 = 0.6847 → 0.685 at 3 dp; 1/H0 = 14.5159 Gyr → 14.5 at 1 dp ≠ 14.0; 0.3153^0.55 = 0.53
≠ 0.48; |0.8111 − 0.811| = 0.0001 ≤ 0.006; |0.818 − 0.811| = 0.007 > 0.006). Clause quotations are
verbatim from the V22 text. This exhibition is authored independently; the second seat verifies
independently, and disagreement is reported, not reconciled.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V22_KIMI_COMPLETE
