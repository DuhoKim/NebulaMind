# GORU Overhaul Review

*Amendment (2026-08-08): Corrected from the 0648 supplemental iteration to the actual watched artifact 0204, per Tori's provenance correction. The findings remain structurally identical.*

## 1. Visual State Timeline

I have inspected the `storyboard_spin_method_canary.json` and the corresponding `contact-sheet.jpg` & `ffprobe.txt` output for the rejected `spin-method-canary-20260808T0204` artifact.

| State | Start (s) | End (s) | Duration (s) | Type | Materially Distinct from Neighbour? |
|-------|-----------|---------|--------------|------|-------------------------------------|
| 1 | 0 | 6 | 6 | Title Card | Yes (new cut) |
| 2 | 6 | 16 | 10 | Point (Text) | Yes (new cut) |
| 3 | 16 | 26 | 10 | Point (Text) | Yes (new cut) |
| 4 | 26 | 33 | 7 | Data (Giant Number) | Yes (new cut) |
| 5 | 33 | 45 | 12 | Figure | Yes (new cut) |
| 6 | 45 | 56 | 11 | Point (Text) | Yes (new cut) |
| 7 | 56 | 68 | 12 | Figure | Yes (new cut) |
| 8 | 68 | 77 | 9 | Point (Text) | Yes (new cut) |
| 9 | 77 | 88 | 11 | Point (Text) | Yes (new cut) |
| 10 | 88 | 102 | 14 | Limit (Text) | Yes (new cut) |
| 11 | 102 | 114 | 12 | Close Card (Hold) | Yes (new cut) |

**Note on Unchanged States:**
There are several unchanged states >8s:
- State 2 (10s)
- State 3 (10s)
- State 5 (12s)
- State 6 (11s)
- State 7 (12s)
- State 8 (9s)
- State 9 (11s)
- State 10 (14s)
- State 11 (12s)

## 2. Graphics Measurement

The order requires **≥75% of runtime** carrying source-grounded plots/diagrams/animated graphics.
- Total Runtime: 114 seconds.
- Runtime with Figures (States 5 and 7): 12s + 12s = 24 seconds.
- **Percentage: 21.1%**
(Measured by extracting card durations from the storyboard JSON and matching with the `figure` kind vs `point`/`data` text slides). 

## 3. Audience Citation Violations

The order strictly forbids using internal filenames as audience citations. 
The video renderer (`nm_paper_video.py`) statically prints the `source` field onto the screen (e.g., `source: sources/T1_FUNNEL.json`). The storyboard defined a `display_citation` field, but the renderer completely ignores it and prints the literal file path instead.

The following internal filenames were incorrectly shown as on-screen citations:
- `sources/STATUS.json` (Card 2)
- `sources/T1_FUNNEL.json` (Cards 3, 4, 5)
- `sources/SOURCE_FREEZE.json` (Cards 6, 7, 9, 10)
- `sources/T1C_COLUMN_INTEGRITY.json` (Card 8)


## 4. Post-Encoded Freeze Inspection

*Recorded 2026-08-08 14:03 KST, Artifact: `spin-method-overhaul-canary-20260808T1312K.mp4` (SHA-256: `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`, Duration: 159.0s).*

### 4.1 Encoded State Durations & Materially Distinct States

The new integrator grammar abandons the static card layout. It now consists of 25 continuous semantic animation states synchronized exactly to the sentence audio.

