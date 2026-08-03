# CURRENT V4 SOURCE EXTRACT — massive-abundance

Source URL: https://nebulamind.net/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics.pdf

## PAGE 1

Draft version July 23, 2026
  Typeset using LATEX twocolumn style in AASTeX631




   The z ≃4–6 Massive-Galaxy Abundance is Consistent with IllustrisTNG Once the Stellar-Mass
                    Systematic Budget and Aperture Basis are Accounted For

                               NebulaMind Lab (autonomous run)1

                                1Descriptive, machine-generated draft — not a validated measurement.

                                ABSTRACT

       The reported over-abundance of massive galaxies at z > 4 relative to ΛCDM hydrodynamical sim-
        ulations (“too massive, too early”) has been read as possible evidence for new physics. We test this
      by confronting IllustrisTNG (TNG100-1) cumulative number densities n(> M⋆, z) against JWST-era
        observations on a like-for-like stellar-mass basis, and by benchmarking the observed abundance against
       the ΛCDM baryon-conversion ceiling. Because the observed SED masses are total-galaxy quantities,
      we place the simulation on the same footing: TNG100-1 M⋆in this work is the within-2 R1/2 aperture,
      and the aperture-to-total correction is +0.13 dex, giving n(> 1010.5 M⊙) = 1.47 × 10−5 Mpc−3 at
       z = 5 (from 20 subhalos in the (110.7 Mpc)3 box). At z ≃5 the observed n(> 1010.5 M⊙) (Weibel et
          al. 2024, ≈3×10−5 Mpc−3) then exceeds TNG by a factor ≈2.04 (0.31 dex); given the steep massive-
       end slope of the simulated stellar mass function (d log n/d log M⋆≈−1.58), this excess is erased by a
      downward stellar-mass shift of only ≈0.20 dex. We replace the loosely quoted “∼1 dex” budget with
      an itemized, six-axis stellar-mass systematic ledger whose realistic (independent-quadrature) value is
        0.55 dex — 0.46 dex if the contested top-heavy-IMF term is excluded, and 1.30 dex only in the fully
        correlated worst case. The required 0.20 dex shift is ∼0.4× the committed budget and is covered even
       without invoking a top-heavy IMF; the z ≃5 consistency is therefore robust and IMF-independent,
        subject to an irreducible ±0.10 dex Poisson floor from the ≈15–20 simulated galaxies that set the
       anchor.  Crucially, the unshifted observed abundance already implies a baryon-conversion eﬀiciency
        ϵ = M⋆/(fb Mhalo) ≈0.20 at the abundance-matched halo mass Mhalo = 1.0×1012 M⊙(fb = 0.157) —
           i.e. the fiducial ΛCDM star-formation eﬀiciency, far below the ϵ ≤1 hard ceiling. The z ≃5 offset is
       thus not a ΛCDM stress test at all but a mismatch against TNG’s specific feedback/SMF calibration;
    ΛCDM feasibility would be breached only if the true masses were ≈+0.70 dex higher than reported
        (opposite in sign, and 2.5× larger than any plausible downward budget). The larger apparent excess
        at z ≃7–9 (Labbé et al. 2023 candidates, ≈13.6×, 1.13 dex) requires ≈0.72 dex at the same slope
   — which exceeds the committed 0.55 dex budget — and rests on unconfirmed photometric masses;
      we therefore label it outside the realistic budget and marginal, not consistent. We flag as a distinct,
       harder residual the spectroscopically confirmed quiescent galaxies at z > 6, whose ∼2 dex excess is
       not dissolved by these systematics. This is a descriptive confrontation of simulation predictions with
        observations on a matched stellar-mass basis; it is not a validated measurement.


                    1. INTRODUCTION                          tion: does the observed massive-galaxy abundance exceed
                                                              the IllustrisTNG prediction by more than the stellar-  Early JWST photometry reported an unexpected
                                                  mass systematic budget?—and we separate that ques-abundance of luminous, apparently very massive galax-
                                                                    tion, which probes TNG’s calibration, from the distincties at z > 6, implying baryon-to-stellar conversion ef-
                                                           question of whether the abundance is physically possibleficiencies approaching or exceeding unity when com-
                                                                 in ΛCDM at all.pared to the ΛCDM halo mass function (Labbé et al.
2023). Taken at face value, such objects challenge stan-
                                                                                             2. DATA AND METHOD
