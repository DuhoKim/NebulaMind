# DRAFT — NOT ORDERED — R3-E pre-registration: are entry 18's printed source components the ones its own metric demands?

**Status:** DRAFT, written under Duho's 2026-09-05 18:56 KST grant ("take the unstarted round-3 preregs — drafting is not
starting"). Round-3 ranked packet cluster **#7** (codex proposal; CONT 3, TRACT 5, score 15, cost 1 seat-day, not blocked).
Nothing runs on this document. No tier, warrant token, standing or stamp moves. Paper HOLD. Nothing outward. Published
peer-reviewed sources only. Nothing from Hwao's lane, pipeline or data.

**Version:** DRAFT 2 (this file). A freeze produces `R3E_DYMNIKOVA_SOURCE_CONSISTENCY_PREREG_2026MMDD.md` with §8 filled,
a C0 reachability exhibition by two seats, and a two-seat design gate, before any seat derives anything.

## 0. Design rules carried from R3D and R3C2 (`R3_PREREG_DESIGN_RULES_20260905.md`) — DRAFT 2

**Rule 1 — C0 first.** Before this document is gated, two seats on different engines each write a reachability exhibition:
one concrete input and the verbatim clause path for every class in §4, or UNREACHABLE with the blocking clause. The lane owner
authors none of it, repairs none of it, verifies ACCESS_SHA after exit, and gates only on PASS+PASS.

**Rule 2 — falsifier asymmetry (a design rule of §4, not a note).** `PROFILE_CONSISTENT` is filed only from a positive printed artefact
for (P2)–(P7). Every way the pipeline can fail lands away from it, as follows — an anchor mismatch in C1 lands on
`R3E_NO_CLASS`; a symbolic timeout or unavailable machinery in any limb lands on `R3E_NOT_EVALUABLE` (or the study's explicit
not-evaluable class where §4 names one) for that item, never on the pass class; a script exception or an unexpected exit
status lands on `R3E_NO_CLASS` with the printed traceback; a control failing its exact expected set lands on `R3E_NO_CLASS`;
a seat disagreement on any classified row is carried as a pair and lands on the study's DISPUTED class where §4 names one,
else on `R3E_NO_CLASS`; a missing artefact is a failure, never a default. No precondition sits on the pass path that the fail
path lacks.

**Rule 3 — the cap, declared now.** After the freeze, one C0 round and one two-seat gate. Repairs are applied against both lists
together, once per version. If a gate round after the first repair returns new non-escalated, non-cosmetic findings, or if
C0 fails a second time, the lane stops, files `R3E_STOP_DIAGNOSIS_<date>.md`, and waits. Class additions, renames and
tier or warrant moves are escalated to Duho at once and never count against the cap.

**Rule 4 — every control executes and prints.** §5 below names each control's exact command, its printed artefact (resolved
command, stdout, stderr, exit status) and the exact token set that defines PASS; a control described but not executed, or a
token asserted from prose, is a defect the gate is asked to flag. Scripts: `r3e_controls.py` (C1 identity, C2 benchmark, C3 deletion probe, negative control), `r3e_limbs.py` (limbs A–C; every symbolic call through `r3c2_timeout.py`), committed and pinned by sha256
beside this document at freeze; each has a positive and a negative form.

**Rule 5 — abort guards and the delivered read set.** Version apply chains fail-stop after every step and write at the end.
The seat's read set is exactly: `R3E_SEAT_PACKET.md`, `SEAT_BRIEF.md`, `r3e_controls.py`, `r3e_limbs.py`, `r3c2_timeout.py`, `R3E_SEAT_PACKET.sha256`, the two pinned Dymnikova texts and the restatement — each pinned in `R3E_SEAT_PACKET.sha256`; no operative command names
a tool outside that set or at an absolute path. Third-seat dispatch through the lane's dispatcher is an administrative action
of the lane owner and is not claimed executable from the packet.

## 1. Question

Entry 18 (Dymnikova 1992, *Gen. Rel. Grav.* 24, 235; warrant `W_CONSTRUCTION_ASSERTED`, both blind seats 2026-09-03) prints
a spherically symmetric metric (its eqs. 11–13) **and** the stress-energy components it says generate it (its eqs. 8 and 14),
together with a mass formula (eq. 10), a de Sitter scale relation (eq. 9) and a curvature limit (eq. 20). The corpus records the
profile as *assumed*, not derived; that is not in question here. The question is narrower and mechanical:

