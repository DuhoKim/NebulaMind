# Lana — C2 V2 Repair Brief (build a NEW versioned candidate; preserve V1)

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_C2_LANA_V2_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_C2_LANA_V2_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at Deepening Gate 2. Dispatched by: Tori (do not self-start).
- Lane: **direct Claude subscription only** — no API-key, no PAYG, no third-party route, no Nous purchased-balance.
- This brief is standalone. It implements `HWAO_C2_REDTEAM_ADJUDICATION_V1` (fix F1–F4). **Public status stays `AWAITING_EXPLICIT_PUBLISH_APPROVAL`; this is NOT a publication step.**

## Your role
Build a **NEW, versioned** C2 candidate `c2-mzr-gated-e2e-candidate-v2/` that applies the four red-team fixes. **V1 is frozen and must not be touched.** Retain every source number/reference, the citation split, and the O/H/TENSION/provenance caveats.

## Frozen V1 (READ-only; NEVER overwrite/edit/delete)
- `packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate/candidate.tex` = `c615b2f39502bf4e15f54e8fba3818ca480c9fd162360044c804893a11bc00d9`
- `…/candidate.pdf` = `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e`
- `…/result.png` = `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` (byte-identical to source figure)

## Allowed READ roots (read-only)
1. Frozen V1 candidate (base for V2): `packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate/candidate.tex`, `result.png`.
2. Source (for number/reference fidelity + byte-identical figure): `/Users/duhokim/…/lab-runs/gated-e2e-demo/draft.tex`, `gated-e2e-demo.json`, `gated-e2e-demo/result.png`.
3. Red-team + adjudication: `packets/C-candidate-build/lana-c2-redteam/SCIENCE_REDTEAM_REVIEW.md`, `reviews/hwao/HWAO_C2_REDTEAM_ADJUDICATION.md`; `packets/C-candidate-build/kun-c2-audit/C2_CONTRACT_AUDIT.md`; baseline; this brief.

## Allowed WRITE root (exclusive to you — single writer; VERSIONED only)
- New V2 deliverables ONLY under `…/packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate-v2/` — do NOT write into the V1 folder.
- V2 receipt: `…/reviews/lana/LANA_C2_V2_RECEIPT.md`.
- Temp ONLY as `…/c2-mzr-gated-e2e-candidate-v2/_tmp_*` (never TMPDIR, /tmp, scratchpad).

## Forbidden (stop and report if any is required)
Overwrite/edit/delete any V1 file; edit or replace any source file or any current Lab artifact (`lab-runs/**`); replace any existing PDF; run the live runner; write to any public/static root; copy the candidate into any public/repo/served location; any DB/SQL/API/wiki/page-version write; deploy/restart; git; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance; Anthropic third-party PAYG routing. **No publication.** **Lane: direct Claude subscription only.** Compile ONLY inside the V2 root.

## Fixes to apply (F1–F4; representation/wording only — introduce NO new scientific number or claim)
1. **F1 — soften the Result interpretive sentence.** Replace the Result sentence that asserts the comparison "provides insights into the relationship between galaxy mass and gas-phase metallicity" with a **descriptive** statement that cross-references the Caveats — e.g. "We present the two median relations (TNG100 and SDSS); their direct comparison is bounded by the unresolved O/H-scale systematic (see Caveats) and is not interpreted as physical here." Keep the source numbers; drop the interpretive-insight claim.
2. **F2 — qualify/remove unsubstantiated "reproducible."** In the Abstract, remove or qualify "reproducible" (the forced `spec.force=true` demo lineage does not substantiate it). Descriptive language only (e.g. "a bounded, descriptive study"), or defer authoritative status explicitly to the Provenance caveat.
3. **F3 — surface the bounding status at Abstract + figure-caption level.** Add a one-line scale-limited / TENSION / anchor flag to the Abstract (e.g. "This is a scale-limited, TENSION-flagged anchor comparison on un-reconciled O/H scales — see Caveats.") AND add a caption note to the figure — **caption text only, never modify the source figure image** — e.g. "median relations on un-reconciled O/H scales; the TNG–SDSS comparison is scale-limited (see Caveats)."
4. **F4 — visible not-submitted tag near Title/Abstract.** Add a visibly-rendered line near the Title/Abstract: "AI-assembled draft — not submitted, not peer-reviewed (`AI_DRAFT_NOT_HUMAN_GOLD`)."

## Must retain (do not weaken or drop)
- All source numbers verbatim: TNG100 `23,722`, SDSS `120,000`, `z=0`, SF-weighted gas metallicity → O/H (solar-scaled). Invent no number and no O/H offset.
- All 5 references verbatim (Qi2025, Torrey2019, Garcia2023, Guo2016, **LaraLopez2013**).
- The Introduction citation **split** (four single-citation sentences).
- The three caveats — **O/H-scale** (bounded "confounded … cannot be interpreted as physical until a common calibration is established"), **TENSION** (carried, not upgraded), **Provenance** (forced-demo lineage) — unchanged or strengthened, never weakened. Keep the original source Caveats paragraph intact.
- The `AI_DRAFT_NOT_HUMAN_GOLD` header comment + rendered provenance disclosure.

## Figure & compile
- Copy the source `gated-e2e-demo/result.png` into the V2 root (read source → write copy); it must remain **byte-identical** (`ed83a825…`). Never modify the source figure.
- Compile a PDF with `tectonic` INSIDE the V2 root only (`tectonic candidate.tex --keep-logs`), and **save the return code**. If it succeeds, include `candidate.pdf`; if it fails, deliver `.tex` + `COMPILE_NOTE.md` (not a failure state). Never invoke the Lab runner; never write outside the V2 root.

## Deliverables (V2 root)
`candidate.tex`, byte-identical `result.png`, `candidate.pdf` (if compiled), `COMPILE_NOTE.md`, and a `V1_TO_V2_DIFF.md` (or note) enumerating exactly the F1–F4 edits. All science artifacts headed `AI_DRAFT_NOT_HUMAN_GOLD`. Isolated; **no publication**.

## Stop conditions
Any need to invent a number/claim; any temptation to edit V1, a source file, or a current Lab artifact; source drift vs `INPUT_SHA256.txt`; a compile that would write outside the V2 root; a payment/overage/top-up/Nous/PAYG prompt; any public or source mutation.

## Completion contract
`reviews/lana/LANA_C2_V2_RECEIPT.md` must list the V2 file SHA-256, confirm V1 + source untouched (re-state the frozen V1 hashes), enumerate the F1–F4 fixes with before/after, confirm all source numbers/refs + citation split + three caveats retained, the figure byte-identity, the saved tectonic rc, any STOP notes, and a completion state of `DONE` / `PARTIAL` / `BLOCKED` (never relabel PARTIAL/BLOCKED as success). End the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_C2_LANA_V2_COMPLETE_V1`
