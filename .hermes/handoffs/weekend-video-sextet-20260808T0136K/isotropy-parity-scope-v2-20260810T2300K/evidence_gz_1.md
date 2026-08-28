URL: https://arxiv.org/pdf/2102.08414

# Galaxy Zoo DECaLS: Detailed Visual Morphology Measurements from Volunteers and Deep Learning for 314,000 Galaxies

Mike Walmsley $ ^{1} \\star $ , Chris Lintott 1 , Tobias Géron 1 , Sandor Kruk 2 , Coleman Krawczyk 3 Kyle W. Willett 4 , Steven Bamford 5 , Lee S. Kelvin 6 , Lucy Fortson 7 , Yarin Gal 8 William Keel 9 , Karen L. Masters 10 , Vihang Mehta 9 , Brooke D. Simmons 11 Rebecca Smethurst 1 , Lewis Smith 8 , Elisabeth M. Baeten 12 , Christine Macmillan 12

1 Oxford Astrophysics, Department of Physics, University of Oxford, Denys Wilkinson Building, Keble Road, Oxford, OX1 3RH, UK
2 European Space Agency, ESTEC, Keplerlaan 1, NL-2201 AZ, Noordwijk, The Netherlands
3 Institute of Cosmology and Gravitation, University of Portsmouth Dennis Sciama Building, Burnaby Road, Portsmouth, PO1 3FX, UK
4 School of Physics and Astronomy, University of Minnesota, 116 Church St SE, Minneapolis, MN 55455, USA
5 School of Physics and Astronomy, University of Nottingham, University Park, Nottingham, NG7 2RD, UK
6 Department of Astrophysical Sciences, Princeton University, 4 Ivy Lane, Princeton, NJ 08544, USA
7 Minnesota Institute for Astrophysics, University of Minnesota, 116 Church St SE, Minneapolis, MN 55455, USA
8 Oxford Applied and Theoretical Machine Learning (OATML) Group, Department of Computer Science, University of Oxford, Oxford, OX1 3QD, UK
9 Dept. of Physics and Astronomy, University of Alabama, Tuscaloosa, AL 35487, USA
10 Department of Physics and Astronomy, Haverford College, 370 Lancaster Avenue, Haverford, PA 19041, USA
11 Department of Physics, Lancaster University, Bailrigg, Lancaster, LA1 4YB, UK
12 Citizen Scientist, Zooniverse c/o University of Oxford, Keble Road, Oxford OX1 3RH, UK

Last updated XXX; in original form XXX

## ABSTRACT

We present Galaxy Zoo DECaLS: detailed visual morphological classifications for Dark Energy Camera Legacy Survey images of galaxies within the SDSS DR8 footprint. Deeper DECaLS images （r=23.6 vs r=22.2 from SDSS) reveal spiral arms, weak bars, and tidal features not previously visible in SDSS imaging. To best exploit the greater depth of DECaLS images, volunteers select from a new set of answers designed to improve our sensitivity to mergers and bars. Galaxy Zoo volunteers provide 7.5 million individual classifications over 314,000 galaxies. 140,000 galaxies receive at least 30 classifications, sufficient to accurately measure detailed morphology like bars, and the remainder receive approximately 5. All classifications are used to train an ensemble of Bayesian convolutional neural networks (a state-of-the-art deep learning method) to predict posteriors for the detailed morphology of all 314,000 galaxies. We use active learning to focus our volunteer effort on the galaxies which, if labelled, would be most informative for training our ensemble. When measured against confident volunteer classifications, the trained networks are approximately 99% accurate on every question. Morphology is a fundamental feature of every galaxy; our human and machine classifications are an accurate and detailed resource for understanding how galaxies evolve.

arXiv:2102.08414v2 \[astro-ph.GA\] 3 Jan 2022

## 1 INTRODUCTION

Morphology is a key driver and tracer of galaxy evolution. For example, bars are thought to move gas inwards (Sakamoto et al.1999) driving and/or shutting down star formation (Sheth et al.2004; Jogee et al.2005), and bulges are linked to global quenching (Masters et al. 2011; Fang et al.2013; Bluck et al.2014) and inside-out quenching (Spindler et al.2017; Lin et al.2019). Morphology also traces other

key drivers, such as the merger history of a galaxy. Mergers support galaxy assembly (Wang et al. 2011; Martin et al. 2018), though their relative contribution is an open question (Casteels et al. 2014), and may create tidal features, bulges, and disks, allowing past mergers to be identified (Hopkins et al. 2010; Fontanot et al. 2011; Kaviraj 2014; Brooks & Christensen 2015).

Unpicking the complex interplay between morphology and galaxy evolution requires measurements of detailed morphology in large samples. While modern surveys reveal exquisite morphological detail, they image far more galaxies than scientists can visually

- Contact e-mail: [mike.walmsley@physics.ox.ac.uk](mailto:mike.walmsley@physics.ox.ac.uk) classify. Galaxy Zoo solves this problem by asking members of the

