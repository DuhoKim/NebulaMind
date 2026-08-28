URL: https://arxiv.org/pdf/1610.07060

On the nature and correction of the spurious S-wise spiral galaxy winding bias in Galaxy Zoo 1

Wayne B. Hayes, Darren Davis, Pedro Silva

Computer Science Department University of California, Irvine Irvine, California 92697-3435

[whayes@uci.edu](mailto:whayes@uci.edu)

ABSTRACT

The Galaxy Zoo 1 catalog displays a bias towards the S-wise winding direction in spiral galaxies which has yet to be explained. The lack of an explanation confounds our attempts to verify the Cosmological Principle, and has spurred some debate as to whether a bias exists in the real universe. The bias manifests not only in the obvious case of trying to decide if the universe as a whole has a winding bias, but also in the more insidious case of selecting which galaxies to include in a winding direction survey. While the former bias has been accounted for in a previous image-mirroring study, the latter has not. Furthermore, the bias has never been corrected in the GZ1 catalog, as only a small sample of the GZ1 catalog was re-examined during the mirror study. We show that the existing bias is a human selection eect rather than a human chirality bias. In eect, the excess S-wise votes are spuriously \\stolen" from the elliptical and edge-on-disk categories, not the Z-wise category. Thus, when selecting a set of spiral galaxies by imposing a threshold T so that max(PS;PZ) > T or PS+PZ> T, we spuriously select more S-wise than Z-wise galaxies. We show that when a provably unbiased machine selects which galaxies are spirals independent of their chirality, the S- wise surplus vanishes, even if humans are still used to determine the chirality. Thus, when viewed across the entire GZ1 sample (and by implication, the Sloan catalog), the winding direction of arms in spiral galaxies as viewed from Earth is consistent with the ip of a fair coin.

# arXiv:1610.07060v1 \[astro-ph.GA\] 22 Oct 2016

Subject headings:

1. Introduction
   The Cosmological Principle is the assumption that at large scales the universe is homo- geneous and isotropic. Homogeneity says that there is no special location in the Universe, and in particular that the Earth occupies no special location. Isotropy means that there is
   no preferred direction in the universe; for spiral galaxies, this means that the distribution
   of their spin axes should be spread uniformly at random on the celestial sphere. The two
   assumptions together imply that, as seen from the Earth, the distribution of observed arm
   winding directions of N spiral galaxies should be statistically consistent with N ips of a
   fair coin.

The Galaxy Zoo 1 (hereafter GZ1) project (Lintott et al. 2008, 2010) was a website
where humans were presented with random galaxy images from the Sloan Digital Sky Survey
(York et al. 2000). With each galaxy image they were given a choice of 6 \\cartoon" galaxies
and asked which cartoon most resembled the real galaxy. The GZ1 sample has almost
900,000 galaxies. After using SpArcFiRe (Davis and Hayes 2014) to perform an ellipse t of
all GZ1 images, we concentrate on a subsample of 458,012 galaxies whose minor axis were
larger than 14 pixels (semi-minor axis of 7 pixels), which we subjectively determined was the
smallest sized disk on which spiral structure could be observed. For each galaxy, the number
of votes for each of the 6 categories was converted into a fraction (Table 1).

| category | EL | EDGE | S-wise | Z-wise | MG | DK | total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Winner by 50% majority | 261700 | 53873 | 25102 | 23807 | 4431 | 755 | 369668 |
| Percentage | 57.14% | 11.76% | 5.48% | 5.20% | 0.97% | 0.16% | 80.71% |
| Winner by max vote | 309591 | 73009 | 33007 | 31340 | 8406 | 2659 | 458012 |
| Percentage | 67.59% | 15.94% | 7.21% | 6.84% | 1.84% | 0.58% | 100% |

Table 1: The 6 types of votes in Galaxy Zoo 1 across our sample of 458,012 GZ1 galaxies,
along with the fraction of galaxies in each category as voted by the GZ1 humans. Note that
not all galaxies have a winning vote that is a 50% majority, although every galaxy has a
maximum vote (we ignore ties, which are rare).

