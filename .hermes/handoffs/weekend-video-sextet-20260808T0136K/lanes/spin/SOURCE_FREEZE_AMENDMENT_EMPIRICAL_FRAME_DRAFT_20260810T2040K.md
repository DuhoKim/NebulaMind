# DRAFT AMENDMENT — empirical frame determination admissible as a FINDING (amends A3.9 §4/§5)

> **STATUS: DRAFT — NOT IN FORCE. FOR DUHO'S EXPLICIT APPROVAL.** It modifies nothing until Duho grants
> it and an independent seat gates it. `SOURCE_FREEZE.json` stays byte-identical (`f7204bd7…`) and
> `AMENDMENT_A3.9` stays frozen; this sits beside them and binds only if granted. Drafted 2026-08-10
> 20:40 KST by Lana at Duho's instruction. **Do not run the test from this draft.**

## Why this exists — stated without softening either prior ruling
Two rulings stand and this amendment does not overturn them: (i) the **documentary route is exhausted**
across three independent surfaces (CDS/VizieR ReadMe, both primary papers, SDSS `zooMirrorBias` schema —
all procedural, none states the stored orientation, and the archives defer to the papers already read);
(ii) **A3.9 §4 is documentary-only**, so *no empirical test can ESTABLISH the frame under the current
rule* — verbatim: *"A verbatim quotation is required… An inference is not a quotation."* Because the frame
cannot be established from the record, and Duho does not want it left unresolved, the only honest move is to
**lower the evidence bar on the record, and label the result for exactly what it is** — an inference, not a
documented convention. This amendment does that explicitly rather than pretending the documentary bar was
met.

## 1. What it changes, the cost, and finding-vs-establishment
**Change:** an **empirical determination** of the frame becomes admissible for the frame question — the
per-object sign test of §3 — where A3.9 §4/§5 previously excluded it as "an inference."

**Cost, stated plainly:** an empirical determination yields a **FINDING, not an ESTABLISHMENT.** A3.9 §5
reserved "establishes" for *"a verbatim statement of the recording or archival convention… i.e. of how the
stored values are oriented."* An inference from data behaviour is weaker: it tells you the data are
*consistent with* a frame, not that the archive *recorded* one.

**My recommendation on which:** admit it as a **FINDING only**, and forbid it ever being recorded as an
establishment. Erasing the finding/establishment distinction is precisely what A3.9 §5 exists to prevent,
and an empirically-inferred frame must never be citable as a documented one. Concretely: even a conclusive
test resolves `FRAME_UNSTATED` only to **`FRAME_INFERRED` (frame X, empirically inferred; documented
convention still absent)** — it does **not** become `FRAME_AS_SEEN`/`FRAME_DEMIRRORED`, which A3.9 licensed
only on documentary establishment. Whether `FRAME_INFERRED` further unlocks any Land-comparative phrasing
is a **separate decision I recommend gating conservatively** (a Land comparison is a claim about the sky
and should not ride on an inference silently); default is that it does not, and the fenced instrument
reading may state the inferred frame **with its inference label** but no "confirms/contradicts Land."

## 2. Permanent inference labelling, and how to stop the label being lost
The finding must carry, **permanently and in every downstream artifact**, the label that the frame is
**empirically inferred, not a documented convention.** To prevent the label being stripped downstream:
- **Bind the label to the value, not to prose.** Any artifact that states the frame must carry a required
  machine field `frame_basis: "empirical_inference"` travelling with the value; a frame value without that
  field is **invalid input** and fails its own gate. The label cannot be dropped by paraphrase because the
  value is unusable without it.
- **A build-failing OCR/text gate:** any rendered or written artifact that states the frame (or a
  sign/handedness reading that depends on it) without the word-level qualifier "inferred, not documented"
  **fails the build** — the same class of gate that already scans for forbidden terms.
- **The provenance finding stands beside it unchanged:** `LANA_SPIN_FRAME_PROVENANCE_FINDING` (the negative
  documentary result) remains the record that the *documented* convention is absent. The empirical finding
  never supersedes it; the two are recorded together so no later reader can mistake the inference for the
  missing documentation.

## 3. The test — carried forward exactly as defined (Path B)
Restrict to objects carrying **both** a mirrored-condition direction field (`pcS1`, GZ1 Table 5 /
`p_cw_mr1`, SDSS `zooMirrorBias`) **and** the unmirrored (normal-leg) clockwise fraction (the zooSpec/main
GZ1 classification). Per object, examine the **sign of the correlation** between the mirrored-stored
clockwise fraction (`pcS1`) and the unmirrored clockwise fraction. Pre-registered predictions:
- **FRAME_AS_SEEN** (stored as displayed in the mirrored image) → mirroring flips apparent handedness →
  **negative** correlation.
- **FRAME_DEMIRRORED** (stored rotated back to sky) → both fields refer to the same sky-frame handedness →
  **positive** correlation.
The discriminant is the *sign*, opposite under the two conventions. Nothing else is inferred from the test.

## 4. Pre-registered stopping conditions — decided BEFORE any number is seen (the most important part)
The inconclusive conditions carry **equal weight** with the two clean outcomes. All thresholds and the
control construction below are **frozen (sha-pinned) and gated by an independent seat before any
correlation is computed**; the correlation is computed **once**; any outcome that does not clear **every**
gate is recorded **INCONCLUSIVE → the lane returns to `FRAME_UNSTATED` / Path C**, and an inconclusive
result may **never** be talked into a clean one afterward. The pre-registration is the whole integrity of
this test.

Pre-registered rules (exact numbers to be frozen at gate; structure fixed here):
1. **Per-object vote-count floor.** Objects below a frozen minimum vote count in *either* leg are excluded
   (a per-object sign is meaningless at low counts). If the surviving set is below rule 4's floor →
   INCONCLUSIVE.
