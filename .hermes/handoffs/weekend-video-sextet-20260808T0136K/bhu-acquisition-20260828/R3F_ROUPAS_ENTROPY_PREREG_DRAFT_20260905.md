# DRAFT — NOT ORDERED — R3-F pre-registration: does entry 21 derive the Bekenstein–Hawking entropy, or recover it by construction?

**Status:** DRAFT, written under Duho's 2026-09-05 18:56 KST grant ("take the unstarted round-3 preregs — drafting is not
starting"). Round-3 ranked packet cluster **#6** (claude proposal; CONT 4, TRACT 4, score 16, cost 2–4 seat-days as proposed,
re-costed below at 1–2 because the chain is eight equations). Not blocked. Nothing runs on this document. No tier, warrant
token, standing or stamp moves. Paper HOLD. Nothing outward. Published peer-reviewed sources only. Nothing from Hwao's lane.

**Version:** DRAFT 2. A freeze produces `R3F_ROUPAS_ENTROPY_PREREG_2026MMDD.md` with §8 filled, C0 by two seats and a
two-seat design gate before any derivation.

## 0. Design rules carried from R3D and R3C2 (`R3_PREREG_DESIGN_RULES_20260905.md`) — DRAFT 2

**Rule 1 — C0 first.** Before this document is gated, two seats on different engines each write a reachability exhibition:
one concrete input and the verbatim clause path for every class in §4, or UNREACHABLE with the blocking clause. The lane owner
authors none of it, repairs none of it, verifies ACCESS_SHA after exit, and gates only on PASS+PASS.

**Rule 2 — falsifier asymmetry (a design rule of §4, not a note).** `ENTROPY_DERIVED` is filed only from a positive printed artefact
for eq. 24 (limb A), the T0 finding (limb B), the interior claim (limb C). Every way the pipeline can fail lands away from it, as follows — an anchor mismatch in C1 lands on
`R3F_NO_CLASS`; a symbolic timeout or unavailable machinery in any limb lands on `INCONCLUSIVE_CONVENTION` (or the study's explicit
not-evaluable class where §4 names one) for that item, never on the pass class; a script exception or an unexpected exit
status lands on `R3F_NO_CLASS` with the printed traceback; a control failing its exact expected set lands on `R3F_NO_CLASS`;
a seat disagreement on any classified row is carried as a pair and lands on the study's DISPUTED class where §4 names one,
else on `R3F_NO_CLASS`; a missing artefact is a failure, never a default. No precondition sits on the pass path that the fail
path lacks.

**Rule 3 — the cap, declared now.** After the freeze, one C0 round and one two-seat gate. Repairs are applied against both lists
together, once per version. If a gate round after the first repair returns new non-escalated, non-cosmetic findings, or if
C0 fails a second time, the lane stops, files `R3F_STOP_DIAGNOSIS_<date>.md`, and waits. Class additions, renames and
tier or warrant moves are escalated to Duho at once and never count against the cap.

**Rule 4 — every control executes and prints.** §5 below names each control's exact command, its printed artefact (resolved
command, stdout, stderr, exit status) and the exact token set that defines PASS; a control described but not executed, or a
token asserted from prose, is a defect the gate is asked to flag. Scripts: `r3f_controls.py` (C1 identity, C2 uniform-shell positive, C3 deletion probe, negative control), `r3f_limbs.py`, committed and pinned by sha256
beside this document at freeze; each has a positive and a negative form.

**Rule 5 — abort guards and the delivered read set.** Version apply chains fail-stop after every step and write at the end.
The seat's read set is exactly: `R3F_SEAT_PACKET.md`, `SEAT_BRIEF.md`, `r3f_controls.py`, `r3f_limbs.py`, `r3c2_timeout.py`, `R3F_SEAT_PACKET.sha256`, the pinned Roupas text and its rendered copy — each pinned in `R3F_SEAT_PACKET.sha256`; no operative command names
a tool outside that set or at an absolute path. Third-seat dispatch through the lane's dispatcher is an administrative action
of the lane owner and is not claimed executable from the packet.

## 1. Question

