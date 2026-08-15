# DRAFT — post to the decam-legacy-survey forum

**Status: DRAFT, NOT POSTED.** Posting is Duho's decision.
**Channel:** `decam-legacy-survey` Google Group — the survey's own first-listed point of contact
(`legacysurvey.org/contact`). Chosen over `help@legacysurvey.org` so the answer is public and
citable; chosen over emailing named PIs, which the survey's contact page directs against.

**Framing note (not part of the post):** Goru established there is **no permission process** — the
data is public and the published protocol for volume is "use Globus or download bricks." So this is
not a permission request. It asks which channel they would rather we use, and explains why cutouts
look lighter on their infrastructure than bricks do.

**Suggested subject:** DR10 South: ~832k single-band 128×128 cutouts — cutout service or Globus bricks?

---

Hello,

I am preparing a preregistered measurement using DESI Legacy Imaging Surveys DR10 South, and I would
rather ask which retrieval route you prefer than pick one and find out I chose badly.

**What the study needs**

- ~832,393 objects passing a frozen photometric selection in DR10 South
- one **128 × 128 pixel** cutout each at the native 0.262"/pixel — about 33.5" on a side
- **single band (r), float32.** The classifier is a single-channel network, so g and z are not needed
- total pixel payload ≈ **54.6 GB**

**Where I have got to on my own**

I read the guidance that automated high-volume use of the cutout service is discouraged and that
large downloads should go through Globus, so I have not issued any requests. My prepared pipeline
deliberately contains no HTTP client at all and cannot fetch; adding one is a separate step I have
not taken.

I also compared the two routes, and the arithmetic seems to point the opposite way to the general
advice, which is why I am asking rather than assuming:

| route | requests | volume |
|---|---:|---:|
| 128×128 single-band cutouts | 832,393 | **~54.6 GB** |
| single-band `image-r` brick coadds | 270,577 files | **~3.2 TB** |

(brick figure from the compressed `image-r.fits.fz` size of a representative DR10 South brick)

Taking whole bricks moves roughly sixty times more data for a comparable number of requests, since
the coadds are one file per filter. So bricks look worse for your infrastructure, not better — but
you know your actual load and I do not, and I may be missing something obvious.

**The questions**

1. Is a job of this shape acceptable against the cutout service? If so, what rate and concurrency
   would you consider polite? My current plan is one request at a time with five seconds between
   requests, which takes about 48 days. I am happy to go slower, or to run only in windows you'd
   prefer.
2. If you would rather I take bricks via Globus despite the larger volume, I will — please just say so.
3. Is there an option I have not considered? A bulk cutout path, or generating cutouts beside the
   coadds under a NERSC allocation and transferring only the outputs, would both suit me fine.

**Scope**

The study is preregistered and hash-pinned before any data is touched. Published output is
**aggregate only** — I will not release a per-object derived catalogue, since I could not establish
that the image licence extends to redistributing one, and I would rather stay inside the terms than
assume. The standard Legacy Surveys acknowledgement will appear in any resulting paper.

Thanks for maintaining the surveys, and for making the data as reachable as it is.

Duho Kim

---

## Verification block (not part of the post)

| Claim | Source |
|---|---|
| 832,393 objects | frozen Cut-6 parent, `TORI_BS1_CLOSURE_PACKET.md` |
| 128×128, single band r, float32 | PC-1 as amended, `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` (`b06901c8a0f3a057…`) |
| 33.5" | 128 × 0.262 = 33.536 |
| 54.6 GB | 832,393 × 128² × 4 = 54,551,707,648 |
| 1 concurrent / 5.0 s → 48.2 days | `TORI_ACQUISITION_20260814.md` 108–109 |
| ~3.2 TB bricks, 270,577 files | 270,577 × 11,911,680 B — Goru's HTTP HEAD on brick `0001m002` |
| one file per filter | `GORU_SURVEY_ACCESS_FACTS_20260815.md` §1 |
| bulk discouraged, Globus recommended, no permission process | ibid. §2–3 |
| aggregate-only output | F-10; BS-1 licence limb FAILED, `TORI_BS1_LICENCE_20260814.md` |

**Before posting:** the group may require joining before it accepts a post, and joining is itself an
action Duho should take rather than me. The private alternative is `help@legacysurvey.org`, which
trades the public record for confidentiality about sample size and timing.
