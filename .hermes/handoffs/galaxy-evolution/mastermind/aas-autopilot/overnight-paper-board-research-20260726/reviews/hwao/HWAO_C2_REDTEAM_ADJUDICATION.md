# Hwao — C2 Red-Team / Audit Adjudication

- Marker: `OVERNIGHT_PAPER_BOARD_HWAO_C2_REDTEAM_ADJUDICATION_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Adjudicated by Hwao/Fable at Deepening Gate 2, after both C2 review lanes and the public-target mapping were `DONE`. Machine-authored; not human gold. No source/public/DB/product byte changed.

## Inputs relied on (read-only)
- Lana (direct Claude, scientific/representation lens): `SCIENCE_REDTEAM_REVIEW.md` + receipt — overall **PASS**, `BLOCKER 0 / MAJOR 0 / MINOR 4 / OK 7`, no candidate edits (candidate byte-unchanged).
- Kun (Codex gpt-5.5 Pro, mechanical lens): `C2_CONTRACT_AUDIT.md` + receipt — **PASS on all six audit items**, no FAIL, no candidate edits.
- Goru (Antigravity/Gemini, public mapping): `PUBLIC_TARGET_MAP.md` + receipt — served target is **dynamic from `lab-runs/`**; read-only.

## Determination
**V1 (`candidate.tex` `c615b2f3…`, `candidate.pdf` `eed8992d…`) is mechanically PASS and representation-PASS as an isolated, unpublished AI research-note draft** — but it is **NOT READY FOR PUBLIC PROMOTION** until findings **F1 and F3 are fixed**.
- **F1 (mandatory before promotion):** the Result sentence "provides insights into the relationship between galaxy mass and gas-phase metallicity" is an interpretive overreach that conflicts with the Caveats' "cannot be interpreted as physical." Soften to descriptive + cross-reference the Caveats.
- **F3 (mandatory before promotion):** the scale-limited / TENSION / anchor-not-frontier bounding status appears ONLY in the Caveats (p2). Title + Abstract + Figure — the surface most likely to be excerpted/shared — read as a clean result. Surface a one-line scale-limited/TENSION flag in the Abstract and a caption note (caption text only; never modify the source figure image).

## F2 / F4 decision — FIX BOTH in V2 as well
Both are low-cost honesty/representation hardening that align with the owner's publishable bar, so V2 fixes all four:
- **F2:** qualify or remove the unsubstantiated "reproducible" in the Abstract (the forced-demo, `spec.force=true`, sibling-never-compiled lineage does not substantiate reproducibility). Descriptive language only.
- **F4:** add a visible "AI-assembled draft — not submitted, not peer-reviewed" tag near the Title/Abstract, so the AASTeX typesetting cannot read as a formatted/submitted note.

## Dynamic current-Lab replacement — HIGH-RISK, NOT authorized by this gate
Goru's mapping shows the public serving is **dynamic**: the backend (`backend/app/routers/lab_runner.py`) serves `lab-runs/<id>/artifact/<name>` and couples discovery to each run's `<id>.json`. A C2 promotion would therefore **replace `lab-runs/gated-e2e-demo/draft.pdf` (`0d863bff…`, 76,488 B) and `draft.tex` (`f1aeadd8…`) and edit `gated-e2e-demo.json`** — i.e. **mutate a current, immutable baseline INPUT run**, not copy into a benign static public dir.
- This is a **separate high-risk source / current-Lab / public mutation**. It is **NOT authorized by this deepening gate** and must not be performed now.
- It requires the later **exact candidate-specific publish packet**: pre-write backup of `draft.pdf`+`draft.tex`+`<id>.json`, exact before/after files + hashes, a rollback command, guaranteed survival of the visible `AI-draft / forced-demo / TENSION / unresolved-calibration` labels into the served form, a SHA + HTTP smoke-test plan, and the exact `APPROVE PUBLISH <packet_id>` phrase.
- **Open design question flagged to the publish packet:** overwriting `gated-e2e-demo` breaks the immutability of a baseline input run (it is in `baseline/INPUT_SHA256.txt`). The publish packet should weigh promoting to a **new run id / distinct served target** instead of overwriting an immutable input. Hwao's provisional recommendation: **do not overwrite the baseline input**; prefer a new served target. To be resolved in the publish packet, not here.

## This gate's action
Dispatch a Lana V2 repair (direct Claude) that PRESERVES V1 and builds a NEW `c2-mzr-gated-e2e-candidate-v2/` applying the F1–F4 fixes, retaining all source numbers/refs, the citation split, and the O/H/TENSION/provenance caveats. V1 remains frozen and preserved; V2 does not replace it.

## Public status
`AWAITING_EXPLICIT_PUBLISH_APPROVAL` — unchanged. No candidate has crossed a public-write gate; nothing was promoted, replaced, or served this gate.

`OVERNIGHT_PAPER_BOARD_HWAO_C2_REDTEAM_ADJUDICATION_V1`
