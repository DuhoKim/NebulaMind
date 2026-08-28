                                               Publications of the Astronomical Society of Australia (2022), 1–24
                                               doi:10.1017/pasa.2022.41


                                               RESEARCH PAPER


                                               The Pantheon+ Analysis: Improving the Redshifts and Peculiar
                                               Velocities of Type Ia Supernovae Used in Cosmological Analyses
                                               Anthony Carr,1 Tamara M. Davis,1 Dan Scolnic,2 Khaled Said,1 Dillon Brout,3,4 Erik R. Peterson,2 and Richard Kessler5,6
                                               1 School of Mathematics and Physics, University of Queensland, Brisbane, QLD 4072, Australia
                                               2 Department of Physics, Duke University, Durham, NC 27708, USA
                                               3 Center for Astrophysics, Harvard & Smithsonian, 60 Garden Street, Cambridge, MA 02138, USA
                                               4 NASA Einstein Fellow
                                               5 Kavli Institute for Cosmological Physics, University of Chicago, Chicago, IL 60637, USA




arXiv:2112.01471v2 [astro-ph.CO] 11 Oct 2022
                                               6 Department of Astronomy and Astrophysics, University of Chicago, Chicago, IL 60637, USA

                                               Author for correspondence: Anthony Carr, Email: anthony.carr@uq.net.au.


                                               (Received 26 05 2022; revised 05 08 2022; accepted 29 08 2022; first published online 11 10 2022)


                                               Abstract
                                               We examine the redshifts of a comprehensive set of published Type Ia supernovae, and provide a combined, improved catalogue with updated
                                               redshifts. We improve on the original catalogues by using the most up-to-date heliocentric redshift data available; ensuring all redshifts have
                                               uncertainty estimates; using the exact formulae to convert heliocentric redshifts into the Cosmic Microwave Background (CMB) frame; and
                                               utilising an improved peculiar velocity model that calculates local motions in redshift-space and more realistically accounts for the external bulk
                                               flow at high-redshifts. We review 2607 supernova redshifts; 2285 are from unique supernovae and 322 are from repeat-observations of the
                                               same supernova. In total, we updated 990 unique heliocentric redshifts, and found 5 cases of missing or incorrect heliocentric corrections, 44
                                               incorrect or missing supernova coordinates, 230 missing heliocentric or CMB frame redshifts, and 1200 missing redshift uncertainties. The
                                               absolute corrections range between 10–8 ≤ ∆z ≤ 0.038, and RMS(∆z) ∼ 3 × 10–3 . The sign of the correction was essentially random, so the
                                               mean and median corrections are small: 4×10–4 and 4×10–6 respectively. We examine the impact of these improvements for H0 and the dark
                                               energy equation of state w and find that the cosmological results change by ∆H0 = –0.12 km s–1 Mpc–1 and ∆w = 0.003, both significantly
                                               smaller than previously reported uncertainties for H0 of 1.0 km s–1 Mpc–1 and w of 0.04 respectively.
                                               Keywords: cosmology: theory - galaxies: distances and redshifts




                                               1.    Introduction                                                                 analysis, we perform a comprehensive review of the redshifts
                                                                                                                                  of individual SNe used in the latest samples for cosmological
                                               The power of Type Ia Supernovae (SNe Ia) as a probe of the                         analyses and analyse potential biases due to issues with redshifts
                                               expansion history of the universe comes from comparing the                         in the recovery of cosmological parameters.
                                               measured distances of the SNe to the distances expected for
                                               their redshift in different cosmological models (Riess et al.,                        Several recent papers have considered the impact of red-
                                               1998; Perlmutter et al., 1999; Wood-Vasey et al., 2007; Kessler                   shifts errors on supernova cosmology. For example, Steinhardt
                                               et al., 2009; Betoule et al., 2014; Scolnic et al., 2018; Dark                    et al. (2020) determined whether the source for each redshift
                                               Energy Survey, 2019). Since the relative precision of spectro-                    in the Pantheon sample (Scolnic et al., 2018) was either the
                                               scopically measured redshifts is typically significantly greater                  host galaxy spectrum or SN spectrum, and found difference
                                               than that of redshift-independent distances, much more ef-                        in cosmological parameters at a ∼ 3σ level between the two
                                               fort has been spent on improving distance measurements than                       subsets. Rameez & Sarkar (2021) noted changes in the mea-
                                               improving redshift measurements (e.g. Phillips, 1993; Phillips                    sured redshifts of sub-samples of large SN compilations that
                                               et al., 1999; Goldhaber et al., 2001; Guy et al., 2007; Jha et al.,               were larger than the reported uncertainties and questioned
                                               2007; Hicken et al., 2009; Kessler et al., 2009; Scolnic et al.,                  the repeatability of SN experiments. While here we show the
                                               2015; Kessler & Scolnic, 2017; Brout et al., 2019; Kessler et al.,                effect of redshift errors on cosmological parameters remains
                                               2019; Lasker et al., 2019). This prioritisation is supported                      small (relative to their current precision), we note that the red-
                                               by the fact that redshift measurements, either from the host                      shifts came from a variety of sources, with many measurements
                                               galaxies or SNe, are straightforward; small errors are usually                    having been over 20 years ago. Old and/or inhomogeneous
                                               expected to be random, shifting redshifts higher as often as                      redshift measurements are not necessarily a problem, but these
                                               lower. However, with samples of greater than 1000 SNe, sys-                       factors increase the potential for miscellaneous errors to be
                                               tematic uncertainties are of paramount concern, and potential                     carried through different SN samples, so a comprehensive
                                               systematic biases in the redshift measurements must be consid-                    review is warranted. Achieving accurate redshifts for cosmo-
                                               ered (e.g. Huterer et al., 2004; Wojtak et al., 2015; Davis et al.,               logical studies requires multiple stages, and in this paper we
                                               2019; Steinhardt et al., 2020; Mitra & Linder, 2021). In this                     apply improvements at each stage except for performing new
2                                                                                                                                     Anthony Carr et al.


spectroscopic measurements.                                                     detailed in the following sections:
     Redshifts in the heliocentric frame are measured either
from the SN spectrum, which is typically precise on the level                     • Fixed coordinates and miscellaneous bookkeeping redshift
of σz ∼ 0.005 (a somewhat conservative estimation), or the                          errors (Section 2).
host-galaxy spectrum, which is typically precise on the level                     • Updated heliocentric redshift values using the NASA/IPAC
of σz ∼ 0.0002 (see Section 4). Host redshifts are preferred                        Extragalactic Database (NED) when better redshifts were
because the hosts have sharper spectral lines that result in a                      available (Section 3).
more accurate and precise redshift. However, it is essential for                  • Ensured all redshifts have uncertainty estimates (Section
the correct host-galaxy to be associated with the SN (Gupta                         4).
et al., 2016), else SNe will be misplaced on the Hubble diagram.                  • Used the exact redshift conversion when (a) going from
Here we review the host galaxy assignment of all SNe where                          heliocentric redshifts to the CMB frame, and (b) going
possible, and update heliocentric redshifts accordingly.                            from CMB frame to Hubble diagram redshift (Section 5).
     Once the heliocentric redshift is determined, we convert                       These respectively correct for (a) our Sun’s motion with
the redshift into the CMB frame. While the CMB conversion is                        respect to the CMB and (b) the host galaxy’s motion with
standard, an unnecessary approximation has often been applied                       respect to the CMB.
(see, e.g. Carr & Davis, 2021, and references therein) and we                     • Provided improved peculiar velocity estimates that better
replace that with the exact correction (Section 5).                                 represent the bulk flow at large distances (Section 6).
     The final step to obtain accurate cosmological redshifts is
                                                                                    Next, we analyse the impact of each change on cosmolog-
applying the correction to account for the peculiar velocity
                                                                                ical parameters in Section 7 and finally discuss and conclude
of the source. We introduce a slightly improved technique of
                                                                                in Section 8.
estimating peculiar velocities (that also better models the exter-
                                                                                    The Pantheon+ redshifts and accompanying data will be re-
nal bulk flow to arbitrary redshift) based on the existing 2M++
                                                                                leased as a machine readable Centre de Données astronomiques
compilation (Carrick et al., 2015). We apply this correction to
                                                                                de Strasbourg (CDS) VizieR table with the publication of this
all redshifts whereas previously, corrections had been applied
                                                                                work, and also on GitHub at https://github.com/PantheonPlu
only at low redshift, or with a biased model at large redshifts.
                                                                                sSH0ES/DataRelease which will log any possible updates. The
     We thus release a comprehensive update to the redshifts
                                                                                light curves for each SN (see Scolnic et al., 2021), which con-
of all publicly available Type Ia supernovae that make up the
                                                                                tain our updated redshifts and peculiar velocities, are also avail-
‘Pantheon+’ sample. Unlike previous analyses, we do not isolate
                                                                                able at this GitHub. The peculiar velocity method developed
our work to redshifts of ‘cosmologically useful’ SNe (those that
                                                                                for this paper is available at https://github.com/KSaid-1/pvhub.
make it onto the Hubble diagram) since data cuts may be
relaxed or otherwise altered in future analyses.
     This paper is one of many that contribute to the Pan-                      2. Samples and bookkeeping
theon+ sample, culminating in the full cosmology analysis in                    Our aim is to complete a comprehensive review of the redshifts
Brout et al. (2022). This work is companion to Peterson et al.                  assigned to every publicly available SN Ia used for cosmology
(2021), that studies the effects of replacing host galaxy red-                  and other SN Ia studies. We include primarily normal Type
shifts with average redshifts of host galaxy groups on Hubble                   Ia supernovae along with various Ia subtypes, such as ‘1991T–
diagram residuals, and provides group-averaged redshifts and                    like’ or just ‘peculiar’ (Li et al., 2001). The Pantheon+ sample is
group-centre coordinates which we also release here. In addi-                   compiled of supernovae taken from a diverse array of samples,
tion, Peterson et al. (2021) studies the efficacy of using differ-              as listed in Table 1 and shown in Figure 1. The master list of
ent peculiar velocity samples—including those derived in this                   our updated redshifts, which includes the SN and host coordi-
work—on Hubble residuals. Brout et al. (2021) re-calibrates                     nates; heliocentric, CMB, and cosmological (Hubble diagram)
the many photometric systems of Pantheon+ and quantifies the                    redshifts; and peculiar velocity values, can be found in Table 2.
systematic effects of photometric calibration on cosmological                   Including all of these quantities aids in the traceability of the
parameters. Scolnic et al. (2021) releases the 1701 updated light               redshifts (and hosts) and repeatability of the corrections.
curves of 1550 unique SNe Iaa used in the Pantheon+ w analy-
sis and Supernovae and H0 for the Equation of State of dark                     2.1 Description of parameters
energy (SH0ES) H0 analysis (Riess et al., 2022). Peterson et al.
                                                                                The relevant parameters for our study are the redshifts and
(2021), Scolnic et al. (2021) and Brout et al. (2021, 2022) utilise
                                                                                peculiar velocities. The heliocentric redshift (zhel ) is the “ob-
the redshifts of this work, and we utilise the group-averaged
redshifts from Peterson et al. (2021) and distance moduli from                  served” redshift.b We convert from zhel to the CMB frame
Brout et al. (2022) in our analysis of the effects of the redshift              redshift (zCMB ) using the standard formulae in Section 5 and
updates. See https://PantheonPlusSH0ES.github.io for the                        emphasise that we do not approximate these transformations.
other papers that contribute to Pantheon+.                                      CMB-frame redshift refers to the redshift after we correct for
     In this work, the main improvements we implemented are                        b Heliocentric redshifts are not quite the observed redshift, but we assume

                                                                                corrections for the Earth’s motion relative to the sun have been made correctly
   a The cosmology sample of this work differs in number to the full analysis   by the analysis software. This correction is small (∆z . 10–6 ), so its effect
due to our simplified data cuts and lack of full covariance analysis.           would be negligible for current cosmological studies.
Publications of the Astronomical Society of Australia                                                                                                                     3


Table 1. Description of sub-samples and list of changes. NTot is the number of Type Ia (including subtypes) supernova light curves in each sample. See Section
3 for the definition of ‘best NED redshift’. See dot points in Section 2.2 and Section 3 for more detailed descriptions of the improvements.

   Source                                             Abbrev.         Ref.        NTot        zhel range       Improvements
   Hubble Deep Field North (using HST)                HDFN              1, 2      1             1.755          Corrected zhel being listed as zCMB .
   Supernova Cosmology Project (using HST)            SCP                3        8         1.014–1.415        Corrected zhel being listed as zCMB . Added coordi-
                                                                                                               nates. Reassigned uncertainties based on host or SN
                                                                                                               redshift.
   Cosmic Assembly Near Infra-Red Deep Ex-            CANDELS            4        13          1.03–2.26        Corrected zhel being listed as zCMB . Updated several
   tragalactic Legacy Survey and Cluster Lens-        +CLASH                                                   zhel to originally published values. Updated name
   ing And Supernova survey with Hubble (us-                                                                   and coordinates of one SN.a
   ing HST)
   Complete Nearby (Redshift < 0.02) Sample           CNIa0.02           5        17       0.0041–0.0303       Found best NED zhel or added uncertainties where
   of Type Ia Supernova Light Curves                                                                           necessary.
   Center for Astrophysics (1)                        CfA1               6        22        0.0031–0.123       Corrected coordinates of one SN. Found best NED
                                                                                                               zhel . Added uncertainties. Identified hosts.
   Calán/Tololo survey                                CTS                7        29        0.0104–0.101       Found best NED zhel . Added uncertainties. Identi-
                                                                                                               fied hosts.
   Great Observatories Origins Deep Survey            GOODS             8, 9      29        0.457–1.390        Corrected zhel being listed as zCMB . Added coordi-
   and Probing Acceleration Now with Super-           +PANS                                                    nates. Reassigned uncertainties based on host or SN
   nova (using HST)                                                                                            redshift.
   Center for Astrophysics (2)                        CfA2              10        44       0.0067–0.0542       Found best NED zhel . Added uncertainties. Identi-
                                                                                                               fied hosts.
   Low-redshift (various sources)                     LOWZ             11–23      66        0.0014–0.038       Found best NED zhel . Added uncertainties. Identi-
                                                                                                               fied hosts.
   Lick Observatory Supernova Search (2005–           LOSS2             24        78        0.0008–0.082       Found best NED zhel . Added uncertainties where
   2018)                                                                                                       necessary. Identified hosts.
   Center for Astrophysics (4p1, 4p2)                 CfA4              25        94       0.0067–0.0745       Corrected coordinates of one SN. Found best NED
                                                                                                               zhel . Added uncertainties. Identified hosts.
   Swift   Optical/Ultraviolet        Supernova       SOUSA            26, 27     121      0.0008–0.0616       Found best NED zhel . Added uncertainties. Identi-
   Archive                                                                                                     fied hosts.
   Carnegie Supernova Project (DR3)                   CSP               28        134      0.0038–0.0836       Found best NED zhel . Added uncertainties. Identi-
                                                                                                               fied hosts.
   Lick Observatory Supernova Search (1998–           LOSS1             29        165      0.0020–0.0948       Found best NED zhel . Added uncertainties. Identi-
   2008)                                                                                                       fied hosts.
   Center for Astrophysics (3S, 3K)                   CfA3              30        185       0.0032–0.084       Found best NED zhel . Added uncertainties. Identi-
                                                                                                               fied hosts.
   SuperNova Legacy Survey                            SNLS              31        239       0.1245–1.06        Identified 10 hosts and updated those redshifts.
                                                                                                               Added uncertainties.
   Foundation Supernova Survey                        FSS              32, 33     242      0.0045–0.1106       Corrected coordinates of six SNe. Updated one
                                                                                                               redshift.b
   Dark Energy Survey (3YR)                           DES              34, 35     251c      0.0176–0.850       Updated redshifts and reassigned uncertainties
                                                                                                               based on host or SN redshift. One additional redshift
                                                                                                               update.d
   Panoramic Survey Telescope & Rapid Re-             PS1MD             36        370       0.0252–0.670       Identified 20 hosts and updated those redshifts. Up-
   sponse System Medium Deep Survey                                                                            dated one additional redshift.e
   Sloan Digital Sky Survey                           SDSS              37        499f     0.0130–0.5540       Identified hosts. Updated 127 redshifts.
 a SNID vespasion: Pantheon ID was previously ‘vespesian’ (spelled with an e), and coordinates were mistakenly those of the supernova Obama (EGS11Oba)

 (Riess et al., 2018). See new coordinates in Table 3.
 b PSNJ1628383 from FSS shares the same host group as SN 2009eu. See entry in Table A2.
 c The DES sample contains 26 non-confirmed but highly probable SNe Ia spectroscopic classifications (type ‘SNIa?’ in Table 6 of Smith et al., 2020a). Of

 these, 22 pass our cosmology sample quality cuts.
 d Updated with new OzDES redshifts and improved SN host association (M. Smith, private communication). The redshift of DES supernova 1280201

 (DES15X3iv) was updated to the higher precision FSS measurement (ASASSN-15od).
 e The PS1MD redshift of 580104 was updated to the higher precision DES measurement (1261579; DES13X3woy).
 f We include only secure spectroscopic Type Ia classifications from SDSS, which excludes 41 SNe (type ‘SNIa?’, in Table 2 of Sako et al., 2018), four of which

 were originally in Pantheon (2005gv, 2005kt, 2007oq, 2007ow) cf. 22/26 DES ‘SNIa?’ in our cosmology sample, implying the SDSS SNIa? are less secure. A
 further two SNe (2006lo, 2006md) in Pantheon were excluded due to being photometrically classified (type ‘zSNIa’ in Sako et al., 2018).
  References: (1) Gilliland et al. (1999); (2) Riess et al. (2001); (3) Suzuki et al. (2012); (4) Riess et al. (2018); (5) Chen et al. (2020); (6) Riess et al. (1999); (7)
 Hamuy et al. (1996); (8) Riess et al. (2004); (9) Riess et al. (2007); (10) Jha et al. (2006); (11) Jha et al. (2007) and references therein; (12) Milne et al. (2010);
 (13) Stritzinger et al. (2010); (14) Tsvetkov & Elenin (2010); (15) Zhang et al. (2010); (16) Hsiao et al. (2015); (17) Krisciunas et al. (2017a); (18) Burns et al.
 (2018); (19) Contreras et al. (2010); (20) Gall et al. (2018); (21) Wee et al. (2018); (22) Burns et al. (2020); (23) Kawabata et al. (2020); (24) Stahl et al. (2019);
 (25) Hicken et al. (2012); (26) Brown et al. (2014); (27) https://pbrown801.github.io/SOUSA/; (28) Krisciunas et al. (2017b); (29) Ganeshalingam et al. (2010);
 (30) Hicken et al. (2009); (31) Guy et al. (2010); (32) Foley et al. (2018); (33) Scolnic et al. (2021); (34) Brout et al. (2019); (35) Smith et al. (2020a); (36) Scolnic
 et al. (2018); (37) Sako et al. (2018).
