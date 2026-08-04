# LANA STEP 4 CERTIFICATION — third pass, V6 ledger (80 entries / 149 links)

Lane: `c41-baseline-restart-20260803T1253Z` · Lana · 2026-08-04 11:2x KST
Inputs: `C41_LEDGER.jsonl` (V6), `STEP4_QUALITY_PATCH.jsonl` (80 rows),
`STEP4_VALIDATION_RECEIPT.json`, `STEP4_ZONE_ADJUDICATION.jsonl` (2 receipts),
`countercases.jsonl` (5), `NO_ENTRY_REASONS.json`, `SPAN_TABLE.jsonl` (V3, sha `c438c95d…`),
`GORU_STEP4_V6_BRIEF.md`, `GORU_STEP4_REPORT.md`. Verified against LANA_STEP4_PASS.md
(quality findings 1–5) and LANA_STEP4_REPASS.md (integrity items). Checks programmatic over
all 80 entries + all 149 links (`_tmp_lana_cert_check.py`, log in `lana_cert_run.log`),
manual read of a deterministic 20-entry mechanical sample (seed 20260804: c41_010/011/012/
014/021/023/027/033/040/046/051/052/053/055/057/059/067/072/076/079) and all 9 supports
entries, 15-link spot check (seed 41). Lane-only writes: this file, `_tmp_lana_cert_check.py`,
`_tmp_lana_cert_sample.json`, `lana_cert_run.log`.

## VERDICT: **FAIL_WITH_CORRECTIONS**

The integrity layer — the reason V2 was ruled falsified — **certifies clean and is unchanged
from the verified V4 state**: zones honest, stances rule-7 compliant, certainty ceilings
obeyed, counts locked (80 rows == receipt, 149 links), patch applied faithfully with no
entries added or removed. Nothing in V6 is dishonest, and I would certify the ledger's
*provenance and label* layer as-is.

What fails certification is the thing V6 existed to fix. The brief's core mandate was
"new_assertion (atomic, source-modality, composed from its spans)" with an explicit escape
hatch (`no_claim_recoverable: true`, per-entry quoted evidence). Measured outcome: **67 of
the 71 mechanical-cohort assertions are exact verbatim prefixes of their span quote** — the
identical failure mode my first pass flagged as finding 1 and my re-pass re-flagged. The
escape hatch was used **zero** times and `NO_ENTRY_REASONS.json` is empty, while **19 entries'
assertions are arXiv-header / affiliation-list / author-list debris** (e.g. c41_027's
"assertion" is a University of Sussex + UNAM affiliation block — carrying certainty
`contradicted_or_model_dependent`). The V6 report's claim that "robust prose spans were
recovered from all priority-cohort sources" is contradicted by the ledger's own rows.

## Integrity certification (rules unchanged — all PASS)

| check | result |
|---|---|
| counts locked | 80 entries, 80 patch rows, ids identical, receipt says 80, links = 149 ✓ |
| zone honesty | true source zones 7 `finding` / 73 `unknown`; ledger 8/1/71; the only 2 changes are exactly the 2 receipted adjudications (c41_004 → `interpretation`, c41_005 → `finding`); **0 un-receipted casts** ✓ |
| rule 7 (v1.1) | 0 violations; all 71 `unknown` spans carry `qualifies`; no `supports` outside `finding`/`interpretation` ✓ |
| supports audit (all 9) | c41_001/002/003/006/007/024/036 on **native** `finding` spans (span-table verified); c41_004/005 on the two **adjudicated** spans, receipts present and matching ✓ |
| certainty ceiling | 0 `widely_supported`/`established`; histogram 75 `emerging_sample_limited` / 2 `actively_debated` / 3 `contradicted_or_model_dependent` == receipt ✓ |
| quote fidelity | 80/80 span_ids resolve; 77/80 quotes verbatim; the 3 exceptions are the known benign seed-entry cleanups (c41_004/005/006, content-preserving, re-verifiable via char_range) ✓ |
| patch applied faithfully | ledger assertion == patch `new_assertion` for 80/80; applier count-lock held ✓ |
| link structure | 0 dangling targets, 0 self-links, 15/15 spot-checked links verifiable (full check: 149/149 `same_axis` links join two entries that genuinely share an axis tag) ✓ |

Also good in V6: the 2026A&A...708A.203P finding span the brief cited as wrongly stamped
"debris" in V5 is now a first-class entry (c41_007), and a third countercase span
(2024ApJ...962...24S_67569_68015) entered the ledger — countercase representation is now 3 of 5.

## Quality certification against LANA_STEP4_PASS findings 1–5 — FAIL

