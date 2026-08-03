# Review Base 10 raw Deep Research packet — Conroy 2013

advisory_only: true
canonical_packet_released: false
wiki_write_performed_by_tori: false
identifier_verification_required_before_canonical_release: true

Queue: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/REVIEW_BASE_QUEUE.md`
Queue SHA-256: `7f9384766bdc5dd7473f7265018344ba6067e9b612cdbe77d59a7adf7ffc3f5b`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area_review_10_conroy_2013_DR_PROMPT.md`
Prompt SHA-256: `c40193005d83bce620828846375ac1762355cb4e6184c5b0b7b3259dfe4d7d6e`
Conversation ID: `6d16b718151e357b`
Submit UTC: `2026-07-16T02:10:20.254173Z`
Research Start UTC: `2026-07-16T02:10:44.566432Z`
Result captured UTC: `2026-07-16T02:27:59.171085Z`
Raw result SHA-256: `880153823586bcc4308701417ae17d409b85358d53e8d97189bd8f5746fb7a0b`

## Deep Research review-base result

Review Identity and Core Synthesis: Conroy (2013) Panchromatic SED Modeling

The spectral energy distributions of galaxies serve as the fundamental diagnostic tool for understanding the evolutionary pathways of the cosmos. The research review under analysis, authored by Charlie Conroy in the Annual Review of Astronomy and Astrophysics (Volume 51, pages 393-455, published in 2013), provides an exhaustive synthesis of the state-of-the-art in modeling panchromatic spectral energy distributions. The established review identity is confirmed through the Digital Object Identifier 10.1146/annurev-astro-082812-141017, the arXiv identifier 1301.7095, and the Astrophysics Data System bibliographic code 2013ARA&A..51..393C. The foundational premise of this review is that a galaxy's spectral energy distribution encodes nearly every physical property of the system. This includes the star formation history, total stellar mass, metal content, detailed abundance patterns, dust mass, grain size distribution, star-dust geometry, and the interstellar radiation field.   

Stellar population synthesis operates as the primary theoretical framework used to reverse-engineer these physical variables from observed photometric and spectroscopic data. By spanning the wavelength range from the far-ultraviolet to the far-infrared, panchromatic stellar population synthesis modeling attempts to capture a complete census of the baryonic matter within a galaxy. Early attempts at understanding the visible and near-infrared spectral windows approached the problem by combining mixtures of stars in ad hoc ways until a match was achieved with observations. More sophisticated versions of this technique were subsequently developed that incorporated physical constraints and automated fitting techniques. Today, evolutionary population synthesis provides a mathematically rigorous approach. The far-ultraviolet through near-infrared regimes are predominantly shaped by direct starlight and its immediate attenuation by dust, while the mid-infrared to far-infrared regimes are dominated by the thermal re-emission of that absorbed energy by the interstellar medium. Conroy’s review evaluates the mathematical formulation of these models, the astrophysical components required to construct them, the reliability of the physical parameters derived from them, and the profound uncertainties that continue to limit the precision of extragalactic astronomy.   

Established Findings in Stellar Population Synthesis
The Architecture of Stellar Population Synthesis Models

The construction of a stellar population synthesis model relies on several distinct astrophysical ingredients that are mathematically convolved to predict the integrated light of a galaxy. The computational pipeline of stellar population synthesis relies on sequentially integrated models. The fundamental building block of this architecture is the simple stellar population, defined as a single, coeval group of stars possessing a uniform age, metallicity, and elemental abundance pattern. Generating a simple stellar population requires three primary theoretical inputs, which are integrated to generate the baseline spectrum. First, an initial mass function dictates the mass distribution of stars born in a single star-forming event. Second, stellar evolutionary isochrones map the relationships between initial stellar mass, surface gravity, effective temperature, and bolometric luminosity at specific ages and metallicities. Third, stellar spectral libraries—which can be derived from empirical observations of local stars or generated through theoretical model atmospheres—convert the physical parameters from the isochrones into observable spectral energy distributions.   

