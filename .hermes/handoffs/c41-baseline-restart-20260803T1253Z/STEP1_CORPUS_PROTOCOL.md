# C41 Step 1 corpus protocol — rules frozen before title-level selection

Lane: `c41-baseline-restart-20260803T1253Z`
Protocol version: `C41_STEP1_V1`
Authorized gate: Duho, 2026-08-03, `APPROVE C41 STEP 1`
Coordinator: Hwao
Executor: Tori

## Gate boundary

This protocol produces a deterministic, ranked working corpus of at most 180 C41 records. It does
not authorize full-text acquisition, span extraction, claim-ledger construction, prose, product or
DB mutation, wiki/live publication, deployment/restart, or git writes.

The controlling question is the immutable `STEP0_FROZEN_QUESTION.md`, verified at mode 0444 and
SHA-256 `9ac5ca1f6321e2808eec3b9c2d38b8e616e0a9d774f4f277469c38fadbf789e1` before this protocol
was authored. The filter serves its three fixed axes:

1. formation efficiency: star-formation efficiency/regulation, burstiness, IMF, and the bright-end
   UV luminosity function;
2. chemical enrichment: gas metallicity, abundance patterns, enrichment history, and calibration
   comparability;
3. ionizing output: ionizing production and escape, source populations, and the reionization
   budget.

## Rules-before-titles receipt

The rules below were fixed from the frozen question, field schemas, source-code lexicons, and only
aggregate distributions. Before authoring these rules, Tori did not print, inspect, sort, or make a
decision from any individual candidate record or candidate title. Aggregate probes were allowed to
scan title/abstract text only to return counts for predeclared metadata classes; they emitted no
paper identity, title, abstract, author, or identifier.

Peek log: **no candidate-record peeks**. Incidental disclosure note: the coordinator's frozen plan,
a required input to this task, itself quotes one example paper title in its explanatory narrative.
That text was not opened from the corpus, was not used to add or remove any record, and created no
manual identifier/title rule.

## Frozen inputs and observed aggregate schema

The executable reads only the frozen question and these stated local inputs; it performs no network,
DB, model, or git operation. SHA-256 values observed before authoring:

- `cluster_labels_v2.json`: `3032b4796a9603b778003acd0e84b9b644dd2c27f6069fbf67720f200d798ef2`
- `corpus_ga_co_2009_2026.jsonl`: `e5a91e5f867837ec4fd075caa4b7da109816ef9a798df0b52db2e930eeeb9309`
- `delta/new_labels.json`: `e23d22d1ef7d5e222a11fbc73c052df43b23376f3acae5065b47029fd39899b3`
- `delta/new_papers.jsonl`: `34e8cef726a612acbf052474501f5ef006c4ada71d6390b58a75581b23bc30db`
- `dispersion_v2.json`: `8e1cacefe5c621f962042f24c1f76f94514a5694674ae096edf576009559e34a`
- `rank_frontiers_v3.py`: `07da96e071a5d641c696aeb977cd09839c28819d9c048c10c91f651f46bdbe60`
- `tools/nm_dispersion_v2.py`: `10edadd9cc55aff3014bc1752c9a90c0363dc2f6eab02ac41e169d9673cea474`

Aggregate observations, without individual title inspection:

- base labels: 120,676; base C41 members/metadata records: 1,296/1,296;
- July delta labels: 994; delta C41 members/metadata records: 21/21;
- combined input universe: 1,317 records;
- base years: 2009–2026; delta C41 records: all 2026;
- base C41 records all carry `ARTICLE`, `REFEREED`, and `EPRINT_OPENACCESS`; delta records are
  identified arXiv preprints;
- every C41 input record has non-empty title and abstract metadata;
- base citation-count median 46 (range 0–2,133); delta records have no citation-count field;
- `dispersion_v2.json` has 121 measurement rows in C41 across 85 unique base papers before scope
  filtering; measurement status is determined from its quantity-level verdict, not inferred from a
  title.

The 420 MB base JSONL is streamed. It is never loaded in full.

## Membership and identity rules

The selection universe is exactly:

- each base metadata row whose `bibcode` maps to integer cluster 41 in
  `cluster_labels_v2.json`; and
- each delta metadata row whose `arxiv_id` maps to integer cluster 41 in
  `delta/new_labels.json`.

Base identity is `bibcode:<bibcode>`. Delta identity is `arxiv:<arxiv_id-without-version>`. A record
outside C41 cannot enter by ranking. Missing/malformed required files, malformed JSON, or a mismatch
between C41 labels and C41 metadata causes the executable to stop rather than improvise. Duplicate
combined identities have the named exclusion rule `DUPLICATE_IDENTITY`; the first occurrence is
fixed by origin order (base, then delta) and source-file order.

## Text classes fixed before execution

`step1_filter.py` contains the exact case-insensitive regular expressions. They are metadata classes,
not title lists:

- axis lexicons implement the three question axes;
- high-z markers include explicit `z`/redshift values at or above 6 and fixed epoch phrases such as
  high-redshift/high-z, cosmic dawn, first/earliest galaxies, EoR, and reionization;
- calibration-anchor markers include calibration, direct electron-temperature, auroral,
  strong-line, and photoionization-model terms;
- the review class uses review/overview phrases plus recognized review-journal metadata;
- the LRD/AGN boundary class uses Little Red Dot/LRD, AGN/active-galactic-nucleus, and black-hole
  accretion terms;
- the instrument-method class requires strong instrument-design/performance/commissioning language;
- the selection-limit exception uses completeness, selection function/bias, sensitivity, detection
  or flux limit, contamination, and photometric-redshift terms;
