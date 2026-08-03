# Hwao — A/B/C/D First-Pass Roll-Up (honest states)

- Marker: `OVERNIGHT_PAPER_BOARD_HWAO_ABCD_FIRSTPASS_ROLLUP_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Compiled by Hwao/Fable at Deepening Gate 1 from the three C/D receipts, `TORI_CD_FIRSTPASS_VALIDATION_V1`, and the final A/B decisions. Machine-authored; not human gold. No source/public/DB/product byte changed.
- Independently corroborated by Tori CD validation (source 38/38 PASS; all safety counts 0).

## Honest packet states
| packet | target | state | one-line basis |
|---|---|---|---|
| **A** | MZR lineage | **DECIDED (canonical decision)** | canonical = `gated-e2e-demo`; `d8de519cb9c9` = queued-never-compiled precursor; Packet C source = `gated-e2e-demo` (`HWAO_PACKET_A_CANONICAL_DECISION_V1`) |
| **B** | citation integrity | **DECIDED (final citation decision)** | `gated-e2e-demo` = Lana split; Pearson2023 retained; Kun removal rejected+preserved (`HWAO_PACKET_B_FINAL_DECISION_V1`) |
| **C1** | `2ab3c92eea8a` SFMS | **DONE — outline, NOT a paper** | structural outline only; every quantitative slot = `TO BE COMPUTED — NOT IN SOURCE`; no synthetic results; source has no draft |
| **C2** | `gated-e2e-demo` MZR | **DONE — isolated, compiled, forced-demo / TENSION candidate** | `candidate.tex`+`candidate.pdf` (tectonic rc=0); 3-hunk diff vs source; O/H-scale + TENSION + forced-build caveats rendered; 5 refs retained; figure byte-identical |
| **D1** | `7cb504ea7ad3` SMF | **BLOCKED** | prose verdict "requires substantial improvement"; obs-comparison / error-analysis / bias-analysis ABSENT and uncloseable tonight without new data/runner; no prose patch written |
| **D2** | `fesc002` reionization | **PARTIAL** | compiled + MINOR + lit-grounded, but `Chisholm+22`/`Flury+22`/`Simmonds+24` cited-but-unlisted and `citation_entailment.checked=0` = zero positive coverage; no draft patch written |

## C2 candidate freeze (current bytes; do not overwrite)
| file | SHA-256 |
|---|---|
| `packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate/candidate.tex` | `c615b2f39502bf4e15f54e8fba3818ca480c9fd162360044c804893a11bc00d9` |
| `…/candidate.pdf` | `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e` |
| `…/result.png` (byte-identical to source `gated-e2e-demo/result.png`) | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` |
| `…/COMPILE_NOTE.md` | `c4bd54bcd9363d2249925ccfb6c3da0fbf7b4c19bfba46928f96951d41a91c02` |
Candidate PDF: 82,670 bytes, 2 letter pages, PDF 1.5 (Tori-verified). Source→candidate diff = exactly 3 hunks (header comments; Introduction connective split; append-only caveats).

## Recorded in-lane correction (traceability)
Lana's O/H-scale caveat was tightened in-lane (Tori crew catch) so it does not assert the TNG-SDSS difference is definitively systematic OR physical — final wording: "Any apparent TNG-SDSS difference remains confounded by unresolved scale systematics and cannot be interpreted as physical until a common calibration is established." This was a **machine/crew verification catch, not a human paper-history direction**, and was correctly recorded in-lane only — NOT written to any Lab/DB/paper-history store.

## Publishability (honest)
No artifact is a publishable "real paper." C1 is an outline, D1 is BLOCKED, D2 is PARTIAL. **C2 is the only compiled candidate — and only as a clearly-labelled autonomous Lab research-note draft** (forced-demo lineage, `TENSION`, O/H-scale-confounded). It must never be represented as a validated measurement or an accepted paper. Any promotion is of that labelled note, via the explicit publish gate only.

## Next (this gate = deepening, NOT publication)
- C2 scientific/representation red-team (Lana, read-only) + C2 mechanical contract audit (Kun, read-only) — independent cross-model second opinions before any promotion is even considered.
- Publication-target mapping (Goru, read-only): identify the current served public target, route/manifest/index coupling, current bytes+hashes, and backup/rollback requirements — mapping only, no public write.

## Safety / public status
All safety counts remain 0 (source/current-Lab/PDF/public/DB/wiki/git/cron/browser/account/deploy/PAYG). **Public status: `AWAITING_EXPLICIT_PUBLISH_APPROVAL`** — no candidate has crossed a public-write gate; promotion requires a separate candidate-specific packet + exact `APPROVE PUBLISH <packet_id>` phrase.

`OVERNIGHT_PAPER_BOARD_HWAO_ABCD_FIRSTPASS_ROLLUP_V1`
