# Independent Popławski BHU citation audit

**Cutoff:** 2026-08-11. **Custody:** arXiv abstract/version pages, downloaded versioned PDFs and TeX source, Crossref, INSPIRE, and NASA ADS only. The scientific inventory below is from the complete latest PDF of arXiv:1910.10819v2 (5 PDF pages; pp. 1–4 contain text/equations and p. 5 is references), not its abstract.

## 1. Four citation pins

| arXiv pin | Exact arXiv subjects (primary first) | Version history (UTC) | Latest title / arXiv comment | Journal metadata |
|---|---|---|---|---|
| **1007.0587** | **astro-ph.CO**; gr-qc; hep-th | v1 2010-07-04 21:29:24; v2 2010-11-02 18:13:25 | *Cosmology with torsion: An alternative to cosmic inflation*; “8 pages; published version” [7] | *Physics Letters B* **694**(3), 181–185 (2010), DOI **10.1016/j.physletb.2010.09.056**; erratum *Physics Letters B* **701**(5), 672 (2011), DOI **10.1016/j.physletb.2011.05.047**. Crossref classifies both as journal articles. [24][25] |
| **1410.3881** | **gr-qc**; astro-ph.CO; hep-th | v1 2014-10-14 22:27:54; v2 2026-05-26 20:13:54 | v1 *Universe in a black hole with spin and torsion*; v2 *Universe in a black hole in Einstein–Cartan gravity*; “11 pages; published version” [9] | *The Astrophysical Journal* **832**(2), 96 (2016-11-21), DOI **10.3847/0004-637X/832/2/96**; Crossref type `journal-article`. [26] |
| **1910.10819** | **physics.pop-ph**; astro-ph.CO; gr-qc | v1 2019-10-23 21:59:53; v2 2025-05-29 23:59:54 | v1 *Black Hole Genesis and origin of inertia*, 2 pp.; v2 *Universe in a rotating black hole and preferred axis*, “5 pages” [10][11] | **No journal reference or related journal DOI on arXiv.** The only DOI displayed is the arXiv/DataCite DOI **10.48550/arXiv.1910.10819**, not a journal DOI. [11] |
| **2509.11468** | **gr-qc**; astro-ph.CO | v1 2025-09-14 23:21:23; v2 2025-11-19 22:38:22 | *Gravitational collapse with torsion and universe in a black hole*; “6 pages; published version” [13] | *International Journal of Modern Physics A* **40**(32), article 2544007 (2025-09-17), DOI **10.1142/S0217751X25440075**; Crossref type `journal-article`. [27] |

**Category check:** yes—**1910.10819 is primarily physics.pop-ph**, with astro-ph.CO and gr-qc as secondary categories, in both arXiv versions. [10][11]

## 2. Full-text inventory for arXiv:1910.10819v2

### Version caveat

The inherited-axis paper is a **2025 replacement of a different 2019 two-page preprint**. Version 1 is titled *Black Hole Genesis and origin of inertia* and contains no “Rotating frame…,” “Preferred axis,” galaxy-handedness, bulk-flow, or centrifugal-dark-energy sections. Those appear in v2. [10][11]

### Every relevant quantitative or functional statement

1. **Inherited frame, axis, and scale language — theory/descriptive.** The absolute frame is the primordial white hole at rest; the CMB is said to be isotropic “on large scales.” For a rotating parent black hole, “its axis of rotation becomes a preferred axis in the universe,” and the frame is non-inertial although the forces are only called “small.” The text further says the rotating-universe description “should combine” FLRW and Gödel metrics and that the preferred direction gives “small corrections” containing the Kerr radius
   \(a=M/(mc)\), where the paper calls \(M\) the parent-hole angular momentum and \(m\) its mass. No correction metric, coefficient, upper bound, multipole, or angular scale is supplied. **Locator:** abstract and “Absolute frame of reference,” p. 1; “Rotating frame of reference in a rotating black hole,” p. 2. [5]

2. **Zero global quantities — conjecture, not a sky observable.** In the absolute frame, the paper conjectures that “the total momentum and angular momentum of the matter in the universe are zero,” measurable only within an observer’s cosmological horizon. It does not define an estimator or uncertainty, and later invokes conservation of “the angular momentum of the universe” while \(\Omega\neq0\), without explaining the relation between those two statements. **Locator:** “Absolute frame of reference,” p. 2. [5]

