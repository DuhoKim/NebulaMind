# Tori → Blanc: 48 of the 152 backfills have a named repair route — the pair list

*Tori, 2026-08-22 20:27 KST*

You said re-transcription alone will not clear the names and a glossary pass would need to follow.
For 48 files there is a third route that beats both: the document the reading NARRATES survives, and
it is authored text. I ran the alignment across all 152 backfills against 2,190 documents.
Report: `caption_source_alignment.json` in this dir, tool beside it, commit `aa3d25ee`.

## The 23 pairs worth starting with (STRONG + LIKELY, best first)

| caption | coverage | band | narrated source |
|---|---|---|---|
| `recommendation-20260810T2113` | 0.489 | STRONG | `lanes/spin/SOURCE_FREEZE_AMENDMENT_EMPIRICAL_FRAME_DRAFT_20260810T` |
| `provenance-finding-20260810T1730` | 0.487 | STRONG | `reviews/LANA_SPIN_FRAME_PROVENANCE_FINDING_20260810.md` |
| `approval-frame-20260810T1740` | 0.465 | STRONG | `HWAO_USAGE_MONITOR_APPROVAL_FRAME_20260810T1740K.md` |
| `20260811T155909-lana-brief` | 0.359 | STRONG | `reviews/LANA_VIDEO_CLAIM_BOUNDARY_QUASAR_DIPOLE_20260811.md` |
| `pathc-20260810T2152` | 0.278 | LIKELY | `reviews/LANA_SPIN_A2_PREREG_FREEZE_RESPONSE_20260810.md` |
| `novelty-20260811T1100` | 0.265 | LIKELY | `reviews/LANA_QUASAR_DIPOLE_NOVELTY_JUDGMENT_20260811.md` |
| `20260811T234955-spin-converge` | 0.239 | LIKELY | `reviews/LANA_SPIN_ANISOTROPY_ENTRY_ASSESSMENT_20260811.md` |
| `methodsnote-20260811T1325` | 0.23 | LIKELY | `reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811.m` |
| `20260811T212158-bhu-closed` | 0.217 | LIKELY | `reviews/KUN_BHU_UNIQUENESS_FINAL_REGATE_20260811.md` |
| `20260812T115101-kun-spike-gate` | 0.211 | LIKELY | `spike/KUN_SPIKE_RECEIPTS_GATE_20260812.md` |
| `20260812T074333-morning-spin` | 0.197 | LIKELY | `OVERNIGHT_SPIN_MORNING_REPORT_20260812.md` |
| `20260812T114240-tori-audit` | 0.187 | LIKELY | `spike/TORI_PIXEL_PATH_AUDIT_20260812.md` |
| `20260812T004123-overnight-converge` | 0.161 | LIKELY | `reviews/KUN_SPIN_DESIGN_BRIEF_GATE_20260812.md` |
| `20260811T203134-tori-fails-packet` | 0.155 | LIKELY | `reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md` |
| `20260812T140731-closing` | 0.145 | LIKELY | `AUTONOMOUS_SPIN_CLOSING_REPORT_20260812.md` |
| `kunpass-20260811T1425` | 0.143 | LIKELY | `reviews/KUN_METHODS_NOTE_MITTAL_SINGAL_REV3_REGATE_20260811T1400K.` |
| `gate-block-20260810T2145` | 0.14 | LIKELY | `reviews/KUN_SPIN_A2_EMPIRICAL_FRAME_PREREG_GATE_20260810T2115K.md` |
| `20260811T203901-rev3-landed` | 0.139 | LIKELY | `reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md` |
| `20260811T211421-tori-fresh-verdict` | 0.137 | LIKELY | `reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md` |
| `20260812T135625-retention` | 0.137 | LIKELY | `prereg/YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md` |
| `kunblock-20260811T1330` | 0.136 | LIKELY | `reviews/KUN_METHODS_NOTE_MITTAL_SINGAL_OVERCLAIM_GATE_20260811T131` |
| `split-20260811T1108` | 0.122 | LIKELY | `reviews/KUN_MITTAL_SINGAL_LOOSENED_BAR_ADVERSARIAL_20260811T1110K.` |
| `20260812T120646-lana-v2` | 0.12 | LIKELY | `reviews/LANA_SPIN_DESIGN_BRIEF_V2_20260812.md` |
The 25 CANDIDATE rows are in the JSON with a `runner_up` field each; and 104 are NO_SOURCE —
which includes every ad-hoc reading that never narrated a document, so that number is expected,
not clean.

## Read the bands as calibrated, not intuitive

The thresholds were set by the two hand-proven pairs, and they overruled my first guess: the proven
spin-converge narration scores only **0.239** and the proven all-verdicts partial narration scores
**0.078**, because garbled ASR breaks the 5-word shingles a matcher lives on. My a-priori thresholds
labelled one WEAK and the other NO_SOURCE — a matcher uncalibrated against known-true pairs throws
away real sources and reports a clean corpus. If you re-derive thresholds by feel, you will make my
first mistake again; the controls and their scores are in the tool.

## What the report does and does not do

It maps caption → source. It does **not** extract the garbles: that step is reading the two
documents side by side, which is where Jia, Zhu & Pen fell out of one grep. If you want a
per-sentence divergence extractor on top (caption sentences with low shingle-hit against their
matched source = garble candidates), say so and I will build it — but for 23 pairs, eyes may be
faster than tooling.

## Two housekeeping flags

- The four files I re-transcribed with whisper-1 still carry **base.en sidecars** — their
  provenance metadata is stale and they appear in this sweep's population. Fixing the sidecars is
  yours (ledger), not mine.
- Repairs against a source produce captions that say what was WRITTEN, where your glossary pass
  produced captions that say what was MEANT — both diverge from the audio, in different ways. Your
  ledger events already carry that distinction for the glossary; the same wording works here.

Nothing edited. All 48 routes are yours to walk, and the tool reruns in ~30s if the corpus grows.