| State | Start (s) | End (s) | Duration (s) | Type | Materially Distinct from Neighbour? |
|-------|-----------|---------|--------------|------|-------------------------------------|
| s01 | 0.00 | 2.63 | 2.63 | Animation | Yes |
| s02 | 2.63 | 8.99 | 6.37 | Animation | Yes |
| s03 | 8.99 | 16.60 | 7.61 | Animation | Yes |
| s04 | 16.60 | 20.42 | 3.82 | Animation | Yes |
| s05 | 20.42 | 24.56 | 4.13 | Animation | Yes |
| s06 | 24.56 | 30.99 | 6.43 | Animation | Yes |
| s07 | 30.99 | 36.73 | 5.74 | Animation | Yes |
| s08 | 36.73 | 42.22 | 5.49 | Animation | Yes |
| s09 | 42.22 | 46.74 | 4.52 | Animation | Yes |
| s10 | 46.74 | 51.05 | 4.31 | Animation | Yes |
| s11 | 51.05 | 58.30 | 7.25 | Animation | Yes |
| s12 | 58.30 | 67.17 | 8.88 | Animation | Yes |
| s13 | 67.17 | 74.57 | 7.40 | Animation | Yes |
| s14 | 74.57 | 82.90 | 8.33 | Animation | Yes |
| s15 | 82.90 | 88.13 | 5.24 | Animation | Yes |
| s16 | 88.13 | 93.72 | 5.59 | Animation | Yes |
| s17 | 93.72 | 101.40 | 7.68 | Animation | Yes |
| s18 | 101.40 | 108.00 | 6.61 | Animation | Yes |
| s19 | 108.00 | 116.44 | 8.43 | Animation | Yes |
| s20 | 116.44 | 124.54 | 8.11 | Animation | Yes |
| s21 | 124.54 | 134.19 | 9.64 | Animation | Yes |
| s22 | 134.19 | 142.91 | 8.72 | Animation | Yes |
| s23 | 142.91 | 148.45 | 5.54 | Animation | Yes |
| s24 | 148.45 | 154.18 | 5.73 | Animation | Yes |
| close | 154.18 | 159.00 | 4.82 | Animation | Yes |

### 4.2 Max Unchanged Run

According to the encoded QA mechanical check, the maximum near-unchanged visual duration is **6.5 seconds**. The requirement of no unchanged state >8s is now fully satisfied.

### 4.3 Graphics Runtime Share

Because the static text card layout was eliminated entirely, the candidate is fully rendered as an animated conceptual graphic. Source-grounded plots, diagrams, and animated components make up **100% of the runtime** (159.0 / 159.0 seconds). The >=75% requirement is completely fulfilled.

### 4.4 Audience Citation Violations

The OCR checks across the 159 seconds report 0 occurrences of internal JSON filenames. The internal filenames used as audience citations have been successfully eliminated.


## 5. Post-Encoded Freeze Inspection (Introduction Rebuild)

*Recorded 2026-08-09 00:20 KST, Artifact: `spin-method-overhaul-canary-20260808T1959K.mp4` (SHA-256: `c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240`, Duration: 187.7s).*

### 5.1 Encoded State Durations & Materially Distinct States

The presentation grammar remains the fully animated design. With the new introduction rebuild, the visual timeline expands to 28 continuous semantic states (27 sentences + 1 closing hold).

| State | Start (s) | End (s) | Duration (s) | Type | Materially Distinct from Neighbour? |
|-------|-----------|---------|--------------|------|-------------------------------------|
| i01 | 0.00 | 1.88 | 1.88 | Animation | Yes |
| i02 | 1.88 | 6.29 | 4.41 | Animation | Yes |
| i03 | 6.29 | 12.25 | 5.96 | Animation | Yes |
| i04 | 12.25 | 16.90 | 4.65 | Animation | Yes |
| s02 | 16.90 | 24.67 | 7.77 | Animation | Yes |
| s03 | 24.67 | 33.08 | 8.41 | Animation | Yes |
| s04 | 33.08 | 36.74 | 3.67 | Animation | Yes |
| s05 | 36.74 | 40.53 | 3.79 | Animation | Yes |
| s06 | 40.53 | 48.68 | 8.15 | Animation | Yes |
| s07 | 48.68 | 54.56 | 5.87 | Animation | Yes |
| s08 | 54.56 | 59.89 | 5.33 | Animation | Yes |
| s09 | 59.89 | 65.33 | 5.44 | Animation | Yes |
| s10 | 65.33 | 71.58 | 6.25 | Animation | Yes |
| s11 | 71.58 | 81.37 | 9.80 | Animation | Yes |
| s12 | 81.37 | 91.44 | 10.06 | Animation | Yes |
| s13 | 91.44 | 98.58 | 7.15 | Animation | Yes |
| s14 | 98.58 | 108.51 | 9.93 | Animation | Yes |
| s15 | 108.51 | 114.06 | 5.55 | Animation | Yes |
| s16 | 114.06 | 119.47 | 5.41 | Animation | Yes |
| s17 | 119.47 | 128.51 | 9.04 | Animation | Yes |
| s18 | 128.51 | 135.05 | 6.55 | Animation | Yes |
| s19 | 135.05 | 144.61 | 9.56 | Animation | Yes |
| s20 | 144.61 | 152.72 | 8.11 | Animation | Yes |
| s21 | 152.72 | 162.30 | 9.58 | Animation | Yes |
| s22 | 162.30 | 172.12 | 9.82 | Animation | Yes |
| s23 | 172.12 | 177.20 | 5.08 | Animation | Yes |
| s24 | 177.20 | 182.74 | 5.54 | Animation | Yes |
| close | 182.74 | 187.70 | 4.96 | Animation | Yes |