2. **Near-zero guard.** A sign is decisive only if `|ρ| ≥ ρ_min` **and** `p < α`, both frozen at gate. If
   `|ρ| < ρ_min` or not significant → INCONCLUSIVE (consistent with neither frame).
3. **Bias-confound control — the critical one.** The classifier handedness bias, the very effect under
   study, can induce correlation structure of its own. Pre-register a **bias-only control** (e.g. the same
   per-object correlation computed where the frame prediction is null but the bias is present, or a
   permutation preserving the bias structure and scrambling the frame relation). If the control reproduces
   a same-sign correlation at ≥ a frozen fraction of the main magnitude, the sign **cannot be attributed to
   the frame** → INCONCLUSIVE. This control is computed and gated in the same frozen contract as the main
   test.
4. **Subset size and representativeness.** Require ≥ a frozen minimum of matched objects after rule 1; and
   pre-register a selection-function comparison of the matched subset against the full bias sample on
   handedness-relevant covariates (the coverage is 77.6%, with an unknown selection on the missing ~20,493
   objects, per `LANA_T3_REDERIVATION.md` §4.1/§4.3). If the missing subset is non-random in a way that
   could flip the sign → INCONCLUSIVE.

Decision table, fixed before the run: **negative & all gates pass → FRAME_INFERRED = as-seen (labelled
inference); positive & all gates pass → FRAME_INFERRED = de-mirrored (labelled inference); anything else →
INCONCLUSIVE → FRAME_UNSTATED stands.** No fifth outcome; none chosen after seeing the number.

## 5. Reuse of `t2_mirror_bias.py` / `T2_MIRROR_BIAS.json`
- **Reusable:** the parsing/matching infrastructure — it already loads Table 5 (mirrored) against the
  zooSpec (unmirrored) leg on the matched subset with pinned anchors. That plumbing is sound and should be
  **reused**, not rebuilt.
- **Must be adapted, not reused as-is:** its existing computation is the **aggregate asymmetry**
  (`A_normal` vs `A_mirrored`, a dominance-ladder sign-flip) — a **different statistic** from the §3
  **per-object correlation** frame discriminant. The per-object correlation and the rule-3 bias control are
  **new code** added onto the reused parsing; the aggregate-asymmetry output must not stand in for the
  frame test.
- **Has its existing output already touched this question? No — and a caution.** `T2_MIRROR_BIAS.json`
  answered the *asymmetry* (which is exactly the fenced, withheld result whose *interpretation* depends on
  the frame); it did **not** run the per-object frame discriminant, so the frame question is untouched by
  it. **Caution:** because that asymmetry output is already known, whoever runs the frame test has seen
  related numbers — so rule-4's pre-registration must be **frozen and independently gated before** the
  correlation is computed, and the correlation run must be a fresh, separately-receipted computation. This
  is the one place the "decide before seeing" discipline is most exposed.

## 6. What this amendment does NOT unblock — one of four
Even a conclusive, gate-passing test resolves only the **frame** blocker (to `FRAME_INFERRED`). The other
three stand untouched: **`STATUS_RESULT_MISMATCH`** (the A3.8 post-run independent verdict-record review of
`T4_PAIRED_FLIP.json` is unperformed), **`WORKFLOW_STATUS_NOT_RELEASE_READY`** (evidence-freeze, receipts,
referee, video stages pending), and **`LATER_FREEZE_EXCLUDES_NEW_POINTERS`**. Therefore
`BLOCK_SUBSTANTIVE_RESULT_RENDER; ALLOW_METHOD_ONLY_CANARY` **survives even a successful test**,
`video_reportable_now` stays **false**, and the forbidden scope binds unchanged (no T3/T4 result figures, no
dipole-axis interpretation, no parity violation, no BHU support). **This amendment unblocks nothing about
the rendered result.** It converts one blocker from "unresolvable" to "resolvable by a labelled inference,"
and nothing more.

## 7. My recommendation — and my dissent, on the record
This morning I recommended accepting `FRAME_UNSTATED` as **terminal (Path C)**, and I still think that is
the **cleanest** outcome and that the amendment does not weaken the exhaustion/documentary rulings. So my
position is **conditional support, with two clear-eyed caveats Duho should grant this knowing:**
1. **Inconclusive is a genuinely likely honest outcome.** The rule-3 bias confound is real — the effect
   under study can produce the same sign — so there is a material chance the test costs the effort and
   returns INCONCLUSIVE, i.e. back to Path C with nothing gained but a stronger "we tried." Granting this
   is a bet that may honestly lose.
2. **The pre-registration is the whole thing.** If §4's thresholds and controls are frozen and independently
   gated before any number is seen, this is an honest lowering of the bar, not manufacturing a result. If
   that gate is weak or skipped, it becomes exactly the failure it is meant to avoid — an ambiguous number
   massaged into a clean frame. I would refuse to concur with any run whose pre-registration was not gated
   first.
On finding-vs-establishment and the Land-comparative gate, my recommendations in §1 hold: FINDING only,
permanent inference label, and no automatic Land comparison. **If Duho would rather not accept those
constraints, my recommendation flips back to Path C** — an inference recorded as more than an inference is
worse than an honest null.

## 8. Review, if granted
Lana rules the science boundary of the pre-registration; **Kun gates the frozen §4 contract adversarially
BEFORE any correlation is computed** and defaults to BLOCK/INCONCLUSIVE under uncertainty; Tori binds the
frozen contract, the receipts of the single computation, and confirms the `frame_basis` label and the OCR
gate. Yui/any writer touches nothing until all three pass. No number is computed from this draft; Duho
grants or refuses first.