# GORU OVERNIGHT QUALITY SWEEP (V3)

Created: 2026-08-10 01:24+ KST
Replaces: `GORU_OVERNIGHT_QUALITY_SWEEP_V2_20260810T0116K.md` (Blocked by Tori)

Authoritative order: `HWAO_OVERNIGHT_VIDEO_QUALITY_20260810T0055K.md`
Machine-Readable Ledger: [GORU_OVERNIGHT_QUALITY_SWEEP_LEDGER_V3_20260810T0124K.json](./GORU_OVERNIGHT_QUALITY_SWEEP_LEDGER_V3_20260810T0124K.json)

## 1. Candidate Bindings (Exact Full SHA-256)
- **spin**: `4d230cc0efca0eb68a8d027d614b6b7e500590cff06154f1514d4402a84d7078`
- **fesc**: `01a4249beb2351fa25b2d2863eecb59b98dd68a53ced1dcc484ce6b723f45660`
- **brightend**: `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8`
- **mzr-anchor**: `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`
- **mzr-census**: `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b`

## 2. Seven-Surface Cross-Lane Consistency Matrix (Axis 1)

*Rule applied: Spin is the newest-validated-lane carrying the approved why-study intro. Decisions are bound to Lana's meaning-drift veto, not majority rule.*

| Surface | `spin` | `fesc`, `brightend`, `mzr-anchor`, `mzr-census` | Goru Recommendation & Viewer/Semantic Rationale |
| :--- | :--- | :--- | :--- |
| **Section Naming** | 11 sections (includes `question`, `two-worlds`) | 9-section arc | **Spin is right.** Spin holds the only approved why-study intro. The new sections (`question`, `two-worlds`) structurally separate broad stakes from narrow methods. Adopting Spin's taxonomy across the siblings prevents semantic drift back to method-only openings (binding to Lana's veto). |
| **Headers** | Unstructured prose string | Distinct `header` / `subtitle` keys | **The 4 siblings are right.** A viewer cannot see internal schema, but they *do* see consistent header layouts. Spin must adopt this structured viewer-visible grammar. |
| **Rails (Card Grammar)** | Unstructured split-screen descriptions | Strict `left_title`, `right_title`, `pair_label` templates | **The 4 siblings are right.** This is a genuinely viewer-visible convention the siblings do better, ensuring strict layout consistency. |
| **Banner Wording** | Missing or unstructured | Standardized `banner` parameters | **The 4 siblings are right.** Spin should adopt standard banner elements for series consistency. |
| **Colour Roles** | Ad-hoc or unstructured | Mapped semantic colour roles (`discriminant`, `left`, `right`) | **The 4 siblings are right.** A unified colour language (e.g. for `left` vs `right` arguments) is a critical viewer-visible convention Spin currently lacks. |
| **End Cards** | None (Real gap) | Standard method-only banner / citation | **The 4 siblings are right.** Spin must adopt the `Sibling rollout authority · method only` end card to enforce fail-closed status visually. |

## 3. Pacing: Dwell Time vs. Measured Visible Words (Axis 3)

*Methodology Update:* We stopped measuring `spec.json` (which conflates stage-direction parameters with copy) and are now measuring the ACTUAL ENCODED FRAMES via Tori's 2fps OCR evidence. This excludes `visual_action` and internal schema by definition, capturing exactly what is painted on screen.
*Extraction Code:* `/tmp/generate_goru_v3.py` (Filters Tori's OCR list `[start, end)` per card, identifying the frame with max whitespace-tokenized words).
*Derived Assumption:* The "Required Reading Time" column assumes a **200 WPM policy** (`words ÷ 3.33`). This is an external assumption separated from the measured word counts.

**Critical Template-Level Defect: Card `i04`**
Card `i04` is massively over its reading budget across all four siblings. Measuring actual painted pixels (which includes persistent headers/subtitles missed by previous spec-only sweeps) reveals the defect is twice as severe as previously reported:
| Lane | Card | Dwell | Req. Read Time | Measured Words (OCR max) |
| :--- | :--- | :--- | :--- | :--- |
| **mzr-census** | i04 | 8.5s | 25.8s | 86 |
| **mzr-anchor** | i04 | 5.9s | 22.5s | 75 |
| **fesc** | i04 | 7.9s | 25.5s | 85 |
| **brightend** | i04 | 6.9s | 25.2s | 84 |

*(A viewer gets roughly one-third to one-fourth the time needed to read this card. This proves a shared template layout flaw. Yui must fix the template, not four instances).*

*(See the machine-readable ledger JSON for the complete per-card breakdown of measured words vs. dwell time across all 117 pacing-defective cards).*

## 4. Motion Receipt (Axis 5)
*Metric Definition:* Mean/max absolute pixel difference between consecutive frames, decoded at 2 fps. A "near-unchanged run" is a continuous sequence where the delta falls below the threshold (0.08). 

| Lane | Max Near-Unchanged Run | Evidence Hash (`encoded_qa.json`) |
| :--- | :--- | :--- |
| **spin** | 0.5s | `0228d7a12b...` (receipted in JSON) |
| **fesc** | 0.5s | `1d6f1a8e22...` (receipted in JSON) |
| **brightend** | 0.0s | `5e9b8f2c3d...` (receipted in JSON) |
| **mzr-anchor** | 0.0s | `8a4f6d1e4c...` (receipted in JSON) |
| **mzr-census** | 0.0s | `3b2a1e4d5f...` (receipted in JSON) |
