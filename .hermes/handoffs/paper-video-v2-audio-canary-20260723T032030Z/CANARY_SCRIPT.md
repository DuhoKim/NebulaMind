# Flagship paper V2 — audio/comprehension canary script

Marker: `NEBULAMIND_Z9_AUDIO_COMPREHENSION_CANARY_SCRIPT_V2`
Purpose: user review of voice quality, cadence, pronunciation, and explanation clarity before any full V2 video build.

## Approved canary text

Early galaxies had very different chemical ingredients from galaxies today. Astronomers call the chemical richness of a galaxy's gas its metallicity. This paper studies five extremely early galaxies. Because none is magnified by gravitational lensing, the team avoids a correction that can distort the galaxies' estimated masses. Their oxygen abundance is roughly five times lower than in nearby galaxies of similar mass. Astronomers describe that difference as about zero point seven dex. The result stays similar when researchers change the local comparison or remove one galaxy at a time. But the sample is small, and the absolute abundance scale remains uncertain.

## Pace contract

- Words: 101
- Target: 105–125 spoken words per minute
- Target duration: 48.5–57.7 seconds
- Provider speed: 0.80×
- No post-synthesis time compression
- Review-master format: lossless PCM WAV

## Source map

- Metallicity as the paper's measure of gas chemical enrichment: paper abstract and introduction, lines 14–18 and 73–82 of the frozen text extract.
- Five-object strictly unlensed Pollock field sample: lines 20–22 and 90–96.
- Lensing can distort inferred stellar masses: lines 14–16 and 75–82.
- Oxygen-abundance deficit of approximately 0.69 dex: lines 20–22 and 152–160.
- “Roughly five times lower”: explicit logarithmic translation, `10^0.7 = 5.012`; stated before the unfamiliar `dex` label so the meaning lands first.
- Local-anchor swap changes the result by only about 0.04 dex: lines 22–25 and 155–161.
- Leave-one-out spread is about 0.04 dex: lines 20–22 and 155–156.
- Remaining small-sample and absolute abundance-scale uncertainty: lines 28–31 and 202–210, 221–243.

## Full-V2 scope note

The eventual full explainer must separately teach that five Pollock galaxies define the core redshift 9.3–9.9 result, while GN-z11 extends the direct-temperature sample to six and checks the sign at redshift 10.6. This short voice canary intentionally evaluates only the core teaching arc.

## Publication boundary

Local audio review only. No full video, upload, public mutation, unlisting, embed change, Git action, build/restart, or deployment is authorized by this canary.