As can be seen in Table 1, there is a signicant excess of S-wise spiral galaxies, using
either a majority-vote winner, or a less stringent \\max vote" winner; similar surplusses of
S-wise spirals are seen using other, more stringent criteria (Lintott et al. 2008; Land et al.
2008). In our case, using the 50% majority-wins criterion, there are 25102 + 23807 = 48909
galaxies with visible spiral structure, but there is an S-wise excess of 5:86 (see Table 2)
compared to 48909 coin ips; the \\max vote" criterion shows an even stronger excess, with
a statistical signicance of 6:57. As we will see from Table 2 below, the eect gets smaller
as we insist on higher human classication condence, but never goes away even when 100%
of humans agree on the chirality of a small set of galaxies. The statistical signicance of this
bias is detailed as a function of human condence in the rst quarter of Table 2, in which
both the selection of galaxies, and their chirality, are chosen by GZ1 humans. As can be
seen, the bias is detected at a level of somewhere between 3 and 6, depending upon the

25102+23807=48909 human condence level.

Whether this excess is real or not has been a matter of some debate. Lintott et al.
(2008) and Land et al. (2008) show that the bias seems to disappear if galaxy images are
ipped with 50% probability before being shown to humans, suggesting that somehow the
humans are biased towards choosing S-wise galaxies. Whether the bias is a human cognitive
bias, or perhaps due to website design or positioning of the buttons is unclear, and of little
astronomical interest in any case. However, other studies (Longo 2011; Shamir 2012) have
suggested that the bias is real rather than artifactual.

In this paper we put the problem to rest. We show below that the bias is almost certainly
a human bias, and not a property of the actual GZ1 galaxies.

2. Nature of the bias

2.1. More S-wise than Z-wise spins for all values of \\spirality"

Figure 1 shows the frequencies of galaxies with the two winning chiralities, as voted by
GZ1 humans, as a function of their sum PS+ PZ. We refer to this sum as the spirality of a
galaxy, and its value is meant to represent the probability that there exists any observable
1
spiral structure. As can be seen, the S-wise bias manifests across all values of spirality
even down close to zero, where the galaxies are unlikely to be spiral at all. Furthermore, we
note that if one chooses any cuto in spirality (or similarly max(PS;PZ)) meant to isolate
galaxies with visible spiral structure, then any such sample will automatically include more
S-wise than Z-wise galaxies, because the S-wise curve is uniformly above the Z-wise one for
all values of spirality. We shall demonstrate, as did Land et al. (2008) and Lintott et al.
(2008), that this bias is spurious and not reprentative of the true chirality distribution.

P\_{S}+P\_{Z}

(P\_{S},P\_{Z}))

2.2. Do humans actually disagree on chirality?

Land et al. (2008) briey mentioned that there did not appear to be signicant disagreement between humans about chirality. This statement seems at odds with Figure 1. Here we
study that statement in detail, because understanding it may prove crucial to understanding
where the bias comes from. To test the hypothesis that humans can disagree on the chirality
of a galaxy, we introduce the idea of the opposing vote, which we dene for any galaxy as

1
As distinct from GZ1’s PCS= PS+ PZ+ PEDGE, which includes edge-on disks and represents if the
galaxy, as seen from any direction, is a disk galaxy.

P\_{C S}=P\_{S}+P\_{Z}+P\_{E D G E}

* * *

Z S

## of votes

0.20.30.40.50.6
Frequency

0.1 0 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
P\_Z+P\_S

Fig. 1.\| Lines joining the frequency histograms (vertical axis) of S-wise and Z-wise galaxies,