4                                                                                                                                                  Anthony Carr et al.



                             SDSS            CSP                FSS                PS1MD                LOWZ                     CTS              CNIa0.2
                             CfA             DES                SNLS               LOSS                 SOUSA                    HST
                                                   75°
                                                                                                                                                    host-z
                                    60°
                                                                                                                                                    SN-z
                         45°

                 30°

            15°

            0°

           -15°

                -30°

                        -45°                               6h                         0h                            18h

                                    -60°
                                                 -75°



                                      10−2                                                       10−1                                                  100
                                                                                     zhel

Figure 1. Distribution of Pantheon+ SNe across the sky. Many SNe are common between samples, but only one sample is picked to represent each SN.
Redshifts from the host galaxies are represented by black-outlined solid symbols, and redshifts from supernova spectra are colour-outlined unfilled symbols.
Several samples (generally at higher z i.e. SNLS, DES, PS1MD, HST) targeted small sky areas repeatedly, so many SNe are confined to small patches. These
patches are visible where many lighter, unfilled symbols overlap (these groups obscure the underlying host galaxy redshifts which are always the majority).

Table 2. Master table of updated redshifts. Symbols are defined in Section 2.1. The full machine readable table is available online from VizieR and at https:
//github.com/PantheonPlusSH0ES/DataRelease. The online versions of this table include columns for peculiar velocity uncertainty and binary classifications
for if a SN has an associated host, if the redshift is from a host and if the supernova has group values. All peculiar velocities have an uncertainty of 250 km s–1 ,
and all zhel share the same uncertainty as their corresponding zCMB . Blank entries for group information mean the SN has no associated group, and blank
IAUC entries mean there is no IAU name for the SN.

                                                         SN RA          SN Dec        Host RA           Host Dec
        SNID        IAUC              Host           ◦ (J2000)         ◦ (J2000)      ◦ (J2000)         ◦ (J2000)         zhel          zCMB         σzhel    ...
         (1)           (2)            (3)                 (4)             (5)              (6)             (7)            (8)            (9)          (10)
       2001G      2001G         MCG +08-17-043      137.388 25         50.280 92     137.387 21         50.281 86     0.016703         0.017272    1.1×10–5   ...
       2001V      2001V         NGC 3987            179.353 88         25.202 50     179.337 17         25.195 39     0.015007         0.016045    9.0×10–4   ...
       2001ah     2001ah        UGC 06211           167.624 25         55.160 83     167.626 46         55.169 83     0.057763         0.058373    1.5×10–5   ...
       2001az     2001az        UGC 10483           248.615 46         76.029 67     248.620 17         76.029 72     0.040695         0.040593    9.0×10–5   ...
       2001da     2001da        NGC 7780            358.386 58          8.117 39     358.384 04          8.118 14     0.017381         0.016148      7×10–6   ...
       2001en     2001en        NGC 0523             21.345 42         34.025 14      21.336 37         34.024 94     0.015881         0.014937      7×10–6   ...
       2001fe     2001fe        UGC 05129           144.487 92         25.494 81     144.491 67         25.494 78     0.013514         0.014478      8×10–6   ...
       2001gb     2001gb        IC 0582             149.754 00         17.820 11     149.750 96         17.817 14     0.025439         0.026529    1.1×10–5   ...
       2001ic     2001ic        NGC 7503            347.680 58          7.569 56     347.676 17          7.567 69     0.044089         0.042802      9×10–6   ...
       2002bf     2002bf        CGCG 266-031        153.926 29         55.668 53     153.926 04         55.667 47     0.024376         0.024936      7×10–6   ...



only our own peculiar velocity, i.e. we correct for the Planck-                        distant galaxy that is in addition to the Hubble flow. The final
observed CMB dipole. The peculiar velocity (vp ) and cor-                              Hubble-diagram redshift that is used for cosmology (zHD ) is
responding peculiar redshift (zp ) refer to the motion of the                          the final stage, after we have corrected zCMB for the peculiar
Publications of the Astronomical Society of Australia                                                                                      5

                                             Table 2. Master table of updated redshifts (continued).

                                                 vp       Group RA      Group Dec                                               Group vp
          SNID    ...     zHD       σzHD      km s–1      ◦ (J2000)      ◦ (J2000)     Group zhel      Group zCMB   Group zHD    km s–1
           (1)           (11)       (12)        (13)         (14)           (15)          (16)            (17)        (18)        (19)
         2001G    ...   0.01770   8.5×10–4     -127          ...            ...            ...            ...          ...        ...
         2001V    ...   0.01570   1.2×10–3      102      179.514 560    25.171 888     0.014 883       0.015 920    0.015 57      102
         2001ah   ...   0.05886   8.8×10–4     -138          ...            ...            ...            ...          ...        ...
         2001az   ...   0.04101   8.7×10–4     -121          ...            ...            ...            ...          ...        ...
         2001da   ...   0.01659   8.5×10–4     -129      358.404 510     7.930 666     0.017 816       0.016 583    0.017 02      -176
         2001en   ...   0.01509   8.5×10–4      -46       21.041 921    33.581 505     0.016 294       0.015 343    0.015 50      -46
         2001fe   ...   0.01467   8.5×10–4      -57          ...            ...            ...            ...          ...        ...
         2001gb   ...   0.02650   8.6×10–4       9           ...            ...            ...            ...          ...        ...
         2001ic   ...   0.04390   8.7×10–4     -317          ...            ...            ...            ...          ...        ...
         2002bf   ...   0.02525   8.6×10–4      -92          ...            ...            ...            ...          ...        ...



velocity of the distant galaxy. The standard formulae are also                 was in agreement with the host of 2008cm, we update the
given in Section 5, and the derivation of the peculiar velocities              SN coordinates using NED (Table 3).
themselves is described in Section 6. Each of these parameters               • We update the coordinates of CfA1 SN 1996C to those
have uncertainties represented by σ. When the parameters                       of SIMBAD because the NED coordinates are incorrect
come from the host galaxy group (from Peterson et al., 2021)                   (Table 3).
instead of the individual host or SN, the symbol is preceded                 • Where we have identified the host of a SN, host coordinates
by ‘Group’.                                                                    are provided separately to SN coordinates. There was
                                                                               previously no record of SN hosts in Pantheon or some
2.2 Corrections and additions to previous data                                 source catalogues. Heliocentric corrections are performed
Pantheon+ carries over the same SNe from Pantheon and in-                      using host coordinates where possible.
cludes many more SNe from FSS, DES, LOSS, SOUSA and                          • Where an International Astronomical Union name (IAUC)
CNIa0.02, as defined in Scolnic et al. (2021). Therefore, red-                 for a SN exists, we record it alongside the internal ID
shift and bookkeeping mistakes are carried over from Pantheon                  (SNID). The IAUC links SNe that are common across
which were in turn carried over from their original sources,                   samples that use different internal names. However, we
mostly from older SN compilations. After examining each of                     recommend that in future, a dictionary of all names for a
the samples listed in Table 1 we found and fixed various errors,               SN be implemented since SNe without an IAUC must be
and added improvements as follows:                                             matched via position instead.
                                                                             • In collaboration with Peterson et al. (2021), we include
 • GOODS+PANS and SCP had Right Ascension (RA) and                             group-centre coordinates and group-average heliocentric
   Declination (Dec) listed as zeros. As a result, the helio-                  redshifts, from which we derive group zCMB , group zHD
   centric corrections had been made to the incorrect part of                  and group vp (see Table 2).
   the sky. We assign coordinates from the original datasets
   (Riess et al., 2004, 2007; Suzuki et al., 2012) and recompute               As a result of these changes, all SNe now have the same
   zCMB .                                                                  information: both the SNID and IAUC where applicable, both
 • We provide updates to DES redshifts from their 3-year                   SN and host coordinates where applicable, redshifts in the
   values (Smith et al., 2020a) to their (previously unpublished)          heliocentric and CMB frame, and finally our updated peculiar
   values that will be used in DES 5-year cosmology. This                  velocities.
   includes reassigning uncertainty based on whether the
   redshift comes from the host or SN spectrum: 5×10–4 and
   5×10–3 respectively.                                                    3. Reviewing heliocentric redshifts
 • All SCP and GOODS+PANS SNe had redshift uncertain-                      The most accurate redshift for a SN—in the absence of a galaxy
   ties set to 1×10–3 regardless of redshift source, so we reas-           group average redshift—is that of its host galaxy, so it is im-
   signed the uncertainties the same way as with DES.                      perative that the correct host is assigned. This is true at any
 • Six FSS SNe had coordinates that disagreed with both                    redshift, but especially so at low redshift. In this work, we
   the NED entry and FSS-assigned-host by up to tens of                    define the low-z sample as the ∼1000 galaxies with z . 0.12
   degrees. We therefore correct the SN coordinates to the                 (median z ∼ 0.024). These are primarily the SNe that were
   NED coordinates, as listed in Table 3.                                  not uniquely observed in the typical ‘high-z’ surveys of SNLS,
 • One CfA4 SN had its location mistaken for a SN discovered               DES, SDSS, PS1MD and HST, however some SNe in these
   around the same time. The record for 2008cm had the                     surveys are low-z since they were also observed by the low-z
   coordinates of SNF 20080514-002, but since the redshift                 surveys.
6                                                                                                                      Anthony Carr et al.

                                                   Table 3. Corrections to SN positions.

                                                  Prev. RA       Prev. Dec       Updated RA   Updated Dec
                                  SNID           ◦ (J2000)       ◦ (J2000)        ◦ (J2000)     ◦ (J2000)

                                  1996C         207.751 58     +49.341 251       207.7025      +49.318 64
                                  2008cm        202.303 44     +11.272 403       109.161 46    −62.314 69
                                  vespasian     215.136 083    +53.046 728       322.4275       −7.696 58
                                  ASASSN-15ga   208.159 615    +10.718 024       194.863 72    +14.171 05
                                  SN2016aqb     164.193 214    −13.047 481       170.493 33    −13.983 67
                                  ATLAS16bwu     93.620 268    −17.421 361        18.592 75    −13.153 09
                                  PS16bnz       158.658 125    +27.190 117       155.153 75     −2.466 75
                                  PS16eqv        53.168 411    −19.615 435        37.930 83    −25.001 62
                                  ASASSN-17aj   101.946 198      +7.920 005      173.293 75    −10.221 77



    In the interest of thoroughly reassessing the redshifts of                     source.
Pantheon+, we used Aladin (Bonnarel et al., 2000) to visually               In the case of multiple redshifts satisfying any condition,
inspect Pan-STARRS images at every low-z (and occasionally                  we take the most precise redshift.
moderate-z) SN location, to assign and record hosts. It is this          3. If none of the above criteria are satisfied we consider red-
requirement of visual inspection that makes our definition of               shifts that lack an uncertainty estimate, but are not a SN
low-z unique. We also used Dark Energy Camera Legacy                        redshift. In these cases, we set the uncertainty to 9×10–5
Survey, SDSS and DES images where available, and for Dec                    (see Section 4).
. –30◦ we used mostly Digitized Sky Survey 2 images. For                 4. As the last resort we take the redshift derived from the
the hosts we identified, we chose the ‘best’ redshift according             original SN spectrum. In the cases where no redshift un-
to a hierarchy of criteria outlined below. For the three low-z              certainty is reported, we set the uncertainty to be 5×10–3
SNe we could not assign hosts—1996ab, 2007kg and 2008dx—                    (Section 4).
we use the redshift given in the original classification reports.
Apart from these three, there was ambiguity in only six low-z               We examined all redshifts in the low-z sample except those
hosts (see discussion below). In addition the low-z sample for          that come from FSS. These redshifts were not updated because
which we identified redshifts, we confirmed the coordinates             FSS adopt their own hierarchical approach to selecting red-
and host names of all SDSS and FSS SNe.                                 shifts in the literature (Foley et al., 2018). Importantly, FSS
    Some redshifts in NED are supplied with a comment as                measure new host redshifts for SNe previously without host
to their origins, which contribute to picking the best red-             redshifts. Thus, we assume this sample has the best existing
shift. The origins are either ‘from new data’ (i.e. the reference       redshift estimates already.
measured the redshift), ‘from reprocessed raw data’, or ‘from               Out of 2285 unique SNe Ia, 990 heliocentric redshifts have
uncertain origins’. Most redshifts are from uncertain origins,          been updated. This is mainly for low-z hosts, whose redshifts
usually because the sources re-record older redshifts, but also         have been measured multiple times. Some notable cases:
because some NED records do not report that the redshift is
new.                                                                         • All HST supernovae had zhel listed as zCMB . In each case,
    The criteria for picking the best redshift are:                            we use the heliocentric redshifts given by the original
                                                                               publication and recompute zCMB .
