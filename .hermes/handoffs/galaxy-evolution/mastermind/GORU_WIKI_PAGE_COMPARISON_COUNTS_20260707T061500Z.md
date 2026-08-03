# Goru Report: Wiki-Page Comparison Counts

Packet marker: `HWAO_TEAMS_HOLD_REACTIVATION_PACKET_20260707T061500Z`
Status: READ-ONLY MECHANICAL CHECK COMPLETED

## Per-Method Counts and Checks

### Method 1: Packet-Gated Reconciliation
- **H2 Count**: 9 binding (Total: 14)
- **Exact H2 List (Binding Order Checked: PASS)**:
  1. Overview: Galaxy Evolution as a Regulated Baryon Cycle
  2. Dark Matter Halos & Structure Formation
  3. Gas Supply, Star Formation & Feedback
  4. AGN Feedback & Quenching
  5. Environment, Morphology & Structural Growth
  6. Chemical Enrichment & Cosmic Timing
  7. High-Redshift & Reionization Frontier
  8. Observational Evidence & Surveys
  9. Synthesis & Open Tensions
- **Word / Paragraph Count (MD source)**: 1839 words / 34 paragraphs
- **Claim-Marker Count**: 30 unique
- **Full Claim ID List**: [2905, 2906, 2907, 2908, 2909, 2910, 2911, 2912, 2913, 2914, 2915, 2916, 2917, 2918, 2919, 2920, 2921, 2922, 2923, 2925, 2926, 2929, 2930, 2931, 2932, 2933, 2934, 2935, 2936, 2946]
- **Cite-Marker Count**: 0
- **Full Numeric Cite ID List**: []
- **Link / Anchor Count**: 0
- **Method-Leakage Check**: **PASS** — Carries ONLY its own M1 chip IDs. No foreign ID or cross-method import.
- **Published-State Check**: **PASS** — Manifest reads `DRAFT_PREPARED_STATIC_NOT_PUBLISHED`. HTML reads `static · not published`. No live-wiki or `page_versions` mirror referenced.

### Method 2: Source-First Adjudication
- **H2 Count**: 9 binding (Total: 12)
- **Exact H2 List (Binding Order Checked: PASS)**: (Same expected 9 H2s in order)
- **Word / Paragraph Count (MD source)**: 1689 words / 39 paragraphs
- **Claim-Marker Count**: 6 unique
- **Full Claim ID List**: [2942, 2943, 2944, 2945, 2946, 2947]
- **Cite-Marker Count**: 22 unique tags
- **Full Numeric Cite ID List**: [28060, 28062, 28066, 28069, 28073, 28074, 28075, 28087, 28088, 28089, 28091, 28095, 28108, 28123, 28131, 28140, 28141, 28144, 28148, 28151, 28155, 28158]. (Note: Rejected rows like 28070 are never cited in a tag, as expected).
- **Link / Anchor Count**: 0
- **Method-Leakage Check**: **PASS** — Carries ONLY its own M2 chip IDs.
- **Published-State Check**: **PASS** — Manifest reads `DRAFT_PREPARED_STATIC_NOT_PUBLISHED`. HTML reads `DRAFT_PREPARED_STATIC_NOT_PUBLISHED`. No live-wiki or `page_versions` mirror referenced.

### Method 3: Debate-Map-to-Wiki Rebuild
- **H2 Count**: 9 binding (Total: 9)
- **Exact H2 List (Binding Order Checked: PASS)**: (Same expected 9 H2s in order)
- **Word / Paragraph Count (MD source)**: 2121 words / 30 paragraphs
- **Claim-Marker Count**: 0
- **Full Claim ID List**: []
- **Cite-Marker Count**: 0
- **Full Numeric Cite ID List**: []
- **Link / Anchor Count**: 0
- **Method-Leakage Check**: **PASS** — Carries no chip IDs, no foreign leakage.
- **Published-State Check**: **PASS** — Manifest reads `9-H2 confirmed — M3 P1.5 GO issued`. HTML reads `No live-wiki publish, no claim/citation binding — deferred to the P3 gate`. (Note: exact `NOT_PUBLISHED` string absent from HTML, but semantically verifies that no live mirror is referenced).

## Marker & Citation Inventory Summary

| Method | Claim Count | Cite Count | Leakage Detected | Published Status |
| --- | --- | --- | --- | --- |
| M1 (Packet-Gated) | 30 | 0 | None | Static / Not Published |
| M2 (Source-First) | 6 | 22 | None | Static / Not Published |
| M3 (Debate-Map) | 0 | 0 | None | Static / Not Published |

## Leakage Verdict
**PASS**. Each page carries strictly its own method's expected IDs (or none for M3). No cross-method leakage or foreign ID injection detected.

## Safety Ledger
- DB / SQL execution: `0`
- Trust / prose / live wiki mutations: `0`
- Deploy / restart / git mutations: `0`
- External APIs / config mutations: `0`
- File modifications to existing artifacts: `0`

Done marker: `TORI_GORU_DISPATCH_DONE_20260707T061810Z`
