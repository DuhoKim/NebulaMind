# Overnight Video-Quality Decisions — V1

Timestamp: 2026-08-10T01:29:52+09:00  
Writer: Yui integrator, local-only quality lane

## Authority and custody

- Order: `HWAO_OVERNIGHT_VIDEO_QUALITY_20260810T0055K.md` (`4f10d11f…`).
- Spin V5 paperwork correction is already closed. `PACKET_MANIFEST_V5.json` is `9a554227…`; Tori's packet-only adjudication is `PASS_PROVENANCE_RECEIPT_CORRECTION` at `71af98bf…`. The spin MP4 is not to be re-encoded for that correction.
- Protected passing artifacts remain spin `4d230cc0…`, FESC `01a4249b…`, Brightend `c772e643…`, MZR-anchor `c892f3fa…`, and MZR-census `d6014ac0…`. Five cockpit copies remain untouched.
- The four-lane why-study rollout remains held for Duho's own spin watch. Nothing in this track substitutes a crew review for that watch.

## Finding authority

- Goru V1 remains blocked by Tori and is not used.
- Goru V2 report: `d6d1fb4e…`; V2 ledger: `fe6b73ea…`.
- Kun report: `cd3195bc…`.
- Independent recomputation of V2's rows yields 27 cards where `dwell_seconds < measured_visible_word_count × 60 / 200`, split `3 + 4 + 5 + 5 + 10`, not the report prose's stated aggregate of 36. The aggregate is therefore held as a self-description defect. Exact per-card ledger measurements remain reproducible leads, and every candidate must run a fresh candidate-local reading-time audit rather than inherit either aggregate.
- Goru's V2 `section_count` measures underlying timeline labels, not the six-stage rail the viewer sees. It does not justify changing a rail by itself.

## Series decisions

1. **Header grammar:** the correct series grammar is `NEBULAMIND · <LANE-SPECIFIC METHOD>` at left and an explicit no-result banner at right. The right banner is `METHOD DESIGN · NO MEASURED VALUE` for method states. Spin's opening may truthfully use `WHY-STUDY QUESTION · NO ANSWER SELECTED` while its motivation is on screen, returning to the common method banner afterward. This is a semantic exception, not style drift.
2. **Rail:** six displayed stages are the series standard. The shared sibling rail is `MOTIVATION / DISCRIMINANT / SOURCE / ESTIMATOR / CONTROLS / SCIENCE`; spin's six displayed stages are a truthful mapping for its why-study seam. Underlying timeline section counts may differ and are not viewer-facing taxonomy. Do not force eleven spin labels onto siblings or nine sibling implementation labels onto spin.
3. **Colour semantics:** cyan = active focus and flow; blue/purple = paired alternatives; amber = gate, caveat, or withheld state; green = eligible/known-safe state; red = not reportable/blocked. These meanings, rather than identical decorative colour placement, are authoritative.
4. **Card grammar:** one card, one cognitive job. Headline states the move; central visual carries structure; card-local labels carry the evidence categories; burned-in narration caption may not duplicate a dense boundary card without a card-first reading beat.
5. **Boundary/end grammar:** the boundary must show `known / held / next gate` before the closing payoff. End cards return to the opening question, name the discriminating method, and state the withheld-result boundary. Lane-specific nouns remain necessary.
6. **Fonts and laptop legibility:** preserve Avenir Next/Menlo and the existing 1080p layout. Minimum body labels are 20 px only for low-priority rail/citation text; scientific card body and captions target 22–31 px. No downscaling below current minima is permitted to solve overflow; split or lengthen instead.

## Audio and pacing policy for new candidates

- Integrated loudness target: `-20.5 LUFS`.
- Loudness range target: `7 LU`; acceptable measured program range `5–8 LU`.
- True-peak ceiling: `-2.0 dBTP`; encode target `-2.3 dBTP`.
- Narration source sentences remain byte-identical. Reuse existing Alloy 1.18 sentence clips; do not resynthesize.
- Routine pauses: 0.75 s inside a section and 1.4 s at a section boundary. A longer hold is permitted only when a candidate-local reading-time rule or an explicitly named boundary card-first beat requires it.
- Reading-time floor: card-local visible words at 200 WPM plus 0.10 s guard. Recompute on the final spec. Do not trust inherited aggregate counts.
- Boundary split-attention remedy: reveal the full boundary card during the last 3.5 s of the preceding justified section pause with no narration caption; then preserve the complete spoken boundary and its exact subtitle. This is a presentation split, not text deletion.
- Motion must encode reveal, comparison, eligibility flow, stage position, or gate state. Existing low-amplitude background motion may remain only as continuity; it is not evidence of meaningful motion by itself.

## Tonight's implementation order

1. Brightend first because its `i04` deficit and boundary split-attention defect are largest and independently specific.
2. FESC, MZR-anchor, then MZR-census serially under the same quality profile.
3. Spin last, as a separate new candidate only. The protected `4d230cc0…` candidate stays the object Duho was asked to watch; no overnight artifact receives `accepted_by_duho`.

Every byte-changing candidate receives a fresh exact-hash QA/review packet. No new candidate reaches upload, public/frontend, cockpit, `published.json`, DB, deploy, Git, provider/config, billing, or acceptance.