1. We use SDSS Data Release 13 (DR13) redshifts when they                    • SN 1992bk, 2000cp, 2008bf, 2008ff, 2009eu, 2014at and
   are available, as these are usually the most up-to-date mea-                PSNJ1628383 each occurred in a group of galaxies so that
   surement, have low uncertainty, and show stability in that                  a unique host could not be determined. The most accu-
   earlier iterations of SDSS tend to converge on the DR13                     rate treatment of these cases, and in fact in general, is to
   values.                                                                     average the redshifts of host-galaxy-group members, as in
2. Next we consider other sources that include uncertainty                     Peterson et al. (2021), with more members giving a more
   estimates. Among these we choose the one that first satisfies,              accurate redshift. Figure 2 shows images for these six cases,
   in order of decreasing priority:                                            with SN locations and potential hosts indicated. We set
    (a) The most recent source that has taken new data and                     the group redshift uncertainty to the dispersion in group
        measured a new redshift.                                               member redshifts. SN 1992bk is a good example of how
    (b) The most recent source that has reprocessed old data.                  the ‘directional light radius’ (DLR; see Gupta et al., 2016)
    (c) The most recent source that has an uncertain origin.                   might be used to exclude the smaller, less likely cluster
        This may be original data, but may also be from a                      galaxies from being considered as hosts. We do not use
        new publication that uses old redshifts because these                  DLRs to determine the most likely host, and instead visu-
        often appear as new entries in NED. We endeavoured                     ally identify the most likely group members and take their
        to avoid republished redshifts and quote the original                  average redshift, which gives a more accurate estimate of
Publications of the Astronomical Society of Australia                                                                                                     7


    the Hubble-flow redshift than any single group member.
  • Some SNe had multiple unique SDSS redshift measure-
    ments from the same data release. The unique redshifts
    were averaged, and uncertainties estimated from the dis-
    persion of redshift measurements, similar to the ambiguous
    host redshifts (see Table A1). The quoted redshift uncer-
    tainties are often less than the standard deviation of the
    measurements (despite the fact that standard deviations
    measured from small samples are typically underestimated)
    indicating that the redshift uncertainties may be underesti-
    mated; see discussion in Section 4.
  • There were many cases where a SN redshift was quoted
    in place of a more accurate host redshift, as seen in the dis-
    crepancies between the four different redshift sources Sako
    et al. (2018, Table 1 and Table 9), Gupta et al. (2011), and
    Östman et al. (2011). We examined every image of SDSS
    SNe to confirm the host, SN coordinates, and attempt to
    update the redshift using NED. In ambiguous host cases,
    we use the host coordinates published in Sako et al. (2018).               Figure 2. All instances of an ambiguous host where redshifts of multiple
    In this way, we replace 81 SN redshifts with host redshifts.               likely hosts have been averaged (in each case all possible hosts are at ap-
                                                                               proximately the same redshift). In all images, North is up and East to the
  • Zheng et al. (2008) noted in the first year SDSS SN data                   left. Red crosses indicate the location of the SN, and green circles indicate
    release that there was a systematic offset of 3×10–3 be-                   the hosts used. Other objects in the images were not selected because they
    tween host redshifts and SN redshifts, and thus they ap-                   were stars, or were less likely host galaxies due to their size.
    plied the shift to SN redshifts to bring them in line with
    host redshifts. Sako et al. (2018) found a similar offset of
    (2.2 ± 0.4) × 10–3 was present in their larger sample of
                                                                                                       0.01
    SDSS SNe, however they did not apply the shift to the SN                         10−2
                                                                                                      0.005
    redshifts. We confirm that we see the same trend in the 81
    SDSS SNe whose SN-z we replace with host-z. Unlike                                                0.001
                                                                                     10−3
    Sako et al. (2018), we do apply this systematic redshift shift                                5 × 10−4

    of +2.2 × 10–3 to the remaining 46 SDSS SN-zs.c                             σz               1.5 × 10−4
                                                                                          −4
    Table A2 shows the largest disagreements between new                             10
                                                                                                                                                  SDSS
and old redshifts in decreasing level of disagreement, with                                                                                       DES
justifications for the update. Since we expect updates from SN-                                                                                   SNLS
                                                                                     10−5
z to host-z to be large, we focus on disagreements between                                                                                        PS1MD
host-zs.                                                                                                                                          all
                                                                                                                                                  HST
                                                                                     10−6
4. Estimating redshift uncertainties                                                           10−3           10−2           10−1              100
                                                                                                                      zCMB
Ideally, each object would have an individual redshift uncer-
tainty measurement based on its spectrum. However, many
                                                                               Figure 3. Uncertainty in redshift versus redshift. We observe a general up-
surveys (generally those at higher redshift) do not provide                    ward trend with redshift as expected. Samples that use standard uncertain-
this information and instead give overall estimates of redshift                ties have been highlighted with dashed lines. The standard uncertainty of
uncertainties for typical classes of object (e.g. DES, PS1MD,                  1.5×10–4 is that of the 6dF redshifts in the low-z sample.
SNLS; see Figure 3). There are several ways to estimate the
redshift of an object: emission-line redshifting (e.g. Colless
et al., 2001), cross-correlation with templates (Tonry & Davis,                (mostly from Springob et al., 2005), and many more that are
1979), least-squares minimisation (Bolton et al., 2012), or                    unspecified.
from 21 cm H I emission profiles in radio (e.g. Springob et al.,
2005). Each method has its own way of estimating redshift                      4.1 Typical Uncertainties
uncertainty per spectrum, and the Pantheon+ sample has red-                    More problematic than reporting only class-based uncertain-
shifts determined from each of these methods. For instance,                    ties is the non-reporting of uncertainties. Some SN data re-
SDSS uses least-squares minimisation, DES/OzDES uses cross-                    leases did not include uncertainties (e.g., CSP, CfA), in which
correlation, there are many galaxies with 21 cm H I redshifts                  case the only way to obtain an uncertainty estimate is to in-
   c Redshifts are added together by multiplying 1 + z factors, however here   stead use an original measurement of the redshift. Our aim
we apply the correction additively, which we believe is how the systematic     is for every redshift to have an uncertainty estimate, so we
offset was modelled.                                                           must estimate uncertainties where none are reported. Despite
8                                                                                                                                    Anthony Carr et al.


identifying the best primary source according to the hierarchy
above, a small number of sources did not provide uncertainties.
With no information about the spectra themselves, we opt
to set missing uncertainties to a typical value, according to
whether they are host or SN redshifts.
    We examine the redshift uncertainties of five surveys with
redshifts in Pantheon+ or that provide their own galaxy redshift
uncertainty statistics: the Two-degree Field Galaxy Redshift
Survey (2dFGRS; Colless et al., 2001), the WiggleZ Dark En-
ergy Survey (Drinkwater et al., 2018), SDSS, DES/OzDES
(Lidman et al., 2020) and the Digital Archive of H I 21 Cen-
timeter Line Spectra from Springob et al. (2005). However, we
defer the discussion of SDSS-measured redshifts to Section 4.2
as SDSS redshift uncertainties are consistently smaller than
other optical estimates.
    While each method of redshifting naturally provides a way                   Figure 4. Comparison of SDSS DR13 redshift uncertainties and all other
of estimating uncertainty, the more common way to estimate                      low-z SN uncertainties. SDSS DR13 has a tight distribution peaking around
uncertainty is by comparing multiple measurements of the                        1×10–5 , while low-z is much broader due to its heterogeneous redshift sub-
same object. Each survey found:                                                 samples. Redshifts larger than 0.0006 have been collected into a single bin,
                                                                                as the maximum is 0.002 (Perlmutter et al., 1999). The spike in low-z at
                                                                                σz = 0.00015 is due to 6dF, while the SDSS spike at σz = 0.0005 corresponds
    • 2dFGRS: Over 0 < z < 0.3, the RMS of multiple measure-
                                                                                to the uncertainty typically set for a redshift from emission/absorption lines
      ments was σz = 2.8 × 10–4 . The authors found a slight                    in a SN spectrum.
      upwards trend with redshift.
    • WiggleZ: Over 0 < z < 1.3, the standard deviation of
      multiple measurements ranged from σz = 1.7 × 10–4 for                     based on the population of SN redshifts to date and expert
      the highest quality spectra to σz = 2.7 × 10–4 for the lower              opinion. We reiterate that this is a somewhat conservative but
      quality but successfully redshifted spectra. The authors                  fair estimation. As an example, as given by SNID (Blondin
      found no trend with redshift.                                             & Tonry, 2007), the mean redshift uncertainty of the 51 su-
    • OzDES: The collaboration opted to estimate uncertainties                  pernovae with Type Ia SNID classifications from the CfA Su-
      for classes of objects, assigning general SN host galaxies                pernova Group websitee is σz = 4.1×10–3 with a standard
      uncertainties of σz = 1.5 × 10–4 , which the authors state is             deviation of 1.7×10–3 .
      a lower bound.d                                                               See Table A3 for a list of all SNe previously missing uncer-
    • Springob et al. (2005) 21 cm Archive: Compared with                       tainties.
      optical, redshifts determined from the 21 cm line offer im-
      pressive precision. After reanalysing nearly 9000 nearby
      (–0.005 < z < 0.08) H I galaxies, the mean and median red-                4.2    Underestimated SDSS Uncertainties
      shift uncertainty was 1.7×10–5 and 1.2×10–5 respectively.                 We noted in Section 3 that when multiple redshift measure-
                                                                                ments were available in SDSS, the dispersion in redshift values
    For the Pantheon+ low-z sample, which has a mix of op-                      is usually higher than expected from their typical uncertain-
tical and radio redshifts from the literature, we find a me-                    ties of 1×10–5 . This comparison indicates that typical SDSS
dian redshift uncertainty of 9×10–5 , which is consistent with                  redshift uncertainties are somewhat optimistic. We quantify
the above measurements. We also include in this test the 30                     this comparison by calculating both average uncertainty, σz ,
PS1MD and SNLS SNe whose host galaxies we find third                            and dispersion in z, σ(z), for all multiply-measured objects in
party redshifts for, extending to z ∼ 0.50. We show in Figure                   SDSS DR13. Only objects with two or more reliable redshifts
4 the distribution of the redshift uncertainties of this modified               are used.
low-z sample. Since there remain 30 host galaxies that lack
                                                                                     The average uncertainty versus z dispersion for all multiply-
redshift uncertainties, all at low-z, we opt to assign the median
                                                                                measured objects is shown in Figure 5. We perform a linear
uncertainty calculated from the rest of our low-z sample (see
                                                                                fit to the objects with five or more measurements weighted
Table A3).
                                                                                by number of redshift measurements. Calculating standard
    Until now, we have discussed only host galaxy redshifts
                                                                                deviation from few points is systematically biased low (grey
because these have been studied in detail. Estimating redshifts
                                                                                points), so we exclude objects with two–four measurements.
from SN spectra has had less attention. Like host galaxy red-
                                                                                We also exclude dispersions above 0.01 since these dispersions
shifts, there are SN redshifts without uncertainty estimates. In
                                                                                are caused by multiple confident but disparate redshifts. Thus
these cases, we rely on a less concrete estimation of σz = 0.005,
                                                                                the fit was performed on 1,000 of 31,000 objects.
    d To be conservative we have set the host galaxy redshift uncertainty for

DES SNe that are in Pantheon+ to be 5×10–4 (M. Smith, private communica-           e https://lweb.cfa.harvard.edu/supernova/OldRecentSN.html and

tion).                                                                          https://lweb.cfa.harvard.edu/supernova/RecentSN.html
Publications of the Astronomical Society of Australia                                                                                              9


                                                                                    The difference between using the additive approximation and
                                                                                    the correct multiplicative equation is exactly zCMB zSun . Since
                                                                                    zSun is our own motion with respect to the CMB (our velocity
                                                                                    vCMB in the direction of the CMB dipole), it is of order 10–3 .
                                                                                    Therefore, at low-z, the difference between z×  CMB and zCMB
                                                                                                                                                +

                                                                                    appears almost negligible; however, by z ∼ 1, the error is on
                                                                                    the order of 10–3 , which is an order of magnitude larger than
                                                                                    most reported statistical uncertainties in redshifts.
                                                                                        We have ensured that all sub-samples in the new Pantheon+
                                                                                    sample consistently use the multiplicative correction.

                                                                                    5.1.1 Which dipole to use?
                                                                                    The Pantheon sample mostly used the CMB dipole measured
                                                                                    by the Cosmic Background Explorer (COBE) satellite (Fixsen
                                                                                    et al., 1996), in the direction of galactic longitude and lati-
                                                                                    tude (l, b) = (264.14◦ ± 0.30◦ , 48.26◦ ± 0.30◦ ) with a velocity
Figure 5. Standard deviation of multiple SDSS DR13 reliable redshift mea-            COBE = 371 ± 1 km s–1 .
                                                                                    vSun
surements of the same object against the average of their quoted uncertain-
ties. We expect a slope of 1.0 (red dashed line) if the uncertainties are ap-           We update the heliocentric correction to use the dipole
propriate. The solid blue line is a linear fit to all data with five or more mea-   measured by the Planck Collaboration (Planck Collaboration
surements and a dispersion of σ(z) < 0.01, which shows that, consistently,          et al., 2020), (l, b) = (264.021◦ ± 0.011◦ , 48.253◦ ± 0.005◦ )
σ(z) > σz . Every point with σ(z) & 0.01 is a catastrophic redshift failure                            Planck = 369.82 ± 0.11 km s–1 . The difference
caused by at least two distinct confident redshifts.                                with a velocity vSun
                                                                                    in redshift between using the COBE dipole and the Planck
                                                                                    dipole is at most ∼ 10–5 , so this is a small change.
    The uncertainty of 9×10–5 that we apply to sources with
no provided uncertainty reflects the mean dispersion of 9.5×10–5                    5.1.2 Calculating zSun
we calculate for repeated non-outlying SDSS measurements.
                                                                                    The projection of the Sun’s peculiar velocity along the line of
Since we see a gradient of almost unity and a positive offset of
                                                                                    sight to an object is
roughly 3×10–5 between dispersion and estimated uncertainty,
increasing the SDSS uncertainties by this amount would be                                           vSun = vSun · n̂obj = vSun
                                                                                                                           max
                                                                                                                               cos α,            (4)
reasonable, and we test the impact of this increase in our cos-
mological analysis in Section 7.f                                                   where n̂obj is the object’s position vector, and α is the angle
                                                                                    separating the dipole direction and the object.
5. Combining redshifts multiplicatively                                                 Since the Sun’s velocity is small (order of 102 km s–1 ) com-
5.1 Heliocentric corrections                                                        pared to c, the low-z approximation zSun ≈ –vSun /c is adequate,
Most publicly available heliocentric corrections, including                         but we use the full special relativistic calculation
those currently in NED and Pantheon used a low-redshift                                                        s
approximation (although the approximation in NED will be                                                           1 + (–vSun )/c
corrected; see Carr & Davis, 2021). When performing the he-                                           zSun =                        – 1,         (5)
                                                                                                                   1 – (–vSun )/c
liocentric correction, the low-redshift approximation assumes
the observed redshift zhel is an additive combination of zCMB                       because there is negligible computational advantage to the
and the redshift due to our Sun’s peculiar motion, zSun ,                           approximation. The minus signs before vSun have been left
                           zhel = z+CMB + zSun .                            (1)     explicit to emphasise that at zero angular separation (α = 0 in
                                                                                    Equation 4) the object should appear slightly blueshifted due
However, the correct way to combine redshifts is to multi-                          the our velocity directly towards it.
plicatively combine factors of (1 + z), so
                                                                                    5.2 Peculiar velocity corrections
                  (1 + zhel ) = (1 + z×
                                      CMB )(1 + zSun ).                     (2)     The peculiar redshifts arising due to the peculiar velocities of
