# TORI — Longo-axis footprint-variance attempt receipt

**Status:** **UNRESOLVED — ONE AUTHORIZED QUERY ABORTED WITHOUT A RESULT**  
**Kun BS-1 threshold:** `var(cos theta) >= 0.15`  
**Threshold verdict:** **NONE — no moments were returned**

## Plain ruling

The one narrow query authorized by Duho was submitted exactly once. It remained in UWS phase `EXECUTING` for `03:09:56`, from `2026-08-13T09:27:09Z` until the abort request at `2026-08-13T12:37:05Z`. It was then explicitly aborted and reached terminal phase `ABORTED` at `2026-08-13T12:37:07Z`.

No aggregate row was returned. Therefore `mean(cos theta)` and population `var(cos theta)` are **unmeasured**, and Kun's `>= 0.15` requirement is **unresolved**. This is not a failing below-threshold result; no numeric result exists to compare with the threshold. The population, axis, threshold, and scientific framing were not changed.

No replacement global query and no partition query was submitted. An exact partition decomposition was considered only as local implementation work, then removed because multiple new submissions were outside the one-query authorization.

## Authorizing instruction and narrow scope

The instruction recorded for this exception was: Duho authorized **one server-side aggregate computation of `var(cos theta)`** over the exact Cut-6 population, relative to Longo's Galactic axis `(l,b)=(52°,68.5°)`, returning only the count, mean, and variance. The repeated copy of that instruction was treated as one permission, not two.

Explicitly outside scope and not done:

- no chirality, handedness, spin, CW/CCW, or signal field;
- no object row and no object position exported;
- no image request;
- no dipole amplitude or directional statistic beyond the requested moments;
- no sky map and no angular binning;
- no population, axis, or threshold change after runtime was observed;
- no replacement or partition submission without fresh authorization.

## Exact intended population

The query selected the frozen **dered Cut-6** population over documented catalogue keyspace `BRICKID 1…662174`:

1. `brick_primary = 1`;
2. `maskbits = 0`;
3. `type <> 'PSF'`;
4. `flux_r > 0`;
5. left join to `ls_dr10.photo_z` on `(ls_id, release, brickid, objid)`;
6. `0 <= z_phot_median < 0.15`;
7. `dered_mag_r < 17.7`;
8. `shape_r > 1.5`;
9. `POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551`.

Population custody:

- `TORI_SURVEY_ROUTE_BINDING_20260812.md` — SHA-256 `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87`;
- `TORI_CUT6_INCLINATION_COUNT_20260812.md` — SHA-256 `ed6b6e5e957903473c7692d5973f3b2d05a991916ce3aa247365938b0f414651`;
- `TORI_FULL_KEYSPACE_SWEEP_20260813.md` — SHA-256 `9d62960718b4f7aa1bb2eb67a9fddb83d6712698e1bc323fb1d21d1f4965e020`; exact dered Cut-6 count `832,393` and direct zero-tail closure.

Where coverage is mentioned, **BRICKID keyspace is not sky area**. The count certificate measured `BRICKID 1…541000` directly and separately proved `541001…662174` contains zero joined parent rows. The intended variance was an object-position aggregate, not an inference from the `81.700580%` directly scanned keyspace fraction.

## Statistic and what it would reveal

- Longo axis: Galactic `(l,b)=(52°,68.5°)`.
- Reproduced ICRS axis: `(RA,Dec)=(216.98443429552697°,32.060611193471175°)`.
- ICRS unit vector in the query: `(-0.6769717798726208,-0.5098465358556549,0.5308160878610257)`.
- `cos(theta)` was the dot product of each selected sky-position unit vector with that fixed axis vector.
- Intended aggregate: `AVG(cos_theta^2) - POWER(AVG(cos_theta),2)`.
- Intended output columns: contributing count, `AVG(cos_theta)`, and population variance.

Had it completed, this would reveal only whether the selected survey population has enough angular spread relative to the preregistered axis for the proposed geometry. It could not reveal handedness, chirality, CW/CCW imbalance, or dipole amplitude because no signal-bearing field entered the query. Since it did not complete, it revealed no geometry moment either.

## Guard lift and restoration custody

The normal aggregate runner was never weakened. It rejected the query before submission and rejects it now.

