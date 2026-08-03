# P0 Artifact Identity — Lana primary lane

Audit date: 2026-07-27, run started 22:06 KST (13:06 UTC). Lane: `packets/P0-tng-validation/lana/`.

## Reviewed artifact (pinned, primary)

| Field | Value |
|---|---|
| Public URL | `https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf` |
| HTTP status at baseline | 200 (observed 2026-07-27T13:02:48Z = 22:02:48 KST, per `input/PUBLIC_ARTIFACT_IDENTITY.json`) |
| Bytes | 132,831 |
| SHA-256 | `086654e747f13626d853d404557292bd0238f5536ee2173669f2674d37ad62ef` |
| ETag | `W/"206df-19f8ebca74d"` |
| Last-Modified | Thu, 23 Jul 2026 11:29:16 GMT (= 20:29:16 KST) |
| Pages | 4 (pdfinfo) |
| PDF CreationDate | Thu Jul 23 20:28:34 2026 KST (LaTeX/AASTeX631, xdvipdfmx) |
| Local pinned copy | `input/served-p0.pdf` |

**Access attestation:** I (Lana) directly accessed the pinned local copy `input/served-p0.pdf`, recomputed its SHA-256 (`0866…62ef`, exact match to both the input manifest and the public-fetch receipt), ran `pdfinfo` and `pdftotext -layout` on it, and rendered all 4 pages to PNG at 150 dpi (plus a 300 dpi crop of Figure 2) and visually inspected every page and both figures. The review below is a line-level review of this exact byte identity, not a prompt-conditioned summary. A live re-fetch of the PDF bytes was not possible from this lane (`curl` denied by lane permissions); the public identity relies on the baseline receipt captured 4 minutes before this run started. The review URL was independently re-checked live from this lane at ~22:15 KST and still returns HTTP 404.

## Secondary copy (NOT interchangeable)

| Field | Value |
|---|---|
| Path | `input/secondary-3page-source.pdf` |
| Source | `.hermes/handoffs/paper-videos-v2-20260723T034035Z/sources/tng-validation.pdf` |
| Bytes | 120,426 |
| SHA-256 | `f037d89d210130d464e3ddbc2390b020aa3ffeebabab272357102691190f75d6` |
| Pages | 3 |
| PDF CreationDate | Fri Jul 17 00:57:00 2026 KST |

Relationship established by full-text and visual diff: the 3-page copy is an **earlier revision (July 17)** of the same manuscript. The served 4-page copy (July 23) adds: the quantified over-evolution gap (+0.41/+0.49 dex), the selection-debiasing forward model and envelope (+0.46/+0.83, up to ~+1.1 dex, nine (σ, F_lim) configurations), the measured +0.13 dex aperture→total mass offset, expanded systematics, and the "descriptive, non-human-validated, lower bound" framing. Figures 1 and 2 are graphically unchanged between the two; only the Figure 2 caption was updated. Critically, the abstract's matched-Te-scale MZR claim (PP04 O3N2, ~0.24 dex, −0.40 vs −0.27, factor ~1.5) is present **verbatim-equivalent in both revisions**, and in neither revision is it supported by the methods, results, discussion, or figures (see `SECTION_CLAIM_LEDGER.md`). The two copies must not be treated as interchangeable: they differ in byte identity, page count, date, and SFMS claim content.

## Adjacent identities (context)

- History JSON: `input/served-history.json`, 1,394 bytes, SHA-256 `f879ca9b…f7314f`, served 200 at the same baseline. Human-direction record only ("n/a (human-directed)", 2 revisions); it is not a referee verdict.
- Review URL `…galaxy-evolution-tng-validation-draft_review_loop.md`: **HTTP 404** at baseline (2026-07-27T13:02Z) and re-confirmed 404 live from this lane at ~22:15 KST 2026-07-27. The board card (`FrontierDrafts.tsx`) still links it. Treated as an artifact-integrity defect (see `CITATION_AND_REVIEW_LINK_AUDIT.md`).
- Board card: `input/FrontierDrafts.tsx` (SHA-256 match), entry "Calibration is not validation…", `updated: 2026-07-23 20:29` — consistent with the served PDF's Last-Modified (20:29:16 KST) and CreationDate (20:28:34 KST). Card carries no `verdict` field (correct: this draft has no automated-referee verdict).

## Input custody

All 10 files listed in `input/INPUT_MANIFEST.json` were re-hashed with `shasum -a 256` (one file per invocation) at run start; **all 10 hashes match the manifest exactly**. Inputs were treated as immutable; no input file was modified.
