# Tori Gate B source-acquisition receipt

Status: GREEN for persisted source custody; one non-evidentiary network-policy variance is separately disclosed in `TORI_NETWORK_VARIANCE_NOTE.md`.

## Route coverage

- Immutable manual queue routed: 73/73.
- Captured source indices: 37/37, with a unique index→URL map.
- `M018` is the only entry with no citation bound in its captured logical unit; it remains explicitly unresolved rather than borrowing a source.
- Section-2 uncertainty/comparability entries route to the row's authoritative Citation cell under contract r3.
- Document-level `M064`/`M065` route to all 37 source indices.

## Retrieval and evidence store

- Network method records: 119, all labeled `GET`; 99 actual GET attempts and 20 fail-closed host-stop records.
- Results: 91 HTTP 200, 7 HTTP 403, 1 HTTP 404, 20 host-stop records.
- Fetch budget: 99/200 actual attempts.
- OUP failures were resolved through 14 read-only ADS bibliographic queries and 14 arXiv full-text routes.
- Supplemental metadata resolution added 10 full-text routes.
- Direct T1/T2 primary full text is available for 34/37 source indices.
- The three without T1/T2 (`2`, `8`, `13`) are official project/data pages and occur only in document-level source-quality/fidelity entries `M064` and `M065`; they are not silently promoted to primary evidence.
- Source index `32` returned 403 and is bibliographically mapped to source index `33` as the same Chaikin et al. 2026 COLIBRE work. Byte identity is explicitly not claimed.

## Custody checks

- Every persisted raw artifact matches the byte count and SHA-256 in `sources/FETCH_LOG.jsonl`.
- No raw hash mismatches.
- No persisted `POST`, login, form, browser-automation, or write endpoint.
- ADS authentication is recorded only as a boolean; token values are not logged.
- Secret-pattern scan: zero hits.
- No scientific verdict was assigned by Tori.

## Deliverables

- `sources/SOURCE_INDEX_MAP.json`
- `sources/ROUTE_MAP.json`
- `sources/FETCH_LOG.jsonl`
- `sources/EVIDENCE_CATALOG.json`
- `sources/raw/`, `sources/text/`, `sources/metadata/`
- acquisition and resolution summaries

B-P2 may use only the persisted catalog/store. Unresolved or lower-tier evidence must remain fail-closed.

TORI_GATE_B_SOURCE_ACQUISITION_DONE_20260713T034742Z

## Pre-B-P4 custody correction

An independent post-verdict path audit found that `resolve_supplemental_arxiv.py` had attached arXiv `2006.04822` (the muon anomalous-moment review) as an extra candidate for source indices 1, 3, and 4 after an OUP 403/Cloudflare title produced a spurious ADS discovery result. Each affected index already had the correct, independently resolved OUP/ADS primary full text, and Goru's matched spans plus Lana's quotations used those correct first candidates.

The wrong file and metadata are retained only for audit and quarantined in `sources/SUPPLEMENTAL_CONTAMINATION_CORRECTION.json`. `sources/EVIDENCE_CATALOG.json` is now V2 and excludes the three invalid candidates. Mechanical candidate lists and the 13 verdict evidence-path lists that mentioned the extra file must be regenerated/cleaned before B-P4. No verdict meaning changed.

TORI_GATE_B_SOURCE_CUSTODY_CORRECTION_RECORDED_20260713T034742Z
