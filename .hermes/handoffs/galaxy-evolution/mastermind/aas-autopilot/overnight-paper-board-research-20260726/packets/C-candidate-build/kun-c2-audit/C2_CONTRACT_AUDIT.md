# C2 Mechanical Contract Audit

AI_DRAFT_NOT_HUMAN_GOLD

Marker: OVERNIGHT_PAPER_BOARD_PACKET_C2_KUN_AUDIT_V1

Read-only audit. No candidate edit, source edit, recompile, runner invocation, data pull, public write, DB/wiki write, git action, cron/browser/account/deploy action, or payment/PAYG route occurred.

## Summary

Overall result: PASS.

No FAIL discrepancies found. The actual C2 files support Lana's material receipt claims and Tori/Hwao validation claims checked here.

## Source Stability

PASS. Baseline SHA-256 verification for the allowed source files returned OK:

- `gated-e2e-demo/draft.tex`
- `gated-e2e-demo.json`
- `gated-e2e-demo/result.png`

## 1. Source Diff

PASS.

Command: unified `diff -u` from source `gated-e2e-demo/draft.tex` to C2 `candidate.tex`.

Hunk count: exactly 3.

Hunk headers:

```text
@@ -1,3 +1,8 @@
@@ -7,7 +12,7 @@
@@ -15,6 +20,12 @@
```

Hunk nature:

| hunk | finding |
|---|---|
| Header comments | PASS. Adds five `%` comment lines before `\documentclass`, including `AI_DRAFT_NOT_HUMAN_GOLD`, provenance, retained-reference note, and `NOT PUBLISHED`. These are LaTeX comments and do not render. |
| Introduction split | PASS. The only rendered Introduction change is the connective split: `, while ` becomes `. ` between `Qi2025` and `Torrey2019`, and `, and ` becomes `. ` between `Garcia2023` and `Guo2016`. Citation wording and all four citation clauses are retained. |
| Caveats append | PASS. Three caveat paragraphs are appended after the unchanged original Caveats paragraph. No original Caveats text was deleted or weakened. |

No additional or unexpected hunks were present.

## 2. Hash / Figure Identity

PASS.