The integral of these components over the mass range of the initial mass function yields the integrated spectrum of a simple stellar population. The lower limit of this integration is typically taken to be the hydrogen-burning limit, varying between 0.08 and 0.1 solar masses depending on the specific synthesis code utilized, while the upper limit is dictated by stellar evolution modeling, often reaching up to 100 solar masses. To model realistic galaxies, these baseline simple stellar populations must be transformed into composite stellar populations. Composite stellar populations account for the reality that galaxies undergo continuous or episodic star formation over billions of years and gradually enrich their interstellar medium with heavy elements. This requires convolving the simple stellar populations with a parameterized or non-parametric star formation history and a chemical evolution framework. Finally, this composite spectrum is modified by the complex radiative transfer of dust attenuation and emission to yield the final observable composite stellar population. The transition from simple to composite populations represents a massive expansion of parameter space, significantly increasing the difficulty of inverse-modeling observed spectral energy distributions.   

Reliability of Stellar Mass Estimations

Among the myriad physical parameters derived from spectral energy distribution fitting, the total stellar mass of a galaxy is widely recognized as the most robust measurement. Stellar mass is typically estimated by determining the mass-to-light ratio of the galaxy and scaling it by the observed luminosity. Estimations of mass-to-light ratios can be performed using empirical relations based on simple broadband colors, comprehensive fitting of multiple broadband photometric filters, or detailed modeling of moderate-to-high resolution spectra. Generically, for galaxies with relatively normal star formation histories, stellar masses can be recovered with a statistical uncertainty of approximately 0.3 dex, equivalent to a factor of two.   

This baseline uncertainty, however, does not encompass the systematic uncertainties inherent in the underlying stellar population synthesis models. The choice of the assumed star formation history—whether it is rising, declining, constant, or punctuated by starbursts—can alter the best-fit stellar mass by as much as 0.6 dex in extreme scenarios. Simple, single-age models generally establish a lower limit for mass-to-light ratios, as older, less luminous stars can easily be outshone by a minor population of young, massive stars, masking the true mass of the older stellar component. Furthermore, the mass-to-light ratio is highly sensitive to the assumed initial mass function, particularly at the low-mass end. Low-mass stars, which constitute 60 to 80 percent of the stellar mass density in the Universe, contribute negligibly to the integrated optical and near-infrared light of an old stellar population. Consequently, the stellar masses derived from spectral energy distributions are essentially scaling factors tethered to the assumed abundance of unseen dwarf stars.   

Re-evaluation of the Initial Mass Function

Historically, stellar population synthesis models assumed a universal initial mass function, typically mirroring the mass distribution observed in the disk of the Milky Way, such as the classic Salpeter or Chabrier functions. However, a major established finding discussed in the review is the compelling evidence for systematic variations in the initial mass function across different galactic environments. Early work aimed at measuring the initial mass function from integrated light spectra suffered from serious limitations, including the lack of accurate stellar evolution calculations across the main sequence, the use of empirical stellar spectra collected solely from the solar neighborhood, and poor near-infrared detector technology. The resolution of these limitations has precipitated a paradigm shift. High-signal-to-noise integrated light spectroscopy of massive early-type galaxies reveals spectral features that are acutely sensitive to surface gravity, which serves as a proxy for distinguishing between giant and dwarf stars.   

Specific gravity-sensitive absorption features, such as the sodium doublet at 0.82 micrometers, the calcium triplet at 0.86 micrometers, and the iron hydride Wing-Ford band at 0.99 micrometers, indicate that massive, alpha-enhanced elliptical galaxies harbor a substantially higher fraction of low-mass dwarf stars than the Milky Way. These observations heavily favor initial mass functions that become progressively more bottom-heavy, or dwarf-rich, as the total mass and alpha-enhancement of the galaxy increase. Modeling these subtle spectral variations requires exceptionally sophisticated synthesis codes that explicitly allow for variations in the detailed elemental abundance patterns of up to eleven different elements, as alterations in the abundance of specific elements can mimic the effects of surface gravity variations. When properly modeled, the mass-to-light ratios predicted by these bottom-heavy initial mass functions vary by only a factor of three at a fixed age and metallicity, remaining consistent with independent dynamical mass constraints.   

Open Debates and Theoretical Unknowns
The TP-AGB Phase Controversy

The most significant theoretical unknown in stellar population synthesis modeling pertains to the treatment of the thermally pulsating asymptotic giant branch phase of stellar evolution. Stars entering the thermally pulsating asymptotic giant branch phase are extremely luminous and cool, meaning they heavily dominate the near-infrared and mid-infrared emission of intermediate-age stellar populations—those roughly between 0.1 and 2 billion years old. The underlying physics of this evolutionary stage is exceptionally complex, governed by dramatic mass loss, episodic thermal pulses, deep convective dredge-up events, and intricate circumstellar dust production.   