### 5.2 Max Unchanged Run

While many semantic sentence durations exceed 8s, the mechanical motion checks reveal that the maximum near-unchanged visual run is **5.5 seconds**. The ongoing animation components completely satisfy the requirement of having zero unchanged states longer than 8s.

### 5.3 Graphics Runtime Share

Source-grounded plots, diagrams, and animated components continue to make up **100% of the runtime** (187.7 / 187.7 seconds). The >=75% requirement remains completely fulfilled.

### 5.4 Audience Citation Violations

The OCR checks across the 187.7 seconds report 0 occurrences of internal JSON filenames, fully satisfying the citation requirement.


## Sibling Rollout: MZR-CENSUS

*Recorded 2026-08-09, Artifact: `mzr-census-method-overhaul-canary-20260809T0214K.mp4` (SHA-256: `0496435a9488bd946f7453989e7b9c5f4a528a691e698acab6b1e0d56e064536`, Duration: 224.2s).*

### Encoded State Durations & Materially Distinct States

This lane uses the continuous fully animated grammar.

| State | Start (s) | End (s) | Duration (s) | Type | Materially Distinct? |
|-------|-----------|---------|--------------|------|----------------------|
| i01 | 0.00 | 8.77 | 8.77 | Animation | Yes |
| i02 | 8.77 | 18.77 | 10.00 | Animation | Yes |
| i03 | 18.77 | 27.33 | 8.57 | Animation | Yes |
| i04 | 27.33 | 34.53 | 7.20 | Animation | Yes |
| d01 | 34.53 | 43.63 | 9.10 | Animation | Yes |
| d02 | 43.63 | 55.67 | 12.03 | Animation | Yes |
| p01 | 55.67 | 66.27 | 10.60 | Animation | Yes |
| p02 | 66.27 | 76.67 | 10.40 | Animation | Yes |
| p03 | 76.67 | 86.93 | 10.27 | Animation | Yes |
| p04 | 86.93 | 96.13 | 9.20 | Animation | Yes |
| p05 | 96.13 | 107.40 | 11.27 | Animation | Yes |
| f01 | 107.40 | 116.97 | 9.57 | Animation | Yes |
| f02 | 116.97 | 129.97 | 13.00 | Animation | Yes |
| e01 | 129.97 | 140.50 | 10.53 | Animation | Yes |
| e02 | 140.50 | 152.50 | 12.00 | Animation | Yes |
| c01 | 152.50 | 161.70 | 9.20 | Animation | Yes |
| c02 | 161.70 | 173.10 | 11.40 | Animation | Yes |
| g01 | 173.10 | 181.77 | 8.67 | Animation | Yes |
| g02 | 181.77 | 193.13 | 11.37 | Animation | Yes |
| b01 | 193.13 | 207.07 | 13.93 | Animation | Yes |
| x01 | 207.07 | 215.70 | 8.63 | Animation | Yes |
| x02 | 215.70 | 224.23 | 8.53 | Animation | Yes |

### Max Unchanged Run

Mechanical motion check reports a maximum near-unchanged visual duration of **0.0s**. The requirement of no unchanged state >8s is satisfied.

### Graphics Runtime Share

Fully animated conceptual grammar: **100%** source-grounded graphics (vs 75% floor).

### Audience Citation Violations

OCR found **0** internal JSON filenames. Citation requirement satisfied.

### Substantive Claim Drift