according to GZ1 humans, having x = PS+PZ(horizontal axis) among 20 equally-spaced bins in \[0,1\]. Note that all galaxies in the entire GZ1 sample are represented in this plot; galaxies to the left end tend to be elliptical or edge-on, while galaxies to the right end have clearly visible spiral structure. We see that the S-wise bias manifests across the entire spectrum, so for example near x = 1, we see that among all galaxies for which PS+ PZ0:95, slightly more than half have PS0:95, while slightly less than half have PZ0:95. The selection eect manifests because any cuto in PS+ PZthat is intended as a threshold above which a galaxy is considered to have visible spiral structure will automatically include more S-wise than Z-wise galaxies.

* * *

the most popular vote other than the most popular chirality. Note that this is not quite the
same as the second most popular vote, because if the most popular chirality is not the most
popular vote overall, then the opposing vote is actually the winning vote overall. In other
words,

1. When one of the two chiralities is the winning vote, then the opposing vote is the
   second most popular vote.

2. When neither of the two chiralities is the winning vote, the \\opposing vote" is the
   winning vote for that galaxy.


Figure 2 describes the distribution and structure of the opposing votes, as a function of
the most popular chirality, which is just max(PS;PZ), even if that winning chirality is not
the winning vote across all 6 votes. The top half of Figure 2 shows the frequency that each
of the other 5 votes (which are the losing chirality plus EL, EDGE, MG, DK) occur as the
opposing vote. The rst observation is that the losing chirality, min(PS;PZ), is almost never
the opposing vote, even for very small values of the winning vote. That is to say, humans
virtually never disagree on the chirality of a galaxy; even when only a small percentage of
people actually choose a chirality, they still agree on that chirality.

(P\_{S},P\_{Z})

{P\_{S},P\_{Z}})

Instead, the top half of Figure 2 demonstrates that the opposing vote is almost always
either EDGE or EL. This tells us that the selection eect in Figure 1 occurs when people are
uncertain whether they see spiral structure at all; the galaxy may be an edge-on disk galaxy
with indistinct spiral structure, or appear to be elliptical that has faint spiral structure, but
those that choose a chirality in that case tend, for whatever reason, to be slightly more
inclined to choose S-wise over Z-wise, but even in those cases the humans tend to agree with
each other on the chirality chosen. In other words, to arrive at the S-wise bias, humans are
\\stealing" votes from EDGE and EL, not from Z-wise. This allows the bias to exist even
though humans virtually never disagree on chirality. Another interesting observation of the
top half of Figure 2 is that near the origin, the EL and EDGE curves correctly show that,
among galaxies that have no visible spiral structure, about 80% are elliptical and just under
20% are edge-on\|in rough agreement with Table 1.

* * *

Fig. 2.\| Top: Histogram of galaxy count (black bars) and frequency of the opposing vote
(colored curves), as a function of the most popular chirality vote. As can be seen, the losing
chirality is rarely the opposing vote. Bottom: Average value of the opposing vote, with the
same horizontal axis.

* * *

structure but are somehow disrupted so as to make the chirality unclear; one may hazard a guess that they may in fact be advanced mergers.

Finally, again referring to Figure 2, the sharp peak of the losing chirality (yellow line) at x = 0:9 in the top gure is not a problem because, as the lower gure shows, the value of that vote is tiny, as is the value of all the other non-winning votes (as they must be, since the winning chirality is taking 90% of the votes).

These graphs show that humnans do not signicantly disagree with each other when determining chirality, which is an observation that is not at all obvious from any of the studies that have occurred to date. In fact it would be surprising if humans disagreed to any signicant extent on winding direction, because in all but a very small number of cases, our own intuitive observation is that if there is a winding direction at all, it should be fairly obvious. These graphs strongly conrm this intuition. Together, Figures 1 and 2 demonstrate that the bias has nothing to do with humans disagreeing on winding direction. Instead, what is happening is that whenever there is uncertainty about whether or not there exists spiral structure of any chirality\|that is, when a signicant proportion of humans vote either edge-on or elliptical\|then those that do vote for a chirality tend to vote for S-wise. The reason for this is still unknown, but the three obvious choices are (a) a human visual cortex bias; (b) something about the design of the web page for the GZ1 survey induces people to preferentially choose the S-wise button; or (c) there is a real chirality bias in the SDSS sample of galaxies.

