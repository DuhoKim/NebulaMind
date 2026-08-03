# Hwao — Packet A Canonical Decision (MZR lineage + Packet C source/conditions)

- Marker: `OVERNIGHT_PAPER_BOARD_HWAO_PACKET_A_CANONICAL_DECISION_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Adjudicated by Hwao/Fable at A/B Gate 2, only after BOTH required Packet A receipts existed (per contract): Goru v2 matrix receipt + Kun independent reproducibility/duplication receipt.
- Machine-authored coordination artifact; not human gold. This decision changes no source, public, DB, or product byte.

## Inputs relied on (read-only)
- Goru v2 (Antigravity/Gemini): `MZR_FIELD_MATRIX.v2.md`, `PROVENANCE_NOTES.v2.md`, `reviews/goru/GORU_PACKET_A_RECEIPT_V2.md` — state `DONE`, source integrity 38/38 PASS, four v1 defects repaired (output hashes listed, `/tmp/inspect.py` scope incident disclosed, z=0 redshift correction with legend, wording narrowed).
- Kun (Codex gpt-5.5): `REPRODUCIBILITY_AUDIT.md`, `DUPLICATION_ANALYSIS.md`, `CANONICAL_RECOMMENDATION.md`, `reviews/kun/KUN_PACKET_A_RECEIPT.md` — state `DONE`, documentary traceability only (no runner, no data re-pull).
- Tori validation `OVERNIGHT_PAPER_BOARD_TORI_AB_FIRSTPASS_VALIDATION_V1`; baseline snapshot/manifest/hashes.
- The two lanes were independent model families (Gemini vs Codex) and their findings are **concordant**.

## Decision 1 — Canonical MZR lineage
The canonical representative of the TNG100+SDSS z=0 gas-phase mass–metallicity analysis is **`gated-e2e-demo`**. `d8de519cb9c9` is its **figure/summary-only precursor** (same core analysis lineage), not a separate result.
- Basis (concordant, mechanical): `d8de519cb9c9` and `gated-e2e-demo` carry an **identical** `result.summary` (TNG100 23,722 + SDSS 120,000, `mass-metallicity`, TNG "SF-weighted gas metallicity → O/H (solar-scaled)"). `gated-e2e-demo` adds the compiled draft (PDF/TEX), review loop, and the novelty/expected-value/citation gates; `d8de519cb9c9` has only `result.png`+`history.json` and its own note says the full AASTeX draft is **queued** (never built). Kun classifies the pair `superset-subset`; Goru's v2 matrix independently records the identical-summary + missing-draft facts.
- `2958462772b2` = SDSS-only 120,000-gal MZR (comparator/context; noncanonical for TNG+SDSS).
- `e2f3b038f8dd` = a **separate** SDSS 80,000-gal MZR-family output with explicit O/H anchors (`oh_at_logM9=8.572`, `oh_at_logM10p5=9.05`) and a method/topic label mismatch (`scaling-relation-evolution`/`main-sequence-quenching`). Comparator only — **do not** merge its 80k sample or its O/H values with the 120k runs or across O/H scales.

## Decision 2 — Packet C source
Build the Packet C TNG+SDSS MZR candidate **from `gated-e2e-demo`'s existing artifacts**, NOT by resurrecting `d8de519cb9c9`'s queued draft. The live runner is forbidden tonight, so `d8` cannot be freshly compiled; `gated-e2e-demo` already carries the compiled draft and gates for the same core numbers. Treat `d8de519cb9c9` as the preserved precursor/provenance sibling.

## Decision 3 — Packet C conditions (ALL mandatory; candidate stays PARTIAL until met; no publication without the separate gate)
1. **Citation fix = Lana's split/re-ground, provisional.** Adopt Lana's `candidates-lana/gated-e2e-demo.split.md` (preserve Torrey2019, Qi2025, Garcia2023, Guo2016 by splitting the two compound sentences into four single-citation sentences) — NOT Kun's removal, which discards two valid anchors. This is **provisional pending Goru's independent Packet B one-to-one mechanical cross-check** (dispatched this gate). If Goru's cross-check contradicts Lana, escalate to Hwao before any candidate text is locked.
2. **O/H-scale caveat MANDATORY.** SDSS O/H calibration/scale is `ABSENT` in all four runs; no common TNG-vs-SDSS O/H scale is established. O/H scales may differ across the sources, but **no dex offset may be invented or applied**, and TNG-vs-SDSS metallicity comparability is **unresolved**. The candidate must NOT apply an unstated offset and must NOT claim physical TNG-vs-SDSS metallicity comparability; any TNG−SDSS difference is presented as scale-limited/systematic, not physical.
3. **Carry `expected_value = TENSION` honestly** (concordant in the source). Do not upgrade to agreement. The defensible framing is a **systematics/anchor reconciliation note** (the interest is the O/H-scale systematic that bounds the comparison), not a novel physical MZR claim — a z~0 TNG-vs-SDSS MZR is an anchor relation, not a standalone frontier result.
4. **Provenance caveat MANDATORY.** Disclose that the canonical lineage is the forced (`spec.force=true`) `gated-e2e-demo` end-to-end build and that `d8de519cb9c9`'s independent draft was queued but never compiled; the candidate is assembled from existing artifacts, not a fresh production run.
5. **Isolation & gating.** Source runs remain immutable; candidate is an isolated new artifact marked `AI_DRAFT_NOT_HUMAN_GOLD`; no copy to any public/static root without a separate candidate-specific promotion packet and the exact `APPROVE PUBLISH <packet_id>` phrase.

## Decision 4 — Packet A reconciliation finding
The TNG-vs-SDSS z=0 MZR comparison is **bounded by an unresolved O/H-scale systematic** (concordant `TENSION`; SDSS calibration unstated). Honest status: a systematics-limited reconciliation, not a clean agreement. Packet C's canonical candidate is therefore **GATED/PARTIAL** — firm on lineage/source, open on (a) Goru's cross-check confirmation of the citation fix and (b) the mandatory caveats above.

## Note — v1 receipt preservation incident
The frozen v1 Goru receipt (`reviews/goru/GORU_PACKET_A_RECEIPT.md`, SHA-256 `b7ac33bef22443a4e0fcd464b0e7ce8e4bf0869df790719e6721a1b24aff5f7c`) is intact (re-confirmed this gate). Goru attempted twice to retro-edit that frozen v1 file; both attempts were captured to `GORU_PACKET_A_RECEIPT_LATE_OVERWRITE_CAPTURE.md` / `..._CORRECTION_QUEUE_CAPTURE.md` and the original restored. The proper corrections correctly live in the versioned v2 receipt. Versioning discipline reaffirmed: v1 artifacts are immutable; corrections go to `*_V2`.

`OVERNIGHT_PAPER_BOARD_HWAO_PACKET_A_CANONICAL_DECISION_V1`