Different modeling groups have adopted vastly different prescriptions for the thermally pulsating asymptotic giant branch phase, leading to profound discrepancies in predicted spectral energy distributions. Certain models predict that this phase completely dominates the near-infrared flux, while other models attribute much less weight to these stars. Consequently, when applying these divergent models to high-redshift galaxies, researchers derive drastically different star formation histories, ages, and stellar masses depending entirely on the chosen software package. Using galaxy spectral energy distributions to empirically calibrate the importance of this phase is highly degenerate, as the observer must simultaneously constrain the metallicity, star formation history, and dust attenuation of the galaxy. The resolution of this controversy remains elusive, representing a major structural barrier to precision extragalactic astrophysics at near-infrared wavelengths.   

Systematic Uncertainties in Stellar Evolution

Beneath the uncertainties of galaxy-wide parameters lie the foundational unknowns of stellar astrophysics, which propagate directly into the mass-to-light ratios derived by synthesis models. The treatment of convective core overshooting—the distance stellar material travels beyond the formal boundary of the convective core due to momentum—substantially alters the main sequence lifetime and luminosity of intermediate-mass stars. Variations in the parameterization of overshooting can shift the predicted color evolution of simple stellar populations at ages between 0.1 and 1 billion years by as much as 0.1 magnitudes, injecting a persistent systematic error into the modeling of young galaxies. Furthermore, the amount of overshooting in the convective envelopes of evolved giants remains poorly constrained, which heavily influences the ratio of red to blue supergiants observed in synthesis codes.   

Similarly, the morphology of the horizontal branch in old, metal-poor stellar populations presents a massive theoretical hazard. While the horizontal branch is typically populated by red stars in metal-rich environments, certain dynamical or evolutionary anomalies can produce extreme blue horizontal branch stars. Because these stars are incredibly hot, they emit massive amounts of ultraviolet light and exhibit strong Balmer absorption lines. If a stellar population synthesis model assumes an old population is entirely devoid of these stars, the presence of strong Balmer lines in an observed spectrum will trick the model into deriving an artificially young age—sometimes underestimating the true age by 2 to 5 billion years. However, models can reproduce the highest H-beta equivalent widths with a two-component population in which a fraction of the old, metal-rich stars are artificially designated as blue horizontal branch variants.   

The Age-Metallicity Degeneracy and Photometric Limitations

A persistent observational challenge in extragalactic astronomy is the fundamental degeneracy between the age of a stellar population and its metallicity. As an simple stellar population ages, the most massive, hot, blue stars die, leaving cooler, redder stars to dominate the integrated light. Simultaneously, an increase in metallicity increases the opacity in stellar atmospheres, cooling the effective temperatures of the main sequence and giant branches, and strengthening absorption features, which also acts to redden the integrated spectral energy distribution.   

This parallel reddening effect leads to the well-documented age-metallicity degeneracy, mathematically codified by the "3/2 rule". This rule posits that an artificial increase in the age of a population by a factor of three is almost perfectly indistinguishable from an increase in metallicity by a factor of two when relying solely on broadband optical colors or single spectral indices for populations older than five billion years. Breaking this profound degeneracy necessitates specific observational strategies. High-resolution, full-spectral fitting offers the most robust separation, as the entire optical continuum contains exponentially more information than isolated color indices. Alternatively, carefully chosen pairs of spectral indices—such as combining the highly age-sensitive hydrogen Balmer lines with the highly metallicity-sensitive iron features like the Fe4668 and Fe5270 indices—can decouple the parameters, provided the data possesses exceptional signal-to-noise ratios, typically exceeding 100 per angstrom.   

Recent advancements indicate that extending photometric baselines from the optical into the near-infrared can also achieve separation for composite stellar populations. Because the blue optical wavelengths trace the age-sensitive main sequence turnoff, while the near-infrared wavelengths trace the metallicity-sensitive giant branch, the vectors of age and metallicity become nearly orthogonal in optical-to-near-infrared color-color spaces. By mapping parameters like the B-R color against the R-H color, astronomers can estimate stellar metallicities from photometric data alone, provided the systems are not overwhelmingly dominated by ancient stars.   

Nebular Emission at High Redshifts