3. Unbiased machine determination of winding direction
   At this point we have two relevant observations: (1) galaxies voted S-wise signicantly outnumber galaxies voted Z-wise, and (2) humans do not signicantly disagree on chirality. In the absense of evidence for a human bias, this would directly imply that there is a real chirality bias in the universe. Land et al. (2008) convincingly demonstrated that this is not the case by having the GZ1 humans re-classify a subset of spiral galaxies while randomly left-right ipping each image with 50% probability. However, beyond demonstrating that the bias was human, they did not attempt to correct for it on a galaxy-by-galaxy basis.

SpArcFiRe2 Davis and Hayes (2014) is an automated method that decomposes a spiral galaxy into its constituent arms. A very brief summary of how SpArcFiRe works is depicted in Figure 3. As described in Davis (2014); Davis and Hayes (2014), it was tested on a sample

2 SPiral ARC FInder and REporter

* * *

(a)

(b)

(c)

(d)

(e)

(f)

Fig. 3.\| Steps SpArcFiRe (Davis and Hayes 2014) takes in describing a spiral galaxy image.
a) The centered and de-projected image. b) Contrast-enhanced image. c) Orientation eld
(at reduced resolution for display purposes). d) Initial arm segments found via Hierarchical
Agglomerative Clustering (HAC) of nearby pixels with similar orientations and consistent
logarithmic spiral shape, overlaid with the associated logarithmic spiral arcs tted to these
clusters. e) Final pixel clusters (and associated arcs) found by merging compatible arcs. f)
Final arcs superimposed on image (a). Red arcs wind S-wise, cyan arcs wind Z-wise.

of 29,250 GZ galaxy images chosen by the leader of the Galaxy Zoo Project3. Among many
other things, one of SpArcFiRe’s outputs is a determination of the galaxy’s winding direction.
Given a list of found spiral arcs in a galaxy image, there are many ways to determine a global
winding direction for the entire galaxy. Some arcs are longer than others, some may wind in
the opposite direction to the majority, and some \\arcs" are actually just noise mistaken for
an arc. We found that the most reliable measure of the winding direction of the galaxy was
a length-weighted vote of the winding direction of all the discovered spiral arcs.

To demonstrate that this measure is unbiased with regard to spin direction, we refer to
Figure 4, which shows a scatter plot of the left-to-right mirrored vs. unmirrored value of
the galaxy’s pitch angle as measured by SpArcFiRe; in a perfect reversal, the two should be
negatives of each other. We nd that in 29,094 out of 29,250 cases (99.47% of cases), the
4
two are negatives of each other to within 10 degrees. Even more relevant to this paper, we
nd that in all but 5 cases (99.983% of cases), the chirality of the mirrored image is correctly
ipped compared to the unmirrored case. Thus, the chirality determination of SpArcFiRe
4
is unbiased, with respect to ipped images, to better than 2 parts it 10.

10^{4}

3
Stephen Bamford, Personal Communication. The selection criteria were: (GZ1PS+ GZ1PZ) > 0:8 OR
(GZ2F eaturesOrDisk> 0:7 AND GZ2N otEdgeOn> 0:7 AND GZ2spiral> 0:8).

\\mathrm{}{G Z2\_{F e a t u r e s O r D i s k}>0.7 ~~\ \\mathrm{A N D}~~ G Z2\_{N o t E d g e O n}>0.7 ~~\\mathrm{A N D}~~ G Z2\_{s p i r a l}>0.5}

* * *

60 40 20

# 0 mirrored

# −20

# −40

# −60

# −60 −40 −20 0 20 40 60 unmirrored

Fig. 4.\| Galaxy-level pitch angles reported by SpArcFiRe using unmirrored and left-to-right