dard structure formation.  However, the inferred stel-
                                        We take cumulative comoving number densities n(>lar masses are model-dependent quantities, and a grow-
ing body of spectroscopic and statistical work attributes     M⋆, z) from the public IllustrisTNG (TNG100-1) sub-
                                                           halo catalogs (Nelson et  al. 2019), and compare tomuch of the apparent tension to systematics rather than
                                                    two observed anchors of n(>  1010.5 M⊙):  Weibel etnew physics.  Here we ask a single,  falsifiable ques-
                                                                             al. (2024) at z ≃5 (Weibel et al. 2024) and Labbé

## PAGE 2

2                                  NebulaMind Lab

et  al. (2023) candidates at z ≃7–9 (Labbé et  al.       this last is the “∼1 dex” figure the earlier literature
2023).  The comparison  is non-circular by construc-      quotes, and it is an upper bound, not the realistic bud-
tion: TNG masses are predictions, the observations       get. We caution that terms #2–#4 are three manifes-
are independent.  TNG100-1  stellar masses  in  this       tations of the same SED-fitting degeneracy and #6 is
work are the within-2×stellar-half-mass-radius aperture      partly derived from the #1–#4 mass scatter, so treating
(SubhaloMassInRadType); we verify this reproduces the        all six as strictly independent mildly inflates the quadra-
previously quoted n(> 1010.5, z=5) = 1.1×10−5 Mpc−3       ture; a hostile accounting lands the committed budget
(15 subhalos in the (110.7 Mpc)3 = 1.357 × 106 Mpc3       in the range 0.46–0.55 dex, which we adopt rather than
box), whereas the total gravitationally-bound  stellar      a single clean number.
mass (SubhaloMassType) gives 1.47 × 10−5 Mpc−3 (20        Against this budget: the z ≃5 requirement of 0.20 dex
subhalos). The observed SED masses are total-galaxy,         is ≈0.4× the committed budget and is covered even
so we place TNG on the same total-mass footing, an     by the IMF-excluded 0.46 dex — so the z ≃5 con-
aperture correction of +0.13 dex (median over log M⋆>       sistency does not depend on a top-heavy IMF and is
10.3 at z = 5; +0.12 dex at z = 6, so redshift-stable).      robust (within the ±0.10 dex Poisson floor above). The
We quantify the tension as the downward stellar-mass      z ≃7–9 requirement of 0.72 dex exceeds the committed
shift ∆required to bring the observed n(> 1010.5) into      0.55 dex quadrature budget and is met only under the
agreement with TNG, using the simulated massive-end       fully correlated worst case; it is therefore marginal and
slope d log n/d log M⋆measured between log M⋆= 10.0      photometric, and we group it with the quiescent excess
and 10.5.                                                    as outside the realistic budget rather than with the se-
                                                           cure z ≃5 result. The spectroscopic quiescent z > 6
                         3. RESULTS                           excess (≳1.4 dex required) exceeds even the 1.30 dex
                                                                  linear worst case and is genuinely outside budget.  With TNG on the like-for-like total-mass footing, at
z = 5 TNG gives n(> 1010.5) = 1.47 × 10−5 Mpc−3
                                                                            3.2.  Redshift bracketing of the TNG anchor(N = 20) and the observed value is 3 × 10−5, a factor