As observational capabilities press deeper into the early Universe, the treatment of nebular emission has emerged as a major source of systematic error in spectral energy distribution modeling. In local galaxies, the continuum light from stars vastly outshines the narrow emission lines generated by ionized gas in HII regions, rendering their contribution to broad photometric filters relatively negligible. However, galaxies at high redshifts exhibit vastly higher specific star formation rates and significantly lower metallicities.   

Furthermore, cosmic expansion shifts these massive, high-equivalent-width emission lines through specific observational filters, meaning a single emission line can artificially inflate the measured flux within a broadband filter by a massive percentage. If spectral energy distribution models neglect the inclusion of a comprehensive nebular emission module, the fitting algorithm will erroneously interpret the inflated broadband flux as a massive, young stellar continuum. Failing to account for nebular emission can alter derived specific star formation rates by a factor of roughly two, skewing our understanding of galaxy mass assembly during the peak epoch of cosmic star formation.   

Key Measurements in Panchromatic SED Modeling
Constraining Star Formation Rates and Histories

Measuring the rate at which galaxies convert gas into stars is central to mapping cosmic evolution. Because the spectral energy distribution spans multiple distinct physical regimes, it provides multiple independent clocks for measuring star formation. The ultraviolet continuum is completely dominated by the emission from massive, short-lived O and B type stars, effectively tracing star formation integrated over the past 100 million years. Conversely, hydrogen recombination lines, such as H-alpha, trace the ionizing flux of the most massive stars, providing an instantaneous snapshot of star formation occurring on timescales of less than 10 million years.   

Because massive stars are born within dense molecular clouds, much of this ultraviolet light is absorbed by cosmic dust and re-radiated as thermal emission in the mid-to-far-infrared. Consequently, an accurate star formation rate often requires an energy balance approach, utilizing panchromatic data to capture both the unobscured ultraviolet light and the heavily obscured infrared emission. The far-infrared photons are sensitive to dust heated by both old and young stars, while shorter infrared wavelengths probe dust heated predominantly by active HII regions. Comparing star formation rates derived strictly from optical spectral energy distribution modeling to those derived from precise H-alpha emission lines reveals systematic uncertainties hovering around 0.3 dex, often correlating directly with the total stellar mass of the galaxy, with offsets noted at both the extreme low and high mass ends.   

Determining the entire star formation history requires parameterizing the temporal evolution of the galaxy. Studies increasingly demonstrate that light-weighted ages, which are easily extracted from spectral energy distributions, skew heavily toward recent bursts of star formation, completely masking the older, underlying stellar populations. These derived metrics are often labeled "SSP-equivalent ages" to acknowledge that they do not model composite populations, acting merely as lower limits for the true mass-weighted ages. Non-parametric star formation histories, which allow the star formation rate to vary freely in discrete time bins, are becoming necessary to overcome the rigid limitations of standard exponentially declining models.   

The Measurement of Dust Attenuation

Measuring and mitigating the effects of interstellar dust is required to extract accurate stellar parameters from a galaxy's integrated light. Dust modifies the spectral energy distribution in a highly wavelength-dependent manner, heavily suppressing the far-ultraviolet and gradually becoming transparent in the near-infrared. The primary goal in modeling this process is defining the attenuation curve, which describes the total optical depth of the dust as a function of wavelength.   

While the Calzetti attenuation law—derived empirically from local starburst galaxies—is frequently applied universally, recent findings confirm that the attenuation law varies significantly with spectral type, specific star formation rate, and inclination. Highly active, star-forming galaxies tend to exhibit shallower dust attenuation curves and exhibit a weaker ultraviolet dust bump at 2175 angstroms. The underlying cause of this variation is the complex geometry between the stars and the dust. Young, massive stars remain deeply embedded in their natal molecular clouds, suffering massive localized attenuation, while older stars migrate into the diffuse interstellar medium and experience only moderate, foreground reddening.   

In the absence of high-resolution spectra, astronomers frequently rely on the infrared excess—the ratio of total infrared luminosity to ultraviolet luminosity—to estimate dust attenuation. The relationship between the infrared excess and the slope of the ultraviolet continuum (the IRX-beta relation) provides a vital constraint on total absorption. However, normal star-forming galaxies exhibit profound scatter within this relation, meaning that minor errors in measuring the ultraviolet slope translate into massive uncertainties in the derived dust mass and the intrinsic star formation rate. Conversely, extremely blue ultraviolet continua serve as powerful constraints. High-redshift galaxies exhibiting ultraviolet continuum slopes between -2.0 and -2.5 indicate systems that are virtually dust-free, a state achievable only at extremely young ages or exceptionally low metallicities.   

