# PROPERTY EXHIBIT — option A V19: the source decision is the same at two wall-clock times from the same archived inputs (exhibit_property.py output, verbatim; reproduces byte-for-byte)

```
[
 {
  "exhibit": "A-synthetic",
  "identical": true,
  "mode": "with live re-fetch from the archive",
  "times": [
   "2026-09-06T03:12:00Z",
   "2026-10-06T03:11:00Z"
  ],
  "verdicts": [
   {
    "outcome": "ACCEPT-DRAND",
    "round": 6441108,
    "seed_hex": "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",
    "source": "drand-mainnet-default",
    "t_pulse": "2026-09-06T03:11:00Z"
   },
   {
    "outcome": "ACCEPT-DRAND",
    "round": 6441108,
    "seed_hex": "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",
    "source": "drand-mainnet-default",
    "t_pulse": "2026-09-06T03:11:00Z"
   }
  ]
 },
 {
  "exhibit": "A-synthetic",
  "identical": true,
  "mode": "from retained bytes only",
  "times": [
   "2026-09-06T03:12:00Z",
   "2026-10-06T03:11:00Z"
  ],
  "verdicts": [
   {
    "outcome": "ACCEPT-DRAND",
    "round": 6441108,
    "seed_hex": "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",
    "source": "drand-mainnet-default",
    "t_pulse": "2026-09-06T03:11:00Z"
   },
   {
    "outcome": "ACCEPT-DRAND",
    "round": 6441108,
    "seed_hex": "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",
    "source": "drand-mainnet-default",
    "t_pulse": "2026-09-06T03:11:00Z"
   }
  ]
 },
 {
  "exhibit": "B-real-filed-RETRY-record",
  "identical": true,
  "note": "MIN_T_SIGN refuses this record's T_sign under V19; the verdict shown is that refusal \u2014 identical at both times, as the property requires; it is NOT a seed",
  "record_sha256": "1c1d9d4bacc35319e91d46420b8f892e1126cc48059ec69156a0a718428aeb4b",
  "times": [
   "2026-09-06T02:00:00Z",
   "2026-10-06T02:00:00Z"
  ],
  "verdicts": [
   {
    "outcome": "REFUSE-T-SIGN-PREDATES-AMENDMENT",
    "round": null,
    "seed_hex": null,
    "source": null,
    "t_pulse": null
   },
   {
    "outcome": "REFUSE-T-SIGN-PREDATES-AMENDMENT",
    "round": null,
    "seed_hex": null,
    "source": null,
    "t_pulse": null
   }
  ]
 }
]

ALL IDENTICAL: True
EXHIBIT-DIGEST: b790ebdfc65d80183bb4eb32089a8102252e64f380e7ad0c6e7f341411b82060
```