mirrored input images across 29,250 \\clear" spiral galaxies (see text for denition). These galaxy-level pitch angles are calculated as the arc-length-weighted average of all arcs agreeing with the dominant winding direction (as determined by an arc-length-weighted vote). We see that for almost all galaxies the measured pitch angle almost exactly negative, as it should be. The diagonal line gives y = x; cases on this line are visually underrepresented due to overlap. More importantly, only 5 cases out of 29,250 disagree on chirality, showing that SpArcFiRe is chirality-unbiased to a level of almost 1 part in 10,000.

* * *

determined by the unbiased SpArcFiRe algorithm. The statistical signifance of the S-wise
bias is weaker than in the rst quarter of Table 2, but surprisingly, the bias is still signicant
to somewhere between 2 and 3.

4. Unbiased machine determination of spirality

Our goal in this section is to explain how we created a machine learning algorithm
that was capable of reproducing the spirality PS+ PZ, while being simultaneously unable
to reproduce either PSnor PZalone. That is, we want to create a spirality measure for a
galaxy that is provably independent of chirality.

P\_{S}+P\_{Z}

P\_{S}

P\_{Z}

4.1. Building a selector that is unbiased to chirality

As alluded to earlier, the problem is not in the actual determination of chiraltiy. Humans
do not disagree with each other on chirality, and in fact the human determination of chirality
agrees with the SpArcFiRe determination of chirality in between 95% and 98% of cases on the
GZ1 clean sample, depending upon SpArcFiRe’s own determination of its certainty(Davis
2014, tables 5.1 and 5.2, column \\80"), and the cases of chirality disagreement between GZ1
humans and SpArcFiRe appear randomly distributed.

Figure 1 points to the problem: S-wise galaxies outnumber Z-wise ones for any set
of galaxies selected using a criterion of either max(PS;PZ) or PS+ PZgreater than some
threshold, and PSand PZare taken from the human GZ1 vote values. Thus, we must
determine some method of determining if there is a selection bias and if so, try to eliminate
it.

P\_{S}+P\_{Z}

\\alpha,

P\_{S}

P\_{Z}

To do this, we need to create a sample of galaxies that have visible spiral structure
(\\spirality"), but selected in a way that is unbiased to winding direction. To do this we
create a machine learning algorithm that is provided with attributes of the galaxy that are
independent of winding direction, and tell it to attempt to reproduce PS+ PZ. We then
demonstrate that it can reproduce PS+ PZwith reasonable accuracy and then show that it
is unable to simultaneously reproduce winding direction to any level better than chance.

P\_{S}+P\_{Z}.

In order to create such an algorithm, we need to ensure that the features it uses (that
is, the measurements of the galaxy) are features that are independent of chirality. This may
not be trivial, as recent work has suggested that even photometric data may be able to
recover winding diretion to a signicant degree (Shamir 2016). We choose our attributes to
include some photometric attributes that were disjoint with those that Shamir (2016) found

P\_{S}+P\_{Z} to be correlated with chirality, in addition to several SpArcFiRe outputs with all chirality
information removed.

Our list of input attributes to our machine learning algorithm, assumed to be independent of chirality, are as follows. From the SDSS database, we allow parameters used by
Banerji et al. (2010) (colors, de Vaucouleurs t axial ratios, exponential t axial ratios, exponential disk t log likelihood, de Vaucouleurs t log likelihood, star log likelihood, ratios
of Petrosian radii, Adaptive shape measures, adaptive ellipticities, adaptive 4th moment,
and a texture parameter), as well as absolute magnitudes and disk-to-bulge ratios. From
SpArcFiRe (Davis and Hayes 2014) we allow all numerical output parameters including pitch
angles after having taken their absolute value. Such parameters include counts and lengths
of spiral arcs, the absolute value of their pitch angles, and the number and length of arcs
of agreeing and disagreeing chiralities (with the actual chirality replaced by "majority" and
"minority").

Finally, since it is known that machine learning algorithms tend to reproduce the input
distribution of target values we trained our machine on a set of galaxies that were 50-50
S-wise and Z-wise according to the GZ1 humans.

We applied two lters to the data to build a dataset of high-condence spiral galaxies.
For S-wise the rule was ((PS+ PZ> 0:6) \ (PS> 0:5) \ (PSPZ> 0:3)); which means
that there are at least 60% of the votes for spirality, at least 50% of the nal votes were for
PS, and there is at least 30% more votes for PSthan for PZ. The rst and second rules are
eective in ltering out other types of objects and the third in making sure that the humans
have a higher agreement not only in spirality but also in chirality. Similarly to build our
Z-wise set the rule was ((PS+ PZ> 0:6) \ (PZ> 0:5) \ (PZPS> 0:3)). After this we
sampled 19500 objects from each class, to assure we had a balanced dataset, totaling 39000
objects.

((\ P\_{S}\ +\ P\_{Z}:>:0.6)\ cap(\ P\_{S}:>:0.5)\ \\cap\ (P\_{S}:-:P\_{Z}:>:0.3))

P\_{S}

P\_{S}

P\_{Z}

We built a random forest model to predict chirality. As it is common with these models,
we performed what is called a \\hyperparameter" search across possible machine congurations to decide what was the optimal number of trees per forest and the optimal number
of features per tree. We built 45 models with number of trees varying on the interval
f10,15,20,25,30,35,40,45,50g and number of features per tree from f30,40,50,60,70g. We
used a Bernoulli distribution to sample 75% of the data for training the forests and the
remaining 25% to test the models.

* * *

the models built, have an accuracy below 50%, i.e they are worse than a coin ip for tracking chirality. To make sure that our models are not able to indeed predict chirality we decided to further investigate the 3 models that had at least 51% accuracy.

When performing a classication task in machine learning one can have a notion of how condent a model is. For our case we set up the target to be either 0, to predict PZ, or 1, to predict PS. The model outputs a number P within this range: if P < 0:5 we say the predicted class for that object was PZ, if P > 0:5 the predicted class is PS. The more condent a model is that an object belongs to either class the closer the output value will be to those limits (0 and 1). That means that when a model is not very condent of its output, the values predicted will fall mostly in the middle value of the range. To better visualize this distribution Figure 6 shows histograms from the 3 models that had at least 51% accuracy. As we had supposed, the distributions are heavily centered, indicating that the model has a very low level of condence on its predictions. Also, from the 3 models at least 77% of the predictions were between 0.4 and 0.6, i.e., the model had less than 20% of condence on the output for at least 77% of the objects.

To ensure once and for all that these models performance was due to chance we rebuilt those three models using the same data,the same Bernoulli distribution and the same split for test and training and at the end we got dierent accuracy values for the 3 models that were previously at least 51%. The best out of the 3 now has an accuracy of 50.23%.

We conclude that with these models, given these attributes we are unable to retain any information that correlates in any way to chirality of spiral galaxies.

4.2. Using the same machine to predict spirality
Now that we have a list of attributes and a machine that is unable to predict chirality in the form of either PSor PZalone, we use a machine with the same input attributes and hyperparameters to reproduce the sum PS+ PZ, which we term the spirality of a galaxy.

Given a list of human spirality votes PS+ PZfor each galaxy, we train the machine on 75% of the galaxies and test it on the remaining 25%; we do this four times, for four non-overlapping 25% subsets. The concatenation of these four 25% test subsets constitute our database of machine-determined spiralities that are independent of chirality. Given a particular galaxy, the dierence between the human value PS+PZand our predicted spirality PSPis the error for that galaxy. The root mean squared error across all galaxies is a typical

4 This means that the model predicted a value p on the interval 0 < p < 0:5 when the expected value was 0 and and 0:5 <= p <= 1 when the expected value was 1.

* * *

Fig. 5.\| Chirality Prediction using Random Forests with 45 dierent architectures, based

on the number of trees and the number of features for each forest.

* * *

Fig. 6.\| Histograms of the predictions for the 3 models that had the highest accuracy.

Each column represents a model with the rst being the best overall, using 50 trees and 60 features and an accuracy of 51.54%, the second, using 45 trees and 40 features and an accuracy of 51.14%, and the third using 50 trees and 70 features and an accuracy of 51.01%. The rst row amounts for all the values predicted by the model, and the second and third rows shows the values that the model predicted correctly and incorrectly, respectively. 4 measure used to assess the accuracy of a predicted model. In our case, we were able to
produce a machine with an RMSE of 0.137 across our sample of 450,012 galaxies. This is
quite a bit larger than what other machines have done; for example the Kaggle winner was
able to produce an RMSE of just 0.07 (Dieleman et al. 2015). However, they made no eort
to remove human bias, and thus it is not surprising that they are able to reproduce exactly
how the humans voted better than we can.

5. Results

The bottom half of Table 2 shows the results of our chirality bias study when our
unbiased machine (x4) selects galaxies based on predicted spirality. As can be seen, using
this machine to perform selection virtually eliminates the chirality bias, even if humans
still choose the chirality. This conrms our statement earlier that the GZ1 humans have a
selection bias, not a chirality bias. In fact there is no signicant dierence between the two
subtables in the lower half of Table 2: as long as our machine learning algorithm performs the
selection based on unbiased spirality, it doesn’t matter if the winding direction is determined
by humans, or by SpArcFiRe. In either case, the S-wise bias is either vastly reduced, or
reversed, apparently at random.

6. Discussion

Ideally we would like to integrate our new catalog into the GZ1 catalog so as to publish
a \\corrected" vote catalog in which the chirality bias has been removed. However, this is
not as simple as rescaling the PSand PZvalues to our values. Recall that the S-wise votes
are \\stolen" from the edge-on and elliptical categories. Thus, we would need to re-scale all
the vote values on a galaxy-by-galaxy basis, not just the two chirality votes, in order to fully
correct the bias. Furthermore, we would like to do this in a way that only minimally changes
the values of the human votes. Creating a machine algorithm that simultaneously removes
the bias, and also minimizes the change in human vote values, is non-trivial, and left for
future work.

Acknowledgements

P\_{Z}

* * *

## scribing the GZ1 human handedness bias.

REFERENCES

Banerji, M., O. Lahav, C. J. Lintott, F. B. Abdalla, K. Schawinski, S. P. Bamford, D. An- dreescu, P. Murray, M. J. Raddick, A. Slosar, et al. (2010). Galaxy zoo: reproducing galaxy morphologies via machine learning. Monthly Notices of the Royal Astronomical Society 406 (1), 342{353.

Davis, D. R. (2014). Fast Approximate Quantication of Arbitrary Arm-Segment Structure in Spiral Galaxies. Phd thesis, University of California, Irvine.

Davis, D. R. and W. B. Hayes (2014). Sparcre: Scalable automated detection of spiral galaxy arm segments. The Astrophysical Journal 790 (2), 87.

Dieleman, S., K. W. Willett, and J. Dambre (2015). Rotation-invariant convolutional neural networks for galaxy morphology prediction. Monthly notices of the royal astronomical society 450 (2), 1441{1459.

Land et al., K. (2008, August). Galaxy Zoo: the large-scale spin statistics of spiral galaxies in the Sloan Digital Sky Survey. MNRAS 388 (4), 1686{1692.

Lintott et al., C. (2010). Galaxy Zoo 1: Data release of morphological classications for nearly 900,000 galaxies. MNRAS 14 (1), 1{14.

Lintott et al., C. J. (2008). Galaxy Zoo: Morphologies derived from visual inspection of galaxies from the Sloan Digital Sky Survey. MNRAS 389, 1179{1189.

Longo, M. J. (2011, May). Detection of a dipole in the handedness of spiral galaxies with redshifts z ~ 0.04. Phys. Lett. B 699 (4), 224{229.

Shamir, L. (2012). Handedness asymmetry of spiral galaxies with z< 0.3 shows cosmic parity violation and a dipole axis. Physics Letters B 715 (1), 25{29.

Shamir, L. (2016). Asymmetry between galaxies with clockwise and counterclockwise hand- edness. arXiv preprint arXiv:1601.04424.

York et al., D. (2000). The Sloan Digital Sky Survey: Technical summary. Astron. J. 120, 1579{1587.

This preprint was prepared with the AAS LATEX macros v5.2.

* * *

| spirality selector | chirality determination | spiral cutoff |
| --- | --- | --- |
| GZ1 humans | GZ1 humans | 0.4 |
| 0.5 |  |  |
| 0.6 |  |  |
| 0.7 |  |  |
| 0.8 |  |  |
| 0.9 |  |  |
| GZ1 humans | SpArcFiRe | 0.4 |
| 0.5 |  |  |
| 0.6 |  |  |
| 0.7 |  |  |
| 0.8 |  |  |
| 0.9 |  |  |
| unbiased machine | GZ1 humans | 0.4 |
| 0.5 |  |  |
| 0.6 |  |  |
| 0.7 |  |  |
| 0.8 |  |  |
| 0.9 |  |  |
| unbiased machine | SpArcFiRe | 0.4 |
| 0.5 |  |  |
| 0.6 |  |  |
| 0.7 |  |  |
| 0.8 |  |  |
| 0.9 |  |  |

| city |  |  | sigma value p-value |  |
| --- | --- | --- | --- | --- |
|  | S-wise |  |  | Z-wise |
|  | 32016 | 30619 | 4.70σ | 10-6 |
|  | 25625 | 24572 | 4.24σ | 10-5 |
|  | 20952 | 20093 | 3.47σ | 0.0002 |
|  | 16631 | 16004 | 3.28σ | 0.0004 |
|  | 12444 | 11932 | 2.75σ | 0.0030 |
|  | 7774 | 7435 | 2.52σ | 0.006 |
|  | 31633 | 31002 | 2.84σ | 0.002 |
|  | 25417 | 24780 | 2.48σ | 0.007 |
|  | 20774 | 20271 | 2.39σ | 0.010 |
|  | 16533 | 16102 | 1.93σ | 0.030 |
|  | 12339 | 12037 | 1.68σ | 0.050 |
|  | 7708 | 7501 | 0.84σ | 0.250 |
|  | 29979 | 30184 | 0.43σ | 0.130 |
|  | 19829 | 19743 | 0.23σ | 0.400 |
|  | 13130 | 13093 | 1.07σ | 0.150 |
|  | 8510 | 8371 | 1.34σ | 0.100 |
|  | 5028 | 4895 | 1.70σ | 0.040 |
|  | 2231 | 2119 | 0.18σ | 0.40 |
|  | 30103 | 30060 | 0.14σ | 0.45 |
|  | 19800 | 19772 | 0.60σ | 0.30 |
|  | 13063 | 13160 | 1.07σ | 0.15 |
|  | 8371 | 8510 | 1.34σ | 0.09 |
|  | 4895 | 5028 | 1.64σ | 0.05 |
|  | 2121 | 2229 |  |  |

Table 2: Comparing the statistical signicance of the chirality bias. Selector: who selects
the sample (GZ1 humans or an unbiased machine learning algorithm); chirality determination: who performs the chirality determination (GZ1 humans or unbiased SpArcFiRe

nation: who performs the chirality determination (GZ1 humans or unbiased SpArcFiRe
algorithm); spirality cuto:
S-wise and Z-wise: number of S-wise and Z-wise galaxies in above dened sample; the
over-represented chirality is highlighted in bold; sigma and p-value:
and p-value of dierence between S- and Z-wise count compared to same number of coin
ips.

who performs the chirality determination (GZ1 humans or unbiased SpArcFiRe
include only galaxies for which PSP= PS+ PZ> cuto;
number of S-wise and Z-wise galaxies in above dened sample; the
over-represented chirality is highlighted in bold; sigma and p-value: standard deviation
and p-value of dierence between S- and Z-wise count compared to same number of coin

P\_{S P},=,P\_{S}+P\_{Z},>