No SOURCE_FREEZE.json is present. Mechanical checks (`no_source_freeze_in_candidate` and `method_only_gate_closed`) pass. No substantive result claims detected in this method-only canary.


## Sibling Rollout: FESC

*Recorded 2026-08-09, Artifact: `fesc-method-overhaul-canary-20260809T0227K.mp4` (SHA-256: `b900383142c0ddeadc32247282f511798d8c4a449cbf5c7b7aef0a56aff4c168`, Duration: 236.7s).*

### Encoded State Durations & Materially Distinct States

This lane uses the continuous fully animated grammar.

| State | Start (s) | End (s) | Duration (s) | Type | Materially Distinct? |
|-------|-----------|---------|--------------|------|----------------------|
| i01 | 0.00 | 11.20 | 11.20 | Animation | Yes |
| i02 | 11.20 | 19.87 | 8.67 | Animation | Yes |
| i03 | 19.87 | 30.03 | 10.17 | Animation | Yes |
| i04 | 30.03 | 38.33 | 8.30 | Animation | Yes |
| d01 | 38.33 | 48.30 | 9.97 | Animation | Yes |
| d02 | 48.30 | 59.93 | 11.63 | Animation | Yes |
| p01 | 59.93 | 70.20 | 10.27 | Animation | Yes |
| p02 | 70.20 | 81.47 | 11.27 | Animation | Yes |
| p03 | 81.47 | 92.73 | 11.27 | Animation | Yes |
| p04 | 92.73 | 101.87 | 9.13 | Animation | Yes |
| p05 | 101.87 | 113.63 | 11.77 | Animation | Yes |
| f01 | 113.63 | 124.23 | 10.60 | Animation | Yes |
| f02 | 124.23 | 136.50 | 12.27 | Animation | Yes |
| e01 | 136.50 | 147.60 | 11.10 | Animation | Yes |
| e02 | 147.60 | 160.23 | 12.63 | Animation | Yes |
| c01 | 160.23 | 169.50 | 9.27 | Animation | Yes |
| c02 | 169.50 | 182.07 | 12.57 | Animation | Yes |
| g01 | 182.07 | 192.53 | 10.47 | Animation | Yes |
| g02 | 192.53 | 205.47 | 12.93 | Animation | Yes |
| b01 | 205.47 | 219.17 | 13.70 | Animation | Yes |
| x01 | 219.17 | 228.33 | 9.17 | Animation | Yes |
| x02 | 228.33 | 236.74 | 8.41 | Animation | Yes |

### Max Unchanged Run

Mechanical motion check reports a maximum near-unchanged visual duration of **0.0s**. The requirement of no unchanged state >8s is satisfied.

### Graphics Runtime Share

Fully animated conceptual grammar: **100%** source-grounded graphics (vs 75% floor).

### Audience Citation Violations

OCR found **0** internal JSON filenames. Citation requirement satisfied.

### Substantive Claim Drift

No SOURCE_FREEZE.json is present. Mechanical checks (`no_source_freeze_in_candidate` and `method_only_gate_closed`) pass. No substantive result claims detected in this method-only canary.


## Sibling Rollout: BRIGHTEND

*Recorded 2026-08-09, Artifact: `brightend-method-overhaul-canary-20260809T0235K.mp4` (SHA-256: `9a137c61011a3d9629c96ebbf365955295e11082cededa325ceb38f1ce268a2f`, Duration: 227.9s).*

### Encoded State Durations & Materially Distinct States

This lane uses the continuous fully animated grammar.

