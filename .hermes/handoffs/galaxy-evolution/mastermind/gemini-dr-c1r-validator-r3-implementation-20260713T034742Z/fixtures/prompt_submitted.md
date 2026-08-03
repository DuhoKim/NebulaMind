# Deep Research request — Calibration targets vs out-of-sample validations for major galaxy-formation simulations (revised C1R)

Request ID: REQ_JOINT_C1R_20260712T045317Z

Role: You are a literature analyst for a galaxy-evolution research journal. Report only published
work; you have no access to the journal's internal results.

Question (scope unchanged): For each major galaxy-formation simulation project — IllustrisTNG,
EAGLE, SIMBA, FIRE/FIRE-2, ROMULUS, ASTRID, FLAMINGO, and comparable published suites (e.g.
BAHAMAS) — what do the METHOD papers state was used to calibrate the feedback/subgrid model, and
which later observation comparisons are genuinely out-of-sample (not calibration targets, per the
papers themselves)?

OUTPUT DISCIPLINE (read first — binding): The report body is STRUCTURED ONLY, and its EXACT top-to-
bottom sequence is:
(a) the mandatory 4-line meta header (C1);
(b) the five numbered content sections below, in order;
(c) the Links ledger;
(d) the final completion-marker line (C8), alone.
NOTHING ELSE may appear — no abstract, introduction, summary, prose paragraph, or free narrative of
any kind OUTSIDE those allowed units (meta-header lines, table cells, bullet lines, GAP lines, ledger
lines, and the marker line). Every factual claim lives inside a table cell or a single bullet. Any
content outside the permitted units is a contract violation.

Required content sections (exactly five, in this order):

## 1. Calibration ledger
Markdown table, one row per simulation:
| Simulation (method-paper citation) | Stated calibration targets (faithful to source wording) | Feedback parameters tuned (as stated) | Explicitly emergent (stated NOT calibrated) | Notes |
An empty cell is exactly NONE_FOUND. A source that is unclear is AMBIGUOUS_IN_SOURCE plus the quoted
sentence. EVERY claim-bearing cell in the row (calibration-targets, feedback-parameters,
explicitly-emergent, notes) carries its OWN same-cell checkable citation or UNCITED_NOT_USABLE — the
Simulation cell's citation does not cover the other cells (C4).

## 2. Out-of-sample validation ledger
Markdown table, one row per published out-of-sample comparison:
| Simulation | Observable | Result (agreement or tension, with magnitude) | COMPARABILITY | Overlap with a Section-1 calibration target | Citation |
The COMPARABILITY cell is exactly MATCHED_SELECTIONS or NON_COMMENSURABLE_UNMATCHED_SELECTIONS.
The Citation cell is non-empty: a checkable citation or UNCITED_NOT_USABLE. Empty citation cells are forbidden.

## 3. Double-counting warnings
Bullet list only. Each bullet is one published warning against treating a calibration target as
evidence of predictive success, stated as an attributed claim with a same-bullet checkable citation
or UNCITED_NOT_USABLE. No prose outside bullets.

## 4. Feedback-relevant observables map
Markdown table:
| Simulation | Quenched fractions | Gas fractions of passive galaxies | Outflow demographics | Hot-halo/cavity properties | Radio-AGN incidence |
Each observable cell is CALIBRATED, EMERGENT, or NOT_REPORTED. A CALIBRATED or EMERGENT cell carries
a same-cell checkable citation (or UNCITED_NOT_USABLE). A missing status is written exactly as
NOT_REPORTED — NONE_FOUND.

## 5. Gaps
GAP: lines only. Each GAP line either carries a checkable citation OR ends with the exact token
ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED (use this when asserting that no published test exists
and the absence itself cannot be cited). No uncited, unlabeled GAP line is allowed.

## Links ledger
One line per cited item: <short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK
Bidirectional and unique: every citation appearing inline in Sections 1–5 appears exactly once here,
and every row here is cited at least once inline. No duplicates, no orphan rows, no inline-only citations.

BINDING OUTPUT CONTRACT (C1–C8):

C1 (meta header). The body's first lines are exactly:

    # Joint C1R answer — REQ_JOINT_C1R_20260712T045317Z
    Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
    Model: Gemini Pro (selected UI mode; backend version not exposed)
    Simulations covered: <N>

Emit the Model line verbatim as written above — do not substitute a version number or any other
self-identification (a hallucinated version such as "1.5" is a defect). This 4-line meta header is
the first content of the body.

C2 (structure + empty-field device). Exactly the five sections above in order, then the Links
ledger. An empty field is exactly NONE_FOUND — never blank, never padded. Every Section-5 GAP line
carries a checkable citation OR the exact token ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED.

C3 (uncertainty). Every scientific quantitative value carries its source's uncertainty in the same
line/cell, OR the same-line/cell label UNCERTAINTY_NOT_QUOTED_BY_SOURCE. Never invent error bars.
EXEMPT (no token required): run timestamps, request IDs, citation identifiers/URLs (arXiv, DOI, ADS
numbers), section numbers, the meta-header simulation count (the "Simulations covered: N" value), and
project-name suffixes (for example FIRE-2, FIRE-1, TNG50).

