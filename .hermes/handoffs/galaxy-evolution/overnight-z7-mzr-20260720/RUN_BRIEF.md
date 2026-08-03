# Overnight run — z>7 mass–metallicity relation (Trikitear)

**Target (LOCKED):** Is the early-universe (z>7) mass–metallicity offset **physical**, or an
artifact of **mass mismatch + metallicity calibration scale**? The controversy scoring found
metallicity's disagreement is real only after mass-control and only at z>7 (S 7.76 → 2.65).
Attacks the #1 frontier (JWST high-z); non-circular by construction.

## Publishable bar (all four to "clear")
1. Motivation grounded in wiki + literature (DR packet on disk) — not circular.
2. Non-circular result — confront SDSS anchor + JWST high-z AND IllustrisTNG on a MATCHED abundance scale.
3. Defensible conclusion — honest re calibration, aperture, selection, small-N.
4. Compiles (tectonic); automated referee -> ACCEPT/MINOR; honestly labelled.

## Make-or-break: reconcile metallicity calibration FIRST
SDSS-Tremonti (sdss_mzr.csv oh_p50) runs ~0.24 dex high vs Te/PP04-O3N2. Put SDSS + JWST on ONE
scale before any evolution claim. If the z>7 offset vanishes on a matched scale, that IS the result.

## Local assets (use these; do not re-pull unless missing)
- SDSS anchor: research-frontiers-20260716/{sdss_mzr.csv,mzr_results.json,mzr_draft.tex}
- JWST high-z: overnight-research-20260718/s17_jwst_mzr.png ; research-frontiers-20260716/topic5/chworowsky.csv
- Literature (DR done): wiki-expansion-20260715/area1_mass_metallicity_DR_PACKET.md
- Corpus: corpus-ga-co-2009-2026-20260718/ ; Tools: tectonic, ollama qwen3.6:27b-nvfp4, astropy

## Phases
P1 Design (now) · P2 Analysis (matched-scale mass-controlled z>7 offset + bootstrap + TNG) ·
P3 Draft (AASTeX->PDF) · P4 Referee->revise · P5 Gate (descriptive/validated + verdict memo)

## Guardrails
No fabrication; automated results DESCRIPTIVE until human-cleared. Calibration reconciliation
mandatory. All files stay in this lane dir. No live DR/browser (packet on disk). Times in KST.
Crew writes outputs via Bash/python (shared-checkout Write guard is active).

## Morning deliverable
1 candidate paper (.tex+PDF) + figure + referee/revision trail + one-page verdict memo, plus
honestly-labelled supporting numbers. Never presented as validated.