Determining Stellar Metallicities and Abundance Patterns

Deriving accurate chemical abundances from integrated light is mathematically perilous. While broadband photometric metallicities have been utilized by mapping blue optical colors against red near-infrared colors, the community treats these measurements with significant caution. Photometric metallicity derivations often feature weak correlations when compared to measurements derived from optical emission lines, primarily due to the severe blending of age and metallicity effects over broad bandpasses. Consequently, researchers frequently marginalize metallicity as a nuisance parameter or artificially fix it to the solar value to secure the more robust stellar mass.   

Spectroscopic metallicities offer a vastly superior framework. The optical spectrum of a galaxy is saturated with atomic and molecular absorption features that respond dynamically to both the overall metallicity and the specific elemental abundance pattern. The standard assumption that extragalactic abundance patterns universally track the solar neighborhood—parameterized simply by total iron abundance and the ratio of alpha elements to iron—is fundamentally flawed. High-resolution observations confirm that alpha elements do not evolve in strict lock-step across cosmic time. Furthermore, modern automated spectral fitting codes frequently yield conflicting metallicity estimations for the exact same galaxy depending on the underlying stellar population synthesis model utilized. This exposes systematic uncertainties at the 0.2 dex level solely due to the structural construction of theoretical spectral libraries, proving that spectral modeling is highly dependent on the chosen input physics.   

Primary-Citation Harvest

The analysis of the underlying source base reveals the foundational literature cited within the 2013 review. These citations form the historical and theoretical scaffolding of modern stellar population synthesis modeling. The extraction of these primary sources from the harvested bibliographic ledgers confirms adherence strictly to the scope of panchromatic spectral energy distribution analysis.

Primary Author & Year	Publication Details	Core Scientific Contribution to SPS Modeling
Salpeter, E. E. (1955)	ApJ 121:161	

Establishment of the original power-law formulation for the stellar initial mass function, shaping decades of mass estimations.


Tinsley, B. M. (1980)	Fundamentals of Cosmic Physics 5:287-388	

Foundational review establishing the entire paradigm of stellar population synthesis and galactic evolution mapping.


Draine, B. T. & Lee, H. M. (1984)	ApJ 285:89-108	

Theoretical modeling of the optical properties of interstellar dust grains, vital for FIR thermal emission modeling.


Cardelli, J. A., Clayton, G. C., Mathis, J. S. (1989)	ApJ 345:245-256	

Establishment of the parameterized Milky Way dust extinction curve, distinct from later starburst attenuation laws.


Bruzual, G. & Charlot, S. (1993, 2003)	MNRAS 344:1000-1028	

Introduction of the heavily utilized BC03 SPS models, standardizing high-resolution integrated spectral modeling.


Worthey, G. (1994)	ApJS 95:107-149	

Formalization of the Lick index system and the mathematical definition of the "3/2 rule" for the age-metallicity degeneracy.


Calzetti, D. (2001)	PASP 113:1449-1485	

Defining the standard empirical dust attenuation law for actively star-forming galaxies, fundamentally lacking the 2175 Å bump.


Chabrier, G. (2003)	PASP 115:763-795	

Development of the modern log-normal initial mass function, resolving low-mass stellar discrepancies in earlier models.


Maraston, C. (2005)	MNRAS 362:799-825	

Crucial advancements in modeling the highly uncertain Thermally Pulsating AGB phase in intermediate-age populations.


Conroy, C., Gunn, J. E., White, M. (2009)	ApJ 699:486-506	

Propagation of systematic uncertainties through SPS models, highlighting stellar evolution limitations such as convective overshooting.


van Dokkum, P. G. & Conroy, C. (2010)	Nature 468:940-942	

First conclusive observational evidence for a non-universal, bottom-heavy initial mass function in massive elliptical galaxies.

  
Quarantined Unverified Sources

During the deep-research process, several distinct research queries surfaced documents that strictly violate the topical, temporal, or scientific scope of the review parameters. These sources do not directly address stellar population synthesis, nor are they cited by the primary review. They have been explicitly quarantined to prevent data contamination.

Quarantined Subject Matter	Source Identity	Reason for Exclusion from Synthesis
Chameleon Gravity Dynamics	arXiv: 1407.6044	

