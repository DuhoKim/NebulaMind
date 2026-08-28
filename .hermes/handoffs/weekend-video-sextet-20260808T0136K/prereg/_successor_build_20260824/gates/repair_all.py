import re

with open('../PREREG_SUCCESSOR_DRAFT_V25_20260827.md', 'r') as f:
    text = f.read()

# Header update
text = text.replace("V25 — LONGO-AMPLITUDE", "V26 — LONGO-AMPLITUDE")
text = text.replace("V25 is a repair of V24", "V26 is a repair of V25")
text = text.replace("It repairs `PREREG_SUCCESSOR_DRAFT_V23_20260827.md`, sha256\n> `134433199c85ea4566eab7aae146455518d92d314893b3cba7a6a413163454b7` — independently verified.", "It repairs `PREREG_SUCCESSOR_DRAFT_V25_20260827.md`, sha256\n> `50f2e53256cc79707f2a4dfbf737740e6101742deb39365498737c904aa0f59b` — independently verified.")

# Blocker 1
old_b1 = """These columns were measured by the DESI survey before this study existed. Their independence from handedness comes from when the quantities were measured, not from when the predicate is evaluated or from any property of the evaluating process. Therefore, no hermetic worker, capability allowlist or blindness fixture is required, and none is claimed."""
new_b1 = """These columns were measured by the DESI survey before this study existed. The predicate is **outcome-blind with respect to this study's unobserved χ**: its columns and absolute thresholds were fixed **without reading χ and before any image byte**, so it cannot be tuned post hoc. Whether the predicate is independent of handedness *conditional on position* — the property the dipole estimator actually needs — is **not established**. Either preregister a check for it, or record it as a **stated assumption with its risk**."""
text = text.replace(old_b1, new_b1)

# Blocker 2: P8 -> P5 and distinct reason
old_b2_1 = """These thresholds were fixed before any image byte, which makes the predicate preregistered rather than chosen. This is an exclusion predicate applied at analysis time. It is NOT a redefinition of the parent catalogue. V9's `PINNED_PARENT_SHA256`, `PINNED_PARENT_ROWS = 65_060` and `PINNED_SELECTION_BRICKS = 6_445` are unchanged and must stay unchanged so no later reader mistakes this for a new sample.
   
   Row P applies this already-frozen predicate at P8; below threshold records `EXCLUDED-BY-CONFIDENCE`, and any such removal yields `INCONCLUSIVE-BY-CALIBRATION`. A threshold chosen or moved after inference exists voids the run."""
new_b2_1 = """These thresholds were fixed before any image byte, which makes the predicate preregistered rather than chosen. This defines a **distinct closed catalogue-quality exclusion reason** with authenticated evidence fields. It is NOT a redefinition of the parent catalogue. V9's `PINNED_PARENT_SHA256`, `PINNED_PARENT_ROWS = 65_060` and `PINNED_SELECTION_BRICKS = 6_445` are unchanged and must stay unchanged so no later reader mistakes this for a new sample.
   
   The frozen predicate is applied before BS-2f so the **P3 sealed mask genuinely holds 49,211 rows** while the **65,060-row parent identity stays unchanged**. Post-unblinding instrument-confidence handling is kept separate. A threshold chosen or moved after inference exists voids the run."""
text = text.replace(old_b2_1, new_b2_1)

# Terminal states
text = text.replace(
    "**EXCLUDED-BY-ABSENCE**, **EXCLUDED-BY-NONFINITE**, **EXCLUDED-BY-CONFIDENCE**, or **ACCEPTED-FINITE**.",
    "**EXCLUDED-BY-ABSENCE**, **EXCLUDED-BY-NONFINITE**, **EXCLUDED-BY-CONFIDENCE**, **EXCLUDED-BY-CATALOGUE-QUALITY**, or **ACCEPTED-FINITE**."
)
text = text.replace(
    "(5) absent measurement (dropped; `EXCLUDED-BY-ABSENCE`), (6) non-finite measurement (dropped; `EXCLUDED-BY-NONFINITE`), (7) low confidence (dropped; `EXCLUDED-BY-CONFIDENCE`), (8) accepted-finite.",
    "(5) absent measurement (dropped; `EXCLUDED-BY-ABSENCE`), (6) non-finite measurement (dropped; `EXCLUDED-BY-NONFINITE`), (7) low confidence (dropped; `EXCLUDED-BY-CONFIDENCE`), (8) catalogue quality below frozen threshold (dropped; `EXCLUDED-BY-CATALOGUE-QUALITY`), (9) accepted-finite."
)

# Blocker 3: Stage P
old_b3 = """**Measured on the real REDUCED geometry (§2.6): 995/1000, PASS, with every
  trial judged against its own null rather than a shared reference (2026-08-26). The earlier
  997/1000 on the pre-reduction geometry is retracted.**"""
new_b3 = """**The 995/1000 Stage-P result was computed on 65,060 and is superseded pending a rerun on the actual post-quality mask. BS-5p cannot be filled until that rerun exists.**"""
text = text.replace(old_b3, new_b3)