Knowing the morphology of homogeneous samples of hundreds of thousands of galaxies supports science only possible at scale. The catalogues produced by the collective effort of Galaxy Zoo volunteers have been used as the foundation of a large number of studies of galaxy morphology (see Masters 2019 for a review), with the method's ability to provide estimates of confidence alongside classification especially valuable. Galaxy Zoo measures subtle effects in large populations (Masters et al. 2010; Willett et al. 2015; Hart et al. 2017); identifies unusual populations that challenge standard astrophysics (Simmons et al. 2013; Tojeiro et al. 2013; Kruk et al. 2017); and finds unexpected and interesting objects that provide unique data on broader galaxy evolution questions (Lintott et al. 2009; Cardamone et al. 2009; Keel et al. 2015).

Here, we present the first volunteer classifications of galaxy images collected by the Dark Energy Camera Legacy Survey (DECaLS, Dey et al. 2019). This work represents the first systematic engagement of volunteers with low-redshift images as deep as those provided by DECaLS, and thus represents a more reliable catalogue of detailed morphology than has hitherto been available. These detailed classifications include the presence and strength of bars and bulges, the count and winding of spiral arms, and the indications of recent or ongoing mergers. Our volunteer classifications were sourced over three separate Galaxy Zoo DECaLS (GZD) classification campaigns, GZD-1, GZD-2, and GZD-5, which classified galaxies first released in DECaLS Data Releases 1, 2, and 5 respectively. The key practical differences are that GZD-5 uses an improved decision tree aimed at better identification of mergers and weak bars, and includes galaxies with just 5 total votes as well as galaxies with 40 or more. Across all campaigns, we collect 7,496,325 responses from Galaxy Zoo volunteers, recording 30 or more classifications in at least one campaign for 139,919 galaxies and fewer (approximately 5 classifications) for an additional 173,870 galaxies, totalling 313,789 classified galaxies.

For the first time in a Galaxy Zoo data release, we also provide automated classifications made using Bayesian deep learning (Walmsley et al. 2020). By using our volunteer classifications to train a deep learning algorithm, we can make detailed classifications for all 313,789 galaxies in our target sample, providing morphology measurements faster than would be possible than relying on volunteers alone. Bayesian deep learning allows us to learn from uncertain volunteer responses and to estimate the uncertainty of our predictions. It also allows us to identify which galaxies, if labelled, would be most informative for training our classifier (active learning). We chose to partially focus our volunteers on such informative galaxies, requesting 40 classifications per informative galaxy and only 5 for the remainder. Our classifier predicts posteriors for how volunteers would have answered all decision tree questions 1 , with an accuracy comparable to asking 5 to 15 volunteers, depending on the question, and achieving approximately 99% accuracy on every question for galaxies where the volunteers are confident (volunteer vote fractions below 0.2 or above 0.8).

In Section 2, we describe the observations used and the creation

public to volunteer as ‘citizen scientists’ and provide classifications

## 2 IMAGING

## 2.1 Observations

Our galaxy images are created from data collected by the DECaLS survey (Dey et al. 2019). DECaLS uses the Dark Energy Camera (DECam, Flaugher et al. 2015) at the 4m Blanco telescope at Cerro Tololo Inter-American Observatory, near La Serena, Chile. DECam has a roughly hexagonal 3.2 square degree field of view with a pixel scale of 0.262 arcsec per pixel. The median point spread function FWHM is 1. $ ^{ \\prime\\prime} $ 29, 1. $ ^{ \\prime\\prime} $ 18 and 1. $ ^{ \\prime\\prime} $ 11 for g,r,and z, respectively.

The DECaLS survey contributes targeting images for the upcoming Dark Energy Spectroscopic Instrument (DESI). DECaLS is responsible for the DESI footprint in the Southern Galactic Cap (SGC) and the $ \\delta\\leqslant $ 34 region of the Northern Galactic Cap (NGC), totalling 10,480 square degrees 2 . 1130 square degrees of the SGC DESI footprint are already being imaged by DECam through the Dark Energy Survey (DES, The Dark Energy Survey Collaboration 2005) so DECaLS does not repeat this part of the DESI footprint. DECaLS implements a 3-pass strategy to tile the sky. Each pass is slightly offset (approx 0.1-0.6 deg). The choice of pass and exposure time for each observation is optimised in real-time based on the observing conditions recorded for the previous targets, as well as the interstellar dust reddening, sky position, and estimated observing conditions of possible next targets. This allows a near-uniform depth across the survey. In DECaLS DR1, DR2, and DR5, from which our images are drawn, the median 5 $ \\sigma $ point source depths for areas with 3 observations was approximately (AB) g=24.65,r=23.61,and $ z=22.84^{3} $ . The DECaLS survey completed observations in March 2019.

$$
\\delta\\leqslant34
$$

## 2.2 Selection

We identify galaxies in the DECaLS imaging using the NASA-Sloan Atlas v1.0.0 (NSA). As the NSA was derived from SDSS DR8 imaging (Aihara et al. 2011), this data release only includes galaxies that are within both the DECaLS and SDSS DR8 footprint. In effect, we are using deeper DECaLS imaging of the galaxies previously imaged in SDSS DR8. This ensures our morphological measurements have a wealth of ancillary information derived from SDSS and related surveys, and allows us to measure any shift in classifications vs. Galaxy Zoo 2 using the subset of SDSS DR8 galaxies classified both in this work and in Galaxy Zoo 2 (Sec. 4). Figure 1 shows the resulting GZ DECaLS sky coverage. NSA v1.0.0 was not published but the values of the columns used here are identical to those in NSA v1.0.1, released in SDSS DR13 (Albareti et al. 2017); only the column naming conventions are different.