This gives the correct CMB-frame redshift, which is                                 the supernova host galaxies also need to be treated multiplica-
                                                                                    tively. Equation (2) becomes
                                     1 + zhel
                          z×
                           CMB =              – 1.                          (3)                (1 + zhel ) = (1 + zHD )(1 + zSun )(1 + zp ).     (6)
                                     1 + zSun

   f Our increased uncertainty better reflects the observed dispersion between      Here we use the ‘Hubble diagram redshift’ zHD , which is the
SDSS measurements but may still underestimate the uncertainties given the           cosmological redshift we are interested in. This differs in our
typical uncertainty of optical redshifts in Section 4.1.                            nomenclature from the CMB-frame redshift zCMB , because
10                                                                                                                                        Anthony Carr et al.


zCMB takes into account our motion but not the peculiar ve-                           dependence is weak. We quantify the impact of these peculiar
locity of the source. Combined with Equation (2) we see                               velocity corrections on cosmological parameters in Section 7.
                                                                                          In the linear regime, peculiar velocity is related to the
                                     1 + zCMB                                         gravitational acceleration via:
                          zHD =               – 1.                             (7)
                                       1 + zp
                                                                                                                f                     r0 – r
                                                                                                                    Z
Thus the Hubble diagram redshift requires knowledge of the                                              v(r) =          d3 r0 δ(r0 ) 0       ,            (8)
                                                                                                               4π                   |r – r|3
SN host’s peculiar redshift zp , so we turn to how we derive
peculiar velocities.                                                                  where f is the growth rate of the cosmic structure and δ(r) is
                                                                                      the density contrast. This equation has two limitations:
6. Updating peculiar velocity modelling
                                                                                       • Galaxy surveys do not measure the total matter density, so
By applying the heliocentric-to-CMB correction we have ac-
                                                                                         it is assumed that the observed galaxy density (δg ) linearly
counted for the motion of our own solar system with respect
                                                                                         traces the total density, δ = δg /b. Here b is the linear biasing
to the CMB. However, we have not yet accounted for the
                                                                                         parameter, which is different for different types of galaxies,
peculiar velocity of the supernova’s host galaxy (vp ). Remov-
                                                                                         and therefore has to be measured or marginalised over.
ing the redshift due to the estimated peculiar velocity of the
                                                                                       • The region over which we have a sufficient number density
host galaxy leaves the cosmological redshift zHD (Equation 7),
                                                                                         of measured galaxies to do reconstruction is smaller than
which is the redshift needed for the Hubble diagram.
                                                                                         the region for which we need to estimate peculiar velocities.
    In this section, we describe the methodology for comput-
                                                                                         This has been addressed by estimating the “external veloc-
ing the peculiar velocity for each host galaxy. Our treatment
                                                                                         ity”, V ext , which arises due to structures outside the survey
differs from the peculiar velocities used in Pantheon in the
                                                                                         volume, and estimating how that would theoretically decay
following ways:
                                                                                         with distance (Section 6.3).
  • We use the multiplicative equation for combining redshifts
                                                                                      We use the velocity field reconstruction created by Carrick
    (Equation 6).
                                                                                      et al. (2015), which uses data from the 2M++ compilation from
  • We convert the predicted peculiar velocity field to redshift-
                                                                                      Lavaux & Hudson (2011). 2M++ includes data from 2MRS
    space (Section 6.2).
                                                                                      (Huchra et al., 2005), 6dFGS (Jones et al., 2009), and SDSS
  • Outside the measured peculiar velocity field we model the
                                                                                      (Abazajian et al., 2009) and extends to a radius of rmax = 200
    residual bulk flow as a decaying function, rather than a
                                                                                      h–1 Mpc. One slice (SGZ = 0) of the reconstructed density field
    constant external velocity (Section 6.3).
                                                                                      is shown in Figure 6 in the supergalactic plane (SGX – SGY).
  • We flip the vp sign convention used in the Pantheon sample
                                                                                      Figure 7 shows the 2M++ velocity field in redshift-space on a
    (and effected the same change in the SuperNova ANAlysis                           regular spatial grid.
    software (SNANA, Kessler et al., 2009) as of version 11.02).                           A key model parameter to evaluate is β ≡ f /b. The rate
    Now, vp is positive when moving away from us, which is                                                                         γ
                                                                                      of growth is often parameterised by f = Ωm , where γ = 0.55
    consistent with the sign of recession velocities.                                 in the standard cosmological model, ΛCDM. Importantly,
The nominal set of peculiar velocities we derive here are ex-                         however, β is determined empirically rather than computed
amined in the companion paper Peterson et al. (2021) in the                           from the ΛCDM model.
context of the efficacy of different peculiar velocity samples,                            Both β and V ext are derived from a combination of den-
models and parameters of our own model on SN Hubble resid-                            sity field reconstruction and observation. The reconstruction
uals.                                                                                 process delivers a normalised peculiar velocity field, vp,recon. (r),
                                                                                      which gives the directions and relative magnitudes of the pe-
                                                                                      culiar velocities as a function of position. Predictions from
6.1 Estimating peculiar velocities                                                    this peculiar velocity field are compared with galaxies that
The most precise way to estimate peculiar velocities is to mea-                       have peculiar velocities derived from distance measures such as
sure the density field (e.g. through a redshift survey) and use                       the Tully-Fisher relation or Fundamental Plane relation. The
that to predict the expected peculiar velocity field.g This is                        calibrated peculiar velocity field is
known as velocity field reconstruction. Importantly, this method
does not use supernova distances, and therefore does not intro-                                         vp (r) = βvp,recon. (r) + Vext (r).               (9)
duce correlations between the peculiar-velocity-corrected SN
redshift and its measured distance. The reconstruction does                           The parameter β thus acts as a scaling of the normalised veloc-
require an assumed cosmological model, but the cosmological                           ity field (subject to the sample of observed vp ), and V ext is the
                                                                                      residual mean velocity.
    g Directly measuring peculiar velocities using an independent distance                Carrick et al. (2015) measured β = 0.431 ± 0.021 and an
measurement (such as the Tully-Fisher or Fundamental Plane relation) is less          external velocity of |V ext | = 159 ± 23 km s–1 in the direction
precise (∼ 20% uncertainties) and observationally challenging. Due to their
                                                                                      of (l, b) = (304◦ ± 11◦ , 6◦ ± 13◦ ). While we use the velocity
sparseness, direct peculiar velocity catalogues are difficult to interpolate to get
reliable peculiar velocity estimates for galaxies that do not have direct distance    field measured by Carrick et al. (2015), we use an updated
measurements.                                                                         value of β = 0.314+0.031
                                                                                                            –0.047 derived in Said et al. (2020), which
Publications of the Astronomical Society of Australia                                                                                                    11




Figure 6. Slice of the 2M++ reconstructed density field plotted in the super-   Figure 7. 2M++ velocity field plotted on a regular grid of redshift-space po-
galactic plane (SGZ = 0). White areas are regions for which data is missing,    sitions. Note the white regions in Figure 6 have been interpolated over to
therefore the density reconstruction is uncertain.                              make a complete velocity field out to 200 h–1 Mpc, which means those re-
                                                                                gions of the velocity field will have higher uncertainty than other regions.


gives a better fit when comparing SDSS Fundamental Plane
peculiar velocities to the predicted peculiar velocity field. We                ity at that grid point, vp,i . Second, we use inverse distance
confirm that this lower β value results in a lower scatter in the               weighting to interpolate and adjust the irregularly-spaced grid
supernova Hubble diagram, see Peterson et al. (2021).                           in redshift-space to a regular grid. This process is described in
     Carrick et al. (2015) estimated the peculiar velocity uncer-               more detail in Appendix Appendix 2.
tainty to be 250 km s–1 for the galaxies (the particle velocity                     An alternative method is to integrate along the line of sight
field) and 150 km s–1 for galaxy groups (the haloes). In other                  over real-space. This technique is used by the online toolh
words, the uncertainty on an individual galaxy’s peculiar ve-                   associated with Carrick et al. (2015), which was previously used
locity is higher than the uncertainty on peculiar velocity of                   to estimate the Pantheon peculiar velocities. Both methods
the group in which it resides. We note, however, that some                      agree very well, within the uncertainty, as seen in Figure 8.
regions of the reconstruction are less certain than others be-                  The mean difference is only 5 km s–1 (50 times smaller than
cause of incomplete sampling. Unfortunately, sampling is not                    the individual uncertainty).
accounted for in current models, so we adopt the value of
σvp = 250 km s–1 and leave a more precise estimate of the
                                                                                6.3 Velocities beyond rmax
peculiar velocity uncertainty for future work.
                                                                                It is difficult to properly account for velocities outside rmax be-
                                                                                cause we do not have an adequate measurement of the density
6.2 Real vs redshift-space                                                      field to predict individual velocities precisely. However, we
Carrick et al. (2015) provide the velocity field in “real-space”,               expect velocities to continue to behave largely according to
so the position and distance of a galaxy can be used to draw                    the bulk flow trend beyond rmax as a consequence of ΛCDM
the peculiar velocity directly from the modelled velocity field.                large scale structure. In standard ΛCDM a theoretical bulk
However, in supernova cosmology, the distance measured via                      flow magnitude of ∼ 20 km s–1 is expected even for a sphere
the distance modulus should be independent of the redshift.                     with radius z ∼ 1 (grey dashed lines in Figure 9). Accordingly,
This distance should not be used to predict the peculiar velocity               peculiar velocities of galaxies outside rmax should not be set to
to correct the redshift. Converting the observed redshift to                    zero.
distance (by assuming a cosmology) to estimate the peculiar                          To ensure a smooth transition across rmax we have chosen
velocity is valid, but less precise than using the redshift. We                 to model the bulk flow as a decaying function consistent with
therefore convert the reconstructed velocity field of Carrick                   ΛCDM expectations, and in the direction of the bulk flow of
et al. (2015) to redshift-space. While we assume a cosmology                    the 200 h–1 Mpc sphere. While there is a ΛCDM model depen-
for this conversion, any reasonable choice has a negligible                     dence, the impact of this high-z correction on cosmological
effect on the velocity field. Thus we query the peculiar velocity               inferences is small both because the corrections are small (at
model using the coordinates of each host galaxy or SN (RA,                      most ∼ 5 × 10–4 when in the direction of the bulk flow), and
Dec, zCMB ), and Equation 9.                                                    because at high-z these peculiar redshifts represent a small
      The conversion to redshift-space takes two steps. First, for              fraction of the total redshift.
each real-space grid point i we convert the real-space position,
ri , into redshift position zi using the predicted peculiar veloc-                 h https://cosmicflows.iap.f r
12                                                                                                                                          Anthony Carr et al.




                                                 200



     2M ++           2M ++                  −1




          work − P Vcosmicflows.iap.fr [km s ]
  P VThis
                                                 100


                                                   0


                                       −100


                                       −200

                                                       −500           0           500
                                                                 2M ++           −1
                                                              P VThis work [km s    ]

Figure 8. The predicted peculiar velocity for a sample of 851 host galaxies
using two different approaches. Each vp has an uncertainty of 250 km s–1 .
We use the 2M++ velocity field converted from real-space to redshift-space
whereas the method associated with Carrick et al. (2015) (previously used
for Pantheon), integrates over real-space along the line of sight for each host
galaxy. There are only negligible systematic differences between the results
of these techniques, and all scatter is within 1σ.
                                                                                        Figure 9. Top: Pantheon (original) peculiar velocities converted to redshift.
                                                                                        The expected decay of peculiar velocity amplitude according to ΛCDM is
                                                                                        over-plotted (grey dashed), outside the limit of the reconstruction at 200
     We note that there is a slight difference between V ext and                        h–1 Mpc (z ≈ 0.067). The spurious increase in peculiar velocities as redshift
the bulk flow of the 200 h–1 Mpc sphere. The bulk flow of the                           increases is driven by the erroneous use of the low-redshift approximation
                                                                                        (Equation 1). The error term is plotted (red dashed) only for the four SNLS
sphere is the average of the internal velocities (which is small
                                                                                        fields. Bottom: Pantheon+ (this work) peculiar velocities, converted to red-
but non-zero), plus the external velocity. We calculate the                             shift, which are now well-behaved beyond low-redshift.
bulk flow at the 2M++ maximum radius of 200 h–1 Mpc to be
182 ± 23 km s–1 in the direction of (l, b) = (302◦ ± 10◦ , 2◦ ±
9◦ ). At this large radius, the bulk flow is dominated by the                           Figure 9 are the HST SNe with vp = 0, and the somewhat
external bulk flow (Vext ≈ 170 km s–1 : Said et al. 2020; Boruah                        random scatter around z ≈ 0.15 which may have been due to
et al. 2020) plus a small contribution from the mean internal                           assigning 2M++ peculiar velocities outside the 2M++ sphere.
velocities.                                                                             We show in the bottom panel of Figure 9 that these issues are
     Contrary to common expectations, the bulk flow should                              now resolved.
not necessarily converge on the direction of the CMB dipole.
The observed CMB dipole is particular to our own motion,
and is removed with the correction from the heliocentric to                             7. Impact on cosmological parameters
the CMB frame. Dramatic changes to the the magnitude                                    To test the impact of these redshift updates on cosmological
and direction of bulk flow direction become unlikely as we                              parameters we fit for H0 , and (separately) the dark energy
average over spheres that approach the scale of homogeneity.                            equation of state w, in a flat-wCDM model for various differ-
Therefore, we fix the direction of the decaying bulk flow in                            ent combinations of updates as listed in Table 4 and described
the direction of the 200 h–1 Mpc sphere’s bulk flow.                                    below. We only report the changes in these parameters, rela-
     The Pantheon sample peculiar velocities outside the veloc-                         tive to the nominal ‘Final’ set that includes all of the updates
ity reconstruction suffered three main issues which can be seen                         (updated zhel , exact formula for combining redshifts, and new
in Figure 9. The most apparent issue is the increasing vp with                          peculiar velocities). The full Pantheon+ cosmology analysis is
redshift. We show that this artefact is caused by the low-z                             reported in Brout et al. (2022).
approximation of the heliocentric correction by plotting the                                In addition to combinations of redshift updates, we consider
error term (i.e. the difference between Equations 1 and 2) for                          other redshift/sample variations for a total of 14 variations.
the four SNLS fields, as these stretch to high-z. This particular                       Each variation is numbered, as listed in Table 4, and the same
error also occurs for PS1MD and SDSS but is less visible since                          numbering is also included in each figure for easy reference.
these surveys do not extend as far in redshift. Also visible in                         The variations we consider are:
Publications of the Astronomical Society of Australia                                                                                                   13

Table 4. Impact of different corrections, redshift samples, systematics, and uncertainties on cosmological parameters. We define the change in cosmological
parameters to be the variation minus the nominal value (variation 5). NSN refers to the number of supernovae in each sample, which differ between variations
depending on which supernovae pass or fail quality cuts as their redshifts change. The uncertainties (σH0 and σw ) show only the uncertainty due to the
supernova sample size and distance moduli uncertainties, not the expected precision of the measurement.

                                                                                  NSN
            Variation    Variation Description                 Total    0.0233 < zHD < 0.15    zHD > 0.01     ∆H0      σH0      ∆w        σw

                0        None                                  1764             504               1653        −0.12    0.20     0.003    0.045
                1        New zhel                              1764             500               1653        −0.03    0.20     0.009    0.046
                2        New zhel , z×
                                     CMB                       1763             500               1652        −0.02    0.20     0.004    0.046
                3        z×
                          CMB , new vp                         1763             512               1653        −0.06    0.19    −0.008    0.045
                4        New zhel , new vp                     1764             512               1654         0.00    0.19     0.005    0.043
                5        Final (all corrections)               1763             512               1653            0    0.19          0   0.044
                6        Final, only host-z                    1576             495               1466         0.05    0.20    −0.022    0.048
                7        Final, group-z, vp                    1764             514               1650         0.05    0.18    −0.011    0.042
                8        Final, all z – σz                     1764             507               1650        −0.18    0.19     0.011    0.045
                9        Final, all z + σz                     1766             513               1660         0.20    0.19    −0.015    0.045
                10       Final, all z – 4 × 10–5               1765             512               1655        −0.05    0.19     0.013    0.044
                11       Final, all z + 4 × 10–5               1762             513               1652         0.06    0.19    −0.012    0.044
                12       Final, all σz × 3                     1708             512               1598         0.06    0.19    −0.014    0.045
                13       Final, SDSS σz + 3 × 10–5             1763             512               1653         0.00    0.19     0.000    0.044



