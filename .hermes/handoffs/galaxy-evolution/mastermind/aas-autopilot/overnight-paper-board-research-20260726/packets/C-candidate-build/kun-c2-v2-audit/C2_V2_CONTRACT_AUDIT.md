# C2 V2 Mechanical Contract Audit

AI_DRAFT_NOT_HUMAN_GOLD

Marker: OVERNIGHT_PAPER_BOARD_PACKET_C2_KUN_V2_AUDIT_V1

Read-only audit. No V1, V2, source, candidate, PDF, public, DB/wiki, git, cron, browser, account, deploy, runner, recompile, or PAYG action occurred.

## Summary

Overall result: PASS.

No FAIL discrepancies found. V2 applies the F1-F4 fixes plus a non-rendered header-comment update, preserves V1/source/reference/caveat material required by the contract, and supports Lana's V2 receipt claims.

## 1. Hashes -- Source / V1 / V2

PASS.

| file | actual SHA-256 | expected | result |
|---|---|---|---|
| source `gated-e2e-demo/draft.tex` | `f1aeadd8ea43f2fd1e22e9686d23066fdf95e3d5c95937a42d8ddd076bc95a8a` | `f1aeadd8...` | PASS |
| source `gated-e2e-demo.json` | `46ddd75d5f0e5814e814333336d8e6d1b011382c46509012af2aea8cc20af5e2` | `46ddd75d...` | PASS |
| source `gated-e2e-demo/result.png` | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` | `ed83a825...` | PASS |
| V1 `candidate.tex` | `c615b2f39502bf4e15f54e8fba3818ca480c9fd162360044c804893a11bc00d9` | `c615b2f3...` | PASS |
| V1 `candidate.pdf` | `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e` | `eed8992d...` | PASS |
| V1 `result.png` | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` | `ed83a825...` | PASS |
| V2 `candidate.tex` | `bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6` | `bb77d38d...` | PASS |
| V2 `candidate.pdf` | `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d` | `ac59ac60...` | PASS |
| V2 `result.png` | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` | `ed83a825...` | PASS |
| V2 `COMPILE_NOTE.md` | `07456dc5685594211724ef187cd59619d003434f13bfa1a30629d28761f49f9e` | `07456dc5...` | PASS |
| V2 `V1_TO_V2_DIFF.md` | `7950cbf0c2c79afbb3ef5a6f88f0228a9d895fd01406700193cab3fb4de002da` | `7950cbf0...` | PASS |

Baseline `INPUT_SHA256.txt` check returned OK for the three allowed source files. Frozen V1 hashes match the required values, so no V1 hash stop condition was triggered.

## 2. V1-to-V2 Diff Limited To F1-F4 + Header

PASS.

Unified `diff -u` from V1 `candidate.tex` to V2 `candidate.tex` has one hunk:

```text
@@ -1,23 +1,28 @@
```

The changed areas are adjacent, so diff grouped them into a single hunk. The hunk inventory is:

| change | rendered? | contract mapping | result |
|---|---|---|---|
| Header comments updated from V1 C2 note to V2 F1-F4/versioned note | NO | allowed non-rendered `%` header-comment update | PASS |
| Abstract starts with `AI-assembled draft -- not submitted, not peer-reviewed (AI\_DRAFT\_NOT\_HUMAN\_GOLD).` | YES | F4 visible not-submitted / not-peer-reviewed tag | PASS |
| Abstract changes `bounded, reproducible, descriptive study` to `bounded, descriptive study` | YES | F2 removes unsubstantiated `reproducible` | PASS |
| Abstract appends `scale-limited, TENSION-flagged anchor comparison on un-reconciled O/H scales -- see Caveats` | YES | F3 abstract surface flag | PASS |
| Result replaces old interpretive sentence with `We present the two median relations... bounded by the unresolved O/H-scale systematic... not interpreted as physical here.` | YES | F1 softened Result sentence | PASS |
| Figure caption adds `Median relations on un-reconciled O/H scales; the TNG--SDSS comparison is scale-limited (see Caveats).` | YES | F3 caption note, caption text only | PASS |

No other rendered body, Introduction, Data/method, Caveats, or References lines changed in the V1-to-V2 diff.

## 3. Rendered PDF Strings

PASS.

Extractor: `/opt/homebrew/bin/pdftotext`, output to stdout only.

### Present In Rendered PDF

| required string / disclosure | evidence | result |
|---|---|---|
| F4 tag | PDF text contains `AI-assembled draft -- not submitted, not peer-reviewed (AI_DRAFT_NOT_HUMAN_GOLD).` | PASS |
| F3 abstract flag | PDF text contains `scale-limited, TENSION-flagged anchor comparison on un-reconciled O/H scales -- see Caveats.` | PASS |
| F3 caption note | PDF text contains `Figure 1. Mass-metallicity relation. Median relations on un-reconciled O/H scales; the TNG-SDSS comparison is scale-limited (see Caveats).` | PASS |
| F1 softened Result sentence | PDF text contains `We present the two median relations (TNG100 and SDSS); their direct comparison is bounded by the unresolved O/H-scale systematic (see Caveats) and is not interpreted as physical here.` | PASS |
| O/H-scale caveat | PDF text contains `O/H-scale caveat... no common O/H scale... no dex offset... cannot be interpreted as physical until a common calibration is established.` | PASS |
| TENSION caveat | PDF text contains `Tension caveat... returns TENSION... carry that verdict honestly rather than upgrading it to agreement.` | PASS |
| Provenance caveat | PDF text contains `Provenance caveat... AI-assembled candidate... forced (spec.force=true)... isolated and unpublished.` | PASS |
| rendered `AI_DRAFT_NOT_HUMAN_GOLD` | PDF text contains it in the Abstract tag and Provenance caveat. | PASS |

### Absent From Rendered PDF

| forbidden old string | evidence | result |
|---|---|---|
| `provides insights into the relationship` | Absent from extracted V2 PDF text. | PASS |
| `reproducible` | Absent from extracted V2 PDF text. It appears only in non-rendered header comments / change-log contexts, not in rendered PDF text. | PASS |

## 4. Reference Integrity

PASS.

The reference-block diff from source `gated-e2e-demo/draft.tex` to V2 `candidate.tex` is empty. The same block is also unchanged relative to V1 outside the F1-F4 hunk. All five reference entries are present and textually identical:

- `Qi2025`
- `Torrey2019`
- `Garcia2023`
- `Guo2016`
- `LaraLopez2013`

## 5. Citation Split

PASS.

The Introduction is preserved from V1 as four single-citation sentences:

- `[Qi2025] examined star formation rates, metallicities, and stellar masses on kpc-scales in TNG50.`
- `[Torrey2019] investigated the evolution of the mass-metallicity relation in IllustrisTNG.`
- `[Garcia2023] analyzed gas-phase metallicity break radii of star-forming galaxies in IllustrisTNG.`
- `[Guo2016] studied the stellar mass-gas-phase metallicity relation at redshifts between 0.5 and 0.7.`

## 6. Caveats

PASS.

| caveat requirement | evidence | result |
|---|---|---|
| Original source Caveats paragraph intact | V1-to-V2 diff leaves the original Caveats paragraph unchanged; source-to-V2 text matches for that paragraph. | PASS |
| O/H-scale caveat bounded wording retained | V2 contains the same V1 O/H-scale caveat, including no common O/H scale, no dex offset, unresolved comparability, and `cannot be interpreted as physical until a common calibration is established.` | PASS |
| TENSION caveat retained and not upgraded | V2 contains `returns TENSION` and `carry that verdict honestly rather than upgrading it to agreement.` | PASS |
| Provenance caveat retained | V2 contains forced `spec.force=true` lineage, `gated-e2e-demo`, `d8de519cb9c9`, queued/never compiled sibling, existing artifacts, isolated/unpublished. | PASS |
| None weakened | No caveat lines changed in the V1-to-V2 diff. | PASS |

## 7. Figure Byte-Identity

PASS.

V2 `result.png` SHA-256 is `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639`, identical to source `gated-e2e-demo/result.png`. F3 changed only the LaTeX caption text, not the figure image.

## 8. Compile Evidence

PASS.

`COMPILE_NOTE.md` records `rc = 0` and `SUCCESS -- candidate.pdf produced` with 84,831 bytes. `compile.log` records `Writing candidate.pdf`. `candidate.log` records `Output written on candidate.xdv (2 pages, 59100 bytes).`

Warnings found: three cosmetic `Underfull \hbox` warnings at `candidate.tex:34` and `candidate.tex:36`. No `Overfull`, `error:`, `fatal`, leading `!`, missing-package, or missing-font failures were found in the inspected log evidence.

## 9. V2 Receipt Concordance

PASS.

| Lana V2 receipt material claim | evidence checked | result |
|---|---|---|
| Completion state `DONE`; V2 built and compiled | V2 `candidate.pdf` exists; hash matches; compile note rc=0. | PASS |
| V1 frozen / source untouched | Source baseline OK; V1 hashes match frozen values. | PASS |
| V2 deliverable hashes | Recomputed V2 hashes match Lana receipt for `candidate.tex`, `candidate.pdf`, `result.png`, `COMPILE_NOTE.md`, and `V1_TO_V2_DIFF.md`. | PASS |
| F1 applied and old phrase absent | V1-to-V2 diff shows Result replacement; PDF text contains softened sentence; old phrase absent. | PASS |
| F2 applied and `reproducible` absent from rendered PDF | Abstract changed to `bounded, descriptive study`; `reproducible` absent from PDF text. | PASS |
| F3 abstract and caption flags applied | PDF text contains scale-limited/TENSION/anchor abstract flag and caption note; figure image hash unchanged. | PASS |
| F4 visible tag applied | PDF text contains not-submitted/not-peer-reviewed tag with rendered `AI_DRAFT_NOT_HUMAN_GOLD`. | PASS |
| References retained | Reference-block diff empty; all five keys present, including `LaraLopez2013`. | PASS |
| Introduction split retained | Four single-citation Introduction sentences present, unchanged from V1. | PASS |
| Caveats retained and not weakened | O/H-scale, TENSION, Provenance, and original caveat paragraph present; no caveat diff changes. | PASS |
| Figure byte-identical | V2/source figure SHA values match. | PASS |
| Isolated/unpublished; no publication | V2 files are under isolated Lana V2 root; Hwao public status remains `AWAITING_EXPLICIT_PUBLISH_APPROVAL`; this audit made no public writes. | PASS |

## Final PASS/FAIL Table

| audit item | result |
|---|---|
| Hashes -- source/V1/V2 | PASS |
| V1-to-V2 diff limited to F1-F4 + header | PASS |
| Rendered PDF strings | PASS |
| Reference integrity | PASS |
| Citation split | PASS |
| Caveats | PASS |
| Figure byte-identity | PASS |
| Compile evidence | PASS |
| V2 receipt concordance | PASS |

No FAIL discrepancies.

