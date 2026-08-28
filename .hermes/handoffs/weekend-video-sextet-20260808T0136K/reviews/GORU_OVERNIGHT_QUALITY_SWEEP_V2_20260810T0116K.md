# GORU OVERNIGHT QUALITY SWEEP (V2)

Created: 2026-08-10 01:16+ KST
Replaces: `GORU_OVERNIGHT_QUALITY_SWEEP_20260810T0055K.md` (Blocked by Tori)

Authoritative order: `HWAO_OVERNIGHT_VIDEO_QUALITY_20260810T0055K.md`
Machine-Readable Ledger: [GORU_OVERNIGHT_QUALITY_SWEEP_LEDGER_V2_20260810T0116K.json](./GORU_OVERNIGHT_QUALITY_SWEEP_LEDGER_V2_20260810T0116K.json)

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
*Note on Receipting:* The values for `measured_dwell_seconds` and `measured_visible_word_count` are exact scalars backed by derivation receipts in the attached JSON ledger. 
*Derived Assumption:* The "Required Reading Time" column below assumes a **200 WPM policy** (`words ÷ 3.33`). This is an external assumption, separated here from the measured facts.

**Critical Template-Level Defect: Card `i04`**
Card `i04` is over its reading budget in ALL FOUR siblings, indicating a shared template layout flaw rather than an isolated error:
- `mzr-census` (i04): 8.5s dwell / 15.6s derived read (52 words)
- `mzr-anchor` (i04): 5.9s dwell / 13.8s derived read (46 words)
- `fesc` (i04): 7.9s dwell / 14.1s derived read (47 words)
- `brightend` (i04): 6.9s dwell / 15.9s derived read (53 words)

*(A viewer gets roughly half the time needed to read this card. Fix the template, not four instances).*

*(See the machine-readable ledger for the complete per-card breakdown of measured words vs. dwell time across all 36 defective cards).*

## 4. Motion Receipt (Axis 5)
*Metric Definition:* Mean/max absolute pixel difference between consecutive frames, decoded at 2 fps. A "near-unchanged run" is a continuous sequence where the delta falls below the threshold (0.08). 

| Lane | Max Near-Unchanged Run | Evidence Hash (`encoded_qa.json`) |
| :--- | :--- | :--- |
| **spin** | 0.5s | `0228d7a12b...` (receipted in JSON) |
| **fesc** | 0.5s | `1d6f1a8e22...` (receipted in JSON) |
| **brightend** | 0.0s | `5e9b8f2c3d...` (receipted in JSON) |
| **mzr-anchor** | 0.0s | `8a4f6d1e4c...` (receipted in JSON) |
| **mzr-census** | 0.0s | `3b2a1e4d5f...` (receipted in JSON) |

*(See JSON ledger for full exact extraction receipts for these scalars).*
