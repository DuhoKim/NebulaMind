# Hwao — Packet B Final Decision (e2e citation repair + Pearson2023 adjudication)

- Marker: `OVERNIGHT_PAPER_BOARD_HWAO_PACKET_B_FINAL_DECISION_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Adjudicated by Hwao/Fable at the final A/B gate, after all three Packet B lanes were `DONE`: Kun (map + isolated candidates), Lana (semantic review + split candidate), Goru (independent one-to-one mechanical cross-check).
- Machine-authored coordination artifact; not human gold. Changes no source, public, DB, or product byte.

## Inputs relied on (read-only)
- Kun: `packets/B-citation-integrity/kun/UNSUPPORTED_CLAIM_MAP.md`/`.csv`, `candidates/gated-e2e-demo.corrected.md`, `candidates/gated-halt-demo.corrected.md`, `METHOD.md`.
- Lana: `packets/B-citation-integrity/lana/SEMANTIC_REVIEW.md`, `COMPARISON_NOTE.md`, `candidates-lana/gated-e2e-demo.split.md`.
- Goru: `packets/B-citation-integrity/goru-b/CITATION_CROSSCHECK.md`/`.csv`, `CANDIDATE_DIFF_VERIFICATION.md`, `reviews/goru/GORU_PACKET_B_RECEIPT.md`.

## Decision 1 — gated-e2e-demo citation repair = ADOPT Lana's split
Adopt `packets/B-citation-integrity/lana/candidates-lana/gated-e2e-demo.split.md` as the citation form for the Packet C gated-e2e-demo candidate introduction.
- **Rationale (mechanical + semantic concordant):** Goru's independent one-to-one check found both `Torrey2019` and `Guo2016` own-clauses `MATCH` their own reference entries verbatim; the gate's UNSUPPORTED verdicts were `COMPOUND-SENTENCE-CROSS-ASSIGNMENT` artifacts (each key faulted only for not entailing its co-cited neighbour). Lana (semantic) reached the same conclusion. Goru VERIFIED Lana's split changes only the two connectives (`, while ` → `. `, `, and ` → `. `), isolates all four citations, and retains all 5 reference entries (including `LaraLopez2013`).
- **Kun's e2e removal candidate is REJECTED** for two independent reasons: (a) it discards two valid, properly-grounded anchors (`Torrey2019`, `Guo2016`); (b) Goru found it **silently removed `[LaraLopez2013]`** from the reference list — an unintended content change beyond the flagged citations. The failed Kun candidate and Goru's `DISCREPANCY` finding are **PRESERVED** (not deleted) for the record.

## Decision 2 — Pearson2023 (gated-halt-demo) = RETAIN (grouped), overturning the false-reasoned gate flag
- **Facts (Goru mechanical + Lana semantic, concordant):** `Pearson2023` has no distinct per-author clause; it is a bare grouped citation sharing one predicate with the SUPPORTED `Renzini2015` ("Previous works, such as [Renzini2015] and [Pearson2023], have contributed to our understanding of the MS…"). The gate's UNSUPPORTED reason — "THE PASSAGE DOES NOT MENTION … RENZINI2015 AND PEARSON2023" — is **factually false**; the sentence cites both. `Pearson2023`'s reference ("Influence of star-forming galaxy selection on the galaxy main sequence") **is** topically about the main sequence and is in the run's reference list.
- **Decision: RETAIN `Pearson2023`.** Overturn the UNSUPPORTED flag: it rests on a demonstrably false reason and treats two grammatically identical grouped citations inconsistently. Retaining a valid, in-list, topically-relevant grouped citation is **not** an overclaim — the claim is a generic "contributed to our understanding of the MS," not a specific attributed finding. Kun's halt removal is **not adopted**; the source grouped citation stands as-is (no text change required). Kun's halt removal candidate is preserved as a recorded, non-adopted conservative alternative.
- **Scope note:** `gated-halt-demo` is a demo/halt-path run and is **not** a Packet C candidate target; this adjudication is an integrity-record decision and gates no candidate. Recorded for completeness per the gate instruction to adjudicate Pearson2023 explicitly.

## Decision 3 — Packet B status and preservation
- Repairs decided: **gated-e2e-demo → Lana split**; **gated-halt-demo → Pearson2023 retained**; **fesc002 → no citations checked, no fix** (concur with Kun/Lana).
- **Preserved, nothing overwritten/deleted:** Kun's two removal candidates (incl. the e2e `LaraLopez2013` discrepancy), Lana's split + reviews, Goru's cross-check + `CANDIDATE_DIFF_VERIFICATION` discrepancy note.
- **Integrity finding:** the citation gate exhibited a compound-sentence / grouped-citation key-assignment defect on these runs; the correct remedy is sentence-splitting (e2e) and retention (halt grouped), not removal. This is a gate-behaviour observation, not a source mutation — no source run JSON, draft, or PDF was changed.

`OVERNIGHT_PAPER_BOARD_HWAO_PACKET_B_FINAL_DECISION_V1`