> **Do the components the paper prints — the density (8) and the tangential pressure (14) — reproduce, from the printed
> metric (11)–(13) through the Einstein equations, with the mass relation (10) and the curvature limit (20) as printed?**

Plainly: the paper chose a density. Given that choice, does everything else it prints follow?

**What this is not.** Covariant conservation of the *derived* tensor is automatic (contracted Bianchi identity) once the
tensor is computed from the metric. The falsifiable content is whether the **printed** components are those components,
and whether the printed mass and curvature statements follow from them. A seat that "verifies conservation" of a tensor
it computed itself has tested nothing; the checks in §3 are stated so that cannot happen.

## 2. Sources and pins

| role | file | sha256 | note |
|---|---|---|---|
| version of record | `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` | `2f3ca3e10ec016eed83104750d11d2428d5523c712814f68d559724d8b2c6b6f` | OCR of the journal scan; equations garbled at (8), (12), (14), (20) |
| legibility restatement | `../bhu-reading-20260823/sources/ar5iv_gr-qc_0201058_dymnikova_restatement.html` | pinned at freeze | same author's later restatement; used ONLY to read the equations, never as the claim |
| context | `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` | `ded87358184a4239d9f5bd0ffe8c5aee7732e992fc00be8f97370e73cbc7af47` | not an input to any check |

**Transcription rule.** Every equation is transcribed from the 1992 record; where the OCR is ambiguous the restatement's
form is adopted **and the ambiguity is recorded** (control C1). A check whose outcome depends on which reading is taken
files `INCONCLUSIVE_CONVENTION`, not a pass or a fail.

**Printed statements to reproduce** (working transcription, to be re-verified at freeze; SOURCE line ranges from the warrant
audit — profile 118–127, vacuum interpretation 73–85, mass 129, regularity 200–223):

- (P1) metric `ds² = (1 − R_g(r)/r) c²dt² − (1 − R_g(r)/r)⁻¹ dr² − r² dΩ²`, `R_g(r) = r_g (1 − exp(−r³/r*³))`, `r*³ = r0² r_g`;
- (P2) `T⁰₀ = ε0 exp(−r³/r*³)` and `T⁰₀ = T¹₁` (the paper's "A + μ = 0" step);
- (P3) `r0² = 3c⁴/(8πG ε0)` (the de Sitter relation, eq. 9);
- (P4) `T²₂ = T³₃ = ε0 (1 − 3r³/(2r*³)) exp(−r³/r*³)` (eq. 14; the coefficient 3/2 is the OCR-ambiguous item);
- (P5) mass formula `M = (4π/c²) ∫₀^∞ T⁰₀ r² dr` gives `M = r_g c²/(2G)` at infinity (eqs. 6, 10);
- (P6) the Kretschmann scalar is finite at r → 0 and tends to `24/r0⁴` (eq. 20);
- (P7) for r ≪ r*, the source is isotropic (T²₂ → T⁰₀) and the metric is de Sitter with scale r0; for r ≫ r*, Schwarzschild.

## 3. Procedure (one seat-day; every symbolic operation through the committed 120 s wrapper)

Limb A — **from the metric to the source.** Compute G^μ_ν for (P1) symbolically. Read off `T⁰₀`, `T¹₁`, `T²₂` via the Einstein
equations with the paper's sign convention (recorded in C1 from the paper's own Schwarzschild limit). Compare each to (P2),
(P4) **as printed** — exact symbolic equality after simplification, or a printed residual.

Limb B — **the printed relations.** (P3): confirm the r → 0 limit of (P1) is de Sitter with `Λ = 3/r0²` and that `Λ = 8πG ε0/c⁴`
requires exactly (P3). (P5): evaluate the integral with (P2) and (P3) and compare to `r_g c²/2G`. (P6): compute the
Kretschmann scalar of (P1) and its r → 0 limit. (P7): both asymptotic limits.

