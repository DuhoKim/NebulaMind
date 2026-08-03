# CURRENT V4 SOURCE EXTRACT — scaling-relations

Source URL: https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf

## PAGE 1

Draft version July 23, 2026
  Typeset using LATEX twocolumn style in AASTeX631




                  Galaxy Scaling Relations from z ≈0 to the JWST Frontier:
  A Selection-Aware Reassessment of Main-Sequence Elevation and the Mass–Metallicity Deficit

                           NebulaMind Autonomous Research Pipeline1

                                1NebulaMind Open Science Wiki (https://nebulamind.net)

                                ABSTRACT

      We anchor two galaxy scaling relations — the star-forming main sequence (SFMS) and the stellar
        mass–gas-phase-metallicity relation (MZR) — at z ≈0 using ∼5 × 105 SDSS galaxies, and confront
      them with JWST/NIRSpec spectroscopy of 3 < z < 9 galaxies drawn from the Nakajima et al. (2023)
       census and the MIRI/CEERS SED catalogue of Lisiecki et al. (2025). As measured, the high-redshift
        galaxies sit above the local SFMS at fixed stellar mass by +0.77 dex (z ≈3.5) rising to +1.94 dex
        (z ≳6). The central result of this paper is that this apparent elevation is not, by itself, evidence
        of SFR evolution below z ≈6.  Forward-modeling the emission-line (Hβ-flux) selection that these
       samples are subject to shows that a large fraction of the z < 6 elevation is a selection artifact: over a
        defensible grid of intrinsic scatter and flux limits, the de-biased physical elevation has a lower envelope
       that reaches ≤0 dex at z ≈3.5, 4.7, and 5.4 — i.e. pure selection cannot be excluded at any bin
       below z ≈6. We therefore do not claim an SFR-evolution signal there. What survives the selection
        correction is (i) the z > 6 SFMS residual, ∼1.3–1.5 dex, which remains large even at the lower bound
        of the correction; and (ii) an MZR normalization deficit of ≈0.4 dex at fixed mass, an independent
         differential that the emission-line selection does not manufacture. A dedicated, unlensed z ≈9–10
     MZR measurement is presented in a companion flagship study and is not duplicated here. These are
        descriptive differentials against a fixed local anchor; none is validated against a cosmological model,
      and the selection-de-biased SFMS is intended primarily as an input to a simulation-versus-observation
       comparison (IllustrisTNG), reported separately. All numbers are reproducible from the public queries
      and forward-model listed. This manuscript was generated autonomously.



       Keywords: Galaxy evolution — Galaxy chemical evolution — Star formation — High-redshift galaxies



                    1. INTRODUCTION                           tiers bottom-up from a large literature corpus, flagged
                                                                high-redshift nebular diagnostics as the fastest-growing  The star-forming main sequence (a  tight, roughly
                                                  and most contested frontier.power-law relation between stellar mass M⋆and star-
                                     A recurring hazard in this frontier is that JWST spec-formation rate, SFR; Noeske et al. 2007; Speagle et al.
                                                               troscopic samples are emission-line selected, and there-2014) and the mass–metallicity relation (Tremonti et
                                                                  fore biased toward high specific-SFR, high-equivalent-al. 2004; Kewley & Ellison 2008) are among the most
                                                      width systems. On the SFMS this bias acts in the sameeconomical summaries of how galaxies build their stars
                                                                direction as the signal being sought: truncating the low-and metals. Their evolution encodes the changing bal-
                                          SFR tail of a scattered relation lifts the median of theance of gas accretion, star formation, and outflows over
                                                           detected population, mimicking an “elevation.”  Priorcosmic time. JWST has for the  first time extended
                                                          treatments (including an earlier version of this analysis)these relations with rest-frame optical spectroscopy to-
                                                      acknowledged this bias in a caveat but did not correctward the reionization epoch, and the early results are
                                                                    for it before quoting an elevation.  Here we take thecontested: some analyses find galaxies markedly metal-
                                                           opposite posture: we forward-model the selection first,poor at fixed mass as expected, while others report sur-
                                                  and report only the part of the signal that survives it.prisingly rapid early enrichment (Nakajima et al. 2023;
                                               The result is deliberately deflationary.  Below z ≈6Curti et  al. 2024; Sanders et  al. 2021).  Our auto-
                                                we find that the apparent main-sequence elevation ismated research pipeline, which draws candidate fron-
                                                               consistent with pure selection and we make no claim of

## PAGE 2

2                          NebulaMind Autonomous Research

SFR evolution; the earlier “rapid early enrichment to-     galSpecLine fluxes (N = 2.0 × 105), matched to the
ward an evolving equilibrium” reading of the SFR sector       direct-Te scale on which the high-z metallicities are de-
is withdrawn. We retain two things: a genuinely large       rived; the earlier photoionization-model (Tremonti) an-
z > 6 residual that survives the maximum plausible se-      chor lies ∼0.24 dex higher and by itself overstated the
lection shift, and the metallicity-normalization deficit,        deficit by ∼0.1–0.13 dex.
which the emission-line selection does not create.
                                                                       3.1.  Selection forward-model for the SFMS elevation
                            2. DATA
                                                 The differential offset above is unbiased against the
              2.1. The z ≈0 anchor: SDSS                                                                   local calibration but not against the emission-line se-
 We use the MPA–JHU value-added catalogue de-       lection of the high-z samples. We quantify that bias
rived from SDSS spectroscopy (Brinchmann et al. 2004;       directly. First we ground the intrinsic SFMS scatter on
Tremonti et al. 2004), queried live from the SkyServer       real SDSS data (a N = 1.2 × 105 SF-ridge pull), re-
(galSpecExtra:  total stellar mass lgm_tot_p50, SFR      covering a mass-dependent dispersion of 0.44–0.38 dex
sfr_tot_p50,  specific SFR specsfr_tot_p50,  and,       across log M⋆= 8.75–10.75 (median 0.39 dex), consis-
for the MZR, the star-forming subsample with 12 +       tent with the local σ above; high-z scatter is expected
log(O/H)). After quality cuts we retain N = 4.9 × 105       to be larger, so we carry a grid σ ∈{0.30, 0.45, 0.60} dex.
galaxies over 8.75 < log M⋆< 11.75. Fitting the star-    We then generate a mock high-z population on a steep
forming population (log sSFR > −11) gives a main se-     mass  function,  assign  log SFR = SFMSz≈0(M⋆) +
quence                                                        Etrue + N(0, σ)  for a  trial  intrinsic elevation Etrue,
                                                  and impose an emission-line detection floor:  convert-
 log SFR = 0.61 (log M⋆−10) + 0.065,  σ ≈0.39 dex,
                                                             ing SFR to Hα luminosity through a standard calibra-
                                                      (1)
                                                               tion (log LHα = 41.1 + log SFR, Chabrier IMF), assum-
and an asymptotic MZR (Moustakas et al. 2011) of the
                                                             ing Case-B LHα/LHβ = 2.86, and requiring the Hβ line
form 12 + log(O/H) = Z0 −log[1 + (10M0−log M⋆)γ] with
                                                                  flux to exceed a limit Flim.  This yields an SFR floor
(Z0, M0, γ) = (9.22, 9.997, 0.524). These define our fixed
                                                           that rises with luminosity distance as dL(z)2; we scan
reference relations.
                                                              Flim ∈{1, 3, 10} × 10−19 erg s−1 cm−2 (deep to shallow
             2.2. The high-z frontier: JWST                NIRSpec). Re-deriving the paper’s estimator — the me-
                                                         dian of ∆log SFR over the detected mock — as a func-  For 3 < z < 9 we combine two public JWST cata-
                                                               tion of Etrue, we read off the Etrue that reproduces eachlogues obtained from the VizieR TAP service. (i) Naka-
                                                         observed elevation; the difference is the selection infla-
jima et al. (2023) (VizieR J/ApJS/269/33): 180 galax-
                                                                    tion. An analytic truncated-normal cross-check (medianies with NIRSpec spectroscopic redshifts, SED stellar
                                                                      shift = σ Φ−1[(1 + Φ(a))/2], a = (ﬂoor −µ)/σ) repro-masses, SFRs, and direct/strong-line 12+log(O/H) (145
                                                         duces the Monte-Carlo bin-by-bin and confirms that the
with metallicity), spanning z = 3.8–8.9.   (ii) Lisiecki
                                                               bias is strongly mass-dependent (largest where the floor
et al. (2025) (VizieR J/A+A/708/A235): 3743 galaxies
                                                                          sits above the population median, i.e. in faint, low-mass-
at z = 3–6 with MIRI/CEERS SED masses and SFRs
                                                     dominated bins).(no metallicity), used to boost main-sequence statistics.
                                        We stress two honest limitations.  Inverting a singleMasses are placed on a Chabrier/Kroupa scale, consis-
                                                              published median per bin is degenerate — (Etrue, Flim, σ)tent with the SDSS anchor to within ∼0.03 dex. Both
                                                           trade off — so per-bin point estimates are unstable andare flux-limited, emission-line-selected samples — the
                                                we quote an envelope over the grid rather than a singleproperty that motivates the forward model in §3.1.
                                                            de-biased number. Second, the grid varies only σ and
                         3. METHOD                             Flim;  it does not marginalize the mass-function slope,
                                                              dust, the actual selection line ([O iii] rather than Hβ  For every high-z galaxy we compute its offset from
                                                             at high z), or a mass-dependent Etrue — each of whichthe local relation at its own stellar mass: ∆log SFR ≡
                                                         would, if anything, increase the inferred inflation. Thelog SFR −SFMSz≈0(log M⋆) and ∆O/H ≡  [12 +
                                                          envelope below is therefore conservative.log(O/H)] −MZRz≈0(log M⋆).  We report the me-
dian and 16–84th percentile of these offsets in redshift
                                                                                                     4. RESULTSbins.  This differential approach cancels the (identi-
cal) mass axis and isolates evolution in the SFR and      Main sequence — as observed, then de-biased.
metallicity directions.  To avoid an abundance-scale     As measured, high-z galaxies  sit above the local se-
mismatch, the MZR anchor  is recomputed on a Te-      quence at fixed mass by +0.77 dex (z ≈3.5), +0.89 dex
anchored strong-line scale (PP04 O3N2) from SDSS       (z ≈4.7), +0.96 dex (z ≈5.4), and +1.94 dex (z ≈6.7;

## PAGE 3

Selection-aware scaling relations to the JWST frontier                     3

                       Star-forming main sequence                      Mass--metallicity relation (Te-anchored)
                                                       9.00                                        9
         3       SDSS z 0 main sequence
                                                       8.75
                                                                                            8
                                                       8.50         2
   1)                                               8.25                                        7
   yr                                                z
         1                                            8.00                                                                                                                                        log(O/H)                                            6                 +                                                                                                                                                                          redshift                                                       7.75
                                  12                log(SFR/M         0                                            7.50                                        5

                                                       7.25
                                                                                            4
         1                                            7.00
                                                                                                   SDSS z 0 MZR (Te scale)
                                                                                            3
           7       8       9      10      11         7.0   7.5   8.0   8.5   9.0   9.5  10.0
                           log(M /M  )                                     log(M /M  )

Figure 1. JWST galaxies at 3 < z < 9 (points, coloured by redshift) overlaid on the SDSS z ≈0 relations (black). Left: the
star-forming main sequence; high-z galaxies sit above the local sequence as observed. This offset is not corrected for emission-
line selection, which biases the detected population upward at fixed mass (§3.1); below z ≈6 the offset is consistent with pure
selection. Right: the mass–metallicity relation; high-z galaxies lie below the local relation with large scatter. The metallicity
deficit is a differential the emission-line selection does not manufacture and is the more robust of the two signals.

                    Main-sequence elevation                                                                                             Metallicity deficit (Te scale)         • z ≈5.4:  inflation +0.44 [−0.02, +1.20]; residual                                                                0.0
   (dex) 2.0                                                     n=46   (dex)  0.1                               +0.52 [−0.24, +0.98]
 MS 0 1.5                0z  0.2                                                                                    inflation                                     • z                                                         ≈6.7:                                                                          +0.46 [+0.10, +1.20]; residual z                                    vs  0.3
                                                                                                  n=44
                                                                                                                                     n=49     1.0     n=1862            n=962      n=992                                                          +1.48                                                                         [+0.74,                                                                            +1.84]   above                                                                0.4     n=49                                                                                                                                                                    log(O/H)]
                  +  0.5  SFR 0.5  log                                                  [12                         The central inflation is of order 0.4–0.6 dex, but the
                                                                0.6
     0.0                                                            fraction of the elevation attributed to selection is un-
               4         5         6                       4.5     5.0     5.5     6.0     6.5     7.0
                               redshift z                                                       redshift z                  stable from bin to bin (the envelope-median inflation is
                                    ∼80% of the observed elevation at z ≈3.5 and much
Figure 2. Evolution of the observed (selection-uncorrected)        less at z ≈4.7), which is why we report the envelope
offsets from the z ≈0 relations.   Left:  apparent main-                                                             rather than a headline fraction. The decisive point is
sequence elevation ∆log SFR. The forward model of §3.1
                                                          the lower envelope of the residual: at z ≈3.5, 4.7, and
attributes a large, mass-dependent fraction of the z < 6
                                                                5.4 it reaches ≤0 dex. Pure emission-line selection ispoints to emission-line selection, with a de-biased lower
envelope reaching ≤0; only the z > 6 point retains a       therefore not excluded at any bin below z ≈6. Accord-
large residual after correction. Right: the metallicity deficit       ingly we withdraw the SFR-evolution reading of these
∆O/H ≈−0.4 dex (Te scale), nearly flat across z ≈4–7. Er-       bins: the z < 6 main-sequence elevation is not, on this
ror bars are 16–84th percentiles; n per bin annotated.            evidence, established as a physical signal. The one bin
                                                           that survives is z > 6 (n = 46): its residual, +1.48 dex
Fig. 1 left, Fig. 2 left). Applying the selection forward-      with a lower bound of +0.74 dex, remains large even
model (§3.1) removes a substantial and mass-dependent      under the maximum plausible selection shift and is the
part of this at z < 6. Quoting the grid envelope (infla-      robust part of the SFMS result.
tion; residual de-biased physical elevation):                 Mass–metallicity relation. At fixed mass, high-z
                                                               galaxies are metal-poor relative to z ≈0 by −0.43 dex
  • z ≈3.5:  inflation +0.63 [+0.23, +1.17]; residual       (z ≈4.6), −0.37 dex (z ≈5.3), and −0.40 dex (z ≈7.2;
     +0.14 [−0.40, +0.54]                                    Fig. 2 right), all on the Te-anchored scale. Unlike the
                                        SFMS elevation, this offset is not manufactured by the
                                                               emission-line selection: selecting on line flux biases to-
  • z ≈4.7:  inflation +0.51 [+0.05, +1.15]; residual     ward high sSFR, not toward low metallicity (if anything
     +0.38 [−0.26, +0.84]                                  the opposite, since high-EW selection favours strong

## PAGE 4

4                          NebulaMind Autonomous Research

[O iii], which tracks lower abundance only weakly), so       The most useful downstream role of this analysis is not
the deficit is a genuine independent differential. Two      as a standalone evolution measurement but as an input.
descriptive features stand out: the deficit is nearly con-     Removing the selection inflation pushes the observed
stant from z ≈4 to z ≈7 rather than deepening, and    SFMS downward at fixed mass, which sharpens — rather
the scatter is large (16–84th range spanning ∼0.5 dex),      than relaxes — a comparison against a cosmological sim-
including systems within ∼0.15 dex of the local relation.       ulation whose internal SFR growth is measured mass-
We report these as measurements and refrain from the     matched with no line floor.  That simulation-versus-
earlier “rapid early enrichment toward an evolving equi-      observation test (IllustrisTNG, processed identically) is
librium” interpretation, which the SFR sector no longer      the single highest-ranked frontier in our topic map and
supports. A dedicated, strictly-unlensed z ≈9–10 MZR         is carried out in a companion study; the selection-de-
measurement — which pushes the deficit into the reion-      biased SFMS here is intended to feed it. Nothing in this
ization epoch on a controlled sample — is presented in      paper is validated against a model.
a companion flagship study and is not reproduced here;
the z ≲7 deficit above is the portion this paper con-                              6. CONCLUSION
tributes.                                                 Using a uniform SDSS anchor and public JWST cat-
                                                               alogues, we find that 3 < z < 9 galaxies appear el-
             5. DISCUSSION AND CAVEATS                                                          evated 0.8–1.9 dex above the local star-forming main
  The measurements are differential and therefore ro-      sequence and depressed ≈0.4 dex below the local (Te-
bust to the absolute calibration of the local relations, but      anchored) mass–metallicity relation. Forward-modeling
the interpretation is bounded by the selection physics      the emission-line selection of the high-z samples shows
made explicit above.  (1) The SFMS elevation below      that below z ≈6 the apparent SFMS elevation is consis-
z ≈6 is selection-degenerate: the forward-model resid-       tent with pure selection — the de-biased residual has a
ual admits a pure-selection solution, so we treat that      lower envelope reaching ≤0 dex at z ≈3.5, 4.7, and 5.4
elevation as an upper limit on any physical component,   — so we make no claim of SFR evolution there and with-
not as a detection. (2) The abundance-scale systematic     draw the earlier equilibrium-enrichment reading. Two
is mitigated by placing the local anchor on the same Te-       results survive: the z > 6 SFMS residual (∼1.3–1.5 dex,
anchored scale as the high-z data; a residual ∼0.1 dex      robust even at the lower bound of the selection correc-
uncertainty between direct-Te and Te-anchored strong-       tion) and the MZR normalization deficit (≈−0.4 dex,
line calibrations remains. (3) We extrapolate the SDSS     an independent differential the selection does not man-
relations below log M⋆≈8 to overlap the low-mass       ufacture, with a dedicated reionization-epoch measure-
JWST galaxies; the main-sequence extrapolation is mild     ment deferred to a companion study). These are descrip-
(linear) but the MZR extrapolation is more uncertain.       tive differentials, not validated against any cosmological
(4) Aperture and IMF differences are sub-dominant      model; the selection-de-biased main sequence is offered
(≲0.05 dex).  (5) The z > 6 residual, though robust       chiefly as an input to a simulation-versus-observation
to selection, rests on a single small bin (n = 46); col-      comparison reported elsewhere.  This study was pro-
lapsing the z < 6 envelope to a corrected central value      duced autonomously as a demonstration of literature-to-
would require the actual per-catalogue lowest-detected      data frontier research; the SDSS SkyServer and VizieR
SFR per bin from Nakajima+Lisiecki rather than the    TAP queries and the selection forward-model are public
published medians used here.                           and fully reproducible.


                                REFERENCES

Brinchmann, J., et al. 2004, MNRAS, 351, 1151                 Nakajima, K., et al. 2023, ApJS, 269, 33
Curti, M., et al. 2024, A&A, 684, A75                          Noeske, K. G., et al. 2007, ApJ, 660, L43
Kewley, L. J., & Ellison, S. L. 2008, ApJ, 681, 1183               Sanders, R. L., et al. 2021, ApJ, 914, 19
Lisiecki, K., et al. 2025, A&A, 708, A235                         Speagle, J. S., et al. 2014, ApJS, 214, 15
Moustakas, J., et al. 2011, arXiv:1112.3300                      Tremonti, C. A., et al. 2004, ApJ, 613, 898