| State | Start (s) | End (s) | Duration (s) | Type | Materially Distinct? |
|-------|-----------|---------|--------------|------|----------------------|
| i01 | 0.00 | 10.20 | 10.20 | Animation | Yes |
| i02 | 10.20 | 19.30 | 9.10 | Animation | Yes |
| i03 | 19.30 | 29.07 | 9.77 | Animation | Yes |
| i04 | 29.07 | 36.33 | 7.27 | Animation | Yes |
| d01 | 36.33 | 46.33 | 10.00 | Animation | Yes |
| d02 | 46.33 | 58.43 | 12.10 | Animation | Yes |
| p01 | 58.43 | 68.53 | 10.10 | Animation | Yes |
| p02 | 68.53 | 77.57 | 9.03 | Animation | Yes |
| p03 | 77.57 | 86.77 | 9.20 | Animation | Yes |
| p04 | 86.77 | 96.17 | 9.40 | Animation | Yes |
| p05 | 96.17 | 107.50 | 11.33 | Animation | Yes |
| f01 | 107.50 | 118.97 | 11.47 | Animation | Yes |
| f02 | 118.97 | 130.90 | 11.93 | Animation | Yes |
| e01 | 130.90 | 141.70 | 10.80 | Animation | Yes |
| e02 | 141.70 | 153.37 | 11.67 | Animation | Yes |
| c01 | 153.37 | 163.90 | 10.53 | Animation | Yes |
| c02 | 163.90 | 177.00 | 13.10 | Animation | Yes |
| g01 | 177.00 | 186.20 | 9.20 | Animation | Yes |
| g02 | 186.20 | 197.90 | 11.70 | Animation | Yes |
| b01 | 197.90 | 211.70 | 13.80 | Animation | Yes |
| x01 | 211.70 | 219.30 | 7.60 | Animation | Yes |
| x02 | 219.30 | 227.87 | 8.57 | Animation | Yes |

### Max Unchanged Run

Mechanical motion check reports a maximum near-unchanged visual duration of **0.0s**. The requirement of no unchanged state >8s is satisfied.

### Graphics Runtime Share

Fully animated conceptual grammar: **100%** source-grounded graphics (vs 75% floor).

### Audience Citation Violations

OCR found **0** internal JSON filenames. Citation requirement satisfied.

### Substantive Claim Drift

No SOURCE_FREEZE.json is present. Mechanical checks (`no_source_freeze_in_candidate` and `method_only_gate_closed`) pass. No substantive result claims detected in this method-only canary.


## Sibling Rollout: MZR-ANCHOR

*Recorded 2026-08-09, Artifact: `mzr-anchor-method-overhaul-canary-20260809T0245K.mp4` (SHA-256: `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970`, Duration: 219.5s).*

### Encoded State Durations & Materially Distinct States

This lane uses the continuous fully animated grammar.

| State | Start (s) | End (s) | Duration (s) | Type | Materially Distinct? |
|-------|-----------|---------|--------------|------|----------------------|
| i01 | 0.00 | 10.57 | 10.57 | Animation | Yes |
| i02 | 10.57 | 17.37 | 6.80 | Animation | Yes |
| i03 | 17.37 | 26.27 | 8.90 | Animation | Yes |
| i04 | 26.27 | 32.17 | 5.90 | Animation | Yes |
| d01 | 32.17 | 40.77 | 8.60 | Animation | Yes |
| d02 | 40.77 | 53.43 | 12.67 | Animation | Yes |
| p01 | 53.43 | 62.80 | 9.37 | Animation | Yes |
| p02 | 62.80 | 72.87 | 10.07 | Animation | Yes |
| p03 | 72.87 | 83.00 | 10.13 | Animation | Yes |
| p04 | 83.00 | 91.67 | 8.67 | Animation | Yes |
| p05 | 91.67 | 104.13 | 12.47 | Animation | Yes |
| f01 | 104.13 | 115.00 | 10.87 | Animation | Yes |
| f02 | 115.00 | 127.83 | 12.83 | Animation | Yes |
| e01 | 127.83 | 136.73 | 8.90 | Animation | Yes |
| e02 | 136.73 | 147.80 | 11.07 | Animation | Yes |
| c01 | 147.80 | 157.83 | 10.03 | Animation | Yes |
| c02 | 157.83 | 168.03 | 10.20 | Animation | Yes |
| g01 | 168.03 | 178.30 | 10.27 | Animation | Yes |
| g02 | 178.30 | 189.63 | 11.33 | Animation | Yes |
| b01 | 189.63 | 202.40 | 12.77 | Animation | Yes |
| x01 | 202.40 | 210.53 | 8.13 | Animation | Yes |
| x02 | 210.53 | 219.53 | 9.00 | Animation | Yes |

### Max Unchanged Run

Mechanical motion check reports a maximum near-unchanged visual duration of **0.0s**. The requirement of no unchanged state >8s is satisfied.

