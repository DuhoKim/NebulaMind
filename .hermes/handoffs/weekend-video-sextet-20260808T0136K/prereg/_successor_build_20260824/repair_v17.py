import re
import hashlib

filepath = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V17_20260827.md"

with open(filepath, "r") as f:
    text = f.read()

# Blocker 1
s63_text = """### §6.3 General conduct clauses

- **No strata in the estimator.** The centred slope needs no tertiles; the one-shot strata
  hazard is retired by design.
- **Calibration.** Bin-construction algorithm and the 3 × 9 joint allocation with V3-pred's
  nine HC strata are frozen in code (`calibration_bins()`, `assign_bins()`,
  `allocate_handcheck()` — proportional, largest remainder, explicit tie rule, and BOTH
  inherited floors enforced: ≥ 10 per non-empty joint cell **and ≥ 30 real labels per live
  inherited HC stratum** (V6 enforced only the first; a gate produced a formally-filled but
  invalid sample). Infeasible floors FAIL rather than shrink. `calibration_bins()` states and
  IMPLEMENTS one tie rule and refuses degenerate bins. Numeric boundaries are instantiated and
  sealed at **BS-2f** from positions and flags only. **BS-8f** reports â, σ_a, a_LB, per-bin
  â_b, σ_ab, a_LB_b, ε̂ and the full Cov_a via `accuracy_from_handcheck()`, which implements
  **the inherited HC-1H estimator** `a = (raw − ε)/(1 − 2ε)` with the shared-ε derivative
  propagated — so Cov_a's off-diagonal is a real shared-error term, not an additive constant.
  (V6 returned the raw agreement rate and both gates caught it.) **Admissibility (`adjudicate_path()`):**
  `max_b |â_b − â| ≤ 0.03` AND every `a_LB_b ≥ 0.85` → scalar path; spread failure only →
  profile path; any `a_LB_b < 0.85` → **INCONCLUSIVE-BY-CALIBRATION, pre-unblinding halt.**
  V3-pred's HC-1H measurement and validity rules (committee, sealed keys, HC-5, HC-6) are
  carried by quotation at freeze.
- **Void rule.** Any post-first-real-χ change to ANY binding rule, parameter, algorithm, slot
  schema, randomness/serialization contract, reference-code byte, or decision threshold in
  this preregistration voids the run; only the mechanical filling of predeclared class-E
  values by their frozen producers is exempt. Post-read amendments cannot cure a void.
- **One change per iteration** (external-practice adoption, 2026-08-25): every gated revision
  of this text changes one thing per finding, and the §10 trace maps finding → change; any
  change not traceable to a finding is listed separately with its hypothesis stated.
- **No claim stronger than its check.** Gate-state sentences never exceed the cited
  artifact's first line.
- **Custody.** Receipts with digests; deliverables sha-pinned at gate dispatch by the gate's
  own report (an external witness) and committed to git; self-referential hash chains are not
  custody; describe-vs-compute discipline throughout.
- **Blind double, honestly scoped** (gpt56-V5 F6 / codex-V5 F3): because §0 makes the code
  bodies normative, a second implementation cannot be required to reproduce body-defined bytes
  without reading them. Therefore: the second product is a **clean-room reimplementation from
  this constitution plus a published per-function normative specification** (op order stated),
  and it is gated against the reference on the fixture battery. Where the spec is insufficient
  to reproduce a digest, that is a **spec defect to be repaired**, not an agreement failure.
  Divergence in any integer, sequence, or verdict is a STOP recorded as a finding — never
  reconciled by editing either implementation toward the other.
"""
old_s63_text = """### §6.3 General conduct clauses

- **No strata in the estimator.**
- **Calibration.**
- **Void rule for changes.**
- **One change per iteration.**
- **No claim stronger than its check.**
- **Custody.**
- **Blind double, honestly scoped.**
"""
text = text.replace(old_s63_text, s63_text)
text = text.replace("citing V15 lines 570–573 which void any post-first-real-χ change to a decision threshold.", "citing §6.3 which voids any post-first-real-χ change to a decision threshold.")

# Blocker 2
old_stage_c = """**Stage C (class E, BS-5f; after inference, before unblinding).** The same frozen generator,
addresses and pass rule, run on the **sealed accepted-position mask** (BS-2f: brickid, objid,
position, acceptance flag, calibration-bin label — never a χ sign), with the measured a_LB
(scalar) or {a_LB_b} (profile) from BS-8f. FAIL → **INCONCLUSIVE-BY-POWER declared before
unblinding; the run halts; no real-sky statistic is ever formed.**"""
new_stage_c = """**Pre-Stage-C Calibration Gate:** Before running Stage C, the measured calibration bound must be checked. If any bin's `a_LB_b < 0.85`, it emits an immediate pre-unblinding `INCONCLUSIVE-BY-CALIBRATION` and the run halts. Only if all bins satisfy `a_LB_b >= 0.85` may Stage C run.

**Stage C (class E, BS-5f; after inference, before unblinding).** The same frozen generator,
addresses and pass rule, run on the **sealed accepted-position mask** (BS-2f: brickid, objid,
position, acceptance flag, calibration-bin label — never a χ sign), with the measured a_LB
(scalar) or {a_LB_b} (profile) from BS-8f. FAIL → **INCONCLUSIVE-BY-POWER declared before
unblinding; the run halts; no real-sky statistic is ever formed.** **BS-5f certifies only the locked pre-attrition BS-2f mask. Because any post-unblinding removal immediately terminates the run with `INCONCLUSIVE-BY-CALIBRATION`, there is no post-attrition Stage-C reevaluation.**"""
text = text.replace(old_stage_c, new_stage_c)

