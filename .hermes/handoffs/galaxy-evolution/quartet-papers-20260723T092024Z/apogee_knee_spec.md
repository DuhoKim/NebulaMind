# Frontier #53 — APOGEE α-element [Mg/Fe] "knee": overnight-run build spec
Author: Goru (rigor/numeric lane). Checkout: /Users/duhokim/NebulaMind/NebulaMind.
Template: tools/nm_ionizing_budget.py + tools/lab_runner_worker.py + tools/overnight_loop.py.

---

## 0. VERDICT — READ FIRST

**R5 novel datum (one sentence):** *The signed, pre-registered offset
`Δ[Fe/H]_knee ≡ [Fe/H]_knee(observed) − [Fe/H]_knee(GCE)` between the high-α
sequence [Mg/Fe] knee measured on the homogeneous APOGEE DR18 ASPCAP scale and
the knee predicted by a frozen analytic leaky-box + t^−1.1 SNIa-DTD one-zone GCE
model — reported together with whether that offset's SIGN survives an
ASPCAP-raw ↔ calibrated abundance-scale swap.*

**GO / NO-GO on R5: NO-GO (lean) on the frontier bar — CONDITIONAL-GO only if the
spatial axis is recovered.**

Why NO-GO, stated plainly (this is better found now than at dawn):

1. The novelty gate (`nm_fulltext_layer.py`, run 2026-07-24) returns the exact
   prior art that already owns both halves of this datum:
   - **Nidever et al. 2014 (2014ApJ...796...38N)** — *measures* the high-α
     sequence track/knee across the APOGEE disk. So "we locate the knee" is not new.
   - **Vincenzo et al. 2021 (2021MNRAS.508.5903V, Weinberg group)** and
     **Weinberg+19 two-process** — already *confront* the [α/Fe] two-sequence
     distribution with an analytic GCE / DTD. So "we compare the knee to a GCE
     model" is not new either.
   The proposed datum is therefore a **re-measurement on a newer data release
   (DR18 ASPCAP) plus a model confrontation whose qualitative answer is already
   published** (knee near [Fe/H]≈−0.4…−0.5; analytic GCE roughly reproduces it).
   That is a *new decimal on a known quantity*, not a new physical result. It
   fails the standing bar (MEMORY: "frontier not low-hanging", "autopilot
   publishable bar": compiles+honest ≠ publishable; needs a non-circular,
   defensible, genuinely-new result).

2. **The one genuinely-new axis is forbidden by the data reality you already
   verified.** The live frontier in Gaia–APOGEE GCE is the *radial and age
   dependence* of the knee (inside-out enrichment, radial migration): does
   `[Fe/H]_knee` move with guiding radius R_g / age? That requires `glon/glat`
   (→ R_gal) or ages — but `snr/glon/glat` are **not on `aspcapStar`**, and the
   `aspcapStar ⋈ apogeeStar` coordinate join **times out** on SkyServer. With
   only the *global* [Mg/Fe]–[Fe/H] plane we are confined to exactly
   Nidever14 + Vincenzo21 territory.