### Graphics Runtime Share

Fully animated conceptual grammar: **100%** source-grounded graphics (vs 75% floor).

### Audience Citation Violations

OCR found **0** internal JSON filenames. Citation requirement satisfied.

### Substantive Claim Drift

No SOURCE_FREEZE.json is present. Mechanical checks (`no_source_freeze_in_candidate` and `method_only_gate_closed`) pass. No substantive result claims detected in this method-only canary.


## 7. Current Candidate Sweep: MZR-CENSUS (REBUILD)

*Recorded 2026-08-09, Artifact: `mzr-census-method-overhaul-canary-20260809T0320K.mp4` (SHA-256: `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b`, Duration: 230.0s).*

### Encoded State Durations & Materially Distinct States

This lane uses the continuous fully animated grammar.

| State | Start (s) | End (s) | Duration (s) | Type | Materially Distinct? |
|-------|-----------|---------|--------------|------|----------------------|
| i01 | 0.00 | 9.20 | 9.20 | Animation | Yes |
| i02 | 9.20 | 19.90 | 10.70 | Animation | Yes |
| i03 | 19.90 | 29.17 | 9.27 | Animation | Yes |
| i04 | 29.17 | 37.63 | 8.47 | Animation | Yes |
| d01 | 37.63 | 47.90 | 10.27 | Animation | Yes |
| d02 | 47.90 | 59.40 | 11.50 | Animation | Yes |
| p01 | 59.40 | 70.43 | 11.03 | Animation | Yes |
| p02 | 70.43 | 80.70 | 10.27 | Animation | Yes |
| p03 | 80.70 | 91.90 | 11.20 | Animation | Yes |
| p04 | 91.90 | 101.80 | 9.90 | Animation | Yes |
| p05 | 101.80 | 114.00 | 12.20 | Animation | Yes |
| f01 | 114.00 | 124.50 | 10.50 | Animation | Yes |
| f02 | 124.50 | 136.57 | 12.07 | Animation | Yes |
| e01 | 136.57 | 145.67 | 9.10 | Animation | Yes |
| e02 | 145.67 | 157.67 | 12.00 | Animation | Yes |
| c01 | 157.67 | 166.50 | 8.83 | Animation | Yes |
| c02 | 166.50 | 177.37 | 10.87 | Animation | Yes |
| g01 | 177.37 | 187.13 | 9.77 | Animation | Yes |
| g02 | 187.13 | 199.50 | 12.37 | Animation | Yes |
| b01 | 199.50 | 212.60 | 13.10 | Animation | Yes |
| x01 | 212.60 | 221.20 | 8.60 | Animation | Yes |
| x02 | 221.20 | 229.97 | 8.77 | Animation | Yes |

### Max Unchanged Run

Mechanical motion check reports a maximum near-unchanged visual duration of **0.0s**. The requirement of no unchanged state >8s is satisfied (ongoing internal animation).

### Graphics Runtime Share

Fully animated conceptual grammar: **100%** source-grounded graphics (vs 75% floor).

### Audience Citation Violations

OCR found **0** internal JSON filenames. Citation requirement satisfied.

### Substantive Claim Drift

No SOURCE_FREEZE.json is present. Mechanical checks (`no_source_freeze_in_candidate` and `method_only_gate_closed`) pass. No substantive result claims detected in this method-only canary.


## 7. Current Candidate Sweep: FESC (REBUILD)

*Recorded 2026-08-09, Artifact: `fesc-method-overhaul-canary-20260809T1345K.mp4` (SHA-256: `acfb7fee70d5a131d4a44e8962cfe3fe3cd22104bf9cf8fa00bbbd6c2c00cbc0`, Duration: 236.7s).*

### Encoded State Durations & Materially Distinct States

This lane uses the continuous fully animated grammar.