3. **Rotating-frame equations — explicit functional forms, but generic mechanics rather than fitted cosmological predictions.** With \(\boldsymbol\Omega(t)\), the paper gives \(\mathbf v_0=\mathbf v+\boldsymbol\Omega\times\mathbf r\); the rotating-frame Lagrangian (Eq. 1); its derivatives (Eq. 2); and
   \[
   m\,d\mathbf v/dt=-\partial U/\partial\mathbf r-m\boldsymbol\alpha\times\mathbf r-2m\boldsymbol\Omega\times\mathbf v-m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r),\quad \boldsymbol\alpha=d\boldsymbol\Omega/dt
   \]
   (Eq. 3). It identifies Euler, Coriolis, and centrifugal terms; gives centrifugal magnitude \(m\Omega^2\rho\); gives \(\mathbf p=\mathbf p_0\) (Eq. 4); \(E=\tfrac12mv^2-\tfrac12m(\boldsymbol\Omega\times\mathbf r)^2+U\) (Eq. 5); and \(E=E_0-\mathbf M\cdot\boldsymbol\Omega\) (Eq. 6). These are functional/descriptive dynamics; no numerical \(\Omega\), \(\dot\Omega\), force, or Coriolis amplitude is predicted. **Locator:** “Rotating frame…,” pp. 2–3, Eqs. 1–6. [5]

4. **Galaxy spin alignment and handedness — qualitative directional/sign predictions.** Energy minimization via Eq. 6 is used to claim that “most galaxies should therefore tend to rotate in a preferred direction” with angular momentum parallel to \(\boldsymbol\Omega\), so clockwise and counterclockwise counts “should be different.” This supplies parallel alignment and nonzero asymmetry as qualitative outcomes. It supplies no convention tying clockwise/counterclockwise to either pole of the axial direction, no predicted fraction/asymmetry amplitude, no dispersion, no tolerance, and no redshift or scale function. “Most” is prose, not an operational lower bound for a defined sample. **Locator:** “Preferred axis,” p. 3. [5]

5. **Handedness numbers are retrospective empirical inputs, not model-derived forecasts.** The paper reports:
   - \(\sim10^4\) spirals, \(z\sim0.04\): axis \((\alpha,\delta)=(217^\circ,32^\circ)\);
   - \(\sim10^5\) spirals, \(z<0.3\): \((132^\circ,32^\circ)\);
   - \(\sim10^6\) DESI Legacy spirals: more counterclockwise in the north and more clockwise in the south, axis \((243^\circ,39^\circ)\);
   - \(\sim10^2\) JADES spirals, \(z<2\): the count opposite the Milky Way’s spin is \(\sim50\%\) higher than the same-spin count.

   It then takes coordinate means and states \((\alpha,\delta)=(197^\circ\pm47^\circ,34^\circ\pm3^\circ)\). This is a finite numerical, data-informed axis estimate, not a direction derived from parent-black-hole parameters. No averaging prescription, confidence level, covariance, axial/antipodal convention, or theoretical map to RA/Dec is given; the paper itself says the RA error is relatively large and more data are needed. **Locator:** “Preferred axis,” pp. 3–4. [5]

6. **Bulk flow — qualitative theory plus retrospective magnitude/direction.** The predicted relation is motion “perpendicular to the preferred axis and away from it” due to centrifugal force. The cited observational input is \(\sim10^2\) early-type galaxies and a cluster bulk-flow speed **630 km s⁻¹** toward \((128^\circ,-41^\circ)\). Eqs. 7–8 apply spherical trigonometry to that direction and the data-mean spin axis, obtaining \(\cos c=-0.143\) and \(c=98.2^\circ\), described as nearly perpendicular. These are finite empirical/derived values, not a model prediction of speed or direction. No predicted speed, lower bound, uncertainty, radius/wavenumber, redshift, or angular tolerance around 90° is supplied. **Locator:** “Preferred axis,” p. 4, Eqs. 7–8. [5]

7. **Rotation as dark energy — explicit functional identifications, no calibrated history.** For a closed universe the paper replaces the cylindrical centrifugal magnitude with \(m\Omega^2r\), away from the primordial white hole; acceleration is \(\Omega^2r\). It equates this form to \((1/3)\Lambda c^2r\), giving
   \[
   H=(\Lambda/3)^{1/2}c=\Omega,\qquad \Lambda=3\Omega^2/c^2.
   \]
   Coriolis effects depend on \(\boldsymbol\Omega\) and galaxy velocity. Conservation of angular momentum is then said to make \(\Omega\) decrease as the universe expands, so the effective \(\Lambda\) and dark energy decrease with time; different parent black holes yield different dark energies. These are functional/monotonic claims. The paper gives no \(\Omega(a)\), \(\Omega(z)\), \(\Lambda(a)\), \(w(z)\), moment-of-inertia model, numerical present \(\Omega\), or uncertainty. **Locator:** “Dark energy as centrifugal force,” p. 4. [5]

