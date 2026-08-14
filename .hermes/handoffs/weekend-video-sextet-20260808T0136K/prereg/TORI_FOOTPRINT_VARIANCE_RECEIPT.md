# TORI — frozen-footprint variance receipt

**Assembled UTC:** `2026-08-14T06:45:24Z`  
**Route:** Lana Tier 3 — exact post-Cut-6 counts per brick; geometry local  
**Verdict:** **PASS**  
**BS-1 status:** **SATISFIED ON THE BOUNDED TIER-3 ROUTE**

## Plain ruling

The count-weighted brick-centre value is `0.445201348111956`. Its margin above `0.15` is `0.295201348111956`, which is at least twice the `0.0124` error bracket. Under Lana's binding rule, BS-1 is satisfied on this route.

This receipt supersedes the prior UNRESOLVED receipt while preserving both earlier attempt receipts byte-for-byte as history. The failed attempts were handled correctly; the failure was the old server-side query shape. The successful route sent no trigonometry or axis-relative geometry to NOIRLab.

## Measured bounded statistic

- frozen population: `832,393` dered Cut-6 objects;
- nonempty selected bricks: `270,577`;
- count-weighted `mean(cos theta)` at brick centres: `-0.109116141652194`;
- count-weighted `mean(cos² theta)` at brick centres: `0.457107680481017`;
- count-weighted `var(cos theta)` at brick centres: `0.445201348111956`;
- preregistered threshold: `0.15`;
- margin above threshold: `0.295201348111956`;
- half-diagonal bound: `0.177 deg = 0.00309 rad`;
- conservative variance error bracket: `|V_object - V_center| <= 0.0124`;
- conservative object-variance interval: `[0.432801348111956, 0.457601348111956]`;
- twice-error margin required for PASS: `0.0248`;
- binding decision rule: PASS if `V_center - 0.15 >= 0.0248`; FAIL if `V_center + 0.0124 < 0.15`; INCONCLUSIVE otherwise.

The `0.0124` bracket is more than ten times smaller than the `0.15` threshold. It follows from the 0.25-degree brick geometry, the `0.177`-degree half-diagonal bound, and the fact that `cos theta` is 1-Lipschitz in great-circle angle. It is carried conservatively rather than replaced with the smaller within-brick estimate discussed by Lana.

## Exact server-side acquisition

- partition coverage: `67/67`;
- BRICKID keyspace: `1…662174`, disjoint and exhaustive;
- aggregate rows returned: `270,577` per-brick count rows;
- summed grouped population: `832,393`;
- frozen population match: **TRUE**;
- server projection: `brickid`, `COUNT(*) AS n_cut6_dered`;
- grouping: `GROUP BY t.brickid`;
- server-side trigonometric terms: **0**;
- server-side axis/angular terms: **0**;
- object rows exported: **0**;
- object positions exported: **0**.

The ordinary one-row aggregate guard remained armed and byte-identical at SHA-256 `228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51`. It was never opened. A dedicated fail-closed grouped-count validator permitted only the two-column `brickid`/`COUNT(*)` schema while retaining the trigonometry, position, signal, row-export, and mutation bans.

## Local geometry

The official static DR10-south brick product supplied only the brick grid centres used locally:

- URL: `https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/survey-bricks-dr10-south.fits.gz`;
- SHA-256: `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a`;
- static rows: `366,912`;
- required columns: `brickid`, `ra`, `dec`;
- Longo axis used locally only: Galactic `(l,b)=(52,68.5) deg`, frozen equatorial `(RA,Dec)=(216.984434295527, 32.060611193471) deg`.

No object coordinates crossed the wire and no local geometry was computed until all 67 count partitions and the exact population check passed.

## Hash custody

- launch authorization: `8717f4473d196dbacb55235f1e25048c9d15b8ecdf1c26420b2cfc0aed990132`;
- prelaunch verification: `dd11818d97f3b4f6b203e980277ba7a9a5f3a4e113974355a0087d95f22b84ea`;
- grouped-count manifest: `2d85c044693633b6d9d74e9fae026965d16ed645708dcdff9781120267c3ed51`;
- final counts outcome: `d57f4278d5bf9633efbbc87c3555946c993f72d975553e2aede9986d168d5a72`;
- static-product custody: `5e969bf623ec07a0366355fb5f723b31e4365fd7e03ccc07e1addd32f379881a`;
- official static product: `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a`;
- combined per-brick counts: `4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0`;
- local geometry result: `0d3c188410a77df1074d4525d0a6f369391cf8465449a0067a09acfdefb3692f`;
- reconstruction custody: `549a74e87b9f7c53e0b9fb924f6ed797c3f6dc403eab36fbd69763c12bd19678`;
- grouped-count worker executed code: `af8ba9b54f060418e3a720b177f5b3b8b2f93c8bc3561eeb326dd584461c6415`;
- orchestrator executed code: `b69fef3544d59775f6a9e9bf0fa6c8205f61681c0a7616f86b7289f4ac95cc24`;
- reconstructor executed code: `d334e5114ff69fa37b2e4137a0c5a34f60ba87ccf9633cd515e6198b302fcd0e`;
- Goru audit: `3dba46c58bc2c01920c22af273f36cbbe1358e5c1375b9e8b23aa9c49acf0a15`;
- Kun audit: `e14c76a4bf45f8d3535ff50d5f761ddc9af3de4c4f538a660b5653cfc1a3dc17`;
- Lana audit: `04738a649b9d0533ce6070a5b8327839de7878250f092c517e950bba248b2c44`;
- preserved global-attempt receipt: `ef995652531d35cf3dc68df542661f9c503b571be9d34e4423de0347c63bf20e`;
- preserved partition-attempt receipt: `f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289`;
- superseded unresolved receipt SHA-256: `f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289`.

## Scope boundary

- aggregate per-brick count rows: `270,577`;
- object rows: **0**;
- object positions: **0**;
- images: **0**;
- chirality computed: **0**;
- handedness, spin, CW/CCW fields joined or referenced: **0**;
- angle bins or sky maps: **0**;
- dipole amplitude computed: **0**;
- accepted-sample variance claimed: **NO** — this receipt is for the frozen dered Cut-6 population;
- publication/acceptance/commit/push: **0**.

## Supersession

- `TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md` remains immutable history at `ef995652531d35cf3dc68df542661f9c503b571be9d34e4423de0347c63bf20e`.
- `TORI_FOOTPRINT_VARIANCE_PARTITIONED_ATTEMPT_20260814.md` remains immutable history at `f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289`.
- This file replaces the prior UNRESOLVED `TORI_FOOTPRINT_VARIANCE_RECEIPT.md` at `f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289` only after complete Tier-3 reconstruction.
