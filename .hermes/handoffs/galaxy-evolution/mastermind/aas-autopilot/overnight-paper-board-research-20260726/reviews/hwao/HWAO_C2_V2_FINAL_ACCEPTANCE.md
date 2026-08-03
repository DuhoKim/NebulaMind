# Hwao — C2 V2 Final Acceptance (candidate mechanics) + Publication BLOCKED

- Marker: `OVERNIGHT_PAPER_BOARD_HWAO_C2_V2_FINAL_ACCEPTANCE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Adjudicated by Hwao/Fable at Deepening Gate 4 from the independent V2 audit, the new-run mapping, and Tori's route validation. Machine-authored; not human gold. No source/public/DB/product byte changed.

## Inputs relied on (read-only)
- Kun V2 audit (Codex gpt-5.5/ChatGPT Pro): `KUN_C2_V2_AUDIT_RECEIPT.md` + `C2_V2_CONTRACT_AUDIT.md` — **PASS on all nine items, no discrepancies**.
- Goru new-run mapping (Antigravity/Gemini): `GORU_C2_V2_NEW_RUN_MAPPING_RECEIPT.md` + `NEW_RUN_TARGET_MAP.md` — self-reported `DONE`, but **route-invalid** (see below).
- Tori route validation: `TORI_C2_V2_ROUTE_VALIDATION_V1` — `V2_AUDIT_PASS__GORU_NEW_RUN_MAP_FAIL_INVALID_ROUTE_ID`.
- `backend/app/routers/lab_runner.py` (route validators + list visibility).

## Decision 1 — V2 candidate mechanics: FINAL-ACCEPTED
Accept the V2 candidate's **build and mechanics**, based on Kun's independent nine-item PASS (concurring with Lana's build receipt and Hwao's provisional acceptance):
1. Hashes source/V1/V2 · 2. V1→V2 diff limited to F1–F4 + non-rendered header · 3. Rendered PDF strings (F1–F4 present; old overclaim "provides insights…" and "reproducible" absent) · 4. Reference integrity (5 refs incl. LaraLopez2013) · 5. Citation split (four single-citation sentences) · 6. Caveats (O/H-scale bounded, TENSION carried, provenance; original paragraph intact, none weakened) · 7. Figure byte-identity (`ed83a825…`) · 8. Compile evidence (rc=0, 84,831 B) · 9. V2 receipt concordance.
- V2 frozen: `candidate.tex bb77d38d…`, `candidate.pdf ac59ac60…`, `result.png ed83a825…`. V1 (`c615b2f3`/`eed8992d`) and source (`f1aeadd8`/`46ddd75d`) remain frozen.
- This is final acceptance of the **candidate**, not a publication authorization.

## Decision 2 — Publication remains BLOCKED (invalid route id in the first mapping)
Goru's first new-run mapping used the id `gated-e2e-demo-c2-v2`, which is **not routable**: `backend/app/routers/lab_runner.py` rejects any request where `not rid.isalnum()` (`get_run` l.183, `get_artifact` l.196). The hyphens make `rid.isalnum()` False, so `/api/lab/runs/gated-e2e-demo-c2-v2/artifact/draft.pdf` would return `400`. The mapping's self-reported `DONE` **must not be used as publish evidence**.
- The failed first map (`publication/goru-v2-new-run-map/NEW_RUN_TARGET_MAP.md`) and its receipt are **preserved unchanged** as a recorded failed mapping.
- **Corrected legal id: `c2v2e2e0726a`** — independently rechecked: `isalnum()` True, length 12 (≤ 32), and `lab-runs/c2v2e2e0726a.json` + `lab-runs/c2v2e2e0726a/` are ABSENT (create-only). Conforms to the `create_run` 12-char alphanumeric convention (l.134).
- A repair mapping (dispatched this gate) must re-derive the create-path against this legal id, grounded in the source-code route validators and `list_runs` visibility (top-level `status:"done"` + non-empty `result.summary`, l.157–161).

## Net status
- **V2 candidate: FINAL-ACCEPTED (mechanics).**
- **Publication: BLOCKED** — requires (a) the corrected route-valid new-run mapping (`c2v2e2e0726a`), then (b) the exact candidate-specific publish packet + `APPROVE PUBLISH <packet_id>` phrase. Per the standing adjudication, promotion is create-only to a new run id; the baseline `gated-e2e-demo` input is never overwritten.

## Public status
`AWAITING_EXPLICIT_PUBLISH_APPROVAL` — unchanged. Nothing promoted, replaced, or served this gate.

`OVERNIGHT_PAPER_BOARD_HWAO_C2_V2_FINAL_ACCEPTANCE_V1`
