# GORU BRIEF — Step 3 repair round (Tori spot-check FAIL: quote mangling + zone mislabels)

Lane: `c41-baseline-restart-20260803T1253Z`. You are Goru. Tori's blind verdict on your span table
is FAIL (`TORI_STEP3_SPOTCHECK.md`) on two mechanisms — read it first. Recall was 94.2%: your
COVERAGE is good; the repairs are mechanical. Root-cause note for fairness: defect 1 traces to the
original brief specifying a 600-char cap without cap semantics — that ambiguity is the
coordinator's, not yours. Fix both defects, re-run, hand back.

## Repairs

1. **Quote fidelity** — quotes must be VERBATIM substrings of the extracted source text, always:
   - Cap by trimming to the last complete SENTENCE boundary that fits within 600 chars (if the
     first sentence alone exceeds 600, hard-cut at 600 exactly — still a verbatim substring).
   - NEVER insert `...` or any character not in the source into the `quote` field.
   - Add fields: `truncated: true/false` and `full_span_chars: <n>` so downstream stages know.
2. **Zone heuristics** — eliminate the false-`finding` class Tori documented (methods text,
   figure/table captions, reference-list transitions labeled `finding`):
   - Detect and tag caption blocks (`Figure N`, `Table N` starts) and bibliography/reference zones;
     they are `caption` / `references`, never `finding`.
   - Label `finding` ONLY with positive evidence (results/findings/conclusion heading proximity or
     result-verb signal); when the heading map is unclear, use `unknown` — `unknown` is honest,
     `finding` is a claim.
3. Re-run `step3_extract.py` (keep determinism; bump `protocol_version` to `C41_STEP3_V2`);
   regenerate `SPAN_TABLE.jsonl` + `STEP3_SUMMARY.json` in place (v1 copies: move to
   `_tmp_goru_v1_backup/` first — do not silently overwrite the failed evidence).

## Deliverable

Append a `## Repair round (V2)` section to `GORU_STEP3_REPORT.md`: what changed in the driver,
new span/zone/truncation counts, v1-vs-v2 delta summary. End the section with marker:
`GORU_STEP3_V2_COMPLETE_20260804`.

Constraints unchanged: lane-only writes, no network, deterministic, no modification of Tori's or
Yui's artifacts.