(0) No corrections This is the original data without any red-                   (Kessler et al., 2009), biases are corrected following the BEAMS
    shift corrections.                                                          with Bias Correction (BBC) framework established in Kessler
(1–4) Partial corrections These variations are the permuta-                     & Scolnic (2017), and distance moduli µ are determined, all
    tions of (a) updating zhel ; (b) combining redshifts multi-                 within the PIPPIN framework (Hinton & Brout, 2020). The
    plicatively, z×CMB (as opposed to using the low-z additive
                                                                                details of this process are given in Brout et al. (2022). The
    approximation); (c) using our new peculiar velocities, vp .                 resulting distance moduli changes can be see in Figure 10.
(5) All corrections The nominal Final data includes all red-
    shift updates.
(6–7) Redshift source We consider first the subset of super-                         The total number of supernovae in each variation changes
    novae that have host-galaxy redshifts (1576 of the 1763                     slightly due to various reasons. When we restrict the red-
    redshifts). Second, for the entire sample we replace host-                  shift range for fitting H0 and w, some borderline-redshift
    galaxy redshifts with the redshift of the host galaxy’s group               supernovae are shifted in and out of the sample due to red-
    when available (186 of 1763 redshifts).                                     shift changes. However, shifting redshifts also affects the light
(8–11) Systematic offsets We consider two different forms                       curve fit parameters. The quality cuts we apply are to these
    of systematic redshift offsets: shifting the redshift by ±σz                fit parameters (among others) and also their errors. A redshift
    (variations 8, 9), and by ±4 × 10–5 (as suggested by Calcino                shift can therefore also shift a supernova in or out of the sample.
    & Davis, 2017; Brout et al., 2019) (variations 10, 11).                     For example, a light curve parameter may pass the cut with the
(12–13) Uncertainty changes The last test is how the size                       shifted redshift, or the fit may be poorer at the shifted redshift.
    of redshift uncertainties affects cosmological parameters
    (as suggested by Steinhardt et al., 2020), so we scale all
                                                                                    We expect µ to change when a supernova redshift changes
    uncertainties up by a factor of 3 (variation 12), and only
                                                                                because the duration of a light curve (stretch) is affected by
    SDSS-measured redshift uncertainties by +3 × 10–5 (varia-
                                                                                time-dilation and its colour is affected by K-corrections, both
    tion 13; see Section 4).
                                                                                of which are dependent on the measured heliocentric redshift
In addition, in Section 7.4 we discuss the sub-sample of SNe                    (but not the peculiar velocity correction); the theoretical basis
that lack host-z (187 SNe; the complement to variation 6), but                  for these variations is explained in Huterer et al. (2004). How-
we do not list this as a numbered variation due to the small                    ever, the distance modulus of a supernova may also change
number of SNe.                                                                  between sample variations without changing the redshift. The
                                                                                procedure for deriving distance moduli for a supernova sample
                                                                                (e.g. using BBC; Kessler & Scolnic, 2017) determines the peak
7.1 Dependence of distance modulus on redshift change                           magnitude (mB ) from the light curve, the global parameters
We analyse each variation independently, meaning that for                       α and β that adjust the stretch (x1 ) and colour (c) of the su-
each: each SN light curve is fit using the SALT2 model Guy                      pernovae, and a correction term for selection biases (δµbias ),
et al. (2010) as derived in Brout et al. (2021) using SNANA                     according to a modified version of the Tripp relation (Tripp,
14                                                                                                                                       Anthony Carr et al.




Figure 10. Difference in distance moduli for selected variations compared to the Final values (variation 5), µFinal . Faint points are individual SNe, while dark
points are binned in redshift. The grey shaded region represents the redshift range used to fit H0 . All deviations in the binned differences are within 1σ, where
the uncertainty comes only from distance modulus uncertainty (and not absolute magnitude calibration). The largest changes come from the updates to zhel
and next largest from the updates to vp .



1998), following Kessler et al. (2019),i

                    µ = mB – M + αx1 – βc – δµbias .                        (10)

Therefore the distance modulus may change even if the red-
shift is not altered since the calibration of α, β and absolute
magnitude (M) depend on the sample as a whole. This ex-
plains the slight changes in distance moduli for variation 6 (the
host-z sample), in which we do not alter any redshifts.
    The dependence of the change in a supernova’s µ between
variations on the change in z is demonstrated in Figure 11,
which shows that the two are strongly correlated (see also
Huterer et al., 2004). This correlation results in a cancellation
that reduces the impact of redshift uncertainties, particularly
at mid-range redshifts (around z ∼ 0.5). This can be seen
in the solid lines in Figure 11, which show the slope (dµ/dz)
of the Hubble diagram at different redshifts. At mid-range                           Figure 11. Change in distance modulus versus change in redshift (circles),
redshifts the slope is the same as the degeneracy direction                          and µ(z) derivatives dµ/dz for given redshifts (black lines). The largest
                                                                                     changes occurred due to amending zhel . The black lines represent the
between redshift change and distance modulus change. Thus
                                                                                     purely theoretical ∆µ that would occur on the Hubble diagram given the
uncertainties in redshift essentially cancel out at these redshifts,                 ∆z on the horizontal axis (in other words, the slope of the Hubble diagram
as they cause points to be shifted along the magnitude-redshift                      at those redshifts). The positive trend demonstrates that a change in red-
relation instead of deviating from it. This may be particularly                      shift is partially cancelled the corresponding change in µ (see discussion in
                                                                                     Section 7.1). This trend is seen in each variation.
helpful for supernova cosmology using photometric redshifts
whose uncertainties are larger than spectroscopic redshifts
(Chen et al., 2022).
                                                                                         For a simplified assessment of how redshift changes im-
     i In Equation 10 the parameters m , δ                                           pact cosmology, it is natural to simply use the published µ
                                      B   bias , x1 , and c are individual to each
supernova, while the parameters M, α, and β are common to the whole                  values, and shift the redshifts (as was done in Davis et al., 2019;
population.                                                                          Steinhardt et al., 2020). For the low-z sample, we show using
Publications of the Astronomical Society of Australia                                                                                              15


the large, transparent symbols in Figure 12 that this gives a                       magnitude and H0 , and we fit over the redshift range zHD >
reasonable approximation to the full analysis that uses recalcu-                    0.01. To estimate the changes in w we use the fast minimisation
lated µ values (smaller symbols). The main difference of not                        routine wFit in SNANA (Kessler et al., 2009) which outputs
recalculating µ is less cancellation of the effect of systematic                    marginalised cosmology parameters w and ΩM ; the complete
redshift changes. At intermediate redshifts one might expect                        fit with a thorough covariance analysis can be found in Brout
that neglecting the cancellation in dµ/dz may overestimate                          et al. (2022).
the deviation due to redshift shifts. Interestingly, we find that                        The results are shown in Table 4 and Figure 12; changes
when fitting for w without re-deriving µ the change in w                            in w are smaller than the statistical uncertainty of .0.03 given
often becomes slightly larger (e.g. variations 0–2) but in some                     in the full Pantheon+ w measurement from Brout et al. (2022)
cases (e.g. variations 8–9, shifting the redshifts by 1σz ) we find                 and the uncertainty of 0.04 from Pantheon (Scolnic et al.,
the shift in w goes in the opposite direction (likely due to σz                     2018). Applying all updates to the original redshifts results in
increasing with z). Overall we find that doing approximate                          ∆w = 0.003. The largest redshift variations, i.e. shifting all
cosmology fits by changing z without changing µ gives rea-                          redshifts by their 1σ uncertainties (variations 8 and 9) result in
sonable results, but for precision cosmology one should refit µ                     |∆w| ≤ 0.015.
whenever zhel changes.

                                                                                    7.4 SN-z vs host-z
7.2 Fitting H0
                                                                                    Using the original Pantheon sample, Steinhardt et al. (2020)
We first fit H0 using the method in Riess et al. (2016), that
                                                                                    find a statistically significant shift in the cosmological parame-
compares the distance modulus data to a low-redshift approxi-
                                                                                    ters derived for the subset of SNe that have redshifts measured
mation of the recession velocity.j The only free parameter in
                                                                                    from the supernova (SN-z) and those that have host-galaxy
this fit is H0 .
                                                                                    redshifts (host-z). Here we revisit this analysis with our up-
    For this fit we focus on only the low-redshift regime of
                                                                                    dated data.
0.0233 < zHD < 0.15, which is the standard range used by
previous supernova cosmology analyses such as Riess et al.                              There are several important differences between Steinhardt
(2016, 2018). In the Final dataset this redshift range contains                     et al. (2020) and our analysis: 1) Steinhardt et al. (2020) fit all
512 SNe of which only 17 lack host galaxy redshifts.                                wCDM parameters simultaneously, 2) our definition of the
    When calculating the uncertainties we only consider the                         SN-z sample is stricter than their not-host-z, in that we allow
statistical uncertainties in the distance moduli of the super-                      host emission-lines in SN-dominated spectra to be assigned to
novae, not the uncertainties in the absolute magnitude cali-                        the host-z sample, and 3) our allocation of SN-z particularly
bration. Thus the uncertainties in H0 in Figure 12 reflect the                      for PS1MD and SDSS SNe differs from theirs. We expect
size of shifts due only to redshift/sample variations and not                       the SDSS classifications to differ because, as we addressed in
the size of uncertainties in the H0 measurements (for example                       Section 3, we updated 81 SN-zs to host-zs (and further, applied
the current uncertainty on H0 from SN cosmology is about 5                          the +2.2 × 10–3 systematic offset to the remaining SN-zs as
times larger).                                                                      determined in Sako et al., 2018). However, the reason for the
    The results are shown in Table 4 and Figure 12, where we                        PS1MD classification differences are unclear; our classifications
see that the redshift improvements we have made have a small                        come directly from reported redshift uncertainties (SN-z have
impact on the value of H0 relative to the uncertainty from the                      uncertainties of 0.01 and host-z 0.001).
SH0ES H0 measurement with uncertainty of 1.0 km s–1 Mpc–1                               We find that restricting the data to only those SNe with
(Riess et al., 2022). We define the difference in cosmological                      host-z (variation 6 in Table 4 and Figure 12) gives ∆H0 =
parameters for each variation to be the variation minus the                         0.05 ± 0.20 km s–1 Mpc–1 (i.e. 0.3σ) relative to the nominal
                                                                                    Final dataset. By contrast, when we restrict the data to the
Final value, i.e. ∆H0 = H0n – H0Final for variation n. Applying
                                                                                    SN-z sample (of which only 17 are in the redshift range of
all updates to the original redshifts results in ∆H0 = –0.12
                                                                                    the H0 fit), we find ∆H0 = –2.8 ± 1.3 km s–1 Mpc–1 .
km s–1 Mpc–1 . The largest redshift variations, i.e. shifting all
redshifts by their 1σ uncertainties (variations 8 and 9) result in                      These results are broadly consistent with Steinhardt et al.
|∆H0 | ≤ 0.2 km s–1 Mpc–1 .                                                         (2020), who found that ∆H0 = 0.45 ± 0.25 km s–1 Mpc–1 for
                                                                                    the host-z sample and ∆H0 = –0.96 ± 0.50 km s–1 Mpc–1 for
                                                                                    the SN-z sample. The significance of the shift in the host-z
7.3 Fitting wCDM
                                                                                    sample is lower in our case, which is likely due to the greater
We also evaluate the impact of the redshift updates on the                          proportion of host-z redshifts in our sample and the corrections
best fit parameters in the flat-wCDM model. This model has                          we have implemented to the SN-z based on the systematic
two free parameters: the matter density Ωm , and the equation                       offset correction determined by Sako et al. (2018). On the
of state of dark energy w, but we implement a Planck-like                           other hand, the H0 shift we find in the SN-z sample is larger
prior on the matter density of Ωm = 0.311 ± 0.010 so we                             than Steinhardt et al. (2020), but our results are of similar
can isolate the impact on w. We marginalise over absolute                           significance (approximately 2σ in each case) since we have
   j v(z, q , j ) ≈ cz
                                                                                  fewer SNe in the SN-z sample.
           0 0    1 + 12 (1 – q0 )z – 61 (1 – q0 – 3q20 + j0 )z2 , which uses the
                    1+z
canonical ΛCDM value of the deceleration parameter q0 = –0.55 and jerk                  Increasing the redshift range over which we fit for H0 adds
j0 = 1.                                                                             some model dependence, but allows us to include more of the
16                                                                                                                                                Anthony Carr et al.


                                                        0.0233 < zHD < 0.15                        zHD > 0.01

                                        Original                                                                            0

                                       New zhel                                                                             1



                                                                                                                                 Corrections
                                            ×
                                New zhel , zCMB                                                                             2
                                      ×
                                 New zCMB , vp                                                                              3

                                   New zhel , vp                                                                            4

                                           Final                                                                            5

                                         Host-z                                                                             6

                                    Group-z, vp                                                                             7

                                         z − σz                                                                             8



                                                                                                                                     Variations
                                         z + σz                                                                             9

                                       z − zsyst                                                                            10

                                       z + zsyst                                                                            11

                                         σz × 3                                                                             12

                             σzSDSS + 3 × 10−5                                                                              13
                                                      −0.25      0.00       0.25           −0.05       0.00       0.05
                                                                ∆H0                                   ∆w

Figure 12. The impact on inferences of H0 and w due to changes in the redshifts. The regular symbols are the nominal results while the faint, larger symbols
come from not recalculating µ after changing redshift so that the partial cancellations seen in Figure 11 are not present. The descriptions on the left hand side
and variation numbers on the right hand side both correspond to the descriptions in Table 4. The H0 fit uses the redshift range 0.0233 < zHD < 0.15, while the
w fit uses the range zHD > 0.01, where the maximum redshift of the sample is 2.26. The uncertainties in both H0 and w only represent the statistical uncertainty
from the SN magnitude uncertainties—they do not contain any uncertainty from distance ladder calibration nor intrinsic dispersion in SN magnitudes. All
variations are small, showing that the cosmology results are robust to small changes in redshift and there is no indication of systematic redshift errors biasing
previous results.



SN-z sample. When we do so the deviation from the nominal                          for this shift can be seen in Figure 10, where the SN-z sample
dataset vanishes, with the results from SN-z alone agreeing                        shows a systematic positive offset in ∆µ at low redshift, but
with the result from host-z alone (within 1σ) for all zmax &                       a negative offset at high redshift. Any shift with a redshift
0.25. Figure 13 shows the impact of including or excluding                         dependence will have an impact on w whereas a constant shift
SN-z from our fit for H0 , as a function of redshift range used in                 would mainly affect H0 .
the fit. The impact is small, with |∆H0 | . 0.05 km s–1 Mpc–1 .                        Given these results, in Section 8 we discuss whether SN-z
    As expected, Figure 13 shows that as we increase the maxi-                     samples should be included in cosmological fits.
mum redshift in our H0 fit the cosmological model-dependence
becomes increasingly apparent. The vapprox (z, q0 , j0 ) equation
in Section 7.2 is a good approximation to the full equation                        7.5    Redshift systematics and uncertainty values
        R z dz
