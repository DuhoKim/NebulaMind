# Representation-boundary audit — C41 worker-Yui visual proposal v10

Verdict: `PASS_REVISION_PACKET_FOR_HWAO_REVIEW / APPROVED_INTEGRATION_BLOCKED`

## Boundary map

| Source representation | Allowed visual representation | Transformation | Guardrail |
|---|---|---|---|
| T1 candidate metadata and `found_by_channels` | Search-channel boxes and `20 + 92 = 112` partition | Exact categorical count in the frozen two-channel VizieR manifest | Do not treat search reach as eligibility/measurement or imply every public repository was exhaustively searched |
| T3 catalogue status records | `67 + 34 + 1 + 10 = 112` eligibility boxes plus `27 / 40` row-contribution status | Exact status and nonzero-row counts | Keep candidate/catalogue/row units explicit; do not imply all 67 contribute rows |
| T3 6,417-row `{table,muv,z}` sample | Redshift–reported-UV-like-magnitude point plane with source-table provenance | One source row to one point; color by exact stored-value `muv <= -20` predicate; diamonds outline the five non-dominant tables | No jitter, smoothing, interpolation, density estimate, unique-galaxy claim, or bandpass-homogenization implication |
| T3 slice predicate `10 <= z < 11.5` | Half-open x-axis support | Exact row filter | Both inclusive and exclusive bounds remain visible |
| Stored-value predicate `muv <= -20` | Dashed reported-magnitude cut and amber subset | Exact row filter yielding `176 / 453` | Stored-value qualifier, no-bandpass caveat, slice, and denominator travel together |
| Frozen published-LF roster status | Separate right-hand data-requirements block | Textual status only | Say missing extractable LF data; never encode as zero galaxies, zero published LFs, or a zero-valued point |
| Paper §6 reproducibility requirements | Five procedural checklist boxes | Direct conceptual grouping | Label procedure, not a new measurement |
| Paper-specific review record | Study-status line | Human clearance for Lab landing only | Do not imply journal peer review, independent validation, or a journal result |

## Encoded-content checks on v10 proposal frames

- Axis geometry is explicit: redshift `z` on x; catalogued UV-like absolute magnitude `(AB)` on y; astronomical magnitude direction places more negative/brighter values higher.
- The `z = 11.5` upper boundary is explicitly marked excluded.
- The raw row cloud remains visible when the bright subset and roster-status boundary are added.
- The proposal discloses that 27 of 67 counted catalogues contribute rows in the frozen slices, while 40 contribute zero.
- The proposal discloses that COSMOS2025 LePhare supplies 420 of 453 slice rows and 161 of 176 bright rows; the five other tables remain geometrically distinguishable.
- `453` is labeled as raw rows at any magnitude; `176 / 453` is labeled with the reported `M_UV`-like stored-value cut.
- The published-LF statement is spatially separate from the census point cloud.
- The persistent caveat denies completeness correction, density inference, and cross-catalogue merging.
- The persistent caveat also denies bandpass homogenization, preventing the dominant catalogue's `NUVMAG` field from being presented as a uniform 1500-angstrom measurement.
- The search states explicitly limit coverage to the frozen two-channel VizieR manifest and say other repositories were not exhaustively searched.
- The final frame distinguishes Lab-landing clearance from journal review, independent validation, and a journal result.
- Every frame is marked as a worker proposal, not an official candidate.
- Audience-facing citations name the paper/Lab, the dominant VizieR table, and five other tables rather than internal paths. Because the public paper does not expose the `453` denominator, the frames explicitly require an audience-reachable supplement before release; `AUDIENCE_DATA_SUPPLEMENT_PROPOSAL.json` remains local and unapproved.

## Known representation conflict outside the proposal

The public Flagship Studies component still has generic status copy saying no flagship has human clearance and displays `not accepted`, while the paper-specific review loop/history records Duho's clearance to land. Its metadata also says `30` disqualified while the frozen final census says `34`. Hwao must reconcile both conflicts before approved integration, public release, or website change.

## Non-transferable verdict

This audit authorizes transmission of a revision packet to Hwao only. It does not approve integration, an official MP4, narration, mux, public replacement, or publication. Hwao must independently verify and publish the audience supplement, reconcile public status/count conflicts, and repeat encoded-frame, audio-stream, contact-sheet, critical-frame, paper-naive, and adversarial QA on any official candidate.