- named out-of-scope topic markers cover cosmic-noon quenching, environment, and mergers-as-topic.

A broad axis hit is recorded for coverage. LRD/AGN and named out-of-scope topics must additionally
carry a strong axis hit: chemical and ionizing terms are strong; formation terms are strong when they
name efficiency/regulation, feedback, burstiness, IMF, UVLF, or the bright end rather than merely
saying “star formation.”

## Exclusion rules and priority order

Every excluded record is assigned exactly one first-firing named rule. `SELECTION_EXCLUDED.json`
publishes the rule text, count, and records grouped by this class.

1. `DUPLICATE_IDENTITY`: later occurrence of an already-seen normalized corpus identity.
2. `MALFORMED_REQUIRED_METADATA`: missing normalized identity or empty title/abstract.
3. `UNSUPPORTED_SOURCE_CLASS`: neither a refereed base article nor an identified delta arXiv
   preprint.
4. `LRD_AGN_OUTSIDE_THREE_AXES`: LRD/high-z AGN record without a strong hit on one of the three
   axes. This is the frozen question's LRD boundary clause. AGN-vs-stellar nature alone does not
   form a fourth axis.
5. `INSTRUMENT_OUTSIDE_SELECTION_LIMITS`: instrument-design/performance/commissioning record that
   does not also carry completeness/selection-limit metadata relevant to an axis.
6. `NAMED_TOPIC_OUTSIDE_THREE_AXES`: cosmic-noon quenching, environment, or mergers-as-topic without
   a strong three-axis hit.
7. `NO_THREE_AXIS_SIGNAL`: no formation-efficiency, chemical-enrichment, or ionizing-output metadata
   hit.
8. `NO_HIGH_Z_SIGNAL`: an axis-bearing record without a high-z marker. The sole exception is an
   explicitly tagged chemical-calibration anchor.
9. `REVIEW_CLASS_CAP`: review candidate encountered after 24 reviews have already been included in
   deterministic rank order. Twenty-four is 13.3% of the 180 ceiling: enough for a status backbone,
   never enough to crowd out primary-claim sources.
10. `CALIBRATION_ANCHOR_CAP`: non-high-z chemical-calibration anchor beyond the first eight such
    records in deterministic rank order.
    The cap ranks anchors against each other rather than against the whole pool, so seven
    priority-2-signal anchors were capped out while lower-ranked non-anchors remained in the sealed
    180.
11. `CAPACITY_BELOW_TOP_180`: otherwise eligible record remaining after 180 records are accepted.

There is no post-run hand edit, title veto, author/venue preference, or manual inclusion list.

## Contested-measurement-first ranking

Ranking is deterministic and lexicographic. Higher priority always comes first:

1. priority 4 — direct C41 measurement row in `dispersion_v2.json` whose relevant quantity verdict
   contains `contested`;
2. priority 3 — direct C41 measurement row whose relevant quantity verdict contains `mild`;
3. priority 2 — a strict disagreement hit using the exact `STRICT_TERMS` and physics-tension removal
   rule from `rank_frontiers_v3.py`;
4. priority 1 — a hit on a relevant quantity lexicon copied from the verified v2.2
   `nm_dispersion_v2.py` registry for metallicity/abundances, SFR/SFRD, UVLF, IMF, or f_esc;
5. priority 0 — no contested-measurement signal.

Within a priority, the fixed score is:

`0.75 * recency + 0.23 * log-citation + 0.02 * review_flag`

where `recency = clamp((year - 2009) / 17, 0, 1)` and
`log-citation = clamp(log1p(citation_count) / log1p(1000), 0, 1)`. Missing delta citations are zero,
not guessed. Remaining ties are broken by year descending, citation count descending, then normalized
identity ascending. The review flag is a small awareness bonus only; the hard 24-review cap governs
crowding.

The included list preserves final deterministic rank. Axis and source-class counts are diagnostics,
not title-driven quotas. The downstream 60/30 shrink ladder is not applied here.

## Outputs and reproducibility

Running `python3 step1_filter.py` from any directory writes, atomically and only in this lane:

- `SELECTION_INCLUDED.json`;
- `SELECTION_EXCLUDED.json`;
- `SELECTION_SHAS.txt` with standard `shasum -a 256`-compatible lines for the two selection JSON
  files.

Both JSON files record input SHA-256 values, rule version, summary counts, safety ledger, and the
rank/classification metadata needed for adversarial reproduction. Runtime is printed to stdout and
receipted in `TORI_STEP1_REPORT.md`; runtime is deliberately excluded from selection JSON so reruns
on unchanged inputs are byte-identical.

## Model-prediction sources outside C41

Model/simulation papers outside C41 are **not Step-1 corpus members** and cannot be injected into the
180. At Step 4 only, they may enter a separate claim-ledger role `prediction_source` when a
machine-checkable rule finds all of the following: (a) an explicit prediction for one of the three
axes at z >= 6; (b) an authoritative paper identity; (c) a named model/simulation or stated analytic
assumption set; (d) a predicted observable/quantity with redshift and population scope; and (e) an
explicit link to the C41 observational claim being confronted. Calibration/training overlap with the
observational chain must be ledgered as a scope/circularity limitation. This is an identification-rule
sketch only; Step 1 performs no outside-C41 search or acquisition.

## Safety ledger

- Network: none.
- DB/SQL: none.
- Models/Deep Research/credits: none.
- Product/wiki/live/deploy/restart: none.
- Git writes: none.
- Writes: only the authorized Step-1 lane directory; atomic temporaries use `_tmp_*` there.
