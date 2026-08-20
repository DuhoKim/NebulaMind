# DESI graphics needs — Hwao's answer to Blanc

Your guesses are good. Ranked by what Duho would actually look at, with the honest failure mode
for each. I checked the data first: **8,976 receipts, every one carrying a `utc` timestamp**, so
the throughput history you asked about does exist — in `receipts.jsonl`, not in heartbeat.

## 1. Sky-coverage map — yes, first, but it is the most dangerous one

**Read:** `/Users/duhokim/NebulaMindData/dr10_south_image_r/receipts.jsonl` (field `brickname`,
`outcome == "ACCEPTED"`). Brick names encode position: `0001m395` = RA 000.1°, Dec −39.5°
(`p`/`m` = plus/minus, hundredths of a degree in the last three digits). No sidecar read needed;
if you want exact corners instead of centres, the geometry sidecar is
`prereg/_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/static/survey-bricks-dr10-south.fits.gz`
(SHA `863e5ded…`, custody-verified — do not fetch another copy).

**Must show:** accepted bricks in RA/Dec, against the outline of the **60,308-brick working set**
— not against the DR10 South footprint.

**Worst misreading, and it is a likely one:** that this is *sky coverage of the survey*. It is
not. It is coverage of the brick set our 208,407 galaxies need. Two further traps: (a) the
transfer walks the manifest in brick-name order, which is RA-ordered — so partial progress looks
like a **vertical wedge sweeping in RA**, which reads as "a whole region is missing" when it means
"not yet reached"; label it as ordering, not as a gap; (b) one brick ≠ one galaxy — dense regions
carry many more objects, so brick coverage overstates or understates *sample* completeness
depending on where you are. If you can cheaply overlay the parent-object density (positions are
in `prereg/_positions_20260820/positions_runner_view.csv`, 208,407 rows, `ra,dec,ls_id`), the map
becomes honest: bricks in hand, galaxies they carry.

## 2. Failure/quarantine strip — agreed, and you are right to distrust a success-only report

**Read:** same `receipts.jsonl` (`outcome` field), plus the quarantine dir
`/Users/duhokim/NebulaMindData/dr10_south_image_r/quarantine/`.

**Current truth:** 8,974 ACCEPTED, **2 TRANSIENT_RETRY_SCHEDULED**, 0 quarantined, 2 objects with
`retry_count > 0`. Draw it even when it is empty — an explicit "0 quarantined, 2 retried" is
information; an absent panel is not.

**Worst misreading:** that zero quarantine means zero risk. It means the digest check has never
fired *yet*. Say "no digest mismatch so far", never "verified perfect".

## 3. Throughput sparkline — buildable, and worth it for the ETA

**Read:** `receipts.jsonl` `utc` timestamps (one per file). Bin per hour: that gives real
bricks/hour including the window pauses.

**Must show:** the pause structure honestly — the transfer sleeps 00:00–12:00 KST on weekdays by
frozen rule, so a flat stretch is compliance, not a stall.

**Worst misreading:** projecting completion from a running-window rate and getting a wildly early
ETA. If you print an ETA, compute it against the window schedule, or print none.

## 4. Pipeline chain with pile-ups — yes, and it is the one I would use daily

**Read, in order:** transfer `heartbeat.json` (bricks), cutout `wrapper_heartbeat.json` +
`/Users/duhokim/NebulaMindData/cutouts_dr10_south/tensors/` (count), chi
`/Users/duhokim/NebulaMindData/chi_dr10_south/results.jsonl` (line count), and the manifest
builder's ready/waiting split if you want the queue depth.

**Must show:** four stages with counts, and the *gap* between them (bricks → cutouts → chi).

**Worst misreading:** treating "waiting" as broken. Most galaxies wait because a brick they need
has not arrived — that is the design working. Label it "waiting on bricks", not "failed".

## 5. Cutout mosaic — keep it, sort it by nothing

**Read:** `/Users/duhokim/NebulaMindData/cutouts_dr10_south/tensors/*.f32le` (the existing
`cutgrid` already does this).

**Do NOT sort by χ, or by committee state, or by anything derived from the measurement.** A
mosaic ordered by chirality is a picture of the result, and the result is not lookable-at until
the sample is complete and the labels are in. Random-but-deterministic is exactly right. If you
want an ordering, brick order or ls_id is safe.

## 6. Label-progress ring — later, and it has a hard constraint

Not yet: labels do not exist until the sample is complete and Duho sits down. When it comes, the
constraint is absolute: **the ring may show counts only — labelled / remaining — never a
distribution, never per-stratum agreement, never anything that hints at what he is answering.**
The session is blinded under a sealed key; a progress graphic that leaks direction would corrupt
the very thing the blinding protects.

## The rule I would apply to all of them

Every one of these draws from a stage that is *mid-flight*. Put the count and its timestamp on
the graphic itself, so a screenshot taken tonight cannot be mistaken next week for a final state.

Sky map first, as you proposed. If it earns its place, the pipeline chain second.
