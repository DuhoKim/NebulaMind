# Paper-naive closed-book packet — MZR archive census proposal

Read this packet once. Then answer the questions from memory without reopening it, browsing the web, or reading neighboring files.

## Proposed narration and visual actions

1. This is a census of VizieR catalogue metadata: it asks which single tables are reachable for gas-phase abundance, stellar mass, and redshift together.
   Visual: three labeled metadata columns flow into an archive-table icon. A badge says `METADATA CENSUS — NOT AN MZR MEASUREMENT`; a persistent subtitle says `SINGLE-TABLE METADATA INTERSECTION — CROSS-TABLE JOINS AND CROSSMATCHES NOT ASSESSED`.

2. The search combined semantic UCD tags with column-name variants, and each frozen query returned exactly its pre-counted rows.
   Visual: two retrieval rails labeled `UCD` and `NAME VARIANTS`; a `zero channel failures` check appears.

3. UCD plus name matching reached 5,568 abundance tables, 6,206 mass tables, and 6,687 redshift tables; the name channel added 175, 88, and 20 respectively.
   Visual: three equal-width axis cards show each UCD count, plus-name count, and gain. A note says `counts, not area encoded`.

4. The three axis lists intersected at 178 candidate tables.
   Visual: the three rails merge into `THREE-AXIS REACH: 178`.

5. Modifier columns then emptied a required axis in 21 tables: 19 on redshift and 2 on abundance, leaving 157 recorded candidates.
   Visual: `178 → −21 → 157`, with the dropped branch split into `19 REDSHIFT AXIS EMPTIED` and `2 ABUNDANCE AXIS EMPTIED` plus recorded modifier examples.

6. As a side check, a frozen term regex matched 62 of those 157 recorded descriptions; it is not an eligibility filter, and T2 still applies to all 157.
   Visual: `157` connects directly to T2. `62` branches downward into an inset stamped `FROZEN TERM-REGEX MATCH IN RECORDED DESCRIPTIONS` and `SIDE CHECK ONLY — T2 STILL APPLIES TO ALL 157`.

7. All seven pinned recall members returned, while none of the three controls appeared.
   Visual: `RECALL 7/7` and `CONTROLS APPEARING 0/3` are shown as separate scorecards.

8. Those checks validate retrieval, not precision: the frozen controls did not cover the dominant precision-contamination mode.
   Visual: an amber `PRECISION NOT CERTIFIED` panel appears beside the passing retrieval checks and opens two groups of recorded examples.

9. Recorded examples separate symbol-and-meaning collisions—Galactic height and model-grid metal fraction—from target-domain mismatches: stellar gravitational redshift and gravitational-redshift velocity. They are not T2 rulings.
   Visual: the examples are grouped under `SYMBOL / MEANING COLLISION` and `TARGET-DOMAIN MISMATCH`, with `RECORDED EXAMPLES — NOT T2 RULINGS` held above them and no trend geometry.

10. The T2 rule contract is frozen, but the 157-table eligibility application is not completed, so no eligible-table count or metallicity measurement is reportable yet.
    Visual: the direct path ends at `T2 — CONTRACT FROZEN — APPLICATION NOT COMPLETED — NO ELIGIBLE-TABLE COUNT`, then holds `REPORTABLE NOW` versus `PENDING`.

## Questions

1. What is this work counting, and what is it explicitly not measuring?
2. What two retrieval channels were used?
3. Reconstruct the main count sequence and explain where the 62-term check sits relative to the T2 eligibility application.
4. What does `62` mean, and what does it not mean?
5. What did `7/7` and `0/3` establish?
6. What important failure mode did those checks not certify against?
7. What two precision-failure categories are shown, and which recorded examples belong to each?
8. What is reportable now, and what remains pending?
