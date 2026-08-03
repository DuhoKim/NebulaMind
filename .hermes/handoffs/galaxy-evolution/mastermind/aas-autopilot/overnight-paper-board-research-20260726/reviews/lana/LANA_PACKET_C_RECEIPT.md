# Lana — Packet C Candidate Build — RECEIPT

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_C_LANA_BRIEF_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Implements: `HWAO_PACKET_A_CANONICAL_DECISION_V1` (source = `gated-e2e-demo` artifacts; `d8de519cb9c9` = queued-never-compiled precursor) and `HWAO_PACKET_B_FINAL_DECISION_V1` (adopt Lana's split).
- Lane: direct Claude Max subscription only — no API-key, no PAYG, no third-party route, no Nous purchased-balance.
- All science artifacts headed `AI_DRAFT_NOT_HUMAN_GOLD`. Isolated; **no publication**.

## Completion state: `DONE`
- **C1 (`2ab3c92eea8a` SFMS structural outline): DONE** — structural outline only; NO synthetic results (every quantitative slot = `TO BE COMPUTED — NOT IN SOURCE`).
- **C2 (`gated-e2e-demo` MZR candidate): DONE (with compiled PDF).**

## Source stability (independently re-verified vs `baseline/INPUT_SHA256.txt` — all OK, no drift)
| source file | SHA-256 |
|---|---|
| `gated-e2e-demo/draft.tex` | `f1aeadd8ea43f2fd1e22e9686d23066fdf95e3d5c95937a42d8ddd076bc95a8a` |
| `gated-e2e-demo.json` | `46ddd75d5f0e5814e814333336d8e6d1b011382c46509012af2aea8cc20af5e2` |
| `gated-e2e-demo/result.png` | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` |
| `2ab3c92eea8a.json` | `d2fec6114bb07b400224903f3c77b60889ad4aeab0660c3d1a00b3ccb9f810d6` |
| `2ab3c92eea8a/result.png` | `41b4b2b0f50cadef6aaeb35b1482ee733c73d53a2e2cd9752865664aff532d91` |
| `2ab3c92eea8a/history.json` | `862802dd37640c23ff23f429241932d06a8b34a35a80cc571e4e0d0c3baec642` |

## Deliverables produced (new isolated files under Lana Packet C write root; SHA-256)
| file | SHA-256 |
|---|---|
| `packets/C-candidate-build/lana/c1-sfms-2ab-outline/OUTLINE.md` | `232968c93944e5ba2dd8fb0a0c04969b057bed6d133e7a33d50da819b84a3b46` |
| `packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate/candidate.tex` | `c615b2f39502bf4e15f54e8fba3818ca480c9fd162360044c804893a11bc00d9` |
| `packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate/result.png` | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` |
| `packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate/candidate.pdf` | `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e` |
| `packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate/COMPILE_NOTE.md` | `c4bd54bcd9363d2249925ccfb6c3da0fbf7b4c19bfba46928f96951d41a91c02` |
| `packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate/compile.log` | `d08b2ca1ac7d67ee356dd61463f43e5e1b4d32d46270e55b5d363faf6af60fa6` |
| `packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate/candidate.log` | `bd9dfe8e3a98c380ae7a7a211040a8b436841719b8f3108fc114c57efdf9a8cc` |

The C2 `result.png` copy is byte-identical to source `gated-e2e-demo/result.png` (same SHA-256); the source figure was read and copied, never modified.

## C2 base-text fidelity (mechanically diffed vs source `gated-e2e-demo/draft.tex`)
A unified `diff` of source → candidate yields **exactly three hunks; no other differences**:
1. **Non-rendered header comments added** before `\documentclass` — five `%`-comment lines carrying `AI_DRAFT_NOT_HUMAN_GOLD` and provenance. These are LaTeX comments: they do not render in the PDF and add no document content.
2. **Introduction connective split** — the single Introduction line is replaced so the two compound citation sentences become four single-citation sentences (only `, while ` → `. ` and `, and ` → `. `); citation-content wording is unchanged. This is Lana's Hwao-adopted, Goru-verified split; all four citations (Qi2025, Torrey2019, Garcia2023, Guo2016) are isolated and retained.
3. **Append-only Caveats additions** — three mandatory caveats (O/H-scale, TENSION, provenance) appended AFTER the existing Caveats paragraph, which itself is unchanged (it appears as unmodified diff context).

Summary: the **scientific document body** differs from source only by the authorized Introduction split plus the append-only caveats/provenance, while **non-rendered AI/provenance header comments were also added**. The remaining body sections — Abstract, Data-and-method, Result, the figure line, and the original Caveats paragraph — are **textually preserved from source** (unmodified diff context). The **5 reference entries (Qi2025, Torrey2019, Garcia2023, Guo2016, LaraLopez2013) are textually preserved from source** — the References line is textually identical between source and candidate (verified). No new number, relation, or scientific claim was introduced. (Kun's rejected removal candidate had silently dropped `[LaraLopez2013]`; this candidate preserves it.)

## Caveats applied (C2) — all three mandatory, existing caveats not weakened
1. **O/H-scale caveat** — SDSS O/H calibration/scale absent in source; no common TNG-vs-SDSS O/H scale; scales may differ; **no dex offset invented or applied**; no specific external offset value stated; comparability unresolved. Closing sentence (per Tori in-lane verification correction): *"Any apparent TNG-SDSS difference remains confounded by unresolved scale systematics and cannot be interpreted as physical until a common calibration is established."* — does NOT assert the difference is definitively systematic or non-physical.
2. **TENSION caveat** — carries source `expected_value = TENSION` honestly (not upgraded); framed as a systematics/anchor-reconciliation note; a z~0 TNG-vs-SDSS MZR is an anchor relation, not a novel physical/frontier claim.
3. **Provenance caveat** — discloses forced (`spec.force=true`) `gated-e2e-demo` lineage; `d8de519cb9c9` independent draft queued but never compiled; candidate assembled from existing artifacts, not a fresh production run; isolated and unpublished.

## Compile outcome (C2)
- Engine `tectonic 0.16.9`, run with cwd = C2 root: `tectonic candidate.tex --keep-logs`.
- **Saved rc = 0** (captured immediately after tectonic, not from a pipe tail). **`candidate.pdf` produced** (82,670 bytes). aastex631 fetched successfully.
- Only cosmetic `Underfull \hbox` warnings on the long reference/bibcode lines (inherited from verbatim source strings); no errors. Details in `COMPILE_NOTE.md`, `compile.log`, `candidate.log`. All compile writes stayed inside the C2 root; the Lab runner was not invoked.

## In-lane verification correction (Tori) — recorded for traceability
- **Tori verification correction:** the O/H caveat must not assert an apparent TNG-SDSS difference is definitively systematic or non-physical → the O/H caveat's closing sentence was replaced with the bounded wording shown above. This was an in-lane crew verification catch (Tori), not a human paper-history direction; it is recorded here only, and not written to any Lab/DB/paper-history store (forbidden this lane).

## STOP conditions
None triggered. No number/relation/claim was invented (C1 quantitative slots are all `TO BE COMPUTED — NOT IN SOURCE`); no source drift vs `INPUT_SHA256.txt`; the Lab runner was not run and no data was re-pulled; the compile wrote only inside the C2 root; no payment/overage/top-up/Nous/PAYG prompt; no public or source mutation.

## Constraint attestation
No source file or existing PDF edited or replaced; no write outside the Lana Packet C write root; no memory/config write; no public/static-root, DB/SQL/API/wiki/page-version write; no deploy/restart; no git/cron/browser/account/billing/cloud action; no Nous purchased-balance or third-party PAYG routing; no publication. Prior packet files preserved (untouched).

OVERNIGHT_PAPER_BOARD_PACKET_C_LANA_CANDIDATE_COMPLETE_V1