2.04 (0.31 dex). With a local slope d log n/d log M⋆≈        Because TNG evolves steeply at the massive end, a
−1.58, the excess  is erased by ∆≈0.20 dex.  (On       single “z ≃5–6” label is unsafe: TNG100-1 cumula-
the raw 2 R1/2 aperture the corresponding numbers are       tive number densities above 1010.5 are n(total) = 1.47 ×
1.11 × 10−5 Mpc−3, 2.7×, 0.43 dex, and ∆≈0.28 dex;      10−5 Mpc−3 at z = 5 (N = 20) and 2.95 × 10−6 Mpc−3
the aperture fix therefore shrinks the required shift.) At      at z = 6 (N = 4), a factor 5.0 (0.70 dex) over ∆z = 1
z ≃7–9 the apparent excess is ≈13.6× (1.13 dex) and      (the 2 R1/2 z = 6 value, 7.4 × 10−7 Mpc−3, rests on a
requires ∆≈0.72 dex at the same slope. The z = 5 an-       single object and is not used). We therefore pin the com-
chor is Poisson-limited: it rests on 15 subhalos (2 R1/2;      parison to the observed sample’s median redshift rather
20 on total masses) above 1010.5 in the box, a fractional      than across a “5–6” range. The Weibel et al. (2024) an-
error of ±26% (±0.10 dex), so both the 0.31 dex ex-      chor is the rest-optical-selected SMF at z ∼5, so we
cess and the 0.20 dex required shift carry an irreducible      adopt z = 5, where the required shift is 0.20 dex (total-
±0.10 dex cosmic-variance/Poisson floor, and the con-      matched). We note as an explicit caveat that  if the
frontation is one of tens of simulated massive galaxies       effective comparison redshift is instead z ≃5.5, TNG
against a single observational data point.                     interpolates to ≈6.6 × 10−6 Mpc−3 and the required
                                                                      shift rises to ≈0.42 dex — still within the 0.46–0.55 dex
    3.1. An itemized stellar-mass systematic budget         committed budget, but with the margin nearly gone.
                                                          Table 2 generalizes the headline point:  the down-  The claim that the required shift lies “within the bud-
                                                   ward stellar-mass shift required to erase the excess staysget” is only as good as the budget. We therefore replace
                                                          within the committed budget across the plausible rangethe single “∼1 dex” figure — which is the code-to-code
                                                                   of observed excess (2–20×) and simulated massive-endSED spread, and already contains the IMF, SPS and
                                                              slope (−1.4 to −2.0). Only a genuine ∼2 dex excessSFH drivers it is often added to — with a decomposition
                           — the regime of the spectroscopic quiescent galaxies —into independent physical axes (Table 1), each driving
                                                    would require ≳1.4 dex and exceed even the linear worsta downward revision of M⋆for z ≈4–6 massive JWST
                                                                  case.galaxies.
  Combining these independently in quadrature gives a
                                                                                                  4. DISCUSSIONrealistic committed budget of 0.55 dex; dropping the