# Blocker 4: BS-2a
text = text.replace("pending the refused BS-2a design", "pending the **DESIGN, defined, UNFILLED** BS-2a design")
text = text.replace("**BS-2a is REFUSED by all three seats.**", "**BS-2a is DESIGN, defined, UNFILLED.**")
text = text.replace("| BS-2a **DESIGN, CLASS P — FILLED** |", "| BS-2a **DESIGN, CLASS P — UNFILLED** |")
text = text.replace("already-refused BS-2a design", "already-unfilled BS-2a design")
# "One of fifteen class-P slots is filled" (already correctly says 15, so ensure it says one)
# No change needed if it already says "One of fifteen" but let's check.
text = text.replace("One of fifteen class-P slots is filled (BS-2m).", "One of fifteen class-P slots is filled (BS-2m).")

# Row C2
old_c2 = """| C2 | **Cutout integrity verifier** — `verify_cutout_integrity` symbol and digest to be pinned at BS-2a (**FILLED**). No hermetic worker, capability allowlist or blindness fixture is required. | reads **only** cutouts via row B and fixed parent lists."""
new_c2 = """| C2 | **Cutout integrity verifier** — `verify_cutout_integrity` symbol and digest to be pinned at BS-2a (**DESIGN, defined, UNFILLED**). A hermetic worker, capability allowlist, and blindness fixture are required. | reads **only** cutouts via row B and fixed parent lists."""
text = text.replace(old_c2, new_c2)

# Row E
old_e = """| E | **Acceptance-ledger recompute** | reads **only the separate authenticated acceptance-evidence projections** in the main store (predicate bits only) and fixed parent lists — and computes the structural §2.7(2) predicates from it, **excluding instrument absence/non-finiteness (reason c), which is dropped from the pre-lock structural exclusion**. Does not read the cutout-completion receipt. → atomically writes both the append-only evidence ledger and the realised partition | P2–P3, after complete inference | BS-2a (design), and exactly one verified acceptance-evidence projection per parent object | the realised-partition record, bound by BS-2f |"""
new_e = """| E | **Acceptance-ledger recompute** | reads **only the separate authenticated acceptance-evidence projections** in the main store (predicate bits only), the fixed parent lists, and the authenticated catalogue-quality evidence fields — and computes the structural §2.7(2) predicates and catalogue-quality exclusion from it, **excluding instrument absence/non-finiteness (reason c) and instrument confidence, which remain dropped from the pre-lock structural exclusion**. Does not read the cutout-completion receipt. → atomically writes both the append-only evidence ledger and the realised partition, ensuring the **P3 sealed mask genuinely holds 49,211 rows**. | P2–P3, after complete inference | BS-2a (design), and exactly one verified acceptance-evidence projection per parent object | the realised-partition record (N = 49,211), bound by BS-2f |"""
text = text.replace(old_e, new_e)

# Row F
old_f = """| F | **Calibration-bin sealing** | reads the accepted partition's positions and acceptance flags only (χ-free) → writes sealed boundaries, bin labels, and the hand-check allocation | P3, at BS-2f | BS-8p and the realised partition | the sealed boundary and allocation record | any χ-bearing input to bin construction |"""
new_f = """| F | **Calibration-bin sealing** | reads the accepted partition's positions and acceptance flags only (χ-free) on the genuinely 49,211-row mask → writes sealed boundaries, bin labels, and the hand-check allocation | P3, at BS-2f | BS-8p and the realised partition | the sealed boundary and allocation record | any χ-bearing input to bin construction |"""
text = text.replace(old_f, new_f)

# Clause 10
old_c10 = """*`VOID` reverse reachability is unresolved; therefore clause 10 is not yet executable, and **BS-6 and the first image byte remain blocked** until a pinned producer or conversion handles **every enumerated void antecedent**.*"""
new_c10 = """*`VOID` reverse reachability is unresolved; therefore clause 10 is not yet executable, and **BS-6 and the first image byte remain blocked** until a pinned producer or conversion handles **every enumerated void antecedent**.* Clause 10 phases and effects must treat catalogue-quality exclusion as occurring before BS-2f, separating it from post-unblinding instrument confidence handling."""
text = text.replace(old_c10, new_c10)

# BS-2f table
old_bs2f = """| BS-2f | Hwao | sealed accepted-position mask + sealed calibration boundaries — **value-only: the realised partition produced by BS-2a's frozen code, not a new rule** | Stage C |"""
new_bs2f = """| BS-2f | Hwao | sealed accepted-position mask (N = 49,211) + sealed calibration boundaries — **value-only: the realised partition produced by BS-2a's frozen code, applying catalogue-quality exclusions** | Stage C |"""
text = text.replace(old_bs2f, new_bs2f)

# Blocker 5
old_b5 = """- **One change per iteration** (external-practice adoption, 2026-08-25): every gated revision
  of this text changes one thing per finding, and the §10 trace maps finding → change; any
  change not traceable to a finding is listed separately with its hypothesis stated."""
new_b5 = """- **One change per iteration** (external-practice adoption, 2026-08-25): every gated revision
  of this text changes one thing per finding. The coverage contract requires predecessor-only in-band mappings, plus an external pinned artifact for the current transition (or another non-self-referential design). Historical mappings are explicitly exempted: V1→V15 cite nothing. The V24→V25 mapping must cite only findings the delta demonstrably answers."""
text = text.replace(old_b5, new_b5)


with open('../PREREG_SUCCESSOR_DRAFT_V26_20260827.md', 'w') as f:
    f.write(text)
