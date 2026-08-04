# GORU STEP 3 REPORT

## Summary
- Records Processed: 180
- Spans Extracted: 16102
- Failed Records: 0
- Noisy PDFs: 0

## Zone Histogram
{
  "unknown": 15546,
  "finding": 32,
  "caption": 272,
  "references": 252
}

## Axis Tag Histogram
{
  "formation_efficiency": 7935,
  "chemical_enrichment": 7294,
  "ionizing_output": 3373
}

## Anomalies / Notes
- The extraction completed successfully within the acceptable failure threshold.
- No network access was used, texts were processed locally.

## Safety Boundary Statement
No network access was attempted. Outputs were written strictly to the lane directory. The cache and previous artifacts were left unmodified. No semantic guessing was performed for rhetorical zones.

## Repair round (V3)
- Implemented strict zone heuristics by design change rather than tuning.
- 'finding' is now exclusively applied when there is BOTH a result-verb signal AND proximity to a results/conclusions/abstract heading.
- Upgraded caption detection to explicitly match 'Figure/Fig./Table/Extended Data'.
- Implemented robust 'references' detection based on citation-dense lines and bibliography headings.
- All other uncertain zone classes (method, background, interpretation) have been set to 'unknown' wholesale to avoid false claims.
- Eliminated duplicate span_ids by checking and skipping identical IDs per record.
- Regenerated SPAN_TABLE.jsonl and STEP3_SUMMARY.json as C41_STEP3_V3.

GORU_STEP3_V3_COMPLETE_20260804
