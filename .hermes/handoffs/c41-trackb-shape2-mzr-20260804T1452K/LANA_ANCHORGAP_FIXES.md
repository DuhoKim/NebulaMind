# LANA_ANCHORGAP_FIXES — referee MINOR edits applied to ANCHOR_GAP_PAPER.tex

Lane: `c41-trackb-shape2-mzr-20260804T1452K` · Agent: Lana (drafter, applying own-paper fixes)
Date: 2026-08-04 21:32 KST (stamped via `date`; 2026-08-04T1232Z)
Referee source: `KUN_ANCHORGAP_REFEREE.md` (Kun, verdict **MINOR** — accept after F-R1…F-R4)

## Scope discipline

Exactly the four fixes on Kun's list were applied, in place, to `ANCHOR_GAP_PAPER.tex`.
No number, verdict, null wording, or contract statement changed. Kun's explicitly
"no fix required" items — the "two objects, three rows" clarifying parenthetical
(F-R2's related observation) and every §3 observation — were deliberately **not**
applied, per the nothing-beyond-his-list instruction.

## Fixes applied

**F-R1 — Table 2 (line 281).** S/N-floor row's "Dominant source" label corrected:
`JADES prism/grating` → `JADES prism + compilation`. Kun's recount of the 64-row class:
28 gnprism + 31 gsprism + 5 compilation; the grating tables contribute zero S/N-floor
rows (their exclusions are all no-Hβ / missing-flux / Te-fail). Count (64) unchanged.

**F-R2 — §5.3 Relation to z9–10 study (line 441).** `the $z\geq9.7$ candidates lack the
nebular flux` → `the $z>9.6$ candidates …`. One of the four missing-flux z>9 rows
(gsprism id 230) sits at z = 9.686 < 9.7; the substance (those candidates die at
missing flux) was already correct. Kun offered "z≳9.69" or "z>9.6"; took the latter.

**F-R3 — §4.2 attribution (lines 306–308).** Reworded the recount attribution:
was "the forensic audit recomputed all 64 exclusions from the archived fluxes and
confirmed every stated reason"; now "all 64 exclusions were recomputed directly from
the archived per-row fluxes, confirming every stated reason." The audit document's own
prose says 58 (a disclosed prose-count slip, see PAPER_CHANGELOG.md Recount note); the
correct 64 comes from the direct recount of the per-row sample file, which Table 2's
comment already credited. One clause; the number 64 unchanged.

**F-R4 — §6.5 pipeline seam disclosure (after line 491).** One added disclosure
sentence: the freeze document (`APRIME_PIPELINE_FROZEN.md`) specifies the Hα/Hβ
decrement as primary dust input with source-published A_V fallback, whereas the
executed and reviewed pipeline (B2's approved fix) used the Hγ/Hβ decrement
exclusively — at z>4 the only physically available Balmer pair, so the primary branch
was vacuous and the fallback never fired; all five anchors were derived and reproduced
under Hγ/Hβ consistently. Same class as the already-disclosed PyNeb 1.1.18/1.1.32
seam: documentation defect, not numeric.

## Verification

- `grep` confirms all four new wordings present at lines 281 / 441 / 307 / 491 ff.
- `grep -c 'z\\geq9.7'` → 0; old F-R3 wording ("forensic audit recomputed") → gone.
- No other line of the .tex touched; every quantitative value byte-identical to the
  referee-audited draft.
- Compilation still not run in-lane (no-network / lane-only-writes rule, unchanged
  disclosure in the .tex header).

## Files written this session

1. `ANCHOR_GAP_PAPER.tex` — four in-place edits (F-R1…F-R4).
2. `PAPER_CHANGELOG.md` — "Referee fixes" section appended (marker
   `LANA_ANCHORGAP_FIXES_LOGGED_20260804`).
3. `LANA_ANCHORGAP_FIXES.md` — this report.

LANA_ANCHORGAP_FIXES_COMPLETE_20260804