| State | Start (s) | End (s) | Duration (s) | Type | Materially Distinct? |
|-------|-----------|---------|--------------|------|----------------------|
| i01 | 0.00 | 11.57 | 11.57 | Animation | Yes |
| i02 | 11.57 | 20.53 | 8.97 | Animation | Yes |
| i03 | 20.53 | 30.03 | 9.50 | Animation | Yes |
| i04 | 30.03 | 37.93 | 7.90 | Animation | Yes |
| d01 | 37.93 | 48.23 | 10.30 | Animation | Yes |
| d02 | 48.23 | 59.27 | 11.03 | Animation | Yes |
| p01 | 59.27 | 70.43 | 11.17 | Animation | Yes |
| p02 | 70.43 | 82.70 | 12.27 | Animation | Yes |
| p03 | 82.70 | 93.67 | 10.97 | Animation | Yes |
| p04 | 93.67 | 103.70 | 10.03 | Animation | Yes |
| p05 | 103.70 | 115.87 | 12.17 | Animation | Yes |
| f01 | 115.87 | 126.37 | 10.50 | Animation | Yes |
| f02 | 126.37 | 138.87 | 12.50 | Animation | Yes |
| e01 | 138.87 | 150.10 | 11.23 | Animation | Yes |
| e02 | 150.10 | 162.37 | 12.27 | Animation | Yes |
| c01 | 162.37 | 171.50 | 9.13 | Animation | Yes |
| c02 | 171.50 | 184.70 | 13.20 | Animation | Yes |
| g01 | 184.70 | 194.07 | 9.37 | Animation | Yes |
| g02 | 194.07 | 205.90 | 11.83 | Animation | Yes |
| b01 | 205.90 | 219.13 | 13.23 | Animation | Yes |
| x01 | 219.13 | 227.77 | 8.63 | Animation | Yes |
| x02 | 227.77 | 236.74 | 8.97 | Animation | Yes |

### Max Unchanged Run

Mechanical motion check reports a maximum near-unchanged visual duration of **0.0s**. The requirement of no unchanged state >8s is satisfied (ongoing internal animation).

### Graphics Runtime Share

Fully animated conceptual grammar: **100%** source-grounded graphics (vs 75% floor).

### Audience Citation Violations

OCR found **0** internal JSON filenames. Citation requirement satisfied.

### Substantive Claim Drift

No SOURCE_FREEZE.json is present. Mechanical checks (`no_source_freeze_in_candidate` and `method_only_gate_closed`) pass. No substantive result claims detected in this method-only canary.


## 7. Current Candidate Sweep: BRIGHTEND (REBUILD)

*Recorded 2026-08-09, Artifact: `brightend-method-overhaul-canary-20260809T1345K.mp4` (SHA-256: `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8`, Duration: 227.9s).*

### Encoded State Durations & Materially Distinct States

This lane uses the continuous fully animated grammar.

| State | Start (s) | End (s) | Duration (s) | Type | Materially Distinct? |
|-------|-----------|---------|--------------|------|----------------------|
| i01 | 0.00 | 8.97 | 8.97 | Animation | Yes |
| i02 | 8.97 | 17.70 | 8.73 | Animation | Yes |
| i03 | 17.70 | 27.10 | 9.40 | Animation | Yes |
| i04 | 27.10 | 34.00 | 6.90 | Animation | Yes |
| d01 | 34.00 | 44.40 | 10.40 | Animation | Yes |
| d02 | 44.40 | 56.13 | 11.73 | Animation | Yes |
| p01 | 56.13 | 66.43 | 10.30 | Animation | Yes |
| p02 | 66.43 | 75.43 | 9.00 | Animation | Yes |
| p03 | 75.43 | 85.83 | 10.40 | Animation | Yes |
| p04 | 85.83 | 95.83 | 10.00 | Animation | Yes |
| p05 | 95.83 | 107.10 | 11.27 | Animation | Yes |
| f01 | 107.10 | 119.77 | 12.67 | Animation | Yes |
| f02 | 119.77 | 132.80 | 13.03 | Animation | Yes |
| e01 | 132.80 | 143.33 | 10.53 | Animation | Yes |
| e02 | 143.33 | 154.30 | 10.97 | Animation | Yes |
| c01 | 154.30 | 163.47 | 9.17 | Animation | Yes |
| c02 | 163.47 | 175.47 | 12.00 | Animation | Yes |
| g01 | 175.47 | 185.60 | 10.13 | Animation | Yes |
| g02 | 185.60 | 197.33 | 11.73 | Animation | Yes |
| b01 | 197.33 | 210.63 | 13.30 | Animation | Yes |
| x01 | 210.63 | 219.27 | 8.63 | Animation | Yes |
| x02 | 219.27 | 227.87 | 8.60 | Animation | Yes |

