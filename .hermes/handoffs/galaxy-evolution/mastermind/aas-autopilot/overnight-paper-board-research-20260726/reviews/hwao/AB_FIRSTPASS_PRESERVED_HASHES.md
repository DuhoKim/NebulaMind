# Hwao Preservation Record — A/B First-Pass Freeze

- Marker: `OVERNIGHT_PAPER_BOARD_HWAO_AB_FIRSTPASS_PRESERVED_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Cross-reference: Tori validation `OVERNIGHT_PAPER_BOARD_TORI_AB_FIRSTPASS_VALIDATION_V1` (`reviews/tori/TORI_AB_FIRSTPASS_VALIDATION.md`).
- Authored by Hwao/Fable at the A/B repair gate (machine-authored coordination artifact; not human gold).

## Purpose
Freeze the v1 first-pass Packet A and Packet B deliverables and receipts. All v2 repair / review work MUST be **versioned** (new filenames, e.g. `*.v2.md`, `*_V2.md`, or a lane subfolder). These v1 files must NOT be overwritten, edited, or deleted. Hwao independently recomputed each SHA-256 below; every value matches Tori's record.

## Preserved v1 files (immutable baseline for the repair)
| File (relative to output root) | SHA-256 (v1, PRESERVED) |
|---|---|
| `packets/A-mzr-reconciliation/goru/MZR_FIELD_MATRIX.csv` | `411d1f3be6a0ed9e9e6a380ffd7062c9852f8f34d8e008b22e2136f4d9ae4a0e` |
| `packets/A-mzr-reconciliation/goru/MZR_FIELD_MATRIX.md` | `65048a8d497080b975c763959a36f4400d77475b709909f1004a51abcc8457ac` |
| `packets/A-mzr-reconciliation/goru/PROVENANCE_NOTES.md` | `9fe16d6dd56e66b71a0d235c75bcafd7b21159e018ed1d7ec3c76dfce3bb31c3` |
| `reviews/goru/GORU_PACKET_A_RECEIPT.md` | `b7ac33bef22443a4e0fcd464b0e7ce8e4bf0869df790719e6721a1b24aff5f7c` |
| `packets/B-citation-integrity/kun/UNSUPPORTED_CLAIM_MAP.md` | `54cf78b57b61d0a4ddb755f8a1d6f96ed53e25873a08268a775102af6f720498` |
| `packets/B-citation-integrity/kun/UNSUPPORTED_CLAIM_MAP.csv` | `b1cec58ae9f30b1845988f40c563c50d36f9cb19475f1c53b67e0da55c436f2b` |
| `packets/B-citation-integrity/kun/METHOD.md` | `fc278658bedb6e488a16dff303373310d13e7a0c879ee795892db53e2383b2e2` |
| `reviews/kun/KUN_PACKET_B_RECEIPT.md` | `cac3a11b080ea99dd236da50cb053cfb7176300b0138f9d03fd86abde0a56206` |

Kun's two isolated Packet B candidate files are likewise preserved (do not overwrite):
| File | SHA-256 |
|---|---|
| `packets/B-citation-integrity/kun/candidates/gated-e2e-demo.corrected.md` | `d0bfe94ceb733710fe72393c4683ec439485ca294b845606653e56def32cb56d` |
| `packets/B-citation-integrity/kun/candidates/gated-halt-demo.corrected.md` | `7c46256b5457058367934f6fb40db0ef58eb2e579d5ec60b0475b21a71cceb28` |

## Scope incident (recorded and resolved; safety counts remain 0)
During Packet A v1, the Goru lane created an out-of-scope task helper `/tmp/inspect.py` (716 bytes, SHA-256 `25128dcfdef2855f02d8b7a5bfeffe6cf029e49aa4554004e96c84ad7382417c`), outside the approved output root and against the lane-scoped-temp rule. Tori **rejected its execution**, verified its exact contents and hash, and **removed** the file to restore the scope boundary. No source, public, DB, or product byte changed as a result. Goru's v2 receipt MUST disclose this incident and confirm the corrective (all intermediates under `packets/A-mzr-reconciliation/goru/_tmp_*` only).

## Versioning rule for v2 work
- v2 deliverables use explicit v2 names (`MZR_FIELD_MATRIX.v2.md`, etc.) or a `/v2/` subfolder; v2 receipts are `*_RECEIPT_V2.md` / new receipt filenames.
- The v1 hashes above are the immutable comparison baseline. Any change to a v1 file is a scope violation and closes the lane.

`OVERNIGHT_PAPER_BOARD_HWAO_AB_FIRSTPASS_PRESERVED_V1`