**No further relevant predictions occur on p. 5; it is references only.**

### Literal claim test

- **“No magnitude” — false literally.** v2 contains \(m\Omega^2\rho\), \(m\Omega^2r\), an observed \(\sim50\%\) handedness excess, 630 km s⁻¹, coordinate uncertainties, and \(c=98.2^\circ\). It does, however, contain **no model-derived numerical amplitude** for handedness, alignment scatter, bulk-flow speed, \(\Omega\), or dark energy.
- **“No scale” — false literally but substantially true for the model.** It uses “large scales,” “large-scale bulk flow,” “cosmological horizon,” sample sizes, and redshift cuts. It gives **no theoretical physical scale** (Mpc/Gpc, wavenumber, angular multipole, or transition scale) for any anisotropy.
- **“No functional form” — false.** Eqs. 1–8 and \(H=\Omega\), \(\Lambda=3\Omega^2/c^2\) are explicit forms. What is missing is a calibrated observable function of sky direction, redshift, or distance.
- **“Excludes no finite-precision sky outcome” — too broad.** Parallel spin alignment, unequal handedness, and perpendicular/away bulk flow are directional/sign claims that sufficiently precise null or differently oriented data could contradict. But the paper defines no quantitative acceptance region, probability distribution, amplitude threshold, angular tolerance, scale dependence, or prospective finite-precision forecast. Its finite sky numbers are measurements cited from earlier work or arithmetic derived from them, not blind theory outputs.

## 3. Peer-reviewed version or successor search for 1910.10819

- **arXiv:** v2 says only “5 pages”; unlike the three published pins, it has no “published version” comment, journal reference, or related journal DOI. [11]
- **INSPIRE:** record 1760842 contains the old and new arXiv titles and the three categories, but its metadata has no `publication_info`, no `dois`, and no `refereed` value. Exact-title and Popławski+`rotat*` searches each return only that same arXiv record. [18][29][30]
- **NASA ADS:** the record is bibcode `2019arXiv191010819P`, publication **arXiv e-prints**, with only DOI 10.48550/arXiv.1910.10819. An exact-title search returns that one arXiv record; adding `property:refereed` returns zero. [22][31][32]
- **Crossref:** a Popławski ORCID query returns 10 DOI-registered works, none with the inherited-axis title; it includes the journal versions of 1410.3881 and 2509.11468 but no rotating-axis item. [28]

**Result:** no linked peer-reviewed journal version and no obvious indexed rotating-axis/axis-title successor was found in those four systems as of the cutoff. This is strong evidence for “no known indexed journal version,” not a proof that no semantically retitled successor exists: Crossref ORCID deposits may be incomplete, metadata title searches are not exhaustive full-text searches, and “successor” has no unique bibliographic definition.

## Explicit unresolved items

1. Whether a journal successor exists under a wholly different title and without an arXiv relation/ORCID deposit cannot be excluded by metadata alone.
2. The paper does not specify how its four axis coordinates and uncertainties were combined, their confidence levels/covariance, or whether antipodal axes are identified.
3. It does not reconcile “total angular momentum of matter … zero” in the absolute frame with a rotating universe whose angular momentum is conserved.
4. No estimator, likelihood, tolerance, amplitude, physical scale, or redshift law is supplied that converts the qualitative axis/handedness/flow claims into a finite-precision prospective test.

## Sources

[5] https://arxiv.org/pdf/1910.10819v2
    > "These data are consistent with an analysis of CMB dipole signals taken from the Wilkinson Microwave Anisotropy Probe"
    > "A universe born from a rotating black hole should inherit its axis of rotation as a preferred axis"
    > "the total momentum and angular momentum of the matter in the universe are zero"
    > "most galaxies should therefore tend to rotate in a preferred direction"
    > "The mean values of the right ascension and declination of the preferred axis are therefore"
    > "showed a large-scale bulk flow of galaxy clusters with speed 630 km/s"
    > "Applying the law of cosines to this triangle gives"
    > "The cosmological constant generated by the rotation of the universe would not be constant"
    > "Because the angular momentum of the universe is conserved, the angular velocity of the universe decreases as the universe expands"