Entry 21 (Roupas 2022, the de Sitter-core "cosmological black hole" spectrum; warrant `W_ROUTE_CONNECTED` for its ringdown
frequencies, K5 `K5_AMPLITUDE_FREE`) has a section "3 Fluid entropy" (SOURCE lines 161–240, eqs. 17–26) ending in "the fluid
entropy equals the Bekenstein–Hawking entropy" (eq. 25). No K study touched it. The chain as printed:

- (Q1) work and effective pressure for an anisotropic fluid, `P = P_r + (2/3)(P_T − P_r)` (eqs. 17–19);
- (Q2) Euler relation `T s = ρc² + P ⇒ s = −(c²/3T) r ρ′` "using equation (7)" (eq. 20);
- (Q3) Tolman law `T(r)√g_tt = T0` (eq. 21);
- (Q4) the interior contributes no entropy because `P_interior = −ρ0 c²` (line 199);
- (Q5) `S = ∫ s √g_rr 4πr² dr` over the shell equals `−(c²/3T0) ∫ ρ′ 4πr³ dr` (eq. 22), which integrates to eq. 23 and, "using
  equation (14)" and the constant of eq. 12, to **`S = M• c²/T0`** (eq. 24), "for any choice of α and for all solutions (8)";
- (Q6) **`S = S_BH` if `T0 = T_dS ≡ ħc/(2π r_H) = 2 T_BH`** (eqs. 25–26): "Provided α accounts for the quantum indeterminacy
  of the event horizon (2), this Tolman temperature *may be identified* with the cosmological temperature".

So the paper's own wording places the area law behind a conditional. The question is whether anything printed **fixes** that
condition:

> **Is the Tolman temperature `T0` determined by the construction's printed equations, or is `T0 = T_dS` an input? And does
> the α-independent identity `S = M• c²/T0` (eq. 24) reproduce exactly from the printed spectrum?**

Plainly: the paper shows the shell's entropy is its energy divided by one temperature. Does the paper derive that temperature,
or choose it so the famous answer comes out?

## 2. Sources and pins

| role | file | sha256 |
|---|---|---|
| version of record (arXiv text of the published paper) | `../bhu-reading-20260823/sources/2203.13295_clean.txt` | `82f0d604d5b43c86ad893af052cf03dfaafda73e681b80e8123f51ec2789a2ab` |
| rendered copy for equation legibility | `../bhu-reading-20260823/sources/ar5iv_2203.13295.html` | pinned at freeze |

Inputs the seat may use: the paper's eqs. 1–16 (spectrum, eqs. 7, 8, 12, 14 in particular), eqs. 17–26, and STANDARD constants.
Nothing else. No value may be supplied that the paper does not print.

## 3. Procedure (1–2 seat-days; every symbolic operation through the committed 120 s wrapper)

Limb A — **mechanical reproduction of (Q1)–(Q5).** For a general member of the printed spectrum (eq. 8, with the paper's K, N),
compute `s(r)` from (Q2) with P_T from eq. 7; integrate (Q5) symbolically over `[r_H − α/2, r_H + α/2]`; confirm the eq. 12
constant; confirm eq. 24 exactly, and confirm the "for any α, all solutions" claim by leaving K, N, α symbolic. Record the
residual if any. This limb is the study's reproducible content and is α-independent by the paper's own claim.

Limb B — **what fixes `T0`.** Enumerate every printed equation that constrains `T0`. Three findings are possible and the seat
must file exactly one, with quotation: (i) an equation earlier than eq. 26 determines `T0` from the spectrum (derived);
(ii) `T0` first appears as the identification in eqs. 25–26 with "if"/"may be identified" wording (input); (iii) `T0` is
constrained by a printed inequality or bound but not fixed (underdetermined). The seat also records whether the paper
prints any independent derivation of `T_dS = ħc/(2π r_H)` for this geometry or imports it as STANDARD.

Limb C — **the interior claim (Q4).** Confirm `T s = ρ0 c² + P = 0` inside from the printed interior equation of state, and
check whether the shell integral's lower limit `r_H − α/2` places any interior contribution in the shell (a subtlety the
paper's line 199 asserts away).

## 4. Outcome classes (precedence top to bottom; exactly one is filed)

1. `R3F_NO_CLASS` — a pre-audit control fails in every seat, or the packet fails redaction.
2. `INCONCLUSIVE_CONVENTION` — limb A's outcome depends on an unprinted convention (sign of work, which pressure enters the
   Euler relation, proper-volume measure) that the record does not choose; state both readings.
