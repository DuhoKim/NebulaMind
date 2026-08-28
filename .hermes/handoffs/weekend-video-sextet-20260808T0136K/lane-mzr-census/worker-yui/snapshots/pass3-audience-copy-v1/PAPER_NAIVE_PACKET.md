# Paper-naive closed-book packet — MZR archive census pass-3 proposal

Read this packet once. Then answer the questions from memory without reopening it, browsing the web, or reading neighboring files.

## Proposed narration and exact audience copy

Only audience-visible copy is included below. Build directions, verification filenames, source paths, prior verdicts, and the answer key are excluded.

1. This is a census of VizieR catalogue metadata: it asks which single tables are reachable for gas-phase abundance, stellar mass, and redshift together.
   Screen: `A SINGLE-TABLE METADATA CENSUS`; `Which VizieR tables have metadata-reachable columns for gas-phase abundance, stellar mass, and redshift together?`; `METADATA CENSUS — NOT AN MZR MEASUREMENT`; `SINGLE-TABLE METADATA INTERSECTION · CROSS-TABLE JOINS AND CROSSMATCHES NOT ASSESSED`.

2. The search combined semantic UCD tags with column-name variants, and each frozen query returned exactly its pre-counted rows.
   Screen: `TWO RETRIEVAL CHANNELS`; `SEMANTIC UCD TAGS`; `COLUMN-NAME VARIANTS`; `FROZEN QUERIES · ZERO CHANNEL FAILURES`.

3. UCD plus name matching reached 5,568 abundance tables, 6,206 mass tables, and 6,687 redshift tables; the name channel added 175, 88, and 20 respectively.
   Screen: `METADATA REACH BY AXIS`; `ABUNDANCE · UCD 5,393 · UCD + NAME 5,568 · GAIN +175 TABLES`; `STELLAR MASS · UCD 6,118 · UCD + NAME 6,206 · GAIN +88 TABLES`; `REDSHIFT · UCD 6,667 · UCD + NAME 6,687 · GAIN +20 TABLES`; `COUNTS · AREA NOT ENCODED`.

4. The three axis lists intersected at 178 candidate tables.
   Screen: `THREE-AXIS METADATA REACH`; `178 SINGLE TABLES`; `RECORDED METADATA CANDIDATES · NOT ELIGIBILITY RULINGS`.

5. Modifier columns then emptied a required axis in 21 tables: 19 on redshift and 2 on abundance, leaving 157 recorded candidates.
   Screen: `MODIFIER FILTER ACCOUNTING`; `178 − 21 = 157 RECORDED CANDIDATE TABLES`; `19 · REDSHIFT AXIS EMPTIED · e_Z · e_[Z/H]`; `2 · ABUNDANCE AXIS EMPTIED · e_Ha/Hb · e_logOI/Ha · l_logOI/Ha`.

6. As a side check, a frozen term regex matched 62 of those 157 recorded descriptions; it is not an eligibility filter, and T2 still applies to all 157.
   Screen: `DESCRIPTION-TERM SIDE CHECK`; `62 OF 157 RECORDED DESCRIPTIONS MATCHED`; `SIDE CHECK ONLY · NOT AN ELIGIBILITY FILTER · T2 STILL APPLIES TO ALL 157`. The main path sends all 157 directly to T2; the 62 card is a branch, not an input stage.

7. All seven pinned recall members returned, while none of the three controls appeared.
   Screen: `RETRIEVAL INSTRUMENT CHECK`; `RECALL 7/7`; `CONTROLS APPEARING 0/3`.

8. Those checks validate retrieval, not precision: the frozen controls did not cover the dominant precision-contamination mode.
   Screen: `RETRIEVAL CHECK PASSED · PRECISION NOT CERTIFIED`; `FROZEN CONTROLS DID NOT COVER THE DOMINANT PRECISION-CONTAMINATION MODE`.

9. Recorded examples separate symbol-and-meaning collisions—Galactic height and model-grid metal fraction—from target-domain mismatches: stellar gravitational redshift and gravitational-redshift velocity. They are not T2 rulings.
   Screen: `RECORDED EXAMPLES · NOT T2 RULINGS`; `SYMBOL / MEANING COLLISION` with `GALACTIC CARTESIAN HEIGHT` and `STELLAR-GRID METAL FRACTION · MODEL Z`; `TARGET-DOMAIN MISMATCH` with `STELLAR GRAVITATIONAL REDSHIFT` and `GRAVITATIONAL-REDSHIFT VELOCITY`.

10. The T2 rule contract is frozen, but the 157-table eligibility application is not completed, so no eligible-table count or metallicity measurement is reportable yet.
    Screen: `REPORTABLE NOW VERSUS PENDING`. Reportable: `T1 METADATA-ENUMERATION COUNTS`; `178 − 21 = 157 RECORDED CANDIDATE TABLES`; `62/157 DESCRIPTION-TERM SIDE CHECK`; `RECALL 7/7 · CONTROLS 0/3 · PRECISION NOT CERTIFIED`; `T2 RULE CONTRACT FROZEN`. Pending: `T2 APPLICATION TO ALL 157 TABLES`; `ELIGIBLE-TABLE COUNT`; `ANY METALLICITY OR MZR MEASUREMENT`. Gate: `APPLICATION NOT COMPLETED · NO ELIGIBLE-TABLE COUNT`. Close: `SINGLE-TABLE METADATA CENSUS · NOT AN MZR MEASUREMENT`.

## Questions

1. What is this work counting, and what is it explicitly not measuring? Does metadata reach establish that each table carries adjudicated physical measurements?
2. What two retrieval channels were used?
3. Reconstruct the main count sequence and explain where the 62-term check sits relative to the T2 eligibility application.
4. What does `62` mean, and what does it not mean?
5. What did `7/7` and `0/3` establish?
6. What important failure mode did those checks not certify against?
7. What two precision-failure categories are shown, and which recorded examples belong to each?
8. What is reportable now, and what remains pending?