[7] https://arxiv.org/abs/1007.0587v2 — arXiv:1007.0587v2 metadata
    > "Subjects: | Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc); High Energy Physics - Theory (hep-th)"
    > "Sun, 4 Jul 2010 21:29:24 UTC (9 KB)"
    > "Tue, 2 Nov 2010 18:13:25 UTC (12 KB)"
[9] https://arxiv.org/abs/1410.3881v2 — arXiv:1410.3881v2 metadata
    > "Subjects: | General Relativity and Quantum Cosmology (gr-qc); Cosmology and Nongalactic Astrophysics (astro-ph.CO); High Energy Physics - Theory (hep-th)"
    > "Astrophys. J. 832, 96 (2016)"
    > "Tue, 14 Oct 2014 22:27:54 UTC (13 KB)"
    > "Tue, 26 May 2026 20:13:54 UTC (16 KB)"
[10] https://arxiv.org/abs/1910.10819v1 — arXiv:1910.10819v1 metadata
    > "Title:Black Hole Genesis and origin of inertia"
    > "Comments: | 2 pages"
[11] https://arxiv.org/abs/1910.10819v2 — arXiv:1910.10819v2 metadata
    > "Subjects: | Popular Physics (physics.pop-ph); Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc)"
    > "Comments: | 5 pages"
    > "Wed, 23 Oct 2019 21:59:53 UTC (5 KB)"
    > "Thu, 29 May 2025 23:59:54 UTC (9 KB)"
[13] https://arxiv.org/abs/2509.11468v2 — arXiv:2509.11468v2 metadata
    > "Subjects: | General Relativity and Quantum Cosmology (gr-qc); Cosmology and Nongalactic Astrophysics (astro-ph.CO)"
    > "Int. J. Mod. Phys. A 40, 2544007 (2025)"
    > "Sun, 14 Sep 2025 23:21:23 UTC (9 KB)"
    > "Wed, 19 Nov 2025 22:38:22 UTC (8 KB)"
[18] https://inspirehep.net/api/arxiv/1910.10819 — INSPIRE arXiv:1910.10819
    > "Universe in a rotating black hole and preferred axis"
[22] https://ui.adsabs.harvard.edu/abs/arXiv:1910.10819/abstract — NASA ADS arXiv:1910.10819
    > "Publication: arXiv e-prints"
[24] https://api.crossref.org/works/10.1016/j.physletb.2010.09.056 — Crossref 10.1016/j.physletb.2010.09.056
    > "Cosmology with torsion: An alternative to cosmic inflation"
[25] https://api.crossref.org/works/10.1016/j.physletb.2011.05.047 — Crossref 10.1016/j.physletb.2011.05.047
    > "Physics Letters B"
[26] https://api.crossref.org/works/10.3847/0004-637X/832/2/96 — Crossref 10.3847/0004-637X/832/2/96
    > "The Astrophysical Journal"
[27] https://api.crossref.org/works/10.1142/S0217751X25440075 — Crossref 10.1142/S0217751X25440075
    > "Gravitational collapse with torsion and universe in a black hole"
[28] https://api.crossref.org/works?filter=orcid:0000-0001-5593-313X&rows=100&select=DOI,title,author,published,container-title,type — Crossref works with Poplawski ORCID
    > "Total results: 10"
[29] https://inspirehep.net/api/literature?q=title%20%22Universe%20in%20a%20rotating%20black%20hole%20and%20preferred%20axis%22&size=25 — INSPIRE exact-title search
    > "Total: 1 Control number: 1760842"
[30] https://inspirehep.net/api/literature?q=a%20Poplawski%2C%20Nikodem%20and%20title%20rotat*&size=100 — INSPIRE Poplawski rotating-title search
    > "Total: 1 Control number: 1760842"
[31] https://ui.adsabs.harvard.edu/search/q=title%3A%22Universe%20in%20a%20rotating%20black%20hole%20and%20preferred%20axis%22&sort=date%20desc%2C%20bibcode%20desc&p_=0 — ADS exact-title search
    > "Your search returned 1 results"
[32] https://ui.adsabs.harvard.edu/search/q=title%3A%22Universe%20in%20a%20rotating%20black%20hole%20and%20preferred%20axis%22%20property%3Arefereed&sort=date%20desc%2C%20bibcode%20desc&p_=0 — ADS exact-title refereed search
    > "Your search returned 0 results"