3. `ENTROPY_UNREPRODUCED` — eq. 24 is **unreproduced from the stated inputs** after two attempts; print the residual. (This
   class outranks the T0 question because if (Q5) fails, (Q6) has nothing to rest on.)
4. `ENTROPY_ASSUMED` — eq. 24 reproduces, and limb B finds (ii): the area law follows only from the identification
   `T0 = T_dS`, which the paper introduces conditionally and does not derive.
5. `ENTROPY_UNDERDETERMINED` — eq. 24 reproduces, and limb B finds (iii).
6. `ENTROPY_DERIVED` — eq. 24 reproduces, and limb B finds (i): a printed equation fixes `T0` from the construction.

**Stated before ordering:** the paper's own conditional wording makes class 4 the likely outcome. The study is still worth its
day because eq. 24 is a non-trivial, α-independent identity nobody has checked, and because the record should say in one
line what the corpus's strongest-sounding "this is really a black hole" claim rests on. If Duho judges the likely outcome
too predictable to spend a seat-day on, the honest alternative is an annotation on entry 21 quoting lines 221–226.

## 5. Controls

- **C1 SOURCE_IDENTITY** — byte-exact anchors for eqs. 7, 8, 12, 14, 20, 22, 24, 25, 26 and the line-221 wording.
- **C2 POSITIVE** — the same pipeline on a uniform-density shell with `P_T = P_r` must return the textbook `S = (ρc² + P)V/T`.
- **C3 DELETION_PROBE** — delete eq. 14 (horizon coincidence) from limb A and demand failure with the exact code set
  `{R3F_C3_NO_HORIZON_RELATION}`; a limb that still returns eq. 24 without it has not used the paper's chain.
- **C4 HARNESS** — live `sympy` version print through the wrapper.
- **Negative control** — plant `P = P_r` in (Q1) and require a non-zero residual against eq. 24.


**Executable form (Rule 4) — each line is one printed run; PASS is defined by its printed output only:**

```
/usr/bin/python3 r3f_controls.py c1 ../bhu-reading-20260823/sources/2203.13295_clean.txt  → C1_SOURCE_IDENTITY=PASS|FAIL for eqs. 7, 8, 12, 14, 20, 22, 24, 25, 26 and line 221
/usr/bin/python3 r3f_controls.py c2  → C2_POSITIVE=PASS only if the uniform isotropic shell returns S=(ρc²+P)V/T symbolically, printed
/usr/bin/python3 r3f_controls.py c3  → must print exactly {R3F_C3_NO_HORIZON_RELATION} and exit 1
/usr/bin/python3 r3c2_timeout.py 120 -- /usr/bin/python3 -c 'import sympy; print(sympy.__version__)'  → C4_HARNESS
/usr/bin/python3 r3f_controls.py neg  → planted P=P_r must print a non-zero residual against eq. 24
```

## 6. Seats

Blind double, two engines, packet only, ACCESS_SHA verified by the lane after exit, no read before exit, no edit under a
running seat. Lane's own second route for limb A (by hand for K = 1, N = 3) sealed before dispatch.

## 7. Closed-check against prior studies

K5 audited entry 21's ringdown amplitude and stopped at limb A without touching the interior thermodynamics. R3D was
entries 18–20. No ledger entry is re-run. This study does not test whether the object exists, only whether the printed
entropy chain is self-supporting.

## 8. Versions

| version | date (KST) | change |
|---|---|---|
| DRAFT 1 | 2026-09-05 (this file) | written; not ordered, not frozen, not gated |
| DRAFT 2 | 2026-09-05 | Blanc's 22:33 note: the five R3D/R3C2 lessons carried in as §0 design rules (C0 first; falsifier asymmetry with the error-landing rule; declared cap; executable controls with named commands; abort guards + enumerated read set); still not ordered, not frozen, not gated |

R3F_PREREG_DRAFT_COMPLETE