| file | actual SHA-256 | expected / source identity | result |
|---|---|---|---|
| `candidate.tex` | `c615b2f39502bf4e15f54e8fba3818ca480c9fd162360044c804893a11bc00d9` | Expected `c615b2f39502bf4e15f54e8fba3818ca480c9fd162360044c804893a11bc00d9` | PASS |
| `candidate.pdf` | `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e` | Expected `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e` | PASS |
| C2 `result.png` | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` | Source `gated-e2e-demo/result.png` also `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` | PASS |

Additional observed PDF property: `candidate.pdf` is 82,670 bytes.

## 3. PDF-Text Extraction

PASS.

Extractor used: `/opt/homebrew/bin/pdftotext`, output to stdout only.

| required disclosure | rendered in PDF text | comment-only? | evidence |
|---|---|---|---|
| O/H-scale caveat | YES | NO | PDF text contains `O/H-scale caveat. A specific limitation applies...`; it states SDSS O/H scale is absent, no common O/H scale is established, no dex offset is invented/applied, comparability is unresolved, and apparent differences remain confounded until common calibration. |
| TENSION caveat | YES | NO | PDF text contains `Tension caveat. The source expected-value assessment for this comparison returns TENSION...`; it states TENSION is carried rather than upgraded. |
| Provenance caveat | YES | NO | PDF text contains `Provenance caveat. This is an AI-assembled candidate...`; it states forced `spec.force=true` lineage, `gated-e2e-demo`, `d8de519cb9c9`, queued/never compiled sibling draft, existing artifacts, isolated/unpublished. |
| `AI_DRAFT_NOT_HUMAN_GOLD` | YES | NO | PDF text contains `(AI_DRAFT_NOT_HUMAN_GOLD)` inside the rendered provenance caveat. |

The non-rendered header comment also contains `AI_DRAFT_NOT_HUMAN_GOLD`, but the required rendered disclosure is present independently in the PDF body.

## 4. Claim Surface

PASS.

Audit rule used: rendered scientific/numeric claims were checked against `gated-e2e-demo/draft.tex` and `gated-e2e-demo.json`; mandatory provenance/caveat contract claims were checked against source JSON plus Hwao Packet A/B decisions. No new numerical measurement or relation was introduced by the candidate.

### Numeric / Factual Surface

| candidate claim or token | location in candidate | supporting source / contract evidence | result |
|---|---|---|---|
| `TNG100`, `23,722`, `SDSS`, `120,000` | abstract and result | Present in source draft abstract/result and `gated-e2e-demo.json result.summary`. | PASS |
| `TNG uses SF-weighted gas metallicity to O/H (solar-scaled)` / solar O/H wording | abstract, data/method, result | Present in source draft abstract/data/result and source JSON summary. | PASS |
| `z=0` TNG-vs-SDSS gas-phase MZR | data/method and caveats | Present in source draft data/method/caveats and source JSON `spec.topic`. | PASS |
| `TNG50`, kpc-scales, star-formation rates, metallicities, stellar masses | Introduction `Qi2025` clause | Present in source Introduction and reference entry. | PASS |
| Torrey mass-metallicity evolution in IllustrisTNG | Introduction `Torrey2019` clause | Present in source Introduction and reference entry; split only isolates it. | PASS |
| Garcia gas-phase metallicity break radii in IllustrisTNG | Introduction `Garcia2023` clause | Present in source Introduction and reference entry; split only isolates it. | PASS |
| Guo redshift range `0.5` to `0.7` and stellar mass-gas-phase metallicity relation | Introduction and reference entry | Present in source Introduction and reference entry. | PASS |
| Figure caption `Mass-metallicity relation` | figure line | Figure line is unchanged from source. | PASS |
| Original limitations: automated/single-selection, lack of calibration, environmental/feedback caveat | original Caveats paragraph | Original Caveats paragraph is unchanged from source. | PASS |
| SDSS O/H calibration/scale absent; no common O/H scale; no dex offset; comparability unresolved | appended O/H caveat | Hwao Packet A mandates this caveat; source JSON/draft contain TNG solar O/H but no SDSS O/H calibration, and expected-value reason mentions scale differences. | PASS |
| `TENSION` expected-value assessment, not upgraded | appended Tension caveat | Source JSON `gates.expected_value.verdict` is `TENSION`; Hwao Packet A mandates carrying it honestly. | PASS |
| `z$\sim$0`, systematics/anchor-reconciliation, not standalone frontier result | appended Tension caveat | Hwao Packet A states this framing. It introduces no new numeric measurement. | PASS |
| `AI_DRAFT_NOT_HUMAN_GOLD`; not fresh production run; forced `spec.force=true`; `gated-e2e-demo` lineage; `d8de519cb9c9` queued/never compiled precursor; existing artifacts; isolated/unpublished | appended Provenance caveat | `gated-e2e-demo.json spec.force=true`; Hwao Packet A decision requires this provenance caveat and records the `d8de519cb9c9` precursor fact; Lana receipt records isolation/unpublished. | PASS |
| Reference years/bibcodes/titles/authors in the 5 entries | References | Reference block is textually identical to source draft; source JSON `lit_reflist` contains the same five entries semantically, with source TEX's exact ASCII `<=` preserved. | PASS |

Claim-surface result: no new scientific number, relation, or unsupported factual claim found.

## 5. Reference Integrity

PASS.

The reference-block diff from source draft to candidate is empty. All five entries are present and textually identical in `candidate.tex`:

- `Qi2025`
- `Torrey2019`
- `Garcia2023`
- `Guo2016`
- `LaraLopez2013`

`LaraLopez2013` was not dropped.

## 6. Receipt-Contract Concordance

PASS.

| Lana receipt material claim | evidence checked | result |
|---|---|---|
| C2 completion state `DONE` with compiled PDF | `candidate.pdf` exists; SHA matches receipt; compile note says rc=0 and success. | PASS |
| Source stability for `gated-e2e-demo` files | Baseline check returned OK for source draft, JSON, and result image. | PASS |
| `candidate.tex`, `candidate.pdf`, `result.png` hashes | Recomputed hashes match Lana receipt and Tori validation. | PASS |
| Figure byte-identical to source | Source and candidate `result.png` SHA are both `ed83a825...`. | PASS |
| Exactly 3-hunk diff | Unified diff has exactly three `@@` hunks. | PASS |
| Header comments non-rendered | Header additions are `%` comments; PDF text does not contain that header text, while rendered AI token appears in provenance caveat. | PASS |
| Introduction split only changes the two connectives | Diff shows only the one Introduction line changed, splitting the two compound citations into four single-citation sentences. | PASS |
| Append-only caveats after unchanged original Caveats paragraph | Diff shows original Caveats paragraph as context and three appended paragraphs after it. | PASS |
| Caveats applied and existing caveats not weakened | PDF text renders O/H-scale, Tension, and Provenance caveats; original Caveats paragraph unchanged. | PASS |
| Five references retained and textually preserved | Reference-block diff is empty and all five keys are present. | PASS |
| No new number, relation, or scientific claim introduced | Claim-surface table above found all rendered scientific/numeric claims traceable to source or Hwao-mandated contract evidence. | PASS |
| Compile rc=0 | `COMPILE_NOTE.md` records saved rc=0; `compile.log` shows Tectonic wrote `candidate.pdf`; only underfull warnings found. | PASS |
| No source edit, isolated/unpublished | Source hashes passed; candidate files are under Lana C2 root; no public/static-root evidence or source mutation observed during this read-only audit. | PASS |

## Final PASS/FAIL Table

| audit item | result |
|---|---|
| Source diff | PASS |
| Hash / figure identity | PASS |
| PDF-text extraction | PASS |
| Claim surface | PASS |
| Reference integrity | PASS |
| Receipt-contract concordance | PASS |

No FAIL discrepancies.