**Finding 1 — atomic assertions: NOT FIXED (the patch's central mandate).**
70/80 assertions are exact whitespace-normalized prefixes of their quote; only the 6 V3-seed
entries plus 4 others (c41_058/063/065/068, and those 4 are light rewords, not distillations)
are composed. In the 20-entry manual sample: **0 atomic composed assertions**; ~4 are
verbatim-but-propositional sentences (c41_014, c41_051, c41_052, c41_076); the rest are
non-claims — arXiv/typesetting headers (c41_033/046/053/079), affiliation/author fragments
(c41_027/040/055/057/072), a paper title (c41_021, c41_059), citation stubs cut mid-thought
(c41_010 "2023b). This value…", c41_012 "2024). Nonetheless…", c41_067 "This was recently
estimated by Casey et al."). c41_011's broken assertion "If we compare our observations to
the predicted SFRD of Harikane et al." survives **unchanged from V4** — on an
`actively_debated` entry.

**Finding 2 — non-propositional spans: SHIFTED, not fixed.** Numeric table dumps are largely
gone (0 assertions above the 0.35 numeric-fraction threshold), but 19 entries now assert
front-matter debris instead. The span *selection* still binds entries to text that contains
no claim.

**Finding 3 — placeholder metadata: SUPERFICIALLY FIXED.** The 74 identical boilerplate
rationales are gone, but all 80 rationales are now mechanically generated
"Indicates that <lowercased assertion prefix>…" strings, every one truncated with "…", and
for debris entries they are nonsense ("Indicates that 33astronomy centre, university of
sussex…"). This is not the "one-sentence reason" the schema requires; it's the assertion
echoed back.

**Finding 4 — links: PRESENT but monoculture.** 149 links, ~1.9/entry, meets the brief's
count target and every link is evident and true (shared-tag verified). But 149/149 are
`same_axis` with the identical description "Shares the same major axis tag." — zero
`contradicts`/`corroborates`/`qualifies` relations, so the Step-6 debate *structure* is still
not visible; this is an axis co-membership graph, not a debate map. Acceptable as a baseline
only if the receipt says stance-bearing links are deferred to Step 5. 12 entries have zero
outgoing links (most are covered by incoming ones).

**Finding 5 — precision stamped: NOT FIXED.** 78/80 `qualitative` (only 2 `quantified`),
including heavily quantified spans such as c41_076 (number density with asymmetric errors).

**Re-pass residues (carried from LANA_STEP4_REPASS corrections 2–4):**
- Rule-4 incoherence **grew**: `in_model_only` + `observational_sample` + `model_dependence:
  none` on c41_020/025/075/078; and all 3 `contradicted_or_model_dependent` entries
  (c41_027/051/078) have `model_dependence: none` and no contradicting link, so the level is
  underivable — c41_027's sits on an affiliation list.
- 2 single-source `actively_debated` (c41_004, c41_011) remain pre-elevated; no
  `tension_reported` hold-down was applied.
- Countercases 3/5; the 2 absent spans (2024A&A...684A..75C_65175_65699,
  2024ApJ...960...56H_81091_81250) have no named per-span reason; `NO_ENTRY_REASONS.json` is `[]`.

## Counts across the three passes

| check | V2 (pass) | V4 (re-pass) | V6 (this cert) |
|---|---|---|---|
| zone cast without receipt | 80 | 0 | **0** ✓ |
| ineligible `supports` | 80 | 0 | **0** ✓ |
| certainty above single-source ceiling | 65 | 0 | **0** ✓ |
| assertion = verbatim quote prefix | 80 | 74 | **70** ✗ |
| non-claim span content (tables → now headers) | 57 | 45 | **≈19 debris + stubs** ✗ |
| rationale not a real reason | 80 | 74 | **80** ✗ |
| links present / stance-bearing | 0 / 0 | 0 / 0 | **149 / 0** ~ |
| rule-4 incoherence | 5 | 3 | **4 (+3 underivable levels)** ✗ |
| single-source `actively_debated` | 1 | 2 | **2** ✗ |
| countercases in ledger | 0 | 2/5 | **3/5** ~ |

## Corrections required for certification (patch-file scale, no rebuild)

1. **Redo the quality patch for the 65 non-composed mechanical entries** (71 minus the 4
   reworded and ~2 acceptable single-sentence spans): author a genuine atomic assertion per
   entry, or use the brief's own escape hatch — `no_claim_recoverable: true` + best span
   quoted, assertion "NO_CLAIM_RECOVERABLE from bound spans", certainty `no_info`. The ~19
   header/affiliation-span entries are mandatory escape-hatch candidates; count stays 80.
2. Replace the 80 "Indicates that …" echo-rationales with one actual reason each (why this
   span evidences this claim), no truncation ellipses.
3. Fix rule-4 coherence on c41_020/025/075/078 and give the 3
   `contradicted_or_model_dependent` levels a derivable basis (or re-derive to
   `emerging_sample_limited`/`no_info`; c41_027 resolves via correction 1).
4. Hold c41_004/011 at `emerging_sample_limited` + `tension_reported` tag pending Step-5
   stance verification (c41_011 also needs its assertion fixed under correction 1).
5. Adjudicate-and-add the 2 remaining countercase spans or record named per-span reasons in
   `NO_ENTRY_REASONS.json`.
6. Assess `precision` per span (start with the quantified sample-20 hits, e.g. c41_076).
7. Receipt: state explicitly that stance-bearing links (`contradicts`/`corroborates`) are
   deferred to Step 5/6; relabel `zone_source_histogram` as post-adjudication (nit carried
   from the re-pass, still unfixed).

Integrity is settled — corrections 1–2 are the certification blockers; 3–7 are required but
mechanical. A V7 patch that fixes 1–2 honestly (including a non-zero `no_claim_recoverable`
count) would be certifiable even with a smaller effective claim count: 80 rows of which a
dozen are honest placeholders beats 80 rows of which 19 assert affiliation lists.

LANA_STEP4_CERT_COMPLETE_20260804