v(z) = c 0 E(z) where E(z) ≡ H(z)/H0 , as long as Ωm ∼ 0.3                         As expected, some of the largest changes in H0 and w occur
for the flat-ΛCDM model. Over the nominal redshift range                           when we add a systematic shift to all redshifts in the sample
of 0.0233 < zHD < 0.15 (black point) a shift of ∆Ωm ± 0.05                         (variations 8–11). However, even when we shift the redshifts
results in ∆H0 ∓ 0.2 km s–1 Mpc–1 , showing the cosmological                       systematically by their uncertainties (variations 8–9) the impact
model-dependence is still sub-dominant to the sampling un-                         is only |∆H0 | ∼ 0.2 ± 0.2 km s–1 Mpc–1 and |∆w| ∼ 0.015 ±
certainties on H0 (which is the purpose of using the restricted                    0.045, smaller than the sample uncertainties in each case.
redshift range).                                                                       Changing the size of the uncertainties on the redshifts has
    For the equation of state of dark energy, the host-z only                      a negligible impact on the cosmological parameters (variations
case (6) shows a shift of ∆w = –0.022 ± 0.048. This is the                         12–13).
largest impact on w of any variation, albeit still insignificant
(0.6σ). Using only SN-z gives ∆w = 0.25 ± 0.16. The reason
Publications of the Astronomical Society of Australia                                                                                              17


                                                                                    standard candle (TRGB or Cepheids), that acts as an anchor.
                                                                                        Finally, many potential systematic redshift errors (for ex-
                                                                                    ample due to the approximate heliocentric to CMB-frame
                                                                                    conversion) are only systematic if the sample covers a small
                                                                                    area of the sky. The low-z supernova sample (z . 0.15), for
                                                                                    which redshift errors could have a large impact, is spread across
                                                                                    most of the sky (see Figure 1). We also confirmed in Section
                                                                                    6.1 that the new peculiar velocities do not systematically dif-
                                                                                    fer from those previously predicted. Thus the updates to the
                                                                                    redshifts of Pantheon+ mostly caused random shifts, predomi-
                                                                                    nantly via updating zhel and vp . Across the whole sample the
                                                                                    root-mean-square deviation of all the redshift changes was
                                                                                    ∼ 3 × 10–3 , however the mean redshift change was an order
                                                                                    of magnitude smaller (∼ 4 × 10–4 ). Within the redshift range
                                                                                    0.0233 < zHD < 0.15, RMS(∆zHD ) ∼ 1 × 10–3 and the mean
Figure 13. The dependence of H0 on the redshift-range we fit over. The hor-         redshift change was ∼ 1 × 10–4 . The mean change is actually
izontal axis shows the maximum redshift used in the fit, keeping the min-           almost completely frame and redshift-range independent, but
imum redshift as zHD = 0.0233. Red shows the Final sample, and blue                 is smaller for the H0 sample because, unlike for the mean zhel
shows the host-z sample in order to demonstrate the impact of excluding
SNe that only have SN-z. As redshift increases the cosmological model de-           of the full sample, it does not account for repeat observations
pendence becomes increasingly important so the grey shading shows the               of the same SNe originally being assigned different zhel . This
range of H0 values from fitting with 0.25 < Ωm < 0.35 in the flat-ΛCDM              resulting impact on H0 is consistent with that predicted by
model (Ωm = 0.35 being the lower edge). At the nominal upper redshift
                                                                                    Davis et al. (2019, see the green dashed line in their Figure 4).
limit of zmax = 0.15 the statistical variance of the sample (black error bar) re-
mains larger than the uncertainty due to even this quite wide range of Ωm .             We compared the cosmological results with and without
                                                                                    the sample that has only supernova redshifts in Section 7.4).
                                                                                    As in previous studies (e.g. Steinhardt et al., 2020), we found
8.   Discussion and Conclusions                                                     differences in the results from these sub-samples, the most
Motivated in part by the fact that a systematic error in redshift                   significant of which was a 2σ deviation in H0 for the SN-z
could affect standard candle derivations of H0 , especially if it                   sub-sample. While it is possible this is a statistical fluctuation
were at low redshift, we have reviewed and revised the red-                         with so few SNe in the SN-z sample, there are reasons to
shifts for the Pantheon+ supernova sample. This includes fix-                       expect a systematic offset from the host-z sample. When host
ing bookkeeping errors, updating heliocentric redshifts when                        galaxies lack redshifts it is usually because they are faint and/or
available, adding uncertainty estimates, converting from the                        low-mass, and SNe Ia properties are correlated with their hosts’
heliocentric to the CMB-frame redshifts without using the                           properties (e.g. Sullivan et al., 2006; Smith et al., 2020b; Wise-
low-z additive approximation, updating peculiar velocity es-                        man et al., 2020). Therefore the SN-z sample could represent
timates at all redshifts, and correcting the peculiar velocities                    a physically different subset of SNe that is not accounted for
from large-scale flow predictions at large redshifts.                               in, e.g. SALT2 modelling. Alternatively, a slight bias could
    These curated redshifts are the ones that should be used in                     arise if, for example, supernova spectral templates do not fully