3. The differential candidate that IS data-feasible without spatial info — an
   **inter-element knee offset** `Δ[Fe/H]_knee(Mg) − Δ[Fe/H]_knee(Ca/Si/O)` on
   identical stars — is plausibly under-reported as a *precise error-barred
   number*, but the offset is small (~0.05–0.10 dex) and almost certainly
   **ASPCAP inter-element-systematics-limited**; the calibration-swap test would
   most likely flag it non-robust → a valid but unexciting null. High risk, low
   novelty payoff. (Weinberg+19's two-process fractions already imply most of it.)

**Condition that flips this to GO:** recover the spatial axis by replacing the
timing-out SkyServer coordinate join with a **local join on `APOGEE_ID`**: pull
`aspcapStar` (chemistry) and `allStar`/`apogeeStar` (glon/glat, or Gaia-derived
R_g) as **two separate SELECTs**, join in-process on the string ID (not a spatial
cross-match). Then the novel datum becomes **`d[Fe/H]_knee / dR_g`** — the radial
gradient of the α-knee on one homogeneous DR18 scale, pre-registered against the
inside-out GCE prediction. THAT clears R5. It is a bigger build (two pulls + ID
join + a radial-bin loop) but it is the honest path to a publishable frontier result.

Everything below is the **full buildable spec** so the lead can (a) override and
run the global confrontation as-is, or (b) green-light the radial extension. It is
written to run either way.

---

## 1. R5 — the datum and its two framings (honest novelty per framing)

| framing | datum | novelty verdict |
|---|---|---|
| (a) Δ between the two sequences' knees | `[Fe/H]_knee(high-α) − [Fe/H]_knee(low-α)` | **REJECT.** The low-α (thin-disk) sequence has no sharp knee — [Mg/Fe] declines gently and monotonically. A "second knee" is ill-defined; the number would be an artifact of the fit, not physics. |
| (b) GCE-confrontation residual | `Δ[Fe/H]_knee = obs − pre-registered-GCE` (+ calibration-swap sign robustness) | **WEAK-NEW.** Methodologically clean (pre-registration + swap), but the quantity is already confronted in Vincenzo21/Weinberg19; new only via DR18 + the robustness flag. This is the "if forced" primary. |
| (c) inter-element knee offset | `Δ[Fe/H]_knee(Mg) − Δ[Fe/H]_knee(Ca)` on same stars | **MAYBE-NEW but HIGH-RISK.** Differential over identical stars cancels the [Fe/H] zero-point (strong non-circularity), but signal is small & systematics-limited → likely non-robust null. |
| (d) **radial gradient** `d[Fe/H]_knee/dR_g` | requires the local ID-join fix (§0 condition) | **GENUINELY-NEW & frontier.** Not achievable with the current `aspcapStar`-only pull. The GO path. |

Primary if the lead overrides to run now: **framing (b)**, `method="alpha-knee-gce"`.
Recommended before running: **framing (d)**, contingent on the ID-join fix.

---

## 2. The exact analysis

### 2.1 APOGEE pull (generalize `sdss_pull`, one line — line 96 of lab_runner_worker.py)
```python
def sdss_pull(cols_sql, where, table="galSpecExtra"):      # add table=…
    r = requests.get(TAP, params={"cmd": f"SELECT TOP 120000 {cols_sql} FROM {table} WHERE {where}",
                                  "format": "csv"}, timeout=240)
    return np.genfromtxt(r.text.splitlines(), delimiter=",", skip_header=2)
```
- **Columns:** `apogee_id, fe_h, fe_h_err, mg_fe, mg_fe_err, alpha_m, teff, logg, aspcapflag`
  (verified: `fe_h, mg_fe, alpha_m` return real two-sequence rows).
- **Quality cuts (WHERE):**
  `fe_h > -1.5 AND fe_h < 0.5 AND mg_fe > -0.3 AND mg_fe < 0.6
   AND fe_h_err < 0.05 AND mg_fe_err < 0.05
   AND logg BETWEEN 1.0 AND 3.5 AND teff BETWEEN 3800 AND 5500
   AND (aspcapflag & 0x800000) = 0`  ← STAR_BAD bit off (bit 23).
  Giants only (logg/teff box) → clean, homogeneous ASPCAP abundances.
- **Expected N:** ~80k–120k giants after cuts (TOP 120000 cap; the sequence is
  well-populated — c3 selection pull already returned ≳10^5 SDSS rows on the same TAP).

### 2.2 High-α membership (the chemical cut — NOT radial)
Boundary line in the [Mg/Fe]–[Fe/H] plane (Hayden/Adibekyan style broken line):
```
high-α  if  [Mg/Fe] > B(fe_h)
B(fe_h) = 0.12 - 0.13*fe_h      for fe_h < 0        # rising toward low metallicity
        = 0.12 - 0.31*fe_h      for fe_h >= 0        # steeper drop at solar+
```
`alpha_boundary ∈ {loose(−0.02 dex), fiducial, strict(+0.02 dex), sloped}` is a grid axis.
Membership feeds only the *ridge* used for the knee; counts are not used (see §2.5).

### 2.3 Knee-finding algorithm (`knee_method` grid axis)
Operate on the **running median ridge** of the high-α sequence, `mg_ridge(fe_h)`
in `fe_h` bins of 0.05 dex, ≥40 stars/bin (reuse `median_rel` from the worker):
1. `broken_stick` (default): least-squares two-line (segmented) fit
   `mg = a1 + s1·fe_h` (fe_h<k) ∪ `a2 + s2·fe_h` (fe_h≥k), continuous at k;
   minimize SSE over knee `k` on a 0.01-dex grid in [−0.8, −0.1]. `k* = [Fe/H]_knee`.
2. `median_changepoint`: max-curvature / PELT-style changepoint on the ridge.
3. `segmented`: bootstrap the two-line fit (1000 resamples) → knee + SE.
Report `[Fe/H]_knee ± SE` (bootstrap SE, 1000 resamples of member stars).

### 2.4 In-code analytic GCE + PRE-REGISTERED parameters (freeze BEFORE the pull)
Weinberg-2017 one-zone leaky-box, closed form for [Mg/Fe] vs [Fe/H]; predicted knee
= [Fe/H] where cumulative SNIa Fe overtakes CCSN Fe given the DTD. **Frozen inputs:**
| param | pre-registered value | source |
|---|---|---|
| SFE timescale τ_* | 2.0 Gyr (thick-disk-fast); grid alt 1.0 Gyr | Weinberg+17 |
| outflow mass-loading η | 2.5 | Weinberg+17 fiducial |
| SN Ia DTD | power-law t^−1.1, t_min = 0.15 Gyr | Maoz+12 |
| DTD index (grid) | {−1.0, −1.1, −1.3} | — |
| CCSN [Mg/Fe] plateau | +0.30 dex | Weinberg+19 process ratios |
| SNIa Fe fraction | 0.5 of total Fe at late times | Weinberg+19 |
`gce_knee(params) → [Fe/H]_knee^model` (expected ≈ −0.45 to −0.50 for τ_*=2 Gyr).
Params are hard-coded constants in the module (like the reionization anchors),
cited inline; the runner's ADS layer refetches exact numbers for the manuscript.

### 2.5 ASPCAP selection function — forward-modelled / neutralised
APOGEE selection is a dereddened (J−Ks) color–magnitude cut on giants — a
**spatial/photometric** selection we CANNOT reconstruct without `glon/glat`.
Handled two honest ways, both grid-exposed via `selection_weight`:
- **off (fiducial):** the knee estimator uses the *ridge location*, not number
  counts, so it is first-order insensitive to how many stars sit at each [Fe/H].
  State this as the primary defence.
- **on:** reweight member stars by an inverse-MDF prior (flatten the [Fe/H]
  histogram to a uniform target) and refit the ridge; the knee shift between
  on/off is a reported systematic, not a correction claimed as truth.
This is the honest analogue of the f_esc "corner" — we bound the selection
sensitivity, we do not pretend to invert the selection function.

---

## 3. Non-circularity → `noncircular_robust` (the calibration-swap test)

Mirrors `run_ionizing_budget` exactly (O32↔beta swap → here ASPCAP-raw ↔ calibrated):
- Compute `Δ_raw  = [Fe/H]_knee(obs, aspcap_raw)    − [Fe/H]_knee(GCE)`
- Compute `Δ_calib= [Fe/H]_knee(obs, calibrated)    − [Fe/H]_knee(GCE)`
  where `calibrated` applies a fixed literature ASPCAP zero-point/tilt
  (e.g. an [Fe/H]-dependent offset from the ASPCAP–optical comparison, and/or
  an external Mg calibration). Both are computed on the SAME stars.
- `noncircular_robust = (sign(Δ_raw) == sign(Δ_calib))` — the headline "the DR18
  knee sits {above/below} the DTD-predicted knee" is only reported if the sign
  survives the abundance-scale swap. A flip ⇒ the offset is calibration-driven,
  not physical ⇒ SHELVE.
- **Differential design:** because Δ is (obs − model) and the swap changes only
  the abundance scale on identical stars, an overall [Fe/H] zero-point that shifts
  BOTH the observed knee and (implicitly) the comparison cancels to first order —
  that is the structural independence, not a fitted nuisance.

**Triage wiring (one-line generalisation, like `sdss_pull`):** the module sets
`res["knee"] = {..., "noncircular_robust": bool, "delta_raw": …, "delta_calib": …}`
AND a top-level `res["noncircular_robust"]`. Generalise `overnight_loop.triage`:
```python
nc = (res.get("fesc") or res.get("knee") or {}).get("noncircular_robust")
...
if res.get("fesc") or res.get("knee"): ok = ok and bool(nc)
```
So the calibration-swap gate binds this run exactly as it binds f_esc.

---

## 4. R2 — pre-registered falsification threshold

- **Statistic:** `Δ[Fe/H]_knee = [Fe/H]_knee^obs − [Fe/H]_knee^GCE`.
- **Threshold (pre-registered):** the frozen-DTD GCE is FALSIFIED iff
  `|Δ[Fe/H]_knee| > 0.10 dex` **AND** the sign is stable across **every** grid
  corner (§5) **AND** `noncircular_robust == True`.
- **N & achievable significance:** with N≈10^5 high-α members, the bootstrap SE
  on the knee is ~0.01–0.02 dex, so a 0.10-dex offset is >5σ *statistically*.
  Therefore the measurement is **systematics-limited, not statistics-limited** —
  the honest falsification is the grid-stability + swap test, not the σ. If the
  offset is <0.10 dex or sign-unstable across corners, the frozen DTD is **not
  rejected** (consistent-with, reported as such).

---

## 5. Systematic-corner sweep grid (à la f_esc 232-pt)

| axis | values | n |
|---|---|---|
| `alpha_boundary` (chemical cut) | loose / fiducial / strict / sloped | 4 |
| `knee_method` | broken_stick / median_changepoint / segmented | 3 |
| GCE `dtd_index` × `tau_sfe` | {−1.0,−1.1,−1.3} × {fast 1 Gyr, fid 2 Gyr} | 6 |
| `selection_weight` | off / on | 2 |
| `abund_scale` (= the swap) | aspcap_raw / calibrated | 2 |

**Grid = 4 × 3 × 6 × 2 × 2 = 288 points** (comparable to the f_esc 232-pt grid).
Each point is one queued spec; the run is "robust" iff `sign(Δ)` and the R2
verdict are stable across all 288. (Add `element ∈ {mg,o,si,ca}` → ×4 = 1152 if
the lead also wants the inter-element framing (c).)

---

## 6. Build shape

### 6.1 Bespoke module `tools/nm_alpha_knee.py` (mirror `nm_ionizing_budget.py`)
```
run_alpha_knee(rec, res, plt)          # entry, mirrors run_ionizing_budget; sets res, returns True
  fetch_apogee(where, cols)            # calls generalised sdss_pull(..., table="aspcapStar")
  classify_high_alpha(fe_h, mg_fe, boundary) -> mask
  ridge(fe_h, mg_fe, mask)             # running-median ridge (reuse worker.median_rel)
  find_knee(ridge, method) -> (k, se)  # broken_stick | median_changepoint | segmented
  gce_knee(dtd_index, tau_sfe, eta, ...) -> k_model    # frozen analytic leaky-box knee
  apply_scale(fe_h, mg_fe, scale)      # aspcap_raw | calibrated  (the swap)
res["knee"] = {"fe_h_knee_obs":[lo,med,hi], "fe_h_knee_gce":k_model,
               "delta":[lo,med,hi], "delta_raw":…, "delta_calib":…,
               "noncircular_robust":bool, "boundary":…, "method":…, "corner":…}
res["title"], res["summary"], res["provenance"]  # provenance: APOGEE DR18 ASPCAP catalog data
res["figure_url"] set by caller (result.png = [Mg/Fe]–[Fe/H] plane + ridge + both knees)
```
Self-check `__main__` with a dummy `plt` (copy the `_P` stub from the template).

### 6.2 New `study()` branch in `lab_runner_worker.py` (after the ionizing block)
```python
elif method in ("alpha-knee-gce", "alpha-element-knee"):
    import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
    from nm_alpha_knee import run_alpha_knee
    log(rec, "measuring APOGEE DR18 high-alpha [Mg/Fe] knee vs pre-registered GCE…")
    made = run_alpha_knee(rec, res, plt)
```
Map `data_sources` containing `"apogee"` → the `aspcapStar` pull inside the module.

### 6.3 `overnight_loop` spec-dict format (one dict per grid point)
```python
{
  "topic": "alpha-element-knee-gce-confrontation",
  "topic_source": "frontier-53-gaia-apogee-gce",
  "data_sources": ["apogee"],
  "method": "alpha-knee-gce",
  "outputs": ["aastex-draft", "dr-review-loop"],
  "force": True,
  # --- grid params ---
  "alpha_boundary": "fiducial",     # loose|fiducial|strict|sloped
  "knee_method": "broken_stick",    # broken_stick|median_changepoint|segmented
  "dtd_index": -1.1,                # -1.0|-1.1|-1.3
  "tau_sfe": "fid",                 # fast|fid
  "selection_weight": False,        # False|True
  "abund_scale": "aspcap_raw",      # aspcap_raw|calibrated  (the swap)
  "corner": "fiducial"              # label for STATUS ledger
}
```
Generate the 288-spec queue by `itertools.product` over the six axes (replacing the
z-sweep list comprehension in `overnight_loop.main`), write to `--queue` JSON.
`triage`/`STATUS.md` already report `grounded/verdict/noncircular/headline`; the §3
one-line `triage` generalisation makes the swap gate binding.

---

## 7. Honest bottom line

The build is straightforward and mirrors the working f_esc template one-for-one.
The blocker is **not** engineering — it is that the only datum the current
`aspcapStar`-only pull can produce (global knee vs frozen GCE) is a re-measurement
+ known confrontation (Nidever14 / Vincenzo21 / Weinberg19), i.e. it does not clear
R5's "genuinely new" gate. **Recommend NO-GO as scoped; CONDITIONAL-GO on the
radial extension (§0) once the `allStar`/`apogeeStar` ID-join replaces the timing-out
coordinate join, giving `d[Fe/H]_knee/dR_g` — the actual frontier datum.**