C4 (citation labeling). Every calibration or validation statement carries, within the SAME logical
unit (a single bullet, or the individual table cell that makes the claim), a checkable citation
(arXiv ID, DOI, ADS bibcode, or URL) OR the same-unit label UNCITED_NOT_USABLE. A citation in one
cell does NOT cover other cells: in a multi-cell table row (e.g. Section 1's calibration-targets,
feedback-parameters, explicitly-emergent, and notes cells), EVERY claim-bearing cell repeats its own
checkable citation or UNCITED_NOT_USABLE — a citation in the Simulation cell or a dedicated Citation
cell does not satisfy the other claim-bearing cells. Empty citation cells are forbidden.

C5 (wording contract). In your own voice the following settled/causal register is BANNED
(case-insensitive): establish, establishes, established, establishing, proves, proven, confirms
that, settles, settled question, resolves the debate, definitively, conclusively, is now known,
"demonstrates that … causes". A source's own claim in that register may appear ONLY as an explicit
attributed quote with a checkable citation. Before finalizing, perform an INTERNAL LITERAL
SELF-AUDIT: scan your own draft for each banned term above and remove or re-attribute every
own-voice occurrence. Do not output the audit.

C6 (estimand / commensurability). Each Section-2 ROW has its dedicated COMPARABILITY cell containing
exactly one token — MATCHED_SELECTIONS or NON_COMMENSURABLE_UNMATCHED_SELECTIONS — and nothing else in
that cell. Any quoted fraction or incidence, anywhere in the body, carries the four qualifiers in
exactly this syntax within the same line/cell:
TRACER=<...>; SELECTION=<...>; DENOMINATOR=<...>; REDSHIFT=<...>
using NOT_APPLICABLE as the value of any individual qualifier that does not apply (e.g.
REDSHIFT=NOT_APPLICABLE). Label honestly; the semantic correctness of these labels is checked later
by human review.
Do not make a simulation-observation comparison outside Section 2. If one is unavoidable in an
allowed bullet or GAP line, that same logical unit must contain exactly one of the two exact tokens
MATCHED_SELECTIONS or NON_COMMENSURABLE_UNMATCHED_SELECTIONS. A comparison elsewhere without one of
those tokens is a C6 failure.

C7 (links ledger — bidirectional, unique, quarantined). Every inline citation appears in the Links
ledger; every ledger row is cited inline at least once; each ledger row is unique; each ledger row
ends with QUARANTINED_PENDING_LOCAL_CHECK. No orphan rows, no inline-only citations, no duplicates.

C8 (completion marker). The exact string

    GEMINI_WEB_JOINT_C1R_OUTPUT_DONE_20260712T045317Z

appears exactly once, as the standalone final non-empty line of the body. Nothing may follow it — no
"End of Report", no sign-off, no blank-line-then-text. A marker present only in a chat-UI completion
element and not in the body counts as ABSENT and the run is rejected.

SILENT PREFLIGHT (perform before emitting; DO NOT output any of it as a section, note, or line):
verify (1) the body sequence is exactly meta header → five sections → Links ledger → final marker
line, with no content outside those allowed units; (2) the Model line is exactly `Model: Gemini Pro
(selected UI mode; backend version not exposed)`; (3) every empty field is NONE_FOUND, and every GAP
line is cited or ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED; (4) every scientific number has an
uncertainty or UNCERTAINTY_NOT_QUOTED_BY_SOURCE, with the C3 exemptions (including the meta-header
simulation count) respected; (5) EVERY claim-bearing cell — not just one per row — carries its own
citation or UNCITED_NOT_USABLE, and no citation cell is empty; (6) the C5 literal self-audit passed;
(7) every Section-2 row's COMPARABILITY cell holds exactly one token, every simulation-observation
comparison outside Section 2 also carries exactly one of those tokens in the same logical unit,
every Section-4 cell is
CALIBRATED/EMERGENT (with a same-cell citation) or exactly `NOT_REPORTED — NONE_FOUND`, and every
quoted fraction uses `TRACER=<...>; SELECTION=<...>; DENOMINATOR=<...>; REDSHIFT=<...>` (with
NOT_APPLICABLE per qualifier as needed); (8) the Links ledger is bidirectional, unique, and every row
ends with QUARANTINED_PENDING_LOCAL_CHECK; (9) the marker appears exactly once as the final non-empty
line. If any check fails, fix it silently, then emit only the final report.

Safety locks:
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not present generated DOI/ADS/arXiv IDs as verified; all IDs are quarantined pending local check.
- Do not propose edits to any local artifact; produce this report body only.

Final reminder: the last non-empty line of your report must be exactly
GEMINI_WEB_JOINT_C1R_OUTPUT_DONE_20260712T045317Z
with no text after it.
