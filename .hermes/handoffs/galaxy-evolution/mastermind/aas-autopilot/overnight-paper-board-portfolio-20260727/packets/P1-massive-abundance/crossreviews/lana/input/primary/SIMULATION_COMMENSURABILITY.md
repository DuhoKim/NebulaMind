# Simulation Commensurability

## Named TNG Identity

The served manuscript identifies the simulation comparison as IllustrisTNG TNG100-1 and quotes counts in a `(110.7 Mpc)^3` box. The public TNG data-release paper identifies IllustrisTNG as a cosmological magnetohydrodynamical suite with TNG100 and TNG300 publicly released, 100 snapshots, and Planck-like cosmology; it also cautions that TNG100 balances volume and resolution rather than maximizing rare-object statistics.

Public TNG convention checks support that `SubhaloMassInRadType[4]` is a stellar mass within twice the stellar half-mass radius, while `SubhaloMassType[4]` is all mass bound to the subhalo. TNG forum guidance also says the closest mass definition to the observations should be used, with `SubhaloMassInRadType[4]` a common starting point. These definitions support the manuscript's distinction between the historical 2Rhalf count and the later all-bound/total count.

## What Matches

- Statistic requested: cumulative `n(>Mstar,z)`.
- Threshold: `Mstar > 10^10.5 Msun`.
- Redshift anchor: z=5 for the headline comparison, with z=6 listed as a redshift-sensitivity caveat.
- Aperture reconciliation: historical `2 x R_half` TNG mass gives `N=15`, `n=1.11e-5 Mpc^-3`; all-bound `SubhaloMassType` gives `N=20`, `n=1.47e-5 Mpc^-3`.
- Threshold reconciliation: using observed `n~3e-5`, the raw aperture excess is about 2.7x or 0.43 dex, requiring `0.43/1.58 = 0.27-0.28 dex`; the all-bound footing excess is 2.04x or 0.31 dex, requiring `0.31/1.58 = 0.20 dex`.

## What Does Not Yet Match

- The TNG counts are reported by the served manuscript, not independently reproduced from the TNG catalogs in this lane.
- The TNG galaxy population is not separated into centrals and satellites. A total subhalo GSMF does not map one-to-one to a distinct-host analytic HMF without occupancy accounting.
- There is no mock-observed TNG SED pipeline, no matched photometric selection, and no redshift/mass posterior forward model.
- The observed source is a rest-optical-selected JWST GSMF. The manuscript treats its masses as total-galaxy SED masses, but the exact IMF/aperture convention is not carried into every comparison row.
- Box variance and missing large-scale modes are not propagated beyond the Poisson floor from 15-20 simulated objects.

## Native Ratio Versus Analytic Proxy

The manuscript's `epsilon = Mstar/(fb Mhalo)` benchmark uses an analytic halo mass function abundance match. That is an effective deterministic abundance-matching conversion factor. It is not the native baryon-conversion ratio achieved by individual TNG central galaxies.

A native TNG physical ratio would require matching central galaxies to parent haloes, choosing a halo mass definition such as `M200c`, using a defined stellar aperture, and reporting the median and scatter of `Mstar/(fb M200c)`. The served manuscript does not perform that native diagnostic, so claims about LCDM physical feasibility should remain a ceiling/proxy statement rather than a TNG-achieved-efficiency statement.

## Figure Representation

The page-3 visual inspection of the pinned PDF found a stale label in Figure 1: the arrow annotation says `erased by 0.28 dex Mstar`, while the same figure caption and prose say the total-mass-footing correction is `0.20 dex`. This is a representation defect. It does not erase the later calculation, but it prevents a clean pass for artifact consistency.

## Verdict

`PARTIAL`: the aperture/count reconciliation is conceptually right and the 0.28-to-0.20 arithmetic is internally consistent. The comparison is not fully commensurable until the observed cumulative density is directly sourced, TNG counts are reproducibly regenerated or pinned as data output, central/satellite and selection differences are recorded, and volume/scatter/occupancy are propagated.
