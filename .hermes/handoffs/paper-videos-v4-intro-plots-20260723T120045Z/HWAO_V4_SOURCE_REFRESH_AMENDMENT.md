# HWAO AMENDMENT — V4 source refresh (response to Tori verification)

Author: Hwao (coordinator) · Written: 2026-07-23 ~14:10 KST (05:10Z)
Input read this turn: `TORI_SOURCE_VERIFICATION.md` (verdict `PASS_WITH_MANDATORY_AMENDMENT`) — no other tools or searches were run.
This amendment modifies `HWAO_V4_INTRO_PLOTS_DIRECTION.md`; it does not replace it. All hard exclusions remain in force: no media, no public/YouTube/visibility change, no website/DB/runtime/deploy/restart, no git, no V3-artifact mutation.

## Ruling on each verifier correction

**T1 — Renderer root cause (cover page hard-wired into scene 1): ACCEPT.**
Independently matches my own §0 finding (`build_paper_videos_v2.py:274`, reused by V3 layouts). No change needed; the V4 grammar already removes it.

**T2 — Four of five live PDFs no longer match the V3 freeze; two changes substantive: ACCEPT, with receipt condition.**
Reason: Tori's SHA table is exact and falsifiable, and the two content diffs cited (scaling-relations now bounding the sub-z≈6 SFMS elevation as consistent with pure selection; massive-abundance moving to like-for-like total-mass footing with factor 2.04 / 0.20 dex / 0.46–0.55 dex committed budget) are precisely the kind of claim-level drift that would make V4 narrate superseded numbers. I could not re-verify the downloads this turn (tools prohibited); acceptance is therefore conditional on the G0 freeze below reproducing Tori's current-live hashes. If G0's hashes differ from Tori's table, the source is still moving — stop and re-verify before anything else.
Consequences I adopt:
- Every quantitative claim in my direction that was anchored to the old freeze (including the z9 −0.47/−0.69±0.03/−0.65/Isobe numbers and the tng "~0.3 dex low" line) is now **provisional until re-anchored to the new freeze**. z9's PDF hash changed too; its numbers may survive, but they must be re-confirmed, not assumed.
- Contract §1.4's "frozen figure/data source" now means the **new V4 freeze**, not the V2/V3 one. The V2/V3 freeze stays untouched as the record of what was published.
- Flag for Duho (decision, not action): the live public V3 videos narrate at least one superseded quantity (massive-abundance 2.7/0.28 dex vs current 2.04/0.20 dex). Whether to annotate, replace, or leave V3 is a separate user gate; nothing here touches V3.

**T3 — Reordered next gates (freeze current → extract → claim-diff → rewrite narration → then plot inventory): ACCEPT.**
Reason: my G1 (figure inventory against the old freeze) would have inventoried stale figures; inventory work before a stable source contract is wasted or, worse, quietly wrong. The verifier's order is strictly safer and I adopt it verbatim (gate table below).

**T4 — Plot-map corrections: ACCEPT ALL FIVE.**
- scaling-relations: both Fig 1 (JWST points vs local SFMS/MZR) and Fig 2 (offsets vs z) inventoried; allowed claim must carry the **no-SFMS-evolution-below-z≈6 / consistent-with-selection boundary**. My map's claim row is superseded.
- massive-abundance: **my axes row was wrong** — Fig 1 x-axis is redshift, y-axis cumulative number density above the fixed mass threshold; claim numbers become 2.04 / 0.20 dex. I had flagged the caption as truncated/unverified; the verifier resolved it against me, correctly.
- z9-metallicity: Fig 1 = mass–metallicity plane confirmed (my row stands, numbers pending re-anchor per T2).
- tng-validation: Fig 1 relation-vs-mass, Fig 2 offsets-vs-redshift confirmed (my rows stand, numbers pending re-anchor).
- mzr-framework: no paper figure; source-quoted procedure diagram explicitly labeled non-data, unless the new-freeze inventory finds a legitimate figure/table — identical to my direction, now conditioned on the new freeze.

**T5 — Safe state: ACKNOWLEDGED.** Matches this lane's record; nothing rendered or mutated.

## Amended gate order (supersedes §6 of the direction)

- **G0 — Current-source freeze (EXACT NEXT GATE — Tori, bounded):** download the five canonical `source_url` PDFs into **this v4 lane** (`sources-v4/`), record `V4_SOURCE_FREEZE.json` with per-file sha256/bytes/url/UTC time, and extract per-paper text (`.md`) and figure inventory (figure count, page, caption, pixel size). Acceptance: hashes match Tori's current-live table exactly (any mismatch ⇒ stop, report drift, no downstream work); V2/V3 freeze files untouched. Scope: network GETs of the five public PDFs + writes inside this lane only — nothing else.
- **G1 — Claim-level diff (Goru mechanical diff; Lana semantic ruling):** current manuscripts vs V3 narration/cards/captions ⇒ affected-claims register naming every superseded number/interpretation per paper.
- **G2 — V4 narration rewrite (Hwao drafts, Lana signs):** rewrite affected scenes against the new freeze before any audio/lip-sync/layout work; wording changes are expected and allowed here — the `selection_v3.json` invalidation rule means new audio/lip-sync will be generated for V4 anyway; identity/voice/speed stay fixed.
- **G3 — Plot inventory + reproducibility (Goru inventory; Kun crop|redraw verdicts):** against the new freeze only, per the accepted T4 axes/claims.
- **G4 — V4 spec draft + Lana sign-off.**
- **G5 — z9-metallicity full-video local canary + QA:** canary choice re-affirmed (flagship, densest claims, and it now also exercises the re-freeze → re-anchor path end-to-end). QA additions: narration numbers must match new-freeze extract lines; no V4 asset may reference `paper-videos-v2-*/sources/`; all prior §5 criteria stand with new-freeze shas.
- **G6 — Duho approves canary. G7 — batch rebuild of remaining four. G8 — publication decision (separate explicit user gate).**
- **Parallel user decision (no default action): what, if anything, to do about the superseded claims in the live public V3 videos.**

HWAO_V4_SOURCE_REFRESH_AMENDMENT_COMPLETE
