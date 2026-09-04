ACCESS_SHA=5a441713e680d6f24f0920a0f0dcf9fd42ae8b01ba4511bdb3c349311e42ae63
GATE=PREREG_SOUND_WITH_REPAIRS

### Explicit Checks
1. **LINE TRACING**: The cited lines do not contain exactly what is claimed due to PDF text extraction artifacts. L87 actually contains ` ˜ =   − αn2f ,` (missing the `ε` character) and L126 contains `K = β(κ  ˜ )2 ,` (also missing `ε`). L128 contains a ligature: `coeﬃcient`. A string match for `K = β(κ ε̃)²` will fail.
2. **THE DRAFT GATE'S REPAIR**: Verified. The frozen version correctly carries the exact wording: "prints the exact text and line numbers".
3. **OUTCOME CLASSES**: Classes 3 (fitted) and 4 (free) are exhaustive and mutually exclusive in principle, but they are distinguishable *only in principle* by inferring author intent from the text. There is no operational step or mathematical control defined to separate them; control C4 explicitly lumps them together ("evidence for class 3 or 4").
4. **CONTROLS**: The set of controls is complete but inconsistent with custody requirements. C5 (harness pinned) is a decoration, not a real custody control. Asking an LLM to literal-print a pre-written text block with a pre-computed SHA proves nothing about the environment it runs in, as the agent will just echo the text.
5. **CIRCULARITY**: The design bounds circularity. Section 6 explicitly declares "The observables are the object under test, never an input to the determination of β," ensuring the audit procedure itself cannot be circular.
6. **RE-RUN**: Verified. The audit targets the production coefficient `β` and explicitly states it does not re-run K3, which audited the distinct spin-density closure coefficient `α`.
7. **FAIRNESS**: There is no slip asserting the paper is wrong; it remains within "unreproduced" boundaries. The closest judgmental terms are "tuned parameter" (L21) and "gap" (L51), which describe theoretical properties, and "defect" (L74), which refers to the audit lane's own executable discipline, not the paper.

### Numbered Repairs
1.
- Quoted sentence: `- **C1 — source identity.** Reproduce \`K = β(κ ε̃)²\` and the L128 sentence from the pinned version of record. Exact assertion: \`C1_SOURCE_IDENTITY=PASS\`.`
- Defect: The PDF-extracted version of record has font artifacts and actually reads `K = β(κ  ˜ )2 ,` (missing the epsilon) and uses a ligature in `coeﬃcient`. A seat instructed to reproduce the clean strings will fail C1, halting the gate.
- EXACT replacement: `- **C1 — source identity.** Reproduce \`K = β(κ  ˜ )2 ,\` and the L128 sentence containing \`coeﬃcient\` (with ligature) from the pinned version of record. Exact assertion: \`C1_SOURCE_IDENTITY=PASS\`.`

2.
- Quoted sentence: `**Every seat prints this block at the top of its output, and the result file records it:**`
- Defect: C5 is a decoration (cargo-cult control). Asking a seat to print a pre-written text block with a hardcoded SHA proves nothing about the actual environment, as the seat will simply copy-paste it. A true custody control requires executing environment-probing commands and printing their live output.
- EXACT replacement: `**Every seat must execute live commands to verify its python version and python3 binary SHA, printing the actual execution output at the top of its record, and the result file records it:**`

3.
- Quoted sentence: `Classes 3 and 4 are distinct and must not be merged: a fitted coefficient is a calibration, a free one is a gap.`
- Defect: Classes 3 and 4 are currently only distinguishable in principle. Since C4 groups them together, a seat needs a specific operational instruction to differentiate them based on the text.
- EXACT replacement: `Classes 3 and 4 are distinct and must not be merged: a seat separates them by quoting the exact text where the author either targets a specific observable value (fitted) or leaves the parameter arbitrary (free).`

### Answer to 8
The design can stall. Control C2 ("Vary β symbolically") asks a seat to perform symbolic dependence mapping on the paper's chain. However, the paper computes the scale factor a(t) and reconstructs the potential V(φ) numerically (L244: "We numerically solve the Friedmann equations..."). Asking an automated seat to symbolically map dependence through a complex numerical solver chain will likely cause symbolic engines (like SymPy) to hang indefinitely, stalling the seat-day without triggering the "two attempts" failure condition because the process never returns.

R3A_PREREG_GATE_COMPLETE