the future for all supernova cosmology analyses using these                         account for the blueshift due to the velocity of the visible side
data. They are available at the CDS VizieR database and also                        of the supernova’s photosphere.
https://github.com/PantheonPlusSH0ES/DataRelease, and the                               Given the greater uncertainty in supernova redshifts com-
code that generated the peculiar velocity predictions can be                        pared to host-galaxy redshifts, and the potential for bias (as
found at https://github.com/KSaid-1/pvhub.                                          seen with SDSS SNe in Zheng et al., 2008; Sako et al., 2018),
    We found that these redshift updates do not have a large                        one could consider removing all supernovae that lack a host
impact on cosmological results. This fortunate circumstance                         redshift from cosmology samples. This would reduce the cos-
arises for a few reasons. Firstly, errors at high-z are relatively                  mologically useful sample size slightly, and thus sacrifice a
unimportant, because the relative uncertainty in redshift de-                       small amount of precision for potentially greater accuracy. At
creases as redshift increases. That is compounded by the fact                       z < 0.15 approximately 3% of the Type Ia supernova sam-
that a particular ∆z corresponds to a much smaller distance dif-                    ple lacks host galaxy redshifts, but that proportion increases
ference at high-z than at low-z. Furthermore the ∆µ versus                          to approximately 10% at high redshift. Excluding the SN-z
∆z correlation we mentioned in Section 7.1 and Figure 11                            excludes a different proportion of the supernova population
reduces the impact of redshift errors, especially near z ∼ 0.5.                     as a function of redshift. While this effect should be mon-
Thus at high-z even a large error in redshift gives a small error                   itored for future cosmological studies (and should motivate
in expected magnitude.                                                              further follow-up efforts to get host-z), we have shown here
    Secondly, for the SNe at very low redshifts (z < 0.01) that                     that the impact of including or excluding the SN-z sample
are used to calibrate the SN Ia absolute magnitude, the redshifts                   remains small relative to the uncertainties in the measurement
are not used—they are replaced by the brightness of another                         (Figure 13).
18                                                                                                                          Anthony Carr et al.


     Finally, we have also made sure all supernova redshifts now      pay our respects to elders past and present.
have estimated uncertainties. As noted by Steinhardt et al.
(2020), uncertainties are important because sampling from a           References
symmetric redshift uncertainty systematically prefers a larger        Abazajian, K. N., Adelman-McCarthy, J. K., Agüeros, M. A., et al. 2009, ApJS,
µ for a given redshift due to the sublinear nature of the µ(z)           182, 543
relation. This would effectively reduce the gradient of the µ(z)      Balam, D. 2016, Transient Name Server Classification Report, 2016-48, 1
relation at low-z and cause samples with large uncertainties          Bassett, B., Becker, A., Brewington, H., et al. 2006, Central Bureau Electronic
                                                                         Telegrams, 743, 1
(such SN-z) to prefer a smaller H0 . Furthermore, the precision
                                                                      Bassett, B., Becker, A., Bizyaev, D., et al. 2007, Central Bureau Electronic
of redshift indirectly affects one of the largest systematic uncer-      Telegrams, 1102, 1
tainties in SNe Ia analyses: the determination of their intrinsic     Betoule, M., Kessler, R., Guy, J., et al. 2014, A&A, 568, A22
scatter. If the precision is not correctly measured, more or          Blondin, S., Modjaz, M., Kirshner, R., Challis, P., & Calkins, M. 2007, Central
less scatter will be attributed to the intrinsic variation of SN Ia      Bureau Electronic Telegrams, 978, 1
distances, which could bias the modelling used to determine           Blondin, S., & Tonry, J. L. 2007, ApJ, 666, 1024
accurate distances. Additionally, the precision and accuracy          Blondin, S., Matheson, T., Kirshner, R. P., et al. 2012, AJ, 143, 126
of redshifts must be known accurately when using SNe Ia to            Bolton, A. S., Schlegel, D. J., Aubourg, É., et al. 2012, AJ, 144, 144
measure growth-of-structure. In that case, instead of applying        Bonnarel, F., Fernique, P., Bienaymé, O., et al. 2000, A&AS, 143, 33
peculiar velocities to SNe from an external model, one uses           Boruah, S. S., Hudson, M. J., & Lavaux, G. 2020, MNRAS, 498, 2703
SNe Ia to measure peculiar velocities.                                Bosma, A., & Freeman, K. C. 1993, AJ, 106, 1394
     Most of the uncertainties we provide are based on the            Brout, D., Scolnic, D., Kessler, R., et al. 2019, ApJ, 874, 150
precision of a particular survey or sample. A better method           Brout, D., Taylor, G., Scolnic, D., et al. 2021, arXiv e-prints,
                                                                          arXiv:2112.03864
for determining uncertainties would be to estimate them on a
                                                                      Brout, D., Scolnic, D., Popovic, B., et al. 2022, arXiv e-prints,
spectrum-by-spectrum basis. However, we tested the impact                 arXiv:2202.04077
of changing the uncertainties (see Figure 12) and it had a            Brown, P. J., Breeveld, A. A., Holland, S., Kuin, P., & Pritchard, T. 2014,
negligible affect on the cosmological results, so we conclude            Ap&SS, 354, 89
that the uncertainties we provide are sufficient for current data.    Burns, C. R., Parent, E., Phillips, M. M., et al. 2018, ApJ, 869, 56
     While new surveys and datasets will continue to come             Burns, C. R., Ashall, C., Contreras, C., et al. 2020, ApJ, 895, 118
online over the next decade, the sample presented here will not       Calcino, J., & Davis, T. 2017, J. Cosmology Astropart. Phys., 2017, 038
easily be replaced due to its utility for measuring H0 , which is     Carr, A., & Davis, T. 2021, ApJ, 914, 97
rate-limited by the number of SNe in the very-nearby universe         Carrick, J., Turnbull, S. J., Lavaux, G., & Hudson, M. J. 2015, MNRAS, 450,
                                                                          317
and will take another 30 years to re-accumulate. Because of
                                                                      Chen, P., Dong, S., Kochanek, C. S., et al. 2020, arXiv e-prints,
that importance, in this work we endeavour to provide an                  arXiv:2011.02461
updated and homogeneously treated set of supernova redshifts          Chen, R., Scolnic, D., Rozo, E., et al. 2022, arXiv e-prints, arXiv:2202.10480
that we hope will be useful to the community.                         Childress, M., Aldering, G., Antilogus, P., et al. 2013, ApJ, 770, 107
                                                                      Colless, M., Dalton, G., Maddox, S., et al. 2001, MNRAS, 328, 1039
                                                                      Colless, M., Peterson, B. A., Jackson, C., et al. 2003, arXiv e-prints, astro
Acknowledgement                                                       Contreras, C., Hamuy, M., Phillips, M. M., et al. 2010, AJ, 139, 519
The authors thank A. Whitford, C. Chang, Y. Lai, A. Glanville         Dark Energy Survey. 2019, ApJ, 872, L30
and L. Rauf for assisting in visual inspection of host galaxies       Davis, T. M., Hinton, S. R., Howlett, C., & Calcino, J. 2019, MNRAS, 490,
and performing redshift checks in NED (Section 3). We also                2948
thank C. Howlett, M. Colless, and M. Hudson for useful dis-           de Vaucouleurs, G., de Vaucouleurs, A., Corwin, Herold G., J., et al. 1991,
                                                                         Third Reference Catalogue of Bright Galaxies (Springer-Verlag New York)
cussions on peculiar velocities and M. Smith for insights into
                                                                      Drinkwater, M. J., Byrne, Z. J., Blake, C., et al. 2018, MNRAS, 474, 4151
SN host galaxies. TMD is the recipient of an Australian Re-
                                                                      Falco, E. E., Kurtz, M. J., Geller, M. J., et al. 1999, PASP, 111, 438
search Council Australian Laureate Fellowship (project number
                                                                      Filippenko, A. V., Wong, D. S., & Ganeshalingam, M. 2007, Central Bureau
FL180100168) funded by the Australian Government. DS is                   Electronic Telegrams, 984, 1
supported by DOE grant DE-SC0010007, DE-SC0021962                     Fixsen, D. J., Cheng, E. S., Gales, J. M., et al. 1996, ApJ, 473, 576
and the David and Lucile Packard Foundation. DS is supported          Folatelli, G., Morrell, N., Phillips, M. M., et al. 2013, ApJ, 773, 53
in part by the National Aeronautics and Space Administration          Foley, R. J., Scolnic, D., Rest, A., et al. 2018, MNRAS, 475, 193
under Contract No. NNG17PX03C issued through the Ro-                  Fouqué, P., Durand, N., Bottinelli, L., Gouguenheim, L., & Paturel, G. 1992,
man Science Investigation Teams Programme.                                Catalogue of Optical Radial Velocities, Monographies de la base de donneés
                                                                          extragalactiques (Observatoire de Lyon)
     This work has made use of the NASA/IPAC Extragalactic
                                                                      Gall, C., Stritzinger, M. D., Ashall, C., et al. 2018, A&A, 611, A58
Database, which is funded by the National Aeronautics and
                                                                      Ganeshalingam, M., Li, W., Filippenko, A. V., et al. 2010, ApJS, 190, 418
Space Administration and operated by the California Institute         Garnavich, P., Marion, H., Challis, P., Blondin, S., & Kirshner, R. 2007,
of Technology. This work was also supported by resources pro-             Central Bureau Electronic Telegrams, 1176, 1
vided by the University of Chicago Research Computing Cen-            Gilliland, R. L., Nugent, P. E., & Phillips, M. M. 1999, ApJ, 521, 30
ter, and based in part on data acquired at the Anglo-Australian       Goldhaber, G., Groom, D. E., Kim, A., et al. 2001, ApJ, 558, 359
Telescope. We acknowledge the traditional custodians of the           Gupta, R. R., D’Andrea, C. B., Sako, M., et al. 2011, ApJ, 740, 92
land on which the AAT stands, the Gamilaraay people, and              Gupta, R. R., Kuhlmann, S., Kovacs, E., et al. 2016, AJ, 152, 154
Publications of the Astronomical Society of Australia                                                                                                        19


Guy, J., Astier, P., Baumont, S., et al. 2007, A&A, 466, 11                       Scolnic, D., Brout, D., Carr, A., et al. 2021, arXiv e-prints, arXiv:2112.03863
Guy, J., Sullivan, M., Conley, A., et al. 2010, A&A, 523, A7                      Scolnic, D. M., Jones, D. O., Rest, A., et al. 2018, ApJ, 859, 101
Hamuy, M., Phillips, M. M., Suntzeff, N. B., et al. 1996, AJ, 112, 2408           Silverman, J. M., Foley, R. J., Filippenko, A. V., et al. 2012, MNRAS, 425,
Hicken, M., Challis, P., Jha, S., et al. 2009, ApJ, 700, 331                         1789
Hicken, M., Challis, P., Kirshner, R. P., et al. 2012, ApJS, 200, 12              Smith, M., D’Andrea, C. B., Sullivan, M., et al. 2020a, AJ, 160, 267
Hinton, S., & Brout, D. 2020, The Journal of Open Source Software, 5, 2122        Smith, M., Sullivan, M., Wiseman, P., et al. 2020b, MNRAS, 494, 4426
Hsiao, E. Y., Burns, C. R., Contreras, C., et al. 2015, A&A, 578, A9              Springob, C. M., Haynes, M. P., Giovanelli, R., & Kent, B. R. 2005, ApJS,
                                                                                     160, 149
Huchra, J., Jarrett, T., Skrutskie, M., et al. 2005, in Astronomical Society of
   the Pacific Conference Series, Vol. 329, Nearby Large-Scale Structures and     Stahl, B. E., Zheng, W., de Jaeger, T., et al. 2019, MNRAS, 490, 3882
   the Zone of Avoidance, ed. A. P. Fairall & P. A. Woudt, 135                    Steinhardt, C. L., Sneppen, A., & Sen, B. 2020, ApJ, 902, 14
Huchra, J. P., Vogeley, M. S., & Geller, M. J. 1999, ApJS, 121, 287               Stritzinger, M., Burns, C. R., Phillips, M. M., et al. 2010, AJ, 140, 2036
Huchra, J. P., Macri, L. M., Masters, K. L., et al. 2012, ApJS, 199, 26           Sullivan, M., Le Borgne, D., Pritchet, C. J., et al. 2006, ApJ, 648, 868
Huterer, D., Kim, A., Krauss, L. M., & Broderick, T. 2004, ApJ, 615, 595          Suzuki, N., Rubin, D., Lidman, C., et al. 2012, ApJ, 746, 85
Jha, S., Riess, A. G., & Kirshner, R. P. 2007, ApJ, 659, 122                      Theureau, G., Bottinelli, L., Coudreau-Durand, N., et al. 1998, A&AS, 130,
Jha, S., Kirshner, R. P., Challis, P., et al. 2006, AJ, 131, 527                     333
Jones, D. H., Read, M. A., Saunders, W., et al. 2009, MNRAS, 399, 683             Tonry, J., & Davis, M. 1979, AJ, 84, 1511
Jørgensen, I., Chiboucas, K., Webb, K., & Woodrum, C. 2018, AJ, 156, 224          Tripp, R. 1998, A&A, 331, 815
Kawabata, M., Maeda, K., Yamanaka, M., et al. 2020, ApJ, 893, 143                 Tsvetkov, D. Y., & Elenin, L. 2010, Peremennye Zvezdy, 30, 2
Kessler, R., & Scolnic, D. 2017, ApJ, 836, 56                                     van den Bosch, R. C. E., Gebhardt, K., Gültekin, K., Yıldırım, A., & Walsh,
                                                                                     J. L. 2015, ApJS, 218, 10
Kessler, R., Bernstein, J. P., Cinabro, D., et al. 2009, PASP, 121, 1028
                                                                                  Wang, L., Baade, D., Clocchiatti, A., et al. 2008, Central Bureau Electronic
Kessler, R., Brout, D., D’Andrea, C. B., et al. 2019, MNRAS, 485, 1171
                                                                                     Telegrams, 1509, 1
Kiyota, S., Holoien, T. W. S., Stanek, K. Z., et al. 2014, The Astronomer’s
                                                                                  Wang, L., Pulliam, C., & Wheeler, J. C. 1997, IAU Circ., 6753, 2
   Telegram, 6809, 1
                                                                                  Wee, J., Chakraborty, N., Wang, J., & Penprase, B. E. 2018, ApJ, 863, 90
Krisciunas, K., Suntzeff, N. B., Espinoza, J., et al. 2017a, Research Notes of
   the American Astronomical Society, 1, 36                                       Wegner, G., Bernardi, M., Willmer, C. N. A., et al. 2003, AJ, 126, 2268
Krisciunas, K., Contreras, C., Burns, C. R., et al. 2017b, AJ, 154, 211           Wiseman, P., Smith, M., Childress, M., et al. 2020, MNRAS, 495, 4040
Lahav, O., Santiago, B. X., Webster, A. M., et al. 2000, MNRAS, 312, 166          Wojtak, R., Davis, T. M., & Wiis, J. 2015, J. Cosmology Astropart. Phys.,
                                                                                     2015, 025
Lasker, J., Kessler, R., Scolnic, D., et al. 2019, MNRAS, 485, 5329
                                                                                  Wood-Vasey, W. M., Miknaitis, G., Stubbs, C. W., et al. 2007, ApJ, 666, 694
Lavaux, G., & Hudson, M. J. 2011, MNRAS, 416, 2840
                                                                                  Yan, P.-F., Yuan, Q.-R., Zhang, L., & Zhou, X. 2014, AJ, 147, 106
Li, W., Filippenko, A. V., Treffers, R. R., et al. 2001, ApJ, 546, 734
                                                                                  Yuan, F., Quimby, R., Sisson, M. D., et al. 2008a, Central Bureau Electronic
Lidman, C., Tucker, B. E., Davis, T. M., et al. 2020, MNRAS, 496, 19
                                                                                     Telegrams, 1245, 1
Matheson, T., Challis, P., Kirshner, R., Macri, L., & Berlind, P. 2002,
                                                                                  Yuan, F., Quimby, R., Chamarro, D., et al. 2008b, Central Bureau Electronic
   IAU Circ., 8013, 2
                                                                                     Telegrams, 1513, 1
Milne, P. A., Brown, P. J., Roming, P. W. A., et al. 2010, ApJ, 721, 1627
                                                                                  Yuk, H., Zheng, W., Filippenko, A. V., et al. 2014, Central Bureau Electronic
Mitra, A., & Linder, E. V. 2021, Phys. Rev. D, 103, 023524                           Telegrams, 3893, 1
Mueller, J., Rykoski, K. M., Garnavich, P., et al. 1996, IAU Circ., 6317, 1       Zhang, J., & Wang, X. 2014, The Astronomer’s Telegram, 6171, 1
Nakano, S., Zheng, W., Chatzopoulos, E., et al. 2010, Central Bureau Elec-        Zhang, T., Wang, X., Li, W., et al. 2010, PASP, 122, 1
   tronic Telegrams, 2200, 1
                                                                                  Zheng, C., Romani, R. W., Sako, M., et al. 2008, AJ, 135, 1766
Östman, L., Nordin, J., Goobar, A., et al. 2011, A&A, 526, A28
Perlmutter, S., Aldering, G., Goldhaber, G., et al. 1999, ApJ, 517, 565
Peterson, E. R., Kenworthy, W. D., Scolnic, D., et al. 2021, arXiv e-prints,
   arXiv:2110.03487
Phillips, M. M. 1993, ApJ, 413, L105
Phillips, M. M., Lira, P., Suntzeff, N. B., et al. 1999, AJ, 118, 1766
Phillips, M. M., Contreras, C., Hsiao, E. Y., et al. 2019, PASP, 131, 014001
Planck Collaboration, Aghanim, N., Akrami, Y., et al. 2020, A&A, 641, A1
Quimby, R., Madison, D. R., Li, W., Shetrone, M., & Riley, V. 2007, Central
   Bureau Electronic Telegrams, 873, 1
Rameez, M., & Sarkar, S. 2021, Classical and Quantum Gravity, 38, 154005
Riess, A. G., Filippenko, A. V., Challis, P., et al. 1998, AJ, 116, 1009
Riess, A. G., Kirshner, R. P., Schmidt, B. P., et al. 1999, AJ, 117, 707
Riess, A. G., Nugent, P. E., Gilliland, R. L., et al. 2001, ApJ, 560, 49
Riess, A. G., Strolger, L.-G., Tonry, J., et al. 2004, ApJ, 607, 665
Riess, A. G., Strolger, L.-G., Casertano, S., et al. 2007, ApJ, 659, 98
Riess, A. G., Macri, L. M., Hoffmann, S. L., et al. 2016, ApJ, 826, 56
Riess, A. G., Rodney, S. A., Scolnic, D. M., et al. 2018, ApJ, 853, 126
Riess, A. G., Yuan, W., Macri, L. M., et al. 2022, ApJ, 934, L7
Said, K., Colless, M., Magoulas, C., Lucey, J. R., & Hudson, M. J. 2020,
   MNRAS, 497, 1275
Sako, M., Bassett, B., Becker, A. C., et al. 2018, PASP, 130, 064002
Scolnic, D., Casertano, S., Riess, A., et al. 2015, ApJ, 815, 117
20                                                                                                                    Anthony Carr et al.


Appendix 1.   Supplementary Data Tables

                                            Table A1. Averaging of multiple SDSS redshifts.

                       SNID     Host                               zhel         σz               z̄         σz̄
                                                                0.033176     1.0 × 10−5
                       2003cq   NGC 3978                                                      0.033194   1.8 × 10−5
                                                                0.033211     1.2 × 10−5
                                                                0.006352     1.2 × 10−5
                       2003du   UGC 9391                        0.006373     1.2 × 10−5       0.006377   1.6 × 10−5
                                                                0.006406     1.3 × 10−5
                                                                0.016897     0.5 × 10−5
                                                                0.016923     0.7 × 10−5
                       2003Y    IC 0522                                                       0.016892   1.2 × 10−5
                                                                0.016865     0.7 × 10−5
                                                                0.016884     0.8 × 10−5
                                                                0.182908     2.3 × 10−5
                       1580     WISEA J030117.99-003842.4       0.182944     1.9 × 10−5       0.182932   1.2 × 10−5
                                                                0.182945     1.9 × 10−5
                                                                0.028907     1.0 × 10−5
                       2005eq   MCG -01-09-006                                                0.028952   4.5 × 10−5
                                                                0.028996     1.0 × 10−5
                                                                0.262757     5.2 × 10−5
                       13655    WISEA J023605.02-005939.8                                     0.262699   5.9 × 10−5
                                                                0.262640     3.9 × 10−5
                                                                0.048475     1.2 × 10−5
                       2006cq   IC 4239                                                       0.048442   3.3 × 10−5
                                                                0.048409     1.2 × 10−5
                                                                0.132185     3.7 × 10−5
                       18809    WISEA J032331.35+004002.1                                     0.132159   2.6 × 10−5
                                                                0.132133     3.5 × 10−5
                                                                0.246696     2.7 × 10−5
                       20039    WISEA J003931.06+010125.2       0.246882     2.5 × 10−5       0.246809   5.7 × 10−5
                                                                0.246850     2.2 × 10−5
                                                                0.027821     0.6 × 10−5
                       2007su   SDSS J221908.85+131040.4                                      0.027832   1.1 × 10−5
                                                                0.027842     0.6 × 10−5
                                                                0.052828     4.6 × 10−5
                       2008ac   J115345.22+482521.0                                           0.052808   2.0 × 10−5
                                                                0.052788     8.2 × 10−5
                                                                0.021054     1.0 × 10−5
                       2008ds   UGC 299                                                       0.021061   0.7 × 10−5
                                                                0.021068     1.2 × 10−5
                                                                0.020745     1.2 × 10−5
                       2010A    UGC 2019                                                      0.020755   1.0 × 10−5
                                                                0.020765     1.4 × 10−5
                                                                0.033690     1.1 × 10−5
                       2010ag   UGC 10679                                                     0.033715   2.5 × 10−5
                                                                0.033739     1.2 × 10−5
                                                                0.018282     2.6 × 10−5
                       2010ai   WISEA J125925.01+275948.2                                     0.018267   1.5 × 10−5
                                                                0.018252     3.5 × 10−5
                                                                0.089493     1.3 × 10−5
                       590194   WISEA J084056.86+443127.4                                     0.089513   2.0 × 10−5
                                                                0.089532     1.3 × 10−5
                                                                0.016161     0.6 × 10−5
                       2011im   NGC 7364                                                      0.016163   0.2 × 10−5
                                                                0.016164     0.8 × 10−5
                                                                0.016797     1.6 × 10−5
                       2013gs   UGC 5066                                                      0.016812   1.5 × 10−5
                                                                0.016827     1.7 × 10−5
Table A2. Heliocentric redshift update discrepancies ≥ 1×10–3 . Discrepancies that arise from SN redshifts are generally not included (unless they are particularly large or unusual) since they are routinely




                                                                                                                                                                                                                 Publications of the Astronomical Society of Australia
larger than 1×10–3 .

        SNID              Host                               zold          znew        Difference     Comments
        2014bj            WISEA J192240.35+435317.7       0.005         0.043         3.8 × 10−2      Original ATEL adopts a redshift of 0.045 (Zhang & Wang, 2014), subsequent classification 0.043
                                                                                                      (Balam, 2016), photometric host redshift of 0.042 (Yan et al., 2014) is in agreement. Old redshift
                                                                                                      comes from Stahl et al. (2019), which cites CBET 3893 (Yuk et al., 2014). The smaller redshift is a
                                                                                                      valid but less likely fit to the SN spectrum.
        2009dca           UGC 10064                       0             0.021 787     2.2 × 10−2      Only affects CSP DR2 redshift, and was corrected in DR3.
        14782             SDSS J205656.18-001645.0        0.179         0.1604       −1.9 × 10−2      New redshift is spectroscopic host redshift, and agrees with SNID redshift of 0.165 (Östman et al.,
                                                                                                      2011). Sako et al. (2018) publishes the old redshift 0.179, which is a SN redshift. We mention this
                                                                                                      particular example of SN to host redshift because it is an extreme outlier.
        Strolger          ...                             1.01          1.027         1.7 × 10−2      Uncertain origin of zold ; znew matches Riess et al. (2007).
        580104            ...                             0.31          0.3232        1.3 × 10−2      zold comes from PS1MD but was measured to higher precision by DES (580104 is the same SN
                                                                                                      as 1261579).
        Mcguire           ...                             1.37          1.357        −1.3 × 10−2      Potential typo; znew matches Riess et al. (2007).
        2007co            CGCG 172-029                    0.016 962     0.026 962     1.0 × 10−2      Appears to be an error in the SOUSA record (leading 1 should be a 2). znew confirmed by CfA3,
                                                                                                      LOSS records and classification CBET (Blondin et al., 2007).
        2002hu            MCG +06-06-012                  0.03          0.0367        6.7 × 10−3      Origin of zold appears to be the NED reference to IAUC 8013 (Matheson et al., 2002) that incor-
                                                                                                      rectly states a redshift of 0.03. znew is from Matheson et al. (2002), who state the recession ve-
                                                                                                      locity of the host galaxy is 11000 km s–1 , which translates to z = 0.0367.
        2008ad            2MASS J12493690+2819445         0.050         0.055 441     5.4 × 10−3      Appears to be a NED error; classification CBET finds z = 0.054 (Yuan et al., 2008a) while NED
                                                                                                      reports zold = 0.05 for the host name WISEA J124936.88+281944.7. znew from SDSS DR13.
        2010ai            WISEA J125925.01+275948.2       0.0233        0.018 267    −5.0 × 10−3      SN and host are part of a cluster, possibly resulting in zold = 0.0233. Original CBET fits a redshift
                                                                                                      of 0.014 (Nakano et al., 2010), more or less consistent with SDSS DR13 measurement znew =
                                                                                                      0.018267 of nearest galaxy.
        Lancaster         ...                             1.23          1.235         5.0 × 10−3      Possible rounding error; znew matches Riess et al. (2007).
        2005lz            UGC 1666                        0.039 968     0.044 341     4.4 × 10−3      znew from the 2MASS redshift survey (2MRS, Huchra et al., 2012). zold appears to be the original
                                                                                                      SN z of 0.04 (Silverman et al., 2012; Blondin et al., 2012) circularly converted from zCMB .
        2007qe            WISEA J235412.07+272431.9       0.019 977     0.023 96      4.0 × 10−3      zold appears to be a circular conversion of the erroneous NED redshift z = 0.02 from Garnavich
                                                                                                      et al. (2007), who actually quote 0.024. This is consistent with the znew we take from Childress
                                                                                                      et al. (2013) who perform dedicated host spectroscopy.
        2007mma           WISEA J010546.37-004533.6       0.068 921     0.065 349    −3.6 × 10−3      znew comes from SDSS DR13 while zold is the approximate heliocentric correction to the original
                                                                                                      CBET z = 0.07 (Bassett et al., 2007).
        2006cz            MCG-01-38-002                   0.038 33      0.0418        3.5 × 10−3      Origin of zold uncertain. znew from 2dFGRS (Colless et al., 2003).
        2007ci            NGC 3873                        0.021 275     0.017 954    −3.3 × 10−3      Origin of zold uncertain, as it appears to be closer to the average of the two nearest galaxies. We
                                                                                                      take the SDSS DR 13 redshift of the the nearest galaxy, the most likely host.
        1997dg            WISEA J234014.14+261209.8       0.033 960     0.030 81     −3.2 × 10−3      zold is a circular conversion of the original SN redshift estimation of 0.034 from IAUC 6753 (Wang
                                                                                                      et al., 1997), whereas znew is from host spectroscopy (Jha et al., 2006).
        Yowie             ...                             0.46          0.457        −3.0 × 10−3      Potential rounding; znew matches Riess et al. (2007).
        2005M             NGC 2930                        0.0220        0.024 84      2.8 × 10−3      zold from the Catalogue of Optical Radial Velocities (CORV, Fouqué et al., 1992), while znew is
                                                                                                      from Childress et al. (2013).
        2005al            NGC 5304                        0.015 202     0.0124       −2.8 × 10−3      Only affects CSP DR2 record; CSP DR3 redshift agrees with znew from Childress et al. (2013).
        PTF09dnp          WISEA J151925.36+493004.8       0.04          0.037 304     2.7 × 10−3      Origin of zold is unclear as the value of 0.04 only seems to appear in SOUSA, at https://archive.
                                                                                                      stsci.edu/prepds/sousa/. znew is from SDSS DR13.
        1999ej            NGC 495                         0.016 388     0.013 723    −2.7 × 10−3      Origin of zold uncertain, znew from the Third Reference Catalogue of Bright Galaxies (RC3, de
                                                                                                      Vaucouleurs et al., 1991) (which was used in the original CfA2 publication (Jha et al., 2006)).
        2006oa            WISEA J212342.91-005034.7       0.059 936     0.062 573     2.6 × 10−3      znew is from the SDSS II SN Survey data release (Sako et al., 2018). zold appears to be the original
                                                                                                      SN z of 0.06 (Bassett et al., 2006) circularly converted from zCMB .
        2007cv            IC 2597                         0.007 562     0.009 974     2.4 × 10−3      zold is from Bosma & Freeman (1993), which disagrees with all other measurements in NED. znew
                                                                                                      from 6dF DR3 (Jones et al., 2009).
        2017erpa          NGC 5861                        0.0045        0.006 904     2.4 × 10−3      Only affects FSS record. Uncertain origin of zold . znew from 6dF DR3.
                                                                                                                                                                                                                 21
                                                                  Heliocentric redshift update discrepancies ≥ 1×10–3 (continued).                                                                       22

 SNID              Host                                 zold          znew        Difference      Comments
 ASASSN-14lw       WISEA J010647.87-465901.4        0.023           0.0209       −2.1 × 10−3      zold is potentially the average redshift of the galaxy cluster around where ASASSN-14lw occurred
                                                                                                  according to ATEL 6809 (Kiyota et al., 2014). However, znew is the spectroscopic host redshift
                                                                                                  measured by CSP-II (Phillips et al., 2019).
 2007nq            UGC 595                          0.043 523       0.045 21      1.7 × 10−3      Origin of zold uncertain, znew from Childress et al. (2013).
 1993ae            IC 126                           0.017 932       0.019 667     1.7 × 10−3      zold appears to be a circular conversion of the zCMB from Jha et al. (2007), while znew is from 6dF
                                                                                                  DR3.
 2008fr            LEDA 5069093                     0.040 656       0.039        −1.7 × 10−3      zold appears to come from the redshift 0.0407 quoted by SIMBAD, which is the least reliable SNID
                                                                                                  redshift from Silverman et al. (2012, Table 7). We take znew to be the original CBET (Yuan et al.,
                                                                                                  2008b) which agrees with Silverman et al. (2012) Table 1.
 2002fk            NGC 1309                         0.005 585 6     0.007 185     1.6 × 10−3      Origin of zold uncertain. znew taken from 6dF DR3, and agrees with SN 2012Z also hosted by NGC
                                                                                                  1309.
 1999aa            NGC 2595                         0.016 019       0.014 422    −1.6 × 10−3      zold appears to be a double heliocentric correction. znew is from SDSS DR13.
 2019npa           NGC 3254                         0.004           0.005 502     1.5 × 10−3      Origin of zold unclear. znew comes from Springob et al. (2005).
 2008L             NGC 1259                         0.017 845       0.019 28      1.4 × 10−3      zold appears to be roughly the average redshift of the Perseus cluster. We take znew to be that
                                                                                                  of the host galaxy only (Jørgensen et al., 2018).
 2007ux            2MASX J10091969+1459268          0.029 324       0.030 699     1.4 × 10−3      Origin of zold uncertain, znew from SDSS DR13.
 2010cr            NGC 5177                         0.022 925       0.021 551    −1.4 × 10−3      Origin of zold uncertain, znew from SDSS DR13.
 2015N             UGC 11797                        0.013 930       0.012 499    −1.4 × 10−3      zold is from the Updated Zwicky Catalogue (UZC, Falco et al., 1999), while znew is from 2MRS.
                                                                                                  The redshift of UGC 11797 is contentious, possibly due to interaction with UGC 11798.
 PSNJ1628383       NGC 6166b                        0.031 188       0.029 831    −1.4 × 10−3      zold from FSS, but znew is the average of the three nearest galaxies since a unique host cannot
                                                                                                  be determined (Figure 2).
 2006bz            IC 4042A                         0.0268          0.028 115     1.3 × 10−3      zold from CORV while znew comes from SDSS DR6.
 2006kf            UGC 2829                         0.021 299 2     0.020 037    −1.3 × 10−3      znew from 21 cm H I emission (Springob et al., 2005). zold appears to be original CfA Redshift
                                                                                                  Survey z of 0.021301 (Huchra et al., 1999) circularly converted from zCMB .
 2008fp            ESO 428-G014                     0.006 966       0.005 664    −1.3 × 10−3      Only affects CSP DR2 record; zold appears to be a double heliocentric correction. znew comes
                                                                                                  from host spectroscopy (Wegner et al., 2003), and is consistent with SN spectrum (Wang et al.,
                                                                                                  2008) and CSP DR3.
 2004gca           ARP 327 NED04                    0.030 715       0.031 96      1.2 × 10−3      Only affects CSP DR2 record. Origin of zold uncertain. znew from Childress et al. (2013) and con-
                                                                                                  sistent with CSP DR3.
 2006qo            UGC 4133                         0.028 521       0.029 704     1.2 × 10−3      Origin of zold uncertain. znew from 21 cm H I emission (Theureau et al., 1998).
 1996C             MCG+08-25-047                    0.027 016       0.028 235     1.2 × 10−3      zold appears to be a circular conversion of the original redshift (weak Hα emission, Mueller et al.,
                                                                                                  1996), while znew comes from SDSS DR13.
 2006lu            WISEA J091517.24-253600.6        0.054 458       0.0534       −1.1 × 10−3      Only affects CSP DR2 record; zold appears to be the CMB-frame redshift. znew is from Folatelli
                                                                                                  et al. (2013), and is the same redshift quoted by CSP DR3.
 2000B             NGC 2320                         0.020 196       0.019 141    −1.1 × 10−3      Origin of zold uncertain, znew from host spectroscopy (van den Bosch et al., 2015).
 2012hta           NGC 3447A                        0.003 599       0.004 646     1.1 × 10−3      This was a case of the heliocentric-frame redshift being used as the CMB-frame redshift. znew
                                                                                                  comes from SDSS DR13.
 2001fh            WISEA J212042.46+442359.3        0.0123          0.013 303     1.0 × 10−3      Origin of zold uncertain. znew from van den Bosch et al. (2015).
 160099            WISEA J141838.64+541054.8        0.100           0.101 018     1.0 × 10−3      znew is from SDSS DR 13.
 2007cq            WISEA J221440.71+050442.3        0.025           0.026 04      1.0 × 10−3      Origin of zold (SOUSA record) uncertain as it does not match the classification CBET (Filippenko
                                                                                                  et al., 2007). znew is from Childress et al. (2013).
 2007aj            SDSS J124754.53+540038.5         0.031 019       0.30         −1.0 × 10−3      Origin of zold uncertain, and has been replaced by the original SN z (Quimby et al., 2007).




                                                                                                                                                                                                         Anthony Carr et al.
 Eagle             ...                              1.02            1.019        −1.0 × 10−3      Potential rounding; znew matches Riess et al. (2007).
 Rakke             ...                              0.74            0.739        −1.0 × 10−3      Potential rounding; znew matches Riess et al. (2007).
a Missing heliocentric redshift, so these cases are actually CMB-frame redshift discrepancies.
b This host was assigned by FSS because it is the closest and largest of the three nearby galaxies but we do not attempt to pick a unique host (see Figure 2).
Publications of the Astronomical Society of Australia                                                                                               23




Table A3. Supernovae previously without redshift uncertainties. The uncertainty is assigned to be 5×10–3 if the redshift is measured directly from a SN
spectrum without host emission, and 9×10–5 if not.

                            SNID             Host                                       zhel          Assigned Uncertainty
                            1992J            WISEA J100901.19-263836.3                   0.0446             9×10–5
                            1992ae           WISEA J212817.17-613302.7                   0.0752             9×10–5
                            1992aq           APMUKS(BJ) B230147.96-373644.6              0.101              9×10–5
                            1993B            WISEA J103451.50-342635.8                   0.0696             9×10–5
                            1993ac           CGCG 307-023                                0.049 37           9×10–5
                            1995bd           UGC 03151                                   0.015 39           9×10–5
                            1996bl           WISEA J003618.14+112335.3                   0.036              9×10–5
                            2001az           UGC 10483                                   0.040 695          9×10–5
                            2002hua          MCG +06-06-012                              0.0367             1.0×10–3
                            2002kf           CGCG 233-023                                0.019 30           9×10–5
                            2003hu           2MASX J19113272+7753382                     0.075              9×10–5
                            2006an           SDSS J121438.73+121347.7                    0.064              9×10–5
                            2006is           WISEA J051734.55-234659.7                   0.0314             9×10–5
                            2006lu           WISEA J091517.24-253600.6                   0.0534             9×10–5
                            2006td           KUG 0155+361                                0.015 881          9×10–5
                            2008L            NGC 1259                                    0.019 28           9×10–5
                            2008by           WISEA J120520.83+405645.9                   0.045              9×10–5
                            2008cf           LEDA 766647                                 0.046 03           9×10–5
                            2008fk           WISEA J023405.17+012340.2                   0.072              9×10–5
                            2008gb           UGC 02427                                   0.037              9×10–5
                            ASASSN-16es      SDSS J115054.45+021828.1                    0.028 50b          9×10–5
                            ASASSN-16hh      MCG +03-06-031                              0.030 26b          9×10–5
                            ASASSN-16lc      WISEA J192901.71-515812.6                   0.020 33b          9×10–5
                            2017gup          WISEA J032934.19+105825.5                   0.023 16b          9×10–5
                            2017hoq          WISEA J051920.10-173647.6                   0.023 41b          9×10–5
                            2018enc          WISEA J151928.86-095256.6                   0.023 89b          9×10–5
                            2018fop          WISEA J011517.81-065130.5                   0.021 21b          9×10–5
                            2018jjd          GALEXASC J042420.17-315913.5                0.025 60b          9×10–5
                            ASASSN-18da      WISEA J032916.56-235839.3                   0.022 00b          9×10–5
                            ASASSN-18iu      WISEA J175740.54+500200.6                   0.022 30b          9×10–5
                            1996ab           Anonymous                                   0.123              5×10–3
                            2006mp           UGC 10754 NOTES01                           0.023              5×10–3
                            2007aj           SDSS J124754.53+540038.5                    0.030              5×10–3
                            2007kf           WISEA J173130.93+691844.3                   0.0467             5×10–3
                            2007kg           Anonymous                                   0.0067             5×10–3
                            2007kh           SDSS J031512.10+431012.9                    0.050              5×10–3
                            2010hs           WISEA J022537.66+244557.l7                  0.076              5×10–3
                            LSQ13crf         WISEA J031050.33+012519.7                   0.060              5×10–3
                            2014bj           WISEA J192240.35+435317.7                   0.043              5×10–3
                            2017dws          WISEA J154014.24+112040.8                   0.082              5×10–3
                            2017hbi          WISEA J023232.07+352854.8                   0.040              5×10–3
                          a 2002hu is the only exception, which is a host redshift we have inflated the uncertainty on due to

                          particularly ambiguous reporting of redshifts.
                          b Redshift independently measured by Chen et al. (2020), but redshift uncertainties have not been

                          released at the time of writing.
24                                                                                                                  Anthony Carr et al.


Appendix 2. Converting real-space velocities to redshift-space velocities
Here we detail how we transfer the 2M++ velocity reconstruction from real space to redshift space. The purpose of this
transformation is so that we do not need to convert redshifts to distances in order to estimate their peculiar velocities.

Appendix 2.1 Scaling the 2M++ real-space grid
As in Equation 9, the peculiar velocity grid must be scaled from the normalised reconstruction to best match observed peculiar
velocities from the Tully-Fisher and Fundamental Plane relations. Each real-space grid point is scaled by β and adjusted by V ext :

                                                             vp = βvp,recon. + V ext ,                                              (11)

where vp = (vX , vY , vZ ) are the new scaled velocities at real-space grid points r = (X, Y, Z). The projected line of sight velocity
for each grid point is
                                                              vproj. = vp · r̂                                                    (12)

Appendix 2.2 Converting to supergalactic coordinates in real-space
The 2M++ real-space grid is in galactic Cartesian coordinates, so we transform to supergalactic Cartesian coordinates by rotating
via                                                                                    
                                                  – sin(l)          cos(l)         0
                                        R =  – sin(b) cos(l) – sin(b) sin(l)    cos(b) ,                                   (13)
                                                cos(b) cos(l)    cos(b) sin(l) – sin(b)
so that the positive z-direction (now SGZ) is in the direction of the supergalactic north pole, (l, b) = (47.37◦ , 6.32◦ ) (Lahav et al.,
2000). With rSG = (SGX, SGY, SGZ) and vSG = (vSGX , vSGY , vSGZ ),

                                                                   rT      T
                                                                    SG = Rr ,                                                       (14)

and
                                                                  vT      T
                                                                   SG = Rvp .                                                       (15)

The projected line of sight velocity using supergalactic coordinates in real-space is

                                                              vSG,proj. = vSG · r̂SG                                                (16)

Appendix 2.3 Converting to redshift-space
The distance to any grid point is
                                             √           √                 p
                                        D=       r·r =       rSG · rSG =    SGX 2 + SGY 2 + SGZ2 .                                  (17)

We then adjust the redshift of each grid point by its associated peculiar redshift via

                                                         z = [(1 + z̄)(1 + zp ) – 1],                                               (18)

where z̄ is the cosmological redshift corresponding to D in h–1 Mpc using H0 = 100h km s–1 Mpc–1 (making it independent of
H0 ), Ωm = 0.3 (the same value used in the reconstruction process), and zp ≈ vSG,proj. /c. The redshift-space position vector is then
the real-space position vector converted to redshift by the ratio of z to D,
                                                                        z
                                                                   z=     r .                                                       (19)
                                                                        D SG
However, the grid points are now irregularly spaced. Thus, the final step is to use inverse distance weighting to interpolate and
adjust the irregularly-spaced grid to a regular grid.
