ACCESS_SHA=bc79306d52e446706b7517d6a585c3daabea9878ed9a1d1b7f421c5509427ed6
C0_REACHABILITY=PASS

# C0 REACHABILITY EXHIBITION — V28

This tests the document's machinery, not its physics. Each construction is a concrete hypothetical input to the printed decision procedure. No Dymnikova source was read.

Section 4 declares six classes: four scientific and two non-scientific terminal states. The round instruction's later phrase “five scientific classes” conflicts with §4. I test all four live scientific classes plus both terminal states. The retired `DYM_FLOOR_COMPLETION_DEPENDENT` is not tested.

| verdict | concrete input | clause path | reachable yes/no |
|---|---|---|---|
| Class 1 `DYM_FLOOR_DERIVED` | A complete §2c census reproduces `M >= 10 kg` plus printed relations on volume, interior profile, an order-unity coefficient, and exterior form, with those four objects unbound. The exact §2 reading set is: completion-free 0, Euclidean E, uniform-interior U, coefficient-set-to-1 O, and GR-exterior G. Each one-completion reading operates on its corresponding printed relation, is consistent, and retains allowed set `[10 kg,infinity)`. Thus 0,E,U,O,G are all in `P`, all give 10 kg, and `Z=I=empty`. | §2 exact-four-kinds rule fixes the five readings; §3 reproduces a mass bound and enters limb B; §4 puts every reading in `P`; the class-1 row fires because `P` is non-empty, all agree, and `Z` and `I` are empty. | **yes** |
| Class 2 `DYM_FLOOR_UNDERDETERMINED` | A complete census again makes all four completion kinds applicable. Explicit finite set: 0→2 kg, E→2 kg, U→2 kg, O→1 kg, G→2 kg; all allowed mass sets are non-empty intervals beginning at the stated floor. Hence `P` holds two different floors, while `Z=I=empty`. | §2 admits exactly 0 plus four one-completion readings; §3 reproduces a mass bound and enters limb B; §4 puts all five in `P`; its class-2 disagreement rule files class 2. §4.2 reports every reading and chooses none. | **yes** |
| Class 3 `DYM_NO_SIZE_MASS_RELATION` | The exhaustive, control-clean §2c census reproduces no printed size–mass relation and no printed mass bound. | §2c completes; §3 limb A finds neither relation, files class 3, records C3/C4/C6 `NOT_RUN`, and stops. §4 restricts class 3 to limb A. Although unconstrained mass would semantically permit approach to zero, the run never enters limb B, so it cannot also file limb-B-only class 4. | **yes** |
| Class 4 `DYM_NO_POSITIVE_FLOOR` | The census reproduces `M >= 0 kg`, so a mass-bounding relation exists, but every applicable reading retains `[0 kg,infinity)`: `P=empty`, `Z={0,E,U,O,G}`, `I=empty`. | §3 enters limb B because a mass bound was reproduced; §4 assigns all readings to `Z`; the class-4 row fires because `P` is empty and `Z` non-empty. §4.4 and C6 record C6 `NOT_RUN`. | **yes** |
| Class 5 `DYM_SOURCE_BLOCKED` | Required pinned manifest entry 18 is unreadable (permission denied) before C2 or C6 engages. | §2a requires it; §4.5 files `DYM_SOURCE_BLOCKED` when a required source cannot be read; §9 makes later unengaged controls `NOT_RUN`. | **yes** |
| Class 6 `R3D_NO_CLASS` | All evidence is readable/resolved. Both seats otherwise agree on class 1 and 10 kg, but seat A's reached C4 fails because the required premise list is missing. The third seat reruns C4 once; the list is still missing, so C4 fails a second time. | §4.6 first rules out `DYM_SOURCE_BLOCKED`, mandates the rerun, and files `R3D_NO_CLASS` on the persistent control failure. | **yes** |
| C6 condition 1 PASS (`ENTAILED`) | Correctly filed floor `M_floor=10 kg`. | Positive-floor membership supplies a mass; C6 condition 1 dimensional analysis gives `[M]` in kg. C0 permits the entailed route. | **yes** |
| C6 condition 1 FAIL integrity case | Malformed class-1 filing calls dimensionless `r_h/r_0=2` its “floor.” | C6 says test the quantity actually filed; dimension 1 is neither kg nor `M_sun`, so condition 1 fails. This is C0's expressly requested malformed-filing rejection, not a valid substantive positive-floor case. | **yes (malformed filing)** |
| C6 condition 2 PASS | `M_floor=3 sqrt(hbar c/G)`; C2 traces 3 to the reproduced manifest equation and `hbar,c,G` to §2b. | Every provenance chain terminates in a manifest equation or §2b, satisfying condition 2. | **yes** |
| C6 condition 2 FAIL | `M_floor=A sqrt(hbar c/G)`, with provenance ending `A=2, “we choose the simplest value”`, without manifest derivation. | Condition 2 expressly fails a “we choose/simplest form” terminus outside the manifest and §2b. | **yes** |
| C6 condition 3 PASS | `M_floor=3 sqrt(hbar c/G)`; simplified non-§2b free-symbol set `{}`. | Condition 3's exact criterion finds no non-§2b symbol. | **yes** |
| C6 condition 3 FAIL | Class-2 filed family `M_floor=A kg`, with `A>0` but unchosen; free-symbol output `{A}`. | C6 runs on class 2. Under condition 3, recovering a number requires choosing `A`; a free normalization survives. | **yes** |
| C6 condition 4 PASS | Floor 10 kg; the fixity table holds only `G,c,hbar` constant and cites §2b for each. | Every held-constant row has a deriving passage, satisfying condition 4. | **yes** |
| C6 condition 4 FAIL | Floor 10 kg from a derivation holding `rho_0=1` fixed by choice; its fixity row states `NO MANIFEST DERIVING PASSAGE`. | Condition 4 fails a held-constant quantity without a manifest derivation. | **yes** |
| C6 condition 5 PASS | Point floor `[1.000e15,1.000e15] kg`. | No overlap with Planck `[2.176433e-8,2.176435e-8]`, Hawking `[1.729e11,5.190e11]`, or TOV `[4.375e30,5.768e30]`; ΛCDM has no interval. With the complete four-row table, condition 5 passes. | **yes** |
| C6 condition 5 FAIL — Planck | Point `[2.176434e-8,2.176434e-8] kg`. | Its intersection with the Planck interval is the same non-empty point. It overlaps neither other numeric row. The iff rule fails condition 5 and names Planck. | **yes** |
| C6 condition 5 FAIL — Hawking | Point `[2.000e11,2.000e11] kg`. | Its intersection with Hawking is the same non-empty point. It overlaps neither Planck nor TOV. The iff rule fails condition 5 and names Hawking. | **yes** |
| C6 condition 5 FAIL — TOV | Point `[5.000e30,5.000e30] kg`. | Its intersection with TOV is the same non-empty point. It overlaps neither Planck nor Hawking. The iff rule fails condition 5 and names TOV. | **yes** |
| `C6_BREAKER_TEST=PASS` | Class-1 point floor `[1.000e15,1.000e15] kg`; complete artefacts show mass dimension, full allowed provenance, no free symbols, no underived fixity, and a complete no-overlap comparison table. | C6 engages on class 1; all five decision rules pass and the table is complete; the outcomes clause returns `PASS`. | **yes** |
| `C6_BREAKER_TEST=FAIL` | Class-1 point floor `[2.000e11,2.000e11] kg`; conditions 1–4 pass and the complete table shows Hawking overlap. | C6 engages; condition 5 fails; the outcomes clause returns `FAIL`, while §4.1 still files class 1. | **yes** |
| `C6_BREAKER_TEST=NOT_RUN` | The class-3 no-relation/no-bound input above. | §3 explicitly records C6 `NOT_RUN`; §5 says C6 never engages on class 3. | **yes** |

## Partition and path findings

- All six declared classes have a reachable input. All four live scientific classes are reached; there is no fifth live scientific class.
- No constructed admissible case files two classes or none. Limb-B `P/Z/I` makes classes 1, 2, and 4 exhaustive and disjoint. Class 3 is disjoint operationally because the limb-A stop files it before limb B. Thus the requested no-relation/no-bound case files class 3 alone, despite having the semantic zero-approach consequence discussed in §4.
- C6 initially engages on 2 of 6 classes (1 and 2). Once engaged, `C6_BREAKER_TEST=FAIL` can be recorded in **4 of the 6 terminal classes**: classes 1 and 2 directly, `DYM_SOURCE_BLOCKED` after condition 3 remains `UNDECIDED` after fallback, and `R3D_NO_CLASS` after engaged C6 is followed by a persistent control failure. Requested number: **4**.
- Every breaker condition has both requested directions. Condition 1's valid PASS is entailed; its FAIL is only the malformed-filing integrity check licensed by C0, not a valid substantive path.
- The three condition-5 FAIL values independently overlap the Planck, Hawking, and TOV rows using the printed closed intervals.

## Unreachable verdicts and blocking clauses

None. There is no blocking clause to quote.

R3D_C0_EXHIBITION_COMPLETE
