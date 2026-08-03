# P0 Mechanical Claims and Numeric Invariants - Cross-Review

## 1. JSON Parsing & Key Counting
- **NUMERIC_INVARIANTS.json:** Parsed 11 invariant definitions. Keys `name`, `value_dex` or `values_dex`, `locations`, `status` present.
- **REPRESENTATION_MATRIX.json:** Parsed 10 claims (C1 to C14). Keys `id`, `claim`, `abstract`, `results`, `figures`, `state` present.
- **RECEIPT.json & other outputs:** Parsed successfully.

## 2. Arithmetic Recomputation
All arithmetic relations stated by Lana recomputed correctly:
- **TNG internal SFMS growth:** `0.99 + 0.30 = 1.29` (rounded 1.30); `1.15 + 0.30 = 1.45`; `1.30 + 0.30 = 1.60` (rounded 1.61). Valid.
- **Over-evolution gap:** `1.30 - 0.89 = 0.41`; `1.45 - 0.96 = 0.49`. Valid.
- **Aperture mass offset cancellation:** `0.61 x 0.13 = 0.0793` (~0.08 dex). Valid.
- **MZR internal evolution body:** `0.50 / 0.25 = 2.0`. Valid.
- **Naive factor 3-4:** `-0.25 + 0.12 = -0.13`; `0.50 / 0.13 = 3.84` (in 3-4 range). Valid.
- **Matched scale claim contradiction:** `0.40 / 0.27 = 1.48` (~1.5). Deficit `-0.50` moving by `-0.24` offset yields `-0.26`, not `-0.40`. Valid arithmetic contradiction identified by Lana.

## 3. PDF Mapping & Hashes
- **SFMS and MZR values mapped to PDF pages/sections:** Verified in `SECTION_CLAIM_LEDGER.md` (Abstract, §2, §3, §4, §5, Fig 1, Fig 2).
- **Hashes and page counts:** 4-page PDF `0866...62ef` (132,831 bytes) and 3-page July 17 PDF `f037...75d6` (120,426 bytes) visually/hash-verified.
- **Review-link 404 receipt:** Verified Lana's `CITATION_AND_REVIEW_LINK_AUDIT.md` recorded HTTP 404 for the configured review URL.

## 4. Invariant Handling & Bibliography
- **TNG=23,722 and SDSS=120,000:** Lana correctly flagged the TNG "~3e4" vs 23,722 plan-corrected invariant. SDSS PP04 recompute states 2.0e5 vs 120,000 invariant. Handled correctly as QUESTIONABLE/BLOCKED.
- **Bibliography identities/omissions:** Verified Lana's finding that Lisiecki 2025 A&A resolves to a 2026 quiescent paper (wrong identity). Verified missing PP04 and Kennicutt references. 
- **Invented counts, unsupported source IDs, overclaims:** Flagged abstract MZR matched-scale claim as a severe overclaim/contradiction (Z4 in ledger). Flagged underived -0.27 value. No inferred verdict from history JSON.

## 5. State Modification
Primary inputs and public state remained unmodified. Isolation maintained.