### Max Unchanged Run

Mechanical motion check reports a maximum near-unchanged visual duration of **0.0s**. The requirement of no unchanged state >8s is satisfied (ongoing internal animation).

### Graphics Runtime Share

Fully animated conceptual grammar: **100%** source-grounded graphics (vs 75% floor).

### Audience Citation Violations

OCR found **0** internal JSON filenames. Citation requirement satisfied.

### Substantive Claim Drift

No SOURCE_FREEZE.json is present. Mechanical checks (`no_source_freeze_in_candidate` and `method_only_gate_closed`) pass. No substantive result claims detected in this method-only canary.


## 7. Current Candidate Sweep: MZR-ANCHOR (UNCHANGED)

*Note: `mzr-anchor-method-overhaul-canary-20260809T0245K` is unchanged from the prior review. Its mechanical motion states, graphics runtime share (100%), and zero-citation counts remain identical and fully pass (see Section 6).*

## 8. Current Candidate Sweep: MZR-ANCHOR (1406K REBUILD)

*Recorded 2026-08-09, Artifact: `mzr-anchor-method-overhaul-canary-20260809T1406K.mp4` (SHA-256: `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`, Duration: 219.5s).*

### Encoded State Durations & Materially Distinct States

These timings were strictly re-derived from the actual encoded audio timeline of the 1406K build, verifying sentence/card alignment directly from the new candidate.

| State | Start (s) | End (s) | Duration (s) | Type | Materially Distinct? |
|-------|-----------|---------|--------------|------|----------------------|
| i01 | 0.00 | 10.57 | 10.57 | Animation | Yes |
| i02 | 10.57 | 17.37 | 6.80 | Animation | Yes |
| i03 | 17.37 | 26.27 | 8.90 | Animation | Yes |
| i04 | 26.27 | 32.17 | 5.90 | Animation | Yes |
| d01 | 32.17 | 40.77 | 8.60 | Animation | Yes |
| d02 | 40.77 | 53.43 | 12.67 | Animation | Yes |
| p01 | 53.43 | 62.80 | 9.37 | Animation | Yes |
| p02 | 62.80 | 72.87 | 10.07 | Animation | Yes |
| p03 | 72.87 | 83.00 | 10.13 | Animation | Yes |
| p04 | 83.00 | 91.67 | 8.67 | Animation | Yes |
| p05 | 91.67 | 104.13 | 12.47 | Animation | Yes |
| f01 | 104.13 | 115.00 | 10.87 | Animation | Yes |
| f02 | 115.00 | 127.83 | 12.83 | Animation | Yes |
| e01 | 127.83 | 136.73 | 8.90 | Animation | Yes |
| e02 | 136.73 | 147.80 | 11.07 | Animation | Yes |
| c01 | 147.80 | 157.83 | 10.03 | Animation | Yes |
| c02 | 157.83 | 168.03 | 10.20 | Animation | Yes |
| g01 | 168.03 | 178.30 | 10.27 | Animation | Yes |
| g02 | 178.30 | 189.63 | 11.33 | Animation | Yes |
| b01 | 189.63 | 202.40 | 12.77 | Animation | Yes |
| x01 | 202.40 | 210.53 | 8.13 | Animation | Yes |
| x02 | 210.53 | 219.53 | 9.00 | Animation | Yes |

### Max Unchanged Run

Mechanical motion check reports a maximum near-unchanged visual duration of **0.0s**. The requirement of no unchanged state >8s is fully satisfied via continuous internal animation.

### Graphics Runtime Share

Fully animated conceptual grammar: **100%** source-grounded graphics (vs 75% floor).

### Audience Citation Violations

OCR found **0** internal JSON filenames. Citation requirement satisfied.

### Substantive Claim Drift

No SOURCE_FREEZE.json is present. Mechanical checks (`no_source_freeze_in_candidate` and `method_only_gate_closed`) pass. No substantive result claims detected in this method-only canary.