Limb C — **independent conservation check (the only non-automatic one).** Take the PRINTED components (P2), (P4) as given
numbers of the printed metric and evaluate `∇_μ T^μ_r` directly. Non-zero residual ⇒ the printed (P4) is not the tensor the
metric demands (this is limb A's finding by a second route; it is kept because it is what the cluster asked for).

Each limb ends in a machine-checkable record: expression, simplification path, residual. Two attempts per item; a symbolic
timeout is a reportable outcome (`R3E_NOT_EVALUABLE` for that item), not a lost day.

## 4. Outcome classes (precedence top to bottom; exactly one is filed)

1. `R3E_NO_CLASS` — a pre-audit control (C1–C4) fails in every seat, or the packet fails redaction; nothing is filed.
2. `INCONCLUSIVE_CONVENTION` — a check's outcome differs between two admissible readings of the printed text (OCR or sign
   convention) and the record itself does not choose. State the readings and both outcomes.
3. `PROFILE_INCONSISTENT` — at least one of (P2)–(P7) is **unreproduced from the stated inputs** under the recorded reading,
   after two attempts, with the residual printed. Name the item.
4. `PROFILE_CONSISTENT` — every item (P2)–(P7) reproduces exactly under the recorded reading.
5. `R3E_NOT_EVALUABLE` — an item hit the timeout or unavailable machinery in both attempts and no other class applies.

A `PROFILE_CONSISTENT` outcome does **not** change the warrant: the profile stays *assumed*; what it settles is that the paper's
internal chain from the assumption is exact. A `PROFILE_INCONSISTENT` outcome is an annotation proposal for Duho, not a
tier or warrant movement.

## 5. Controls (all run live; a pre-written block with a hardcoded hash proves nothing)

- **C1 SOURCE_IDENTITY** — byte-exact `repr()` match of the transcribed anchors against the pinned 1992 text, plus the
  restatement; each OCR-ambiguous item listed with both readings and the one adopted.
- **C2 GR_BENCHMARK** — the same pipeline run on Schwarzschild (must return T = 0) and on de Sitter (must return
  `T⁰₀ = T¹₁ = T²₂ = Λc⁴/8πG` with the recorded sign); positive control with a required exact output.
- **C3 DELETION_PROBE** — delete the Einstein equations from limb A and demand the pipeline **fails** with the exact code set
  `{R3E_C3_NO_FIELD_EQUATIONS}`; a probe that lets a surviving guard mask the deletion is a control failure.
- **C4 HARNESS** — live `sympy` version print through the wrapper; exit code recorded.
- **Negative control** — a planted coefficient (3/2 → 1) in (P4) must file a non-zero residual in limbs A and C.


**Executable form (Rule 4) — each line is one printed run; PASS is defined by its printed output only:**

```
/usr/bin/python3 r3e_controls.py c1 ../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt  → C1_SOURCE_IDENTITY=PASS|FAIL, each anchor listed with its repr() match
/usr/bin/python3 r3e_controls.py c2  → C2_GR_BENCHMARK=PASS only if Schwarzschild returns T=0 and de Sitter returns the printed isotropic tensor, both printed
/usr/bin/python3 r3e_controls.py c3  → must print exactly {R3E_C3_NO_FIELD_EQUATIONS} and exit 1; any other set = control FAIL
/usr/bin/python3 r3c2_timeout.py 120 -- /usr/bin/python3 -c 'import sympy; print(sympy.__version__)'  → C4_HARNESS=PASS on exit 0 with the version printed
/usr/bin/python3 r3e_controls.py neg  → planted 3/2→1 in (P4) must print a non-zero residual in limbs A and C
```

## 6. Seats

Blind double, two engines (codex via the dispatcher; kimi via `--provider moonshot -m kimi-k3`), packet only, ACCESS_SHA on
the frozen file verified by the lane after exit, nothing read before a seat exits, no edit under a running seat. The
lane's own second route (§3 by hand for (P3), (P5), (P7)) is written and sealed before either seat is dispatched.

## 7. Closed-check against prior studies

R3D (entries 18–20) took metric (P1) as given and asked whether it fixes a minimum mass; it never computed the source. K6 was
ECKS, not Dymnikova. Entry 22's closed-daughter no-go is not reopened: no junction or global existence claim is tested.
No ledger entry is re-run.

## 8. Versions

| version | date (KST) | change |
|---|---|---|
| DRAFT 1 | 2026-09-05 (this file) | written; not ordered, not frozen, not gated |
| DRAFT 2 | 2026-09-05 | Blanc's 22:33 note: the five R3D/R3C2 lessons carried in as §0 design rules (C0 first; falsifier asymmetry with the error-landing rule; declared cap; executable controls with named commands; abort guards + enumerated read set); still not ordered, not frozen, not gated |

R3E_PREREG_DRAFT_COMPLETE