- ordinary guard path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/run_aggregate_tap.py`;
- ordinary guard SHA-256 before: `228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51`;
- ordinary guard verified to reject query before: **YES**;
- one-time exception opened: `2026-08-13T09:27:08Z`;
- exact authorized query SHA-256: `5d4c7812331419eff0ec7dca4e40f690203cb94cc71b6309d7b8694299249ff1`;
- submissions made / limit: `1/1`;
- executed one-time runner custody SHA-256: `0ffeb0d79f0b70faa37b0e0ef17db52988adba9516163b409c663e4c349bd826`;
- one-time submission path closed: `2026-08-13T11:27:14Z`;
- ordinary guard SHA-256 after: `228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51`;
- ordinary guard unchanged and verified to reject query after: **YES**;
- exception submitter physically disabled: **YES**;
- disabled stub SHA-256: `5ff98618c6d8dd8ed1f19d2ba7843fe94ce78af503247212df2ce8a6d1d91de9`;
- exception state: **CLOSED**.

The exception path was closed when its bounded local execution ended. Later monitoring was GET-only against the same recorded job. After the explicit abort, no live variance process or authorized submission path remains.

## UWS and hash custody

- endpoint: `https://datalab.noirlab.edu/tap/async`;
- job: `https://datalab.noirlab.edu/tap/async/v0d4e15lm8hkz7zv`;
- submitted UTC: `2026-08-13T09:27:09Z`;
- phase before abort: `EXECUTING`;
- abort requested UTC: `2026-08-13T12:37:05Z`;
- terminal phase: `ABORTED`;
- query SHA-256: `5d4c7812331419eff0ec7dca4e40f690203cb94cc71b6309d7b8694299249ff1`;
- submission record SHA-256: `b8a11ab632131d2daebc08d48a0c92d0d63a9695bee5b5e540bd722baca79912`;
- abort receipt SHA-256: `c49d43f81c3f245bb349b7b69c77a7d319a6849c273866933a17a243fc73483b`;
- terminal job XML SHA-256: `7f762a6ca94152b8d2026c7c2e3af755431bcff6fe554ae64bb8833126bd2b80`;
- guard lifecycle SHA-256: `af8f71f5dcb1a4a965a175b828919c4751f390cc2a70e27f15d8666ec6bd22ab`;
- completed result artifact: **NONE**;
- result SHA-256: **NONE**;
- aggregate rows returned: **0**.

## Exact submitted query

```adql
SELECT
  COUNT(
      COS(RADIANS(t.dec)) * COS(RADIANS(t.ra)) * (-0.6769717798726208)
    + COS(RADIANS(t.dec)) * SIN(RADIANS(t.ra)) * (-0.5098465358556549)
    + SIN(RADIANS(t.dec)) * 0.5308160878610257
  ) AS n_cut6_dered,
  AVG(
      COS(RADIANS(t.dec)) * COS(RADIANS(t.ra)) * (-0.6769717798726208)
    + COS(RADIANS(t.dec)) * SIN(RADIANS(t.ra)) * (-0.5098465358556549)
    + SIN(RADIANS(t.dec)) * 0.5308160878610257
  ) AS mean_cos_theta,
  AVG(POWER(
      COS(RADIANS(t.dec)) * COS(RADIANS(t.ra)) * (-0.6769717798726208)
    + COS(RADIANS(t.dec)) * SIN(RADIANS(t.ra)) * (-0.5098465358556549)
    + SIN(RADIANS(t.dec)) * 0.5308160878610257,
    2
  )) - POWER(AVG(
      COS(RADIANS(t.dec)) * COS(RADIANS(t.ra)) * (-0.6769717798726208)
    + COS(RADIANS(t.dec)) * SIN(RADIANS(t.ra)) * (-0.5098465358556549)
    + SIN(RADIANS(t.dec)) * 0.5308160878610257
  ), 2) AS var_pop_cos_theta
FROM ls_dr10.tractor_s AS t
LEFT OUTER JOIN ls_dr10.photo_z AS p
  ON t.ls_id = p.ls_id
 AND t.release = p.release
 AND t.brickid = p.brickid
 AND t.objid = p.objid
WHERE t.brickid BETWEEN 1 AND 662174
  AND t.brick_primary = 1
  AND t.maskbits = 0
  AND t.type <> 'PSF'
  AND t.flux_r > 0
  AND p.z_phot_median >= 0
  AND p.z_phot_median < 0.15
  AND t.dered_mag_r < 17.7
  AND t.shape_r > 1.5
  AND POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551
```

## Boundary ledger

- TAP query submissions: **1**
- terminal result rows returned: **0**
- sample rows exported: **0**
- positions exported: **0**
- images requested: **0**
- chirality computed: **0**
- handedness joined or referenced: **0**
- CW/CCW fields joined or referenced: **0**
- dipole amplitude computed: **0**
- sky maps or angular bins: **0**
- replacement global queries: **0**
- partition queries submitted: **0**
- publication/acceptance/commit/push: **0**

## Exact next decision

Kun's footprint-variance item remains open. A new empirical attempt requires fresh authorization specifying either one replacement global query or a bounded exact partition manifest. This receipt grants neither.