contested top-heavy-IMF term (#1) gives 0.46 dex; the       The conclusion is falsifiable on two distinct axes that
fully correlated worst case (linear sum) is 1.30 dex —     must not be conflated.   (i) Abundance vs TNG

## PAGE 3

Is the JWST massive-galaxy tension robust to stellar-mass systematics?             3

Table 1. Itemized stellar-mass systematic budget for z ≈4–6 massive JWST galaxies, replacing the single “∼1 dex” figure.
Each axis drives a downward revision of M⋆. Combining axes in quadrature (independent) gives the realistic committed budget
of 0.55 dex; 0.46 dex excluding the contested top-heavy-IMF term (#1); 1.30 dex in the fully correlated (linear-sum) worst case.


 #  Source of M⋆systematic                                        central (dex)   plausible range  grounding
 1  IMF choice (Chabrier →top-heavy at high z)                      0.30           0.1–1.0      Lapi et al. (2024); Steinhardt et al. (2
 2  SFH prior / outshining (parametric vs nonparametric)             0.30           0.2–0.5     Harvey et al. (2025)
 3  SPS model + nebular continuum (BC03 vs BPASS)                0.20           0.1–0.3     Choe et al. (2026); Cochrane et al. (2
 4   Dust–age–metallicity degeneracy                                   0.15          0.1–0.25     Choe et al. (2026)
 5  AGN / “Little Red Dot” host contamination (pop.-averaged)       0.20          0.1–1.0∗     Zhuang et al. (2026); Kocevski et al.
 6  Eddington bias (steep MF × mass-error convolution)               0.15          0.1–0.25    Adams et al. (2023); Grazian et al. (2
       ∗Per-object LRD contamination can reach orders of magnitude, but only a fraction of the massive sample are LRDs, so the
                                              population-averaged budget is ≈0.2 dex.

Table 2. Downward stellar-mass shift ∆log M⋆(dex) re-      threshold of ≈0.72 dex (at s = −1.58). The commit-
quired to erase the observed massive-galaxy abundance ex-      ted 0.46–0.55 dex budget clears the first with a factor
cess over IllustrisTNG, across the observed excess factor and   ∼2 of margin but falls short of the second — hence
the massive-end simulated SMF slope s = d log n/d log M⋆.
                                                          z ≃7–9 is labelled marginal.  (ii) ΛCDM physical
Entries ≤0.55 dex lie within the committed quadrature bud-
                                                              feasibility (the hard bound). Abundance-matchingget; the z ≃5 row uses the aperture-corrected total-mass
excess.                                                     the observed n = 3 × 10−5 Mpc−3 at z = 5 to a self-
                                                          contained Sheth–Tormen halo mass function (Planck
 Observed excess   s=−1.4  s=−1.6  s=−1.8  s=−2.0        fb = 0.157) gives Mhalo = 1.0 × 1012 M⊙(log = 12.00;
                                   HMF sanity n(> 1012, z=5) = 3.0 × 10−5 Mpc−3, self- 2× (conservative)    0.22      0.19      0.17      0.15
                                                                 consistent). The unshifted M⋆= 1010.50 then implies a 2.04× (z≃5)         0.22      0.19      0.17      0.15
                                                          baryon-conversion eﬀiciency ϵ = M⋆/(fb Mhalo) = 0.20
 13.6× (z≃7–9)       0.81      0.71      0.63      0.57
                           — precisely the fiducial ΛCDM value and well under
 20× (extreme)       0.93      0.81      0.72      0.65
                                                          the ϵ ≤1 hard ceiling (Boylan-Kolchin 2023); after the
                                                             0.20 dex shift, ϵ = 0.13. The ϵ = 1 ceiling is breached
                                                          only if the true masses are +0.70 dex higher than re-
                      Massive-galaxy abundance: TNG vs JWST
                                                         ported — a change opposite in sign, and 2.5× larger,
                                                                           IllustrisTNG n( > 1010.5)
                                   erased by               Weibel+2024 (z   5--6)           than any plausible downward systematic. The observed
                                   0.28 dex M              Labbé+2023 cand. (z   7--9)
                                                    abundance is thus nowhere near physically impossible in
  3]                                     ΛCDM. This benchmark is robust to the HMF prescrip-
   [Mpc 10 5                                                           tion:  across Sheth–Tormen, Tinker-2008 and Press–
 )
 M                                                       Schechter and across halo mass-definition choices, the
     1010.5                                                 abundance-matched Mhalo moves by ≲0.12 dex, shifting
 >                                                              ϵ by ≤∼0.06 (a Tinker-2008 200m mass function gives
  n( 10 6                                                       log Mhalo = 11.90, ϵ ≈0.26) and the +0.70 dex breach
                                                            threshold by ≤∼0.11 dex (to ≈+0.59 dex). The di-
                                                               rection of this HMF sensitivity runs mildly against con-
              4        5        6        7        8        9         sistency (higher ϵ, thinner margin), but ϵ ≈0.2–0.26 is
                                         redshift z                                                     nowhere near unity and the verdict is unchanged.
                                                        Because the unshifted abundance already implies ϵ ≈
Figure 1. Cumulative number density n(> 1010.5 M⊙) vs
                                                             0.20 — the fiducial ΛCDM star-formation eﬀiciency —
redshift.  IllustrisTNG (dark line/circles) compared to ob-
                                                          the z ≃5 offset  is a TNG feedback/SMF-calibrationserved anchors (Weibel+2024 at z ≃5; Labbé+2023 candi-
dates at z ≃7–9). The z ≃5 excess over TNG (on the total-       tension, not a ΛCDM stress test; the 0.20 dex shift
mass footing) is erased by a 0.20 dex downward stellar-mass      only reconciles TNG’s specific SMF. The z ≃7–9 ex-
shift, well within the 0.46–0.55 dex committed systematic       cess, while it may sit within the fully correlated worst-
budget (green arrow).                                         case budget, both exceeds the committed quadrature
                                                      budget and rests on photometric candidate masses that
(from Table 2). The z ≃5 null reverts to a tension      spectroscopy has repeatedly revised downward. A gen-
only if the true mass-systematic budget is < 0.20 dex;       uine, distinct residual remains:  the spectroscopically
the z ≃7–9 point reverts below its slope-dependent      confirmed compact quiescent galaxies at z > 6, whose

## PAGE 4

4                                  NebulaMind Lab

inferred number density lies ∼2 dex above baseline pre-     downward stellar-mass  shift, ∼0.4× the committed
dictions and is not dissolved by the star-forming sys-      0.46–0.55 dex systematic budget and covered even with-
tematics above; this is the one ΛCDM-relevant residual,      out a top-heavy IMF, so we find no robust tension with
warrants dedicated follow-up, and is not claimed to be    TNG at z ≃5 — subject to the ±0.10 dex Poisson floor
resolved here.                                                    of the 15–20-object simulated anchor and to the caveat
                                                           that an effective comparison redshift of z ≃5.5 would
                                                                   raise the required shift to ≈0.42 dex (still within bud-
                                                                   get, thinner margin). We do not claim a measurement
                      5. CONCLUSION                                                                   of consistency, only that the data at these redshifts nei-
  The  “too  massive,  too  early”  reading  of JWST      ther require a departure from ΛCDM nor a change to
massive-galaxy counts at z ≃5 is not a ΛCDM stress    TNG beyond its known stellar-mass systematics. The
test. The unshifted observed abundance already sits at      apparent z ≃7–9 excess is a weaker case:  it requires
a baryon-conversion eﬀiciency ϵ ≈0.20 — the fiducial     ≈0.72 dex, which exceeds the committed budget, and
ΛCDM star-formation eﬀiciency — so ΛCDM is com-       rests on unconfirmed photometric masses — we label
fortably satisfied with no mass revision at all; reach-         it outside the realistic budget and marginal, alongside
ing the ϵ = 1 physical ceiling would require masses      the one genuine ΛCDM-relevant residual, the spectro-
≈+0.70 dex higher than reported, not lower. What       scopically confirmed quiescent galaxies at z > 6 whose
the z ≃5 offset actually probes is TNG’s specific feed-    ∼2 dex excess is not dissolved by these systematics and
back and SMF calibration: once TNG is placed on the         is not claimed to be resolved here. This is a descriptive,
observed total-mass footing (an aperture correction of      automated confrontation; it has not been validated by
+0.13 dex), the factor-2.04 excess is erased by a 0.20 dex     human review.


                                REFERENCES

Adams, N. J., et al. 2023, MNRAS, 518, 4755                    Kocevski, D. D., et al. 2025, ApJ, 986, 126
                                                           Labbé, I., et al. 2023, Nature, 616, 266Boylan-Kolchin, M. 2023, NatAs, 7, 731
                                                                 Lapi, A., et al. 2024, Universe, 10, 141
Choe, J., et al. 2026, A&A, 707, A29
                                                                Nelson, D., et al. 2019, ComAC, 6, 2
Cochrane, R. K., et al. 2025, ApJL, 978, L42                      Steinhardt, C. L., et al. 2023, ApJL, 951, L40
Grazian, A., et al. 2015, A&A, 575, A96                         Weibel, A., et al. 2024, MNRAS, 533, 1808
                                                          Zhuang, M.-Y., et al. 2026, ApJ, 999, 31Harvey, T., et al. 2025, ApJ, 978, 89
