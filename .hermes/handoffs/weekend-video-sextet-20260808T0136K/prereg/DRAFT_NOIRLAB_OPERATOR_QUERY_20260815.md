# DRAFT — operator query to the Legacy Surveys / NOIRLab data team

**Status: DRAFT, NOT SENT.** Sending is Duho's decision. Nothing in this file has been transmitted.
Every figure is drawn from the frozen preregistration and the crew's sourced receipts; see the
verification block at the end.

**Suggested subject:** Guidance on retrieving ~832,000 single-band cutouts from DR10 South — preferred channel?

---

Dear Legacy Surveys data team,

I am preparing a preregistered test of the spiral-galaxy handedness dipole reported by Longo (2011),
using DESI Legacy Imaging Surveys DR10 South. I am writing **before** retrieving anything, because
the volume is large enough that I would rather be told the right way to do it than guess.

**What I need**

- ~832,393 objects passing a frozen photometric selection in DR10 South
- one 128 × 128 pixel cutout each, at the native 0.262"/pixel — about 33.5" on a side
- **single band (r), float32** — the classifier is a single-channel network, so g and z are not needed
- total pixel payload ≈ **54.6 GB**

**Why I am asking rather than starting**

Your documentation discourages automated high-volume use of the cutout service and directs large
downloads to Globus. I read that as covering a request of this size, so I have not issued any
requests. My prepared pipeline is deliberately built with no HTTP client at all and cannot fetch;
adding one is a separate, reviewed step I have not taken.

**What I would like to know**

1. Is a request of this size and shape acceptable against the cutout service at all? If so, what
   request rate and concurrency would you consider appropriate? My current plan is deliberately
   conservative — one request at a time, minimum five seconds between requests — which would take
   about 48 days. I am happy to run slower, or in windows you prefer.
2. Would you rather I pull coadd bricks via Globus and cut locally? By my arithmetic that moves far
   more data (~3.2 TB for single-band `image-r` across ~270,577 bricks, versus ~54.6 GB of cutouts),
   so it seemed worse for your infrastructure, not better — but you know your load better than I do.
3. Is there a channel I have not considered — a bulk cutout service, a collaborator compute
   allocation at NERSC where I could generate cutouts beside the coadds and transfer only the
   outputs, or something else?

**Scope, so you know what this becomes**

The study is preregistered and hash-pinned before any data is touched. The published output is
**aggregate only** — I will not be publishing a per-object derived catalogue, because I could not
establish that your terms cover redistributing one, and I would rather stay inside them than assume.
Standard Legacy Surveys acknowledgement will appear in any paper.

I am glad to adjust the request shape, the rate, or the channel to whatever suits you. Thank you for
maintaining the surveys and for making the data this accessible.

With thanks,
Duho Kim

---

## Verification block (not part of the message)

| Claim | Source |
|---|---|
| 832,393 objects | frozen Cut-6 parent, `TORI_BS1_CLOSURE_PACKET.md` |
| 128 × 128, single band r, float32 | PC-1 as amended, `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` (`b06901c8a0f3a057…`) |
| 0.262"/px → 33.5" | 128 × 0.262 = 33.536, arithmetic |
| 54.6 GB | 832,393 × 128² × 4 bytes = 54,551,707,648 |
| 1 concurrent, 5.0 s minimum → 48.2 days | `TORI_ACQUISITION_20260814.md` lines 108–109; 832,393 × 5 s |
| bulk discouraged, Globus recommended | `GORU_SURVEY_ACCESS_FACTS_20260815.md` §2–3, from survey documentation |
| ~3.2 TB single-band bricks | 270,577 × 11,911,680 B, Goru's measured HTTP HEAD on brick `0001m002` |
| aggregate-only output | F-10, and BS-1's failed licence limb — `TORI_BS1_LICENCE_20260814.md` |

**Open before sending:** the correct recipient address has not been established. It should go to the
address the survey publishes for data questions, not guessed.
