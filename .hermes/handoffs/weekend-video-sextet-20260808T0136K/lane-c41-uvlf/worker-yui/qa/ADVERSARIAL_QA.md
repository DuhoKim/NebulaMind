# Adversarial scientific and representation QA — C41 worker-Yui proposal

Verdict: `INDEPENDENT_V5_FAIL → V10 LOCAL DELTA PASS → REVISION PACKET MAY GO TO HWAO / APPROVED INTEGRATION BLOCKED`

Scope: worker evidence/visual/storyboard proposal only. No encoded candidate, audio, public replacement, or publication verdict.

## Independent attack pass

A read-only delegated reviewer (`deleg_1abe3d79`, task 1) attacked the immutable v5 counts, units, source boundaries, plotted geometry, bandpass semantics, status language, and visible citations. The reviewer independently replayed the T1/T3 artifacts and failed v5 for approved integration. Worker-Yui independently rechecked each finding against the same frozen hashes and reconciled the findings into v10. The independent reviewer did not inspect v10; the v10 disposition below is a local delta verification and does not clear approved integration.

## Findings and correction receipts

### 1. Counted does not mean row-contributing

- Frozen result: 67 catalogue records are `counted`.
- Only 27 contribute rows in the frozen slices; 40 contribute zero.
- Risk in v5: `67 → 6,417` could imply that all 67 contribute evidence rows.
- Correction in v10: state 3 explicitly displays `27 contribute / 40 contribute zero`, labels the 34/1/10 units as candidate tables, and narration carries the same distinction.
- Disposition: `PASS`.

### 2. The target slice is dominated by one source table

- Frozen row replay: `10 <= z < 11.5` contains 453 rows from six tables.
- `J/A+A/704/A339/lephare` contributes 420/453 rows (92.72%).
- It contributes 161/176 rows satisfying the stored-value `muv <= -20` cut (91.48%).
- Risk in v5: one undifferentiated cloud could look like broad independent multi-survey support.
- Correction in v10: circles versus diamonds encode source-table provenance; subtitles state `420 / 453`, `161 / 176`, and `33 rows from five other tables`; the dominant VizieR table identifier is displayed.
- Disposition: `PASS`.

### 3. Stored magnitude fields are not bandpass-homogenized

- The dominant source uses the catalogue field `NUVMAG`; the frozen T3 record carries a rest-NUV/band-mismatch caveat.
- Risk in v6: the axis title `rest-UV M_UV` could be read as one homogeneous 1500-angstrom measurement.
- Correction in v10: the axis says `catalogued UV-like absolute magnitude (AB)`; the threshold is called a reported-magnitude cut; a persistent caveat denies bandpass homogenization; the narration says the catalogued bands are not homogenized to a common rest wavelength.
- Disposition: `PASS`.

### 4. `176` must retain threshold, slice, and denominator

- Frozen replay: 453 rows satisfy the half-open slice; 176 satisfy the stored-value cut at -20.
- Correction retained in v10: `10 <= z < 11.5`, an explicit `z = 11.5 excluded` marker, the reported-magnitude cut, `176 / 453`, and the raw-row label remain on the same state.
- Disposition: `PASS`.

### 5. Census rows are not a luminosity function

- The point cloud is one point per frozen `{table,muv,z}` row with no jitter or smoothing.
- v10 persistently denies completeness correction, density inference, bandpass homogenization, and catalogue merging.
- The published-LF roster status is a separate text plane, not an empty/zero-valued plot.
- Disposition: `PASS`.

### 6. Status and release language

- Paper-specific review/history records human clearance for Lab landing.
- Generic Flagship Studies copy still says no study has human clearance and none is accepted; its metadata says `30` disqualified while the frozen census says `34`.
- v10 adds the allowed paper-specific line: human-cleared for Lab landing, but not journal-refereed, independently validated, or a journal result.
- Worker decision: the science is reportable in a local revision packet with strict caveats; approved integration and public replacement/status claims remain blocked pending Hwao reconciliation.
- Disposition: `PASS_LOCAL_REVISION_PACKET / BLOCK_APPROVED_INTEGRATION_AND_PUBLIC_RELEASE`.

### 7. Display citation support for `453`

- The independent reviewer correctly found that the public paper exposes threshold totals but not the `453` all-magnitude denominator or row-level geometry.
- v10 displays the dominant VizieR identifier and explicitly says an audience-reachable supplement is required before release.
- `AUDIENCE_DATA_SUPPLEMENT_PROPOSAL.json` records all six table identifiers, source-native columns, slice/cut counts, and the dominant rest-NUV mismatch, but remains local and unpublished.
- Disposition: `BLOCK_APPROVED_INTEGRATION_UNTIL_HWAO_INDEPENDENTLY_VERIFIES_AND_PUBLISHES_AUDIENCE_REACHABLE_SUPPLEMENT`.

### 8. Search-universe scope

- The independent reviewer found that `the public archive` and `hidden majority` overread the frozen search design.
- v10 scopes the opening and narration to the frozen two-channel VizieR manifest and states that other repositories were not exhaustively searched.
- Disposition: `PASS_LOCAL_DELTA`.

## Final adversarial boundary

v10 may be transmitted to Hwao as a revision packet after reconciliation of the delayed reviews. It is not independently cleared for approved integration. Hwao must verify/publish the audience supplement, reconcile the public status and `30`/`34` count conflicts, and repeat final adversarial QA on the exact integration snapshot. C41 remains behind the C31 canary gate; no official candidate, TTS, or publication is authorized.