# Make §10 claim true, this means we keep the text in §10 since it claims §4 edits were made and now they are.

# Blocker 3
# Remove reason (d) from list, it's actually already removed in V16 according to finding 1 "V16 correctly narrows the pre-lock exclusion list to reasons (a)–(b)". Wait, the finding says "(a)–(b)". But the finding 1 also says "lines 358–363 still say “Reason (d) is the outcome-adjacent one,” and lines 371–372 still say “The thresholds in (d) are pinned ... in BS-3.”"
# Also need to assign confidence threshold to Row P state (7) and remove from BS-2a or BS-3.
text = re.sub(r'5\.\s+\*\*The confidence quantity is defined, not merely thresholded\.\*\* Reason \(d\) is the\s+outcome-adjacent one.*?join the ledger against the independently fixed attempt/receipt record\.\n', 
r'''5. **The confidence quantity is defined, not merely thresholded.** The frozen definition must
   name the field or function that produces it, and the exclusion path must be shown — by
   construction, not assertion — unable to read handedness, its sign, its amplitude, or the
   object's position relative to the tested axis. An "absent output" may not be asserted: it is
   established by joining the ledger against the independently fixed attempt/receipt record.
''', text, flags=re.DOTALL)

text = text.replace('7. **The thresholds in (d) are pinned before any image byte**, in BS-3, with the same force as\n   any other frozen constant. A threshold chosen or moved after inference exists voids the run.',
'7. **The confidence threshold is defined as part of the Row P state (7) exclusion or the refused BS-2a design**, and will be pinned before any image byte. A threshold chosen or moved after inference exists voids the run.')

text = text.replace('| BS-3 | Hwao | instrument constants τ and `weights_sha256`; `antisymmetry_receipt`', '| BS-3 | Hwao | instrument constant τ (instrument identity) and `weights_sha256`; `antisymmetry_receipt`')

text = text.replace('| BS-2a ⚠ **DESIGN, CLASS P — moved here in V13** | Hwao | **acceptance design**: the numeric confidence threshold **and the named authority that sets it**, retry/failure semantics, the evidence schema for exclusion reasons (a)–(d), the ledger schema, the recomputation code and its fixtures.',
'| BS-2a ⚠ **DESIGN, CLASS P — moved here in V13** | Hwao | **acceptance design**: the numeric confidence threshold **and the named authority that sets it**, retry/failure semantics, the evidence schema for exclusion reasons (a)–(b), the ledger schema, the recomputation code and its fixtures.')

# Blocker 4
# Move unblinding receipt out of the class-E slot table into a separately headed post-unblinding-artifact table/list and retain the count seven, or classify it as the eighth Class-E row and change the prose/lint contract to eight.
# "Recount from the table and make prose, inventory and lint assertion agree." -> I'll change the prose to 8.
text = text.replace("There are 7 class-E slots", "There are 8 class-E slots")
text = text.replace("lint checks this dynamically, requiring `|Class E| == 7`", "lint checks this dynamically, requiring `|Class E| == 8`")

# Blocker 5
# Canonical outcome registry
# §5 says the production path emits "exactly one of four outcomes". I'll change it to "exactly one outcome from the canonical registry".
old_outcomes = """- **REPRODUCED-LONGO:** p < **0.001** AND Longo's sign AND |Â_L − 0.0408| ≤ 3·σ_comb AND
  Â_L ≥ the evaluated floor.
- **REJECTED-AT-LONGO-AMPLITUDE:** p > **0.05** AND (|Â_L| + 3·σ_ours(â)) < **0.0408**.
- **INCONCLUSIVE:** any other numeric outcome, explicitly including 0.001 ≤ p ≤ 0.05.
- **INCONCLUSIVE-BY-POWER / INCONCLUSIVE-BY-CALIBRATION:** §4 / §6; no run."""
new_outcomes = """- **Numeric verdicts:** **REPRODUCED-LONGO** (p < **0.001** AND Longo's sign AND |Â_L − 0.0408| ≤ 3·σ_comb AND Â_L ≥ the evaluated floor), **REJECTED-AT-LONGO-AMPLITUDE** (p > **0.05** AND (|Â_L| + 3·σ_ours(â)) < **0.0408**), **INCONCLUSIVE** (any other numeric outcome).
- **Pre-statistic inconclusive halts:** **INCONCLUSIVE-BY-POWER** (§4) and **INCONCLUSIVE-BY-CALIBRATION** (§6, pre-unblinding or post-unblinding removal).
- **Accounting refusals:** **INCONCLUSIVE-BY-MISSING-RECORD**, **INCONCLUSIVE-BY-DUPLICATE**, **INCONCLUSIVE-BY-ORPHAN**, **INCONCLUSIVE-BY-MALFORMED** (from Row P).
- **Per-attempt exclusions:** **EXCLUDED-BY-ABSENCE**, **EXCLUDED-BY-NONFINITE**, **EXCLUDED-BY-CONFIDENCE**.
- **VOID:** triggered by forbidden acts or protocol/digest deviation."""
text = text.replace("exactly one of four outcomes", "exactly one outcome from the canonical registry")
text = text.replace(old_outcomes, new_outcomes)

