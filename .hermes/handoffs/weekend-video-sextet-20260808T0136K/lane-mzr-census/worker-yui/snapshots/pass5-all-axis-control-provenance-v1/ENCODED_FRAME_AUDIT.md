# Encoded-frame scientific-presentation audit — isolated deepening pass 5

Audit timestamp: 2026-08-08T04:13:35+09:00

## Exact target and method

- Read-only candidate: `/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4`
- Candidate SHA-256: `0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d`
- Unversioned narrated alias is byte-identical to the versioned candidate. No newer narrated MZR cut was found.
- Stream: H.264 1920×1080 at 30 fps plus AAC mono 24 kHz; duration 128.4 seconds; 13,989,937 bytes.
- Fresh sample: 32 encoded frames at `1 + 4n` seconds for `n=0..31`, not the pass-3 `4n` or pass-4 `2 + 4n` sample.
- Contact sheet: `contact_sheet_32frames_offset1.jpg`, SHA-256 `278a6c6f76c0e7c8977cff0aa91bd7c044f4f4c2c64c92bdad1abc3babc8459a`.
- Frame manifest: `FRAME_HASHES.json`, SHA-256 `092b168b8e47921fe41f0ced29c1717c05d12682d4866f0e12a4430e68c02974`; 32/32 frame hashes pinned.
- Full-stream decode completed with no ffmpeg error. Audio meaning was not inferred or audited.

## Verdict

`FAIL_FOR_SCIENTIFIC_REPRESENTATION_ALL_AXIS_SEARCH_SCOPE_ASYMMETRIC_T2_CONTROL_PROVENANCE_AND_PRIOR_BOUNDARIES`

This is a fresh audit of the unchanged failed candidate. It does not clear, replace, or modify that candidate.

## Fresh pass-5 findings

### 1. All three target concepts are prematurely adjudicated at the opening

At 5 seconds the encoded opening says the census is of catalogues “carrying gas-phase metallicity, stellar mass and redshift together.” T1 is explicitly an enumeration stage with no eligibility ruling; it records metadata reach on abundance, mass, and redshift axes. The frozen T2 contract shows that all three axes can contain non-target quantities: abundance can be a line-name collision or stellar metallicity, mass can be black-hole/cluster/model mass, and redshift can be a coordinate, composition symbol, simulation snapshot, or gravitational redshift.

Pass 4 corrected abundance and redshift target-versus-search-axis wording in the proposal, but retained the unqualified audience term `stellar-mass`. Pass 5 therefore identifies the remaining symmetry defect: before T2, all three should be described as `abundance-search`, `mass-search`, and `redshift-search` metadata axes. None is an adjudicated physical measurement at T1.

### 2. The encoded T2 design provenance is one-sided

At approximately 85–97 seconds, the card reports seven gate rounds and twelve decoys, but does not report the three precision anchors. It does not label the numbers as T2 contract-design controls, and it does not visibly distinguish them from eligibility application. The frozen record is balanced and explicit: `12 decoys + 3 anchors`; all fifteen test the criteria, and are not themselves the eligibility criteria or results.

The omission creates two risks:

- the audience can read the decoy count as the complete control design even though three must-retain anchors are part of the same frozen test;
- the audience can mistake successful contract-design review for application of T2 to the 157 candidates.

Safe correction: either omit design-control counts or show the complete, stage-labeled statement `T2 CONTRACT DESIGN · 12 DECOYS + 3 ANCHORS · NOT ELIGIBILITY RESULTS`, while retaining `APPLICATION TO ALL 157 NOT COMPLETED`.

### 3. Derived-count provenance remains non-public

The encoded 157 and 62 cards cite internal filenames/paths, and the close only says every number came from a recorded artifact. That is custody evidence, not an audience-reachable denominator/method supplement. Publication remains closed, so this does not create a new scientific claim; it is an exact release blocker. Before any public release, the integrator must provide an audience-reachable methods/count ledger for internally derived counts. An internal named-run label alone is insufficient for publication.

## Reconfirmed encoded blockers

- The opening and 157 card imply physical-quantity presence rather than metadata-search reach.
- The metallicity/redshift spread is not a census output and visually implies the measurement the census has not made.
- `178 − 21 = 157`, the `19 redshift / 2 abundance` drop split, and modifier reasons are not presented as a graphics-first conservation flow.
- The 62 description-regex matches are promoted to “explicit gas-phase evidence” and shown as a subset bar rather than vocabulary presence only; all 157 still require T2.
- The seven recall members and three controls lack a persistent `T1 RETRIEVAL-INSTRUMENT CHECK` label and `PRECISION NOT CERTIFIED` state.
- The four recorded redshift-axis examples are collapsed rather than separated into `SYMBOL / MEANING COLLISION` versus `TARGET-DOMAIN MISMATCH`, and are not labeled `RECORDED CHARACTERIZATION · NOT T2 RULINGS`.
- The T2 card omits `APPLICATION NOT COMPLETED` and `NO ELIGIBLE-TABLE COUNT`.
- The close does not separate reportable T1 facts from pending T2 application and does not state that no metallicity/MZR measurement exists.
- Long prose holds and section cards dominate; key quantitative/status boundaries are absent or too briefly visualized.

## Evidence-bounded correction decision

A safe pass-5 storyboard correction is justified without changing the already passing static v7 overview:

1. qualify every pre-eligibility axis symmetrically as a search axis, changing `stellar-mass` to `mass-search` wherever the audience could read a T1 physical-quantity adjudication;
2. if T2 design provenance is shown, require the complete `12 decoys + 3 anchors` and label it contract-design controls, not eligibility application;
3. make an audience-reachable methods/count ledger a publication precondition for internally derived denominators.

No count, table ruling, eligible-table number, metallicity/MZR measurement, or new scientific result is added.