1 Excluding the final 'Is there anything odd?' question as it is multiple- choice

2 The remaining DESI footprint is being imaged by DECaLS' companion surveys, MzLS and BASS (Dey et al. 2019)

3 See [https://www.legacysurvey.org/dr5/description/](https://www.legacysurvey.org/dr5/description/) and related pages

* * *

Figure 1. Sky coverage of GZ DECaLS (equatorial coordinates), resulting

Selecting galaxies with the NSA introduces two implicit cuts. First, the NSA primarily includes galaxies brighter than $ m\_{r} = 17.77 $ the SDSS spectroscopic target selection limit. Galaxies fainter than $ m\_{r}=17.77 $ are included only if they are in deeper survey areas (e.g. Stripe82) or were measured using 'spare' fibres after all brighter galaxies in a given field were covered; we suggest researchers enforce their own magnitude cut according to their science case. Second, the NSA only covers redshifts of $ z=0.15 $ or below. To these implicit cuts, we add an explicit cut requiring Petrosian radius (the NSA v1.0.0 PETROTHETA 4 column) of at least 3 arcseconds, to ensure the galaxy is sufficiently extended for meaningful classification.

$$
n\_{r}=17.77
$$

$$
m\_{r}=17.77
$$

$$
z=0.15
$$

For each galaxy, if the coordinates had been imaged in the g,r and z bands, and the galaxy passed the selection cuts above, we acquired a combined FITS cutout of the grz bands from the DECaLS cutout service ( [www.legacysurvey.org](http://www.legacysurvey.org/)).

$$
g r z
$$

$$
g,,r
$$

Galaxy Zoo presents volunteers with $ 4 2 4 \\times 4 2 4 $ pixel square galaxy images. GZD-1 and GZD-2 acquired $ 4 2 4 \\times 4 2 4 $ pixel square FITS cutouts directly from the cutout service. To ensure that galaxies typically fit well within a 424 pixel image, cutouts were downloaded with an interpolated pixel scale s of

$$
\\mathfrak{s}=\\operatorname{{m a x}}(\\operatorname\*{m{m}}(0.04p s0,0.02p g0),0.1)
$$

(1)

where $ p\_{50} $ is the Petrosian 50%-light radius and $ p\_{90} $ is the Petrosian 90%-light radius. Approximately 1% of galaxies have incorrectly large radii reported in the NSA (typically as a result of foreground stars or other interloping sources) and this causes the field to be incorrectly large and hence the target galaxy to appear incorrectly small. To allow researchers to mitigate this issue, we flag images for which there are more source pixels away from the centre than near the centre; specifically, for which the mean distance of all likely source pixels 5 exceeds 161 (approximately the expected value for all pixels). We find by eye that this simple procedure identifies the worst-affected galaxies. We report the mean source pixel distance and distance flags as wrong\_size\_statistic and wrong\_size\_warning, respectively.

$$
p50
$$

$$
p\_{90}
$$

For GZD-5, to avoid banding artifacts caused by the interpolation method of the DECaLS cutout service, each FITS image

was downloaded at the fixed native telescope resolution of 0.262 arcsec 2 per pixel 6 , with enough pixels to cover the same area as 424 pixels at the interpolated pixel scale s . These individually-sized FITS were then resized locally up to the interpolated pixel scale s by Lanczos interpolation (Lanczos 1938). Image processing is otherwise identical between campaigns. Galaxies with incomplete imaging, defined as more than 20% missing pixels in any band, were discarded. For GZD-1/2, 92,960 of 101,252 galaxies had complete imaging （91.8%）. For GZD-5, 216,106 of 247,746 galaxies not in DECaLS DR1/2 had complete imaging （87.2%） $ ^{7}. $

## from the imaging overlap of DECaLS DR5 and SDSS DR8, shown in red.

Darker areas indicate more galaxies. Sky coverage of Galaxy Zoo 2, which

$$
\\mathrm{e y e^{8}}
$$

_𝑁_. For pixels with a
standard deviation below 100, we scale the per-band deviation from

$$
\\sqrt{N}
$$

$$
X\_{i j c}^{\\prime}=\\overline{{X\_{i j}}}+\\alpha(X\_{i j c}-\\overline{{X\_{i j}}})\\quad\\mathrm{w h e r e}\\quad\\alpha=\\operatorname\*{m i n}(0.01\\sqrt{X\_{i j}T/\\lambda},1)
$$

(2)

′
where _𝑋𝑖𝑗𝑐_ and _𝑋_ are the flux at pixel
_𝑖𝑗𝑐_ _𝑋𝑖𝑗_ is the mean flux across bands at pixel
_𝑇_ is the mean exposure time (here, 90 seconds) and

$$
X\_{i j c}
$$

$$
X\_{i j c}^{\\prime}
$$

$$
\\overline{{X\_{i j}}}
$$

Pixel values were scaled by arcsinh $ ( x ) $ to compensate for the high dynamic range typically found in galaxy flux, creating images which can show both bright cores and faint outer features. To remove the very brightest and darkest pixels, we linearly rescale the pixel values to lie on the $ (-0.5,300) $ interval and then clip the pixel values to 0 and 255 respectively. We use these final values to create an RGB image using pillow (Kemenade et al. 2020).

The images are available on Zenodo at [https://doi.org/10.5281/zenodo.4573248](https://doi.org/10.5281/zenodo.4573248). The code used to download the FITS cutouts and convert them to RGB images is available on GitHub for GZD-1, GZD-2 and GZD-5.

4 Azimuthally-averaged SDSS-style Petrosian radius, derived from the r band. See Albareti et al. (2017) and the NSA v1.0.1 data model.

6 Up to a maximum of 512 pixels per side. Highly extended galaxies were downloaded at reduced resolution such that the FITS had exactly 512 pixels per side.

5 Arbitrarily defined as pixels with double the 20th percentile band-averaged value after the scaling in Sec. 2.3.

7 Note that these numbers do not sum to the total number of galaxies classified across both campaigns because some galaxies are shared between campaigns.

8 By Dustin Lang, who we gratefully acknowledge.

* * *

Figure 2. GZD-1, GZD-2 and GZD-5 classification counts, excluding im-

## 3 VOLUNTEER CLASSIFICATIONS

Volunteer classifications for GZ DECaLS were collected during three campaigns. GZD-1 and GZD-2 classified all 99,109 galaxies passing the criteria above from DECALS DR1 and DR2, respectively. GZD-1 ran from September 2015 to February 2016, and GZD-2 from April 2016 to February 2017. GZD-5 classified 262,000 DECALS DR5-only galaxies passing the criteria above. GZD-5 ran from March 2017 to October 2020. GZD-5 used more complex retirement criteria aimed at improving our automated classification (3.1) and an improved decision tree aimed at better identification of weak bars and minor mergers (4.2).

This iteration of the Galaxy Zoo project used the infrastructure made available by the Zooniverse platform; in particular, the open source Panoptes platform (The Zooniverse Team 2020). The platform allows for the rapid creation of citizen science projects, and presents participating volunteers with one of a subject set of images chosen either randomly, or through criteria described in section 3.1.

## 3.1 Selecting Total Classifications

How many volunteer classifications should each galaxy receive? Ideally, all galaxies would receive enough classifications to be confident in the average response (i.e. the vote fraction) while still classifying all the target galaxies within a reasonable timeframe. However, the size of modern surveys make this increasingly impractical. Collecting 40 volunteer classifications for all 314,000 galaxies in this data release would have taken around eight years without further promotion efforts. The larger data sets of future surveys will only be more challenging. In anticipation of future classification demands, we have therefore implemented a variable retirement rate here (motivated and described further in Walmsley et al.2020). Unlike previous data releases, GZ DECaLS galaxies each received different numbers of classifications (Figure 2). Beginning part-way through GZD-5,we prioritise classifications for the galaxies expected to most improve our machine learning models, and rely more heavily on those models for classifying the remainder.

For GZD-1 and GZD-2, all galaxies received at least 40 clas-

sifications 9 (as with previous data releases). GZD-1 galaxies have between 40 and 60 classifications, selected at random, while GZD-2 galaxies all have approximately 40. For GZD-5, galaxies classified until June 2019 also received approximately 40 classifications. From June 2019, we introduced an active learning system. Using active learning, galaxies expected to be the most informative for training our deep learning model received 40 classifications, and the remaining galaxies received at least 5 classifications.

plausibleclassifications(Sec.4.3.1).GZD-1hasapproximately40-60classifications,GZD-2hasapproximately40,andGZD-5haseitherapproximately

$$
\\begin{array}{l} \\mathbb {I} \[ k, w \] = \ - \\sum\_ {k = 0} ^ {N} \\left\\langle \\operatorname {B i n} \\left(k \\mid f ^ {w} (x), N\\right) \\right\\rangle \\log \\left\[ \\left\\langle \\operatorname {B i n} \\left(k \\mid f ^ {w} (x), N\\right) \\right\\rangle \\right\] \ + \\left\\langle \\sum\_ {k = 0} ^ {N} \\operatorname {B i n} \\left(k \\mid f ^ {w} (x), N\\right) \\log \\left\[ \\operatorname {B i n} \\left(k \\mid f ^ {w} (x), N\\right) \\right\] \\right\\rangle \ \\end{array}
$$

(3)

where $ f^{w}(x) $ is the output of the neural network trained to predict the typical volunteer response following Walmsley et al. (2020) and Bin($ k \| f^{w}(x), N $ ) is the probability for k of N volunteers to answer 'Featured' to 'Smooth or Featured' given that networkestimated typical response. Angled brackets indicate the expectation over the distribution of weights, approximated as the expectation over MC Dropout permutations. In short, the negative term gives the entropy of the volunteer vote distribution given the mean model predictions, and the positive term gives the mean entropy from the predictions of each permuted model. The difference between these terms measures the degree of confident disagreement between permuted models. See Walmsley et al. (2020) for more.

$$
f^{w}\\left(x\\right)
$$

$$
k\|f^{w}(x),N)
$$

We used the same architecture and loss function as in Walmsley et al. (2020) while concurrently developing the more sophisticated classifier introduced in this Section. The initial training set was all GZD-5 galaxies fully classified $ ( N > 36 ) $ by the time of activation. Each active learning cycle proceeded as follows. The model was retrained with all galaxies fully classified by the cycle start date Next, unlabelled galaxies were ranked by mutual information (Eqn. 3) and the most informative 1000 of a random $ 3 2 7 6 8^{1 1} $ galaxies were uploaded. Once those galaxies were fully classified by volunteers

9 Note that because classifications from volunteers who respond 'artifact' at implausibly high rates are discounted, the total classifications in Fig.2 and the published catalog are slightly lower - see Sec.4.3.1.

10 'Artifact' answers are sufficiently rare that we chose to ignore votes for this answer when calculating which galaxies to label.

11 To allow for out-of-memory shuffling, binary-encoded galaxy images were stored in 'shards' of 4096 galaxies each. 32,768 corresponds to 8 such shards

* * *

(typically in 1-4 weeks) the cycle was repeated. 6,939 total galaxies were uploaded in total $ ^{12}。 $

Figure 3. ‘Featured’ vote fraction and Petrosian radius (as measured by the
NSA

We emphasise that the number of classifications each galaxy received under active learning is not random. Figure 3 shows how active-learning-prioritised galaxies are dramatically more featured and slightly more extended than the previously-classified random galaxies, matching our intuition that small 'smooth' elliptical galaxies are easier to classify and hence less informative than extended 'featured' galaxies. For details on handling this and other selection effects, see Sec. 6.

We chose to select from a subset of galaxies not yet classified for two reasons. The first was for computational efficiency: calculating the acquisition function requires making 5 predictions per galaxy. The second was that ad hoc experiments showed that galaxies with the very highest acquisition function values were often highly unusual and might be too unusual to learn from effectively. We also added a retirement rule to retire galaxies receiving 5 classifications of 'artifact', to help avoid volunteers being presented with these prioritised artifacts.

## 3.2 Decision Trees

The questions and answers we ask our volunteers define the measurements we can publish. It is therefore critical that the Galaxy Zoo decision tree matches the science goals of the research community.

The questions in a given Galaxy Zoo workflow are designed to be answerable even by a classifier with little or no astrophysical background. This motivates a focus primarily on the appearance of the galaxy, rather than incorporating physical interpretations which would require prior knowledge of galaxies. As an example, the initial question in all decision trees from Galaxy Zoo 2 onwards has asked the viewer to distinguish primarily between "smooth" and "featured" galaxies, rather than "elliptical" and "disk" galaxies. This distinction between descriptive and interpretive classification is not always perfectly enforced. For example, the "features" response to the initial question is worded as "features or disk", and a later question asks whether the galaxy is "merging or disturbed", which requires some interpretation 13 . To aid classifiers, all itera-

tions of Galaxy Zoo have therefore included illustrative icons in the classification interface. Additional help is also available; in the current project, the interface includes a brief tutorial, a detailed field guide with multiple examples of each type of galaxy, and specific help text available for each individual classification task.

PETROTHETA column) for galaxies selected either at random (prior
to enabling active learning) or prioritised as informative. Prioritised galax-

The decision tree used for GZD-1 and GZD-2 has three modifications vs. the Galaxy Zoo 2 decision tree (Willett et al. 2013). The 'Can't Tell' answer to 'How many spiral arms are there?' was removed, the number of answers to 'How prominent is the central bulge?' was reduced from four to three, and 'Is the galaxy currently merging, or is there any sign of tidal debris?' was added as a standalone question.

For GZD-5, we made three further changes. Several Galaxy Zoo studies (e.g. Skibba et al. 2012; Masters et al. 2012; Willett et al. 2013; Kruk et al. 2018) found that galaxies selected with $ 0. 2 < p\_{\\mathrm{b a r}}< 0. 5 $ in GZ2 correspond to 'weak bars' when compared with expert classification such as those in Nair & Abraham (2010). Therefore, to increase the detection of bars, we changed the possible answers to the Does this galaxy have a bar?' question from 'Yes' or No' to Strong', Weak' or No'. We define a strong bar as one that is clearly visible and extending across a large fraction of the size of the galaxy. A weak bar is smaller and fainter relative to the galaxy, and can appear more oval than the strong bar, while still being longer in one direction than the other. Our definition of strong vs. weak bar is similar that of Nair & Abraham (2010), with the exception that they also have an intermediate' classification. We added examples of galaxies with 'weak bars' to the Field Guide and provided a new icon for this classification option, as shown in Figure 4.

$$
0.2{<}p\_{\\mathrm{b a r}}{<}0.5
$$

Second, to allow for more fine-grained measurements of bulge size, we increased the number of 'How prominent is the central bulge?' answers from three ('No', 'Obvious', 'Dominant') to five ('No Bulge', 'Small', 'Moderate', 'Large', 'Dominant'). We also re-included the 'Can't Tell' answer.

Third, we modified the 'Merging' question from 'Merging', Tidal', Both', or None', to the more phenomenological 'Merging', Major Disturbance', Minor Disturbance', or No'. Our goal was to present more direct answers to our volunteers and to better distinguish major and minor mergers, to support recent scientific interest in the role of major and minor mergers on mass assembly (López-Sanjuan et al. 2010; Kaviraj 2013), black hole accretion (Alexander & Hickox 2012; Simmons et al. 2017a), and morphology (Hopkins et al. 2009; Lotz et al. 2011; Lofthouse et al. 2017). We made this final 'merger' change two months after launching GZD-5;

12 Technical errors with duplicate uploads led to some active-learningprioritised galaxies receiving more than 40 classifications; the median number of classifications is 44.

13 The step from visual description to interpretation may explain why a model trained by Fischer et al. (2019) on expert T-Type labels makes more confident predictions than volunteers on whether a subset of low-mass GZ2 galaxies show spiral structure; see Peterken et al. (2021).

* * *

Figure 4. Classification decision tree for GZD-5, with new icons as shown

6722 GZD-5 galaxies (2.7%) were fully classified before that date and so do not have responses from volunteers to this question.

We also make several improvements to the illustrative icons shown for each answer. These icons are the most visible guide for volunteers as to what each answer means (complementing the tutorial, help text, field guide, and 'Talk' forum). Figure 4 shows the GZD-5 decision tree with new icons as shown to volunteers. The decision tree used in GZD-1 and GZD-2 is shown in Figure A1.

For the 'Smooth or Featured?' question, we changed the 'Smooth' icon to include three example galaxies at various ellipticities, and the 'Featured' icon to include an edge-on disk rather than a ring galaxy. For 'Edge On?', we replaced the previous tick icon with a new descriptive icon, and the previous cross icon with the 'Featured' icon above. We also modified the text to no longer specify 'exactly' edge on, and renamed the answers from 'Yes' and 'No' to 'Yes - Edge On Disk' and 'No - Something Else'. For 'Bulge?', we created new icons to match the change from four to five answers. For 'Bar', we replaced the previous tick and cross icons with new descriptive icons for 'Strong Bar', 'Weak Bar' and 'No Bar'. For 'Merger?', we added new descriptive icons to match the updated answers.

Changes to the decision tree complicate comparisons other Galaxy Zoo projects. As we show in the following sections, the available answers will affect the sensitivity of volunteers to certain morphological features, and so morphology measurements made with different decision trees may not be directly comparable. This

difficulty in comparison has historically required us to be conservative in our changes to the decision tree. However, the advent of effective automated classifications allows us to retrospectively make classifications using any preferred decision tree. Specifically, in this work, we train our automated classifier to predict what volunteers would have said using the GZD-5 decision tree, for galaxies which were originally classified by volunteers using the GZD-1/2 decision tree (Section 5.1).

## 4 VOLUNTEER ANALYSIS

## 4.1 Improved Feature Detection from DECaLS imagery


[... middle omitted — see footer ...]

\
Cardamone C., et al., 2009, Monthly Notices of the Royal Astronomical Society, 399, 1191\
\
Caruana R., 1997, Machine Learning, 28, 41\
\
Casteels K. R. V., et al., 2014, Monthly Notices of the Royal Astronomical Society, 445, 1157\
\
Chang J. C. J. C., Amershi S., Kamar E., 2017, Conference on Human Factors in Computing Systems - Proceedings, 2017-May, 2334\
\
Cheng T. Y., et al., 2020, Monthly Notices of the Royal Astronomical Society, 493, 4209\
\
Cook S. R., Gelman A., Rubin D. B., 2006, Journal of Computational and Graphical Statistics, 15, 675\
\
Dey A., et al., 2019, The Astronomical Journal, 157, 168\
\
Dickinson H., Fortson L., Scarlata C., Beck M., Walmsley M., 2019, Proceedings of the International Astronomical Union\
\
Dieleman S., Willett K. W., Dambre I., 2015, Monthly Notices of the Royal Astronomical Society, 450, 1441\
\
Domínguez Sánchez H., et al., 2019, Monthly Notices of the Royal Astronomical Society, 484, 93\
\
Eykholt K., et al., 2018, in Conference on Computer Vision and Pattern Recognition. [http://arxiv.org/abs/1707.08945](http://arxiv.org/abs/1707.08945)\
\
Fang J. J., Faber S. M., Koo D. C., Dekel A., 2013, Astrophysical Journal, 776, 63\
\
Ferreira L., Conslice C. J., Duncan K., Cheng T. Y., Griffiths A., Whitney A., 2020, The Astrophysical Journal, 895, 115\
\
Fischer J\
\
AstronomicalSciencesunderContractNo.AST-0950945toNOAO.\
\
Flaugher B., et al., 2015, Astronomical Journal, 150, 150\
\
* * *\
\
19\
\
Levasseur L. P., Hezaveh Y. D., Wechsler R. H., 2017,The Astrophysical\
Journal, 850, L7\
Lin L., et al., 2019,The Astrophysical Journal, 872, 50\
\
* * *\
\
## 20 M. Walmsley et al\
\
This paper has been typeset from a T E X/LAT E X file prepared by the author.\
\
4 3 2 Weak Bar 1 0 0 1 2 3 4 Strong Bar 2\
\
1 Weak Bar 0 0 1 2 Strong Bar 5 4 3 2 Weak Bar 1 0 0 1 2 3 4 5 Strong Bar 3 2 1 Weak Bar 0 0 1 2 3 Strong Bar 2\
\
1 Weak Bar 0 0 1 2 Strong Bar\
\
Figure12. Posteriorsfor‘Doesthisgalaxyhaveabar?’,forthesamerandom galaxiesselectedinFig.11.Eachpointiscoloredbythepredictedprobability of volunteers giving that many ‘Strong’, ‘Weak’, and (implicitly, as the total answersisfixed)‘None’votes.Thevolunteeranswer(notknowntoclassifier) is circled. For clarity, only the mean posterior across all models and dropout forward passes is shown.\
\
MNRAS,1–20(2021)\
\
* * *\
\
21\
\
_All Galaxies_\
\
_High Volunteer Confidence_\
\
Figure 13. Confusion matrices for each question, made on the test set of 11,346 galaxies in the (random) test set with at least 34 votes. Discrete classifications\
\
* * *\
\
22\
\
Figure 14. Confusion matrices for test set galaxies where the volunteers are confident in that question, defined as having the vote fraction for one answer above\
0.8. Such confident galaxies are expected to have a clearly correct label, making correct and incorrect predictions straightforward to measure but also making\
\
* * *\
\
_Galaxy Zoo DECaLS Data Release_ 23\
\
Smooth Or Featured Smooth Featured-or-disk Artifact\
\
5 10 15 20 Truncated number of votes\
\
Bar Strong Weak No\
\
5 10 15 20 Truncated number of votes\
\
Has Spiral Arms Vote Fraction Mean Deviation Yes Mean absolute deviations between the model predictions and the\
\
Figure 15.\
\
observed vote fractions, by question, for the test set galaxies with approxi- mately 40 volunteer responses. The model is typically well within 10% of the observed vote fractions.\
\
5 10 15 20 Truncated number of votes\
\
Bulge Size Large Moderate Small None\
\
smooth-or-featured\_smooth smooth-or-featured\_featured-or-disk smooth-or-featured\_artifact disk-edge-on\_yes disk-edge-on\_no has-spiral-arms\_yes has-spiral-arms\_no bar\_strong bar\_weak bar\_no bulge-size\_dominant bulge-size\_large bulge-size\_moderate bulge-size\_small bulge-size\_none how-rounded\_round how-rounded\_in-between how-rounded\_cigar-shaped edge-on-bulge\_boxy edge-on-bulge\_none edge-on-bulge\_rounded spiral-winding\_tight spiral-winding\_medium spiral-winding\_loose spiral-arm-count\_1 spiral-arm-count\_2 spiral-arm-count\_3 spiral-arm-count\_4 spiral-arm-count\_more-than-4 spiral-arm-count\_cant-tell merging\_none merging\_minor-disturbance merging\_major-disturbance merging\_merger\
\
0.00 0.05 0.10\
0.25\
0.20\
0.15\
0.10\
0.05 Mean error vs. all votes 0.00 0\
0.25\
0.20\
0.15\
0.10\
0.05 Mean error vs. all votes 0.00 0\
0.15\
0.25\
0.20\
0.15\
0.10\
0.05 Mean error vs. all votes 0.00 0\
0.25\
0.20\
0.15\
0.10\
0.05 Mean error vs. all votes 0.00 0\
Figure 16.\
\
5 10 15 20 Truncated number of votes\
\
Mean error on the true ( _𝑁 >_ 75) vote fractions for either a truncated ( _𝑁_ = 0 to _𝑁_ = 20) number of volunteers (solid) or the automated classifier (dashed). Asking only a few volunteers gives a noisy estimate of the true vote fraction. Asking more volunteers reduces this noise. For some number of volunteers, the noise in the vote fraction is similar to the error of the automated classifier, meaning they have a similar mean error vs. the true vote fraction; this number is where the solid and dashed lines intersect. We find the automated classifier has a similar mean error to approx. 5 to 15 volunteers, depending on the question.\
\
MNRAS,1–20(2021)\
\
* * *\
\
24\
\
Figure 17. Random spiral galaxies where the classifier confuses the most\
likely volunteer vote for spiral arm count between ‘2’ and ‘Can’t Tell’.\
\
\[Image: Im30\]\
\
Figure18. Galaxiesbinnedby‘SmoothorFeatured’votepredictionentropy,\
measuring the model’s uncertainty in the votes. Bins (columns) are equally\
\
* * *\
\
## Galaxy Zoo DECaLS Data Release 25\
\
| 100% | Disk Edge On |  |  |\
| --- | --- | --- | --- |\
|  | 3 N | 5 |  |\
| 80% 60% 40% Ratio in interval 20% 0% | 3 0 | N 4 0 |  |\
| 0% | 20% 40% Credible interval width | 60% | 80% 100% |\
\
Has Spiral Arms 100%\
\
80%\
\
60%\
\
40% 3 _N_ 5 20% Ratio in interval 3 0 _N_ 4 0 0% 0% 20% 40% 60% 80% 100% Credible interval width\
\
Figure 19. Calibration curves for the two binary GZ DECaLS questions.\
\
The _𝑥_-axisshowsthecredibleintervalwidth-fordata-dominatedposteriors, roughly (e.g.) 30% of galaxies should have vote fractions within their 30% credible interval. The _𝑦_-axis shows what percentage actually do fall within each interval width. We split calibration by galaxies with few votes (and hencetypicallywiderposteriors)andmorevotes(narrowerposteriors).Only credible intervals with at least 100 measurements are shown. Calibration for both questions is excellent.\
\
Volunteers (N=5378) Automated (N=43672)\
\
1.0 1.0\
0.8 0.8 _g g_ _av_ 0.6 _av_ 0.6 _W W_\
0.4 0.4\
0.2 0.2\
0.0 0.0\
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 _B a v g B a v g_\
Figure 20. Distribution of bulge size vs. spiral winding, using responses\
\
from volunteers (left) or our automated predictions (right). We observe no clear correlation between bulge size and spiral winding, consistent with M19.Thedistributionsareconsistentbetweenvolunteersandourautomated method. We hope this demonstrates the accuracy and scientific value of our automated classifier.\
\
MNRAS,1–20(2021)\
\
$$\
(\\mathbf{e}.\\mathbf{g}.)\
$$\
\
* * *\
\
## 26 M. Walmsley et al\
\
T00: Is the galaxy simply smooth and rounded, with no sign of a disk? A0: Smooth A1: Features A2: Star or or disk artifact\
\
T07: How rounded is it? T01: Could this be a disk viewed edge-on? A0: A1: In A2: Cigar A0: Yes A1: No Completely between shaped round\
\
T08: Does the galaxy have a bulge T02: Is there a sign of a bar feature through the at its centre? If so, what shape? centre of the galaxy? A0: A1: Boxy A2: No A0: Bar A1: No bar Rounded bulge\
\
T03: Is there any sign of a spiral arm pattern? A0: Spiral A1: No spiral\
\
T09: How tightly wound do the spiral arms appear? A0: Tight A1: Medium A2: Loose\
\
T10: How many spiral arms are there? A0: 1 A1: 2 A2: 3 A3: 4 A4: More than 4\
\
T04: How prominent is the central bulge, compared with the rest of the galaxy? A0: No A2: Obvious A3: bulge Dominant\
\
T05: Is the galaxy currently merging or is there any sign of tidal debris? A0: Merging A1: Tidal A2: Both A3: Neither debris\
\
1st Tier Question 2nd Tier Question 3rd Tier Question T06: Do you see any of these odd features in the image? 4th Tier Question A0: None A1: Ring A2: Lens or A3: Dust A4: Irregular A5: Other A6: arc lane Overlapping\
\
End\
\
Figure A1. Decision tree used for GZD-1 and GZD-2, based on the Galaxy Zoo 2 decision tree. The GZD-5 decision tree is shown in Figure4.\
\
MNRAS,1–20(2021)\
\
* * *\
\
arXiv:2102.08414v2 \[astro-ph.GA\] 3 Jan 2022\
\
# APPENDIX A: GALAXIES WITH CONFIDENT\
\
To intuitively demonstrate the performance of our automated classifier, we show, for a selection of detailed morphology questions, the galaxies with the most confident automated classifications for that question. We show the galaxies with the highest mean posterior for being strongly barred (Fig.A1), edge-on and bulgeless (Fig A2), one-armed spirals (Fig.A3), loosely wound spirals (Fig.A4) and mergers (Fig. A5). We present the galaxies here as shown to Galaxy Zoo volunteers (in color and at 424x424 pixel resolution), but the model makes predictions on more challenging greyscale 224x224 pixel images.\
\
* * *\
\
Figure A1. Galaxies automatically classified as most likely (highest mean posterior) to be strongly barred.\
\[Image: Im1\]\
\
* * *\
\
Figure A2. Galaxies automatically classified as most likely (highest mean posterior) to be edge-on with no bulge.\
\[Image: Im2\]\
\
* * *\
\
Figure A3. Galaxies automatically classified as most likely (highest mean posterior) to have exactly one spiral arm.\
\[Image: Im3\]\
\
* * *\
\
Figure A4. Galaxies automatically classified as most likely (highest mean posterior) to have loosely wound spiral arms.\
\[Image: Im4\]\
\
* * *\
\
Figure A5. Galaxies automatically classified as most likely (highest mean posterior) to be mergers, with automatic ‘featured’ vote\
fraction ¿ 0.5. Only one thumbnail per galaxy pair is shown.\
\[Image: Im5\]

──────── [TRUNCATED] ────────
Showing 29,527 chars (head) + 9,965 chars (tail) of 103,402 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-67f1d1fdc2.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-67f1d1fdc2.md" offset=270 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