# Repair 6
# "Folded on Duho's instruction at 21:48 KST on 2026-08-27, while R15's referee verdicts did not yet exist."
old_banner = "> Folded **on Duho's instruction at 21:48 KST on 2026-08-27, while R15's referee verdicts did\n> not yet exist.** The referee round ran in parallel with the fold. When the verdicts landed\n> during the assembly:"
new_banner = "> The fold was **instructed and initiated at 21:48 KST on 2026-08-27, before any verdict existed.**\n> The verdicts landed during assembly:\n> - CODEX at 21:52:33 KST\n> - GPT56 at 21:53:46 KST\n> \n> The final bytes of V16 were written **after** applying the GPT56 schema-inventory repair. The final pinned bytes were NOT produced before the verdicts existed."
# Wait, let's find the exact text in V16.
text = re.sub(r'> Folded \*\*on Duho\'s instruction at 21:48 KST on 2026-08-27.*?during the fold:', 
"""> The fold was **instructed and initiated at 21:48 KST on 2026-08-27, before any verdict existed.**
> The referee round ran in parallel with the assembly. When the verdicts landed
> during the assembly:""", text, flags=re.DOTALL)
# Also add the final bytes note.
text = text.replace("> The GPT56 blocker is **closed at document-contract level by this edit**",
"> The final bytes of V16 were written **after** applying the GPT56 schema-inventory repair, not before the verdicts existed.\n>\n> The GPT56 blocker is **closed at document-contract level by this edit**")

# Also fix the fold record at the end of the file
old_fold = "The artifact was folded at 21:48 KST, before R15 referee verdicts existed."
new_fold = "The fold was instructed and initiated at 21:48 KST, before R15 referee verdicts existed. The verdicts landed during assembly at 21:52:33 and 21:53:46, and the final bytes were written after applying the GPT56 schema-inventory repair."
text = text.replace(old_fold, new_fold)
text = text.replace("The round had not returned when the fold was performed", "The round had not returned when the fold was initiated, but the final bytes were written after the round returned")


# Repair 7
text = text.replace("These fill the class-P inputs that six gate rounds said could not be closed by writing alone.",
"These are measured candidate values/evidence only; they do not fill BS-5p or any other unreceipted class-P slot.")

text = text.replace("Scalar path: `Â_L = β̂/(2â−1)`.", "Scalar path: `Â_L = β̂/(2â−1)`. Profile path (frozen fallback, §6): `Â_L = β̂/ŵ` with `w_profile()` under **unit weight per accepted object**. The branch predicate (after BS-8f, before any real statistic, explicitly tied to `adjudicate_path()`) selects the scalar path if `max_b |â_b - â| <= 0.03`, and selects the profile path otherwise. This is a profile selection, not a run failure.")
text = text.replace("Profile path (frozen fallback, §6): `Â_L = β̂/ŵ` with\n`w_profile()` under **unit weight per accepted object** — the same empirical measure as β̂.", "")

# Rename V16 to V17 in the title and banner
text = text.replace("# PREREGISTRATION DRAFT V16 —", "# PREREGISTRATION DRAFT V17 —")
text = text.replace("**V16 is a fold.**", "**V17 is a repair of V16.**")
# Also need to record V17's provenance from V16 in the banner
text = text.replace("It folded `SECTION6_DRAFT_AGY_R15.md`, sha256\n> `d2c388a451d076f880c879e888ee7901331adc62142245a285b8ff932d67f01a` — independently verified.",
"It repairs `PREREG_SUCCESSOR_DRAFT_V16_20260827.md`, sha256\n> `1b9b9486736bf734c8cb4ac8cedf54870fd179587e3e1455273ec4724132a0da` — independently verified.")

with open(filepath, "w") as f:
    f.write(text)

with open(filepath, "rb") as f:
    print(hashlib.sha256(f.read()).hexdigest())