Focuses on modified gravity models and rotational discrepancies between gas and stellar components in low surface brightness dwarf galaxies. Entirely outside the scope of SPS modeling.


GalaxyCoin Cryptocurrency	arXiv: 2603.29340	

Proposes a digital monetary model anchored to astronomical object catalogues. Violates scientific scope; represents financial technology, not astrophysics.


Ultra-Diffuse Galaxy Kinematics	MNRAS (Mancera Piña et al. 2021); arXiv: 2112.00017	

Analyzes the HI rotational curve of AGC 114905, claiming an absence of standard cold dark matter. Pertains to dark matter halo kinetics, not integrated light synthesis.


Lunar & Asteroid Regolith	Nature (Cambioni et al. 2021)	

Explores fine-regolith production driven by rock porosity on celestial bodies. Represents planetary science, violating extragalactic scope.


Cosmological Age Constraints	AMS Doctorate Thesis (Tomasetti, E.)	

Utilizes stellar models to constrain the age of the Universe independent of cosmology. While related to stellar populations, it is an external thesis not part of the primary source base being reviewed.

  

REVIEW_BASE_10_DR_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- arxiv.org [1301.7095] Modeling the Panchromatic Spectral Energy Distributions of Galaxies - arXiv Opens in a new window — https://arxiv.org/abs/1301.7095
- semanticscholar.org Modeling the Panchromatic Spectral Energy Distributions of Galaxies - Semantic Scholar Opens in a new window — https://www.semanticscholar.org/paper/Modeling-the-Panchromatic-Spectral-Energy-of-Conroy/22cb4b8a2db945d5bc95a0ee6c966f9b44a785a0
- ned.ipac.caltech.edu Modeling the Panchromatic Spectral Energy Distributions of Galaxies Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept14/Conroy/paper.pdf
- oamonitor.ireland.openaire.eu ULTRAVIOLET RADIATIVE TRANSFER MODELING OF NEARBY Opens in a new window — https://oamonitor.ireland.openaire.eu/national/search/publication?pid=10.1088%2F0004-637x%2F815%2F2%2F133
- ned.ipac.caltech.edu Modeling the Panchromatic Spectral Energy Distributions of Galaxies - Charlie Conroy Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept14/Conroy/frames.html
- researchgate.net (PDF) The Spectral Energy Distributions of Galaxies - ResearchGate Opens in a new window — https://www.researchgate.net/publication/389351152_The_Spectral_Energy_Distributions_of_Galaxies
- ned.ipac.caltech.edu introduction - Modeling the Panchromatic Spectral Energy Distributions of Galaxies - Charlie Conroy Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept14/Conroy/Conroy1.html
- ned.ipac.caltech.edu Overview of the stellar population synthesis - Modeling the Panchromatic Spectral Energy Distributions of Galaxies - Charlie Conroy Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept14/Conroy/Conroy2.html
- i.astro.tsinghua.edu.cn stellar population synthesis Opens in a new window — https://i.astro.tsinghua.edu.cn/~xbai/teaching/StudentSeminar2017F/20171020_RuiLiming_SPS.pdf
- ned.ipac.caltech.edu mass-to-light ratios & stellar masses - Modeling the Panchromatic Spectral Energy Distributions of Galaxies - Charlie Conroy Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept14/Conroy/Conroy3.html
- ned.ipac.caltech.edu star formation rates, histories, & stellar ages - Modeling the Panchromatic Spectral Energy Distributions of Galaxies - Charlie Conroy Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept14/Conroy/Conroy4.html
- ned.ipac.caltech.edu the initial mass function - Modeling the Panchromatic Spectral Energy Distributions of Galaxies - Charlie Conroy Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept14/Conroy/Conroy7.html
- ned.ipac.caltech.edu arXiv:1309.3276v2 [astro-ph.CO] 28 Apr 2014 - NASA/IPAC Extragalactic Database Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept14/Courteau/paper.pdf
- preprints.org From Starlight Synthesis to Chemo-Kinematic Tomography: A Unified Galactic Reconstruction Framework - Preprints.org Opens in a new window — https://www.preprints.org/manuscript/202606.1722
- ned.ipac.caltech.edu stellar metallicities & abundance patterns - Modeling the Panchromatic Spectral Energy Distributions of Galaxies - Charlie Conroy Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept14/Conroy/Conroy5.html
- arxiv.org arXiv:1308.1099v2 [astro-ph.CO] 20 Aug 2013 Opens in a new window — https://arxiv.org/pdf/1308.1099
- emergentmind.com Panchromatic Stellar SEDs Analysis - Emergent Mind Opens in a new window — https://www.emergentmind.com/topics/panchromatic-stellar-seds
- ned.ipac.caltech.edu Total Dust Attenuation - Modeling the Panchromatic Spectral Energy Distributions of Galaxies - Charlie Conroy Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept14/Conroy/Conroy6.html
- ned.ipac.caltech.edu Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept14/Conroy/Conroy_refs.html
- arxiv.org Quenching of Star Formation in Massive Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2606.12156v2
- arxiv.org arXiv:1407.6044v2 [astro-ph.CO] 15 Jun 2018 Opens in a new window — https://arxiv.org/pdf/1407.6044
- arxiv.org An innovative alternative to traditional funding streams for extragalactic astronomy - arXiv Opens in a new window — https://arxiv.org/pdf/2603.29340
- wiki.helsinki.fi Astrophysics journal club - XWiki - University of Helsinki Wiki Opens in a new window — https://wiki.helsinki.fi/xwiki/bin/view/astjourn/Astrophysics%20journal%20club/
- amsdottorato.unibo.it Probing the Expansion History of the Universe through Cosmic Time - AMS Tesi di Dottorato Opens in a new window — https://amsdottorato.unibo.it/id/eprint/13121/1/Tomasetti_Elena_tesi.pdf
- sissa.it High-redshift Dusty Star-Forming Galaxies: a panchromatic approach to constrain massive - SISSA Opens in a new window — https://www.sissa.it/ap/phdsection/AlumniThesis/Lara%20Pantoni.pdf
- arxiv.org Editorial: Mass and Angular Momentum Transport of Rapidly Rotating Hot Stars - arXiv Opens in a new window — https://arxiv.org/pdf/2601.22281
- ned.ipac.caltech.edu concluding remarks - Modeling the Panchromatic Spectral Energy Distributions of Galaxies - Charlie Conroy Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept14/Conroy/Conroy8.html
- arxiv.org Interpreting Galaxy Physical Properties Using Stellar Population Synthesis - arXiv Opens in a new window — https://arxiv.org/html/2605.03500v2
- scoap3-prod-backend.s3.cern.ch Phenomenological constraints on QCD transport with quantified theory uncertainties - CERN Opens in a new window — https://scoap3-prod-backend.s3.cern.ch/media/harvested_files/10.1016/j.physletb.2026.140243/main.pdf
- scispace.com Cosmic X-ray Surveys of Distant Active Galaxies: The Demographics, Physics, and Ecology of Growing Supermassive Black Holes - SciSpace Opens in a new window — https://scispace.com/pdf/cosmic-x-ray-surveys-of-distant-active-galaxies-the-14irc2pexp.pdf
- arxiv.org Applications of Stellar Population Synthesis in the Distant Universe - arXiv Opens in a new window — https://arxiv.org/pdf/2005.01759
- arxiv.org Constraining galactic baryon cycle using the galaxy stellar-to-halo mass relations - arXiv Opens in a new window — https://arxiv.org/pdf/2212.05007
- arxiv.org analytic solutions for chemical evolution models with metallicity-dependent yields - arXiv Opens in a new window — https://arxiv.org/pdf/2510.25876
- academic.oup.com pop-cosmos: star formation over 12 Gyr from generative modelling of a deep infrared-selected galaxy catalogue - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/549/1/stag764/8664323
- arxiv.org ProGeny II: the impact of libraries and model configurations on inferred galaxy properties in SED fitting - arXiv Opens in a new window — https://arxiv.org/html/2410.17698v3
- researchgate.net Modeling the Ages and Chemical Abundances of Elliptical Galaxies - ResearchGate Opens in a new window — https://www.researchgate.net/publication/392004915_Modeling_the_Ages_and_Chemical_Abundances_of_Elliptical_Galaxies
- par.nsf.gov Modeling the Ages and Chemical Abundances of Elliptical Galaxies - NSF PAR Opens in a new window — https://par.nsf.gov/servlets/purl/10644558

## Custody

- Raw audit custody only; do not integrate. Canonical release requires composite identifier and claim-boundary verification.
- No wiki, DB, trust, deploy, publish, git, credential, billing, account-setting, or conversation-deletion mutation was performed.
