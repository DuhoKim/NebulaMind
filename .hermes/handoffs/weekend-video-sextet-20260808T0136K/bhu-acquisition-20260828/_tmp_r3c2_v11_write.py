import io,sys,re
T,OLD,SCR,MAN=sys.argv[1:5]
p="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; s=io.open(p,encoding='utf-8').read()
E=[]
def E_(o,n,t): E.append((o,n,t))
E_("**Tori, 2026-09-05. Version 10 (see §10). OPTION (c) ADOPTED","**Tori, 2026-09-05. Version 11 (see §10; §10.5 for the V10 gate reconciliation). OPTION (c) ADOPTED","header")
E_("C0 by two pattern-blind seats who must agree, then the two-seat gate, before any\nfreeze.**","C0 by two independent seats who must agree, then the two-seat gate, before any\nfreeze.**","header seats")
E_("**Inclusion is assigned independently by the two pattern-blind seats from the §1 rule alone;","**Inclusion is assigned independently by the two independent seats from the §1 rule alone;","§1 seats")
E_("## 2. Method — per claim, in order\n\n1. **Extract**",f"## 2. Method — per claim, in order\n\n**The corpus is pinned: `R3C2_CORPUS_MANIFEST.md` (sha256 `{MAN}`) lists every enumerable text by\ndigest and byte count; a seat enumerates claims from those files and no other. Files listed there as RAW are not enumerable\nand are outside the census, visibly.** *(V11: no version before this one pinned the corpus at all — codex V10.)*\n\n1. **Extract**","§2 corpus")
E_("""> **THE INPUTS THE ARITHMETIC MAY CONSUME** = every ledger record with status `PRINTED` (given in the paper, whatever
> its `origin`) or `STANDARD` (on C3's closed list). **PROVENANCE IS RECORDED, NOT FILTERED**: each record's `origin`
> is cited under C3, `root_origins` is computed by script, and the claim's **`rests_on`** field is computed by the
> same script — `DERIVED_ONLY` when every root origin is `DERIVED` or `STANDARD`; otherwise the most severe root
> origin present, in the fixed order `USES_UNDECLARED` > `USES_IMPORTED` > `USES_FITTED` > `USES_CHOSEN` — with the
> full root-origin set printed beside it. **No seat writes `rests_on`.** The interpretation step reads `rests_on`,
> never the reproduction verdict (§7).""",
f"""> **THE INPUTS THE ARITHMETIC MAY CONSUME** = every ledger record with status `PRINTED` (given in the paper, whatever
> its `origin`) or `STANDARD` (on C3's closed list). **PROVENANCE IS RECORDED, NOT FILTERED**: each record's `origin`
> is cited under C3, independently by both seats; `root_origins` and the per-claim summary field **`rests_on`** are
> computed from the ledger by the pinned script `r3c2_ledger_tools.py` (sha256 `{SCR}`), with the full
> root-origin set printed beside it. **No seat writes `root_origins` or `rests_on`; the script rejects a ledger that
> arrives with either set.**
<!--SEAT-REDACT-->
> *(Master only — the rule the script implements: `DERIVED_ONLY` when every root origin is `DERIVED`, `STANDARD` or
> `MEASURED`; otherwise the most severe root origin present, in the fixed order `USES_UNDECLARED` > `USES_IMPORTED` >
> `USES_FITTED` > `USES_CHOSEN`. A claim with a disputed root carries the pair computed under both classifications and
> is marked `DISPUTED`. The interpretation step reads `rests_on` and the reproduction tally as two facts (§7). V11:
> kimi V10 read the severity order and the "interpretation reads rests_on" sentence from the packet and reconstructed
> the channel the conclusion rides on; both now live here, not in the seat's copy — the seat records provenance and
> never computes or weighs the field.)*
<!--/SEAT-REDACT-->""","§3 blockquote")
E_("""- **`REPRO_EXACT`** — the paper's number follows, within its own stated precision, **from the paper's own recipe
  applied to the inputs it states** (`PRINTED` or `STANDARD`). The claim's `rests_on` is reported beside it.
- *(`REPRO_AFTER_CHOICE` — RETIRED at V10 by the principal's ruling adopting option (c). What it recorded — that the number
  rests on a chosen, fitted, imported or undeclared input — is now the `rests_on` field of a `REPRO_EXACT` or
  `REPRO_FAILED` claim, computed by script. Two blind C0 seats had found the class unreachable under the derivation-only
  wording (§10.3); it is retired, not repaired.)*""",
"""- **`REPRO_EXACT`** — the paper's number follows, within its own stated precision, **from the paper's own recipe
  applied to the inputs it states** (`PRINTED` or `STANDARD`). **Report both numbers.** **Where the paper states no
  precision for the claim, the printed precision is the claim's stated precision: the reproduced value must round to
  the printed numeral at that precision.** The claim's `rests_on` is reported beside it. <!--SEAT-REDACT-->*(kimi V10:
  "13.8 Gyr" against 13.797 was fileable either way; the rule decides it mechanically. codex V10 asked for the name
  to change to `REPRO_WITHIN_STATED_PRECISION`; a class rename is the principal's, escalated in §10.5.)*<!--/SEAT-REDACT-->
<!--SEAT-REDACT-->- *(`REPRO_AFTER_CHOICE` — RETIRED at V10 by the principal's ruling adopting option (c). What it recorded — that the number
  rests on a chosen, fitted, imported or undeclared input — is now the `rests_on` field of a `REPRO_EXACT` or
  `REPRO_FAILED` claim, computed by script. Two blind C0 seats had found the class unreachable under the derivation-only
  wording (§10.3); it is retired, not repaired.)*<!--/SEAT-REDACT-->""","§3 EXACT + retired note")
E_("""- **`REPRO_BLOCKED`** — an input traces to a source **outside this lane that we cannot obtain**. Name it. *(Distinct
  from `REPRO_INPUT_ABSENT`, which is an input the paper simply never states.)*""",
"""- **`REPRO_BLOCKED`** — an input whose value the paper does not print, but for which the paper **names a source (a
  citation)**, where that source is outside this lane and cannot be obtained. Name it. *(Distinct from
  `REPRO_INPUT_ABSENT`, which is an input the paper neither prints nor traces to any named source.)* <!--SEAT-REDACT-->*(kimi V10:
  as written every unobtainable input was first `ABSENT` and the precedence filed it `REPRO_INPUT_ABSENT`, so this
  class's exclusive domain was empty. The named-source test separates them; the precedence below puts BLOCKED first.)*<!--/SEAT-REDACT-->""","§3 BLOCKED")
E_("""- **`REPRO_INPUT_ABSENT`** — an input the equation needs is `ABSENT` from the paper, so the attempt stops there.
  **Name the input.**""","""- **`REPRO_INPUT_ABSENT`** — an input the equation needs is `ABSENT` from the paper — **neither printed nor traced to
  any named source** — so the attempt stops there. **Name the input.**""","§3 INPUT_ABSENT")
E_("""order:** `REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`, then the
**arithmetic group**.""","""order:** `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`, then the
**arithmetic group**.""","§3 precedence")
E_("""3. **`CENSUS_AUDIT_FAILED`** — the audit of §6 cannot reproduce a sampled per-claim outcome. The census is void; report
   which.""","""3. **`CENSUS_AUDIT_FAILED`** — the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, **or the §7
   receipt verification fails**. The census is void; report which.""","§4 AUDIT_FAILED")
E_("""   seats' classification and both quotations. *(Disagreement about provenance is reported, never reconciled — if
   two blind readers cannot agree from the paper's own text what a number's provenance is, that is a finding about
   the corpus, and reconciling it would destroy it.)*""","""   seats' classification and both quotations. <!--SEAT-REDACT-->*(Disagreement about provenance is reported, never reconciled — if
   two blind readers cannot agree from the paper's own text what a number's provenance is, that is a finding about
   the corpus, and reconciling it would destroy it.)*<!--/SEAT-REDACT-->""","§4 ORIGIN_DISPUTED rationale")
E_("""   the other with no class — a gap codex found.)*""","""   the other with no class — a gap codex found.)*

**Exactly one study-level outcome is filed. Where more than one condition holds, file the first in this order:**
`R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`,
`CENSUS_PARTIAL`, `CENSUS_COMPLETE`. **Once a stop class applies, later limbs are unreached and their controls are
`NOT_RUN`.** <!--SEAT-REDACT-->*(Both V10 seats: §3 had a total precedence and §4 did not, so a tally satisfying two
classes had no rule. The order is chronological — controls run before enumeration, enumeration before origin, origin
before audit — which is codex's order; kimi's differed only in placing the denominator dispute first.)*<!--/SEAT-REDACT-->""","§4 total precedence")
E_("— and for **any condition whose failure would refute this lane's own expectation** — ","— and for **every declared condition** — ","C0 stake")
E_("**The exhibitions are authored by a seat and only\n  verified by Tori** — deciding what counts as reachable is where an author's prior would enter, so the author does\n  not decide it.",
"**The exhibition is authored independently by one independent seat and independently verified by a second\n  independent seat; both must return `C0_REACHABILITY=PASS`. The lane owner checks only that every declared outcome\n  and condition has a row and does not judge reachability.**","C0 two seats")
E_("""  `C1_DENOMINATOR_PRINTED=PASS`.
- **C2 — input ledger.** Every input classified `PRINTED` / `STANDARD` / `ABSENT`, each `PRINTED` one carrying file and
  line. `C2_INPUT_LEDGER=PASS`.""",
f"""  **The candidate and exclusion ledgers are JSON files validated by the pinned script:
  `/usr/bin/python3 r3c2_ledger_tools.py census <candidates.json> <exclusions.json>` — exit 0 only if every candidate
  carries exactly one disposition and the printed counts equal the recomputed counts; print its command, stdout and
  exit status.** `C1_DENOMINATOR_PRINTED=PASS|FAIL|NOT_RUN`, PASS only on exit 0.
- **C2 — input ledger.** Every input classified `PRINTED` / `STANDARD` / `ABSENT`, each `PRINTED` one carrying file and
  line, in the JSON schema of C3, validated by `/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> <sources_dir>`
  (exit 0 = PASS; every failure printed). `C2_INPUT_LEDGER=PASS|FAIL|NOT_RUN`.""","C1/C2 validator")
E_("`{claim_id, symbol, status: PRINTED|STANDARD|ABSENT, origin: DERIVED|STANDARD|CHOSEN|FITTED|IMPORTED|UNDECLARED,",
   "`{claim_id, input_id, symbol, status: PRINTED|STANDARD|ABSENT, origin: DERIVED|STANDARD|MEASURED|CHOSEN|FITTED|IMPORTED|UNDECLARED,","C3 schema")
E_("""  `ORIG_EQUATION`→`DERIVED`, `ORIG_CONSTANT`→`STANDARD`, `ORIG_CHOICE_STATED`→`CHOSEN`, `ORIG_FIT_STATED`→`FITTED`,
  `ORIG_CITATION`→`IMPORTED`, `ORIG_SILENT`→`UNDECLARED` — and, except for `ORIG_SILENT`, a **verbatim quotation
  machine-matched to the cited line**.""",
"""  `ORIG_EQUATION`→`DERIVED`, `ORIG_CONSTANT`→`STANDARD`, `ORIG_MEASURED`→`MEASURED` (a quantity the paper reports as
  its own measurement, with the measurement described), `ORIG_CHOICE_STATED`→`CHOSEN`, `ORIG_FIT_STATED`→`FITTED`,
  `ORIG_CITATION`→`IMPORTED`, `ORIG_SILENT`→`UNDECLARED` — and, except for `ORIG_SILENT`, a **verbatim quotation
  machine-matched to the cited line**. **Every input's `origin` is classified independently by both seats.** **Where
  more than one reason code matches the cited sentence, file the first in this order: `ORIG_CITATION`,
  `ORIG_FIT_STATED`, `ORIG_CHOICE_STATED`, `ORIG_MEASURED`, `ORIG_EQUATION`, `ORIG_CONSTANT`, `ORIG_SILENT` — a sentence
  that names an external source for the value is a citation whatever else it says.** <!--SEAT-REDACT-->*(kimi V10's
  attack: "We adopt H₀ = 67.4 from Planck (2018)" filed CHOSEN passed every machine check and reported a less severe
  root; the code precedence makes the citation win. `MEASURED` added because a measured-but-silent input was forced to
  `UNDECLARED`, the most severe root, by construction — kimi's observation 2.)*<!--/SEAT-REDACT-->""","C3 codes")
E_("""  A chain cannot be made to look clean by classifying only its last step. **The same script computes each claim's
  `rests_on` from its `root_origins` by the fixed severity order of §3 and prints the root-origin set beside it; a
  `rests_on` value written by a seat, or absent, fails this control.**""",
f"""  A chain cannot be made to look clean by classifying only its last step. **The script is `r3c2_ledger_tools.py`,
  committed beside this document, sha256 `{SCR}`; the seat runs
  `/usr/bin/python3 r3c2_ledger_tools.py compute <ledger.json> <out.json>` and prints its stdout and exit status. It
  computes each claim's `rests_on` from its `root_origins` and prints the root-origin set beside it; it REJECTS (exit 2) a
  ledger that arrives with `root_origins` or `rests_on` already set; it FAILS (exit 1) on a `derived_from` id that names
  no record, on a cycle, and on a `DERIVED` record with no `derived_from`, so an empty root set cannot occur; where the
  two seats' `origin` classifications differ the record carries `origin_alt` and the claim's `rests_on` is computed under
  both and marked `DISPUTED`.** A `rests_on` value written by a seat, or absent, fails this control.""","C3 script pinned")
E_("""  **What is therefore done:** each seat is run from a **redacted copy directory outside the lane**, containing the
  **seat packet** — not this document — the seat brief and the pinned sources, with the wrapper pointed at that
  directory and **not** at the lane. That is enforceable, and it is the control.""",
"""  **What is therefore done:** each seat is run from a **redacted copy directory outside the lane**, containing the
  **seat packet** — not this document — the seat brief `SEAT_BRIEF.md`, the script `r3c2_ledger_tools.py`, and the
  pinned sources of `R3C2_CORPUS_MANIFEST.md`, with the wrapper pointed at that directory and **not** at the lane. **The
  lane owner lists that directory's contents and their digests in the dispatch record before launch; a copy missing any
  of them is not dispatched.** **This is procedural, not enforced by the filesystem**: nothing here denies a seat an
  absolute path into the lane, so the seat's printed path list is the detection, and `C4_PATTERN_BLIND` is a
  self-reported control with a structural aid, and is labelled so.""","C4 honest")
E_("""  packet is not written and `C4_PACKET_REDACTED=FAIL`**; the study does not proceed on a hand-checked copy.""",
"""  packet is not written and `C4_PACKET_REDACTED=FAIL`**; the study does not proceed on a hand-checked copy. **The
  forbidden list names the pattern's name and topic, the comparison model, gate history, every engine name, every
  person in the custody chain (the lane owner's name included), and every word that signals consequence rather than
  content — expectation, refute, consequential, invisible, favourable, unfavourable, stake, prior, tempting, warn. Build
  command, run from this directory: `/usr/bin/python3 r3c2_build_seat_packet.py`; expected first line of output
  `C4_PACKET_REDACTED=PASS`, then the master and packet digests.**""","C4 forbidden")
E_("`C4_PACKET_REDACTED=PASS`. The seat's declaration and printed path list are kept as\n  secondary detection.","`C4_PACKET_REDACTED=PASS|FAIL|NOT_RUN`. The seat's declaration and printed path list are kept as\n  secondary detection.","C4 packet token")
E_("<!--/SEAT-REDACT-->`C4_PATTERN_BLIND=PASS`.","<!--/SEAT-REDACT-->`C4_PATTERN_BLIND=PASS|FAIL|NOT_RUN`.","C4 blind token")
E_("`C4_PATTERN_BLIND=PASS` requires that printed path list.","`C4_PATTERN_BLIND=PASS` requires that printed path list; any path outside the copy directory is `FAIL`.","C4 seat rule")
E_("expected values fails.** `C5_HARNESS_PINNED=PASS`.","expected values fails.** `C5_HARNESS_PINNED=PASS|FAIL|NOT_RUN`.","C5 token")
E_("`OUT_OF_SCOPE` row fails the control.** `C5B_NO_CROSS_LANE=PASS`.","`OUT_OF_SCOPE` row fails the control.** `C5B_NO_CROSS_LANE=PASS|FAIL|NOT_RUN`.","C5b token")
E_("- **C6 — audit, with a frozen sampling frame.** A third pattern-blind seat","- **C6 — audit, with a frozen sampling frame.** A third independent seat","C6 seat")
E_("""re-classifying every input's `origin` from the pinned sources, and recomputing `rests_on` by the same script**: **(i) every claim whose filed
  outcome asserts that the arithmetic reproduced the number** — the class in which a result unreproduced from the stated inputs is both consequential
  and invisible, so it gets no sampling discount — and **(ii) a sample of `max(1, ceil(0.20 × N))` of the remaining
  included claims**, `N` being the sealed denominator, drawn by
  `random.Random(seed).sample(sorted(claim_ids), k)`.""",
"""re-classifying every input's `origin` from the pinned sources, and recomputing `rests_on` by the pinned script**: **(i) every claim in the arithmetic
  group** — no sampling discount — and **(ii) a sample of `min(max(1, ceil(0.20 × N)), R)` of the remaining included
  claims**, `N` being the sealed denominator and `R` the number of remaining claims (when `R` is zero the sample is empty
  and every included claim is already audited under (i)), drawn by `random.Random(seed_int).sample(remaining_ids, k)`
  where **`remaining_ids = sorted(set(included_ids) − set(arithmetic_group_ids))` and `seed_int = int(seed_hex, 16)`,
  the custodian's seed being 64 lowercase hexadecimal characters**.""","C6 sample")
E_("outside this lane supplies a seed generated independently and unavailable to Tori before that receipt**","outside this lane supplies a seed generated independently and unavailable to the lane before that receipt**","C6 seed custody")
E_("""  *(Seeding from the tally's own digest let the tally's producer reshape non-semantic content — ordering, spacing,
  metadata — until a favourable sample appeared. A seed must not be a function of the thing being audited.)*""",
"""  <!--SEAT-REDACT-->*(Seeding from the tally's own digest let the tally's producer reshape non-semantic content — ordering, spacing,
  metadata — until a favourable sample appeared. A seed must not be a function of the thing being audited.)*<!--/SEAT-REDACT-->""","C6 favourable redacted")
E_("""  `CENSUS_AUDIT_FAILED`. **Classes are cited by name, never by number** — the numbering has shifted twice. `C6_AUDIT_SAMPLE=PASS`.""",
"""  `CENSUS_AUDIT_FAILED`. **A claim whose root-origin set contains an `ORIGIN_DISPUTED` input carries `rests_on` computed
  under both classifications, printed as a pair and marked `DISPUTED`; the `rests_on` tally reports a `DISPUTED` row.**
  **Classes are cited by name, never by number** — the numbering has shifted twice. `C6_AUDIT_SAMPLE=PASS|FAIL|NOT_RUN`.""","C6 disputed + token")
E_("Controls in an unreached limb are `NOT RUN`, never passes.","Controls in an unreached limb are `NOT_RUN`, never passes.","NOT_RUN spelling")
E_("""**What the seal is, and what it is not.** Before the interpretation protocol is opened, Tori commits the tally, then
sends **four digests — tally hash, tally commit id, protocol hash, protocol commit id — to Blanc**, who is outside
this lane and reports to Duho. **The relay is complete only when it is receipted.** Blanc **acknowledges and timestamps the four digests in a
preserved receipt**; the interpretation protocol is **not opened** without that recorded acknowledgement. After
opening, Blanc independently re-hashes the tally and the protocol and verifies both hashes and both commit ids
against the receipt, and **the interpretation report must print the four verified values**. Any mismatch files
`CENSUS_AUDIT_FAILED`, leaves §7 `NOT RUN` and voids the comparison.""",
"""**What the seal is, and what it is not — two receipts.** **(P) Before limb A begins, Tori commits the interpretation
protocol and sends its hash and commit id to Blanc, who is outside this lane and reports to Duho; Blanc acknowledges
and timestamps them in a preserved receipt P; limb A does not begin without receipt P.** **(T) After the tally is
committed and before the protocol is opened, Tori sends the tally hash and tally commit id; Blanc receipts them as T;
the interpretation protocol is not opened without both receipts.** **The relay is complete only when it is receipted.**
After opening, Blanc independently re-hashes the tally and the protocol and verifies all four values against the two
receipts, and **the interpretation report must print both receipts and the four verified values**. Any missing receipt
or mismatch files `CENSUS_AUDIT_FAILED` (§4, whose definition now names this case), leaves the interpretation
`NOT_RUN` and voids the comparison. *(V11: both V10 seats found the single post-tally relay left the protocol in the
lane's own custody while the tally was computed — the exact overclaim §10.2 recorded as repaired at V8 and the operative
text did not contain.)*""","§7 seal")
E_("""Live harness; `ACCESS_SHA` proof for any pinned source audited, verified by Tori after the run and not on the seat's
claim; path lists; 120-second cap on symbolic operations with `SYMBOLIC_TIMEOUT` as a reportable outcome; unreached
controls `NOT RUN`. Blind double, third seat via `nm_referee_dispatch.sh` on a split, Kimi arithmetic with a
no-fallback control, one-page check sheet, Tori re-runs every script, critic note before any ruling.""",
"""Live harness (C5); `ACCESS_SHA` proof for any pinned source audited, verified by the lane owner after the run and not
on the seat's claim; path lists (C5b); 120-second cap on symbolic operations with `SYMBOLIC_TIMEOUT` as a reportable
outcome; unreached controls `NOT_RUN`. Two independent seats; on a split, a third seat dispatched via
`/Users/duhokim/HermesOps/scripts/nm_referee_dispatch.sh` (absolute path; it exists there, not in this directory) with
its `ACCESS_SHA` proof. <!--SEAT-REDACT-->Lane-side procedure, not the seat's: the no-fallback control is the provider log showing
no fallback line for the seat's session, checked by the lane owner; a one-page check sheet `R3C2_CHECK_SHEET_<date>.md`
in plain words with source lines is written by the lane owner after the tally; the lane owner re-runs every script; a
critic note precedes any ruling.<!--/SEAT-REDACT-->""","§9")
m=re.search(r"^\| V10 \| \*this version\* \|.*$",s,re.M); assert m
E_(m.group(0),f"""| V10 | `{OLD[:16]}…` | C0 two blind seats AGREE (`R3C2_C0_EXHIBITION_V10_codex…`, `…kimi…`), then `R3C2_GATE_V10_codex_20260905.md`, `R3C2_GATE_V10_kimi_20260905.md` | C0 PASS+PASS; gate `PREREG_UNSOUND`, `PREREG_SOUND_WITH_REPAIRS` | **option (c) adopted on the ruling; see §10.4; first gate with a settled definition — see §10.5** |
| V11 | *this version* | *(C0 by two independent seats, then two-seat gate — pending)* | — | **both V10 lists applied, leak first; see §10.5** |""","V10/V11 rows")
E_("R3C2_PREREG_V10_OPTION_C_READY_FOR_C0",f"""## 10.5 V11 — the first two-seat gate with a settled definition, reconciled; both lists applied, the leak first ({T})

**Both V10 verdicts bound to `{OLD[:16]}…` and to the packet `e265d3f8…`, both ACCESS and PACKET hashes verified by
the lane owner against the files after each seat exited: codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`.
Both prior R3C2 gates ran against a document with a deliberately open core clause; their verdicts were verdicts on
something else. This is the first gate on the settled design.**

**Q1 — the substantive result of the ruling — came back YES.** codex: under option (c) §3 makes every declared outcome
reachable AND keeps the reproduction question decidable at the per-claim level, the printed-but-chosen `β = 1/929.25`
case traced to exactly one outcome and one `rests_on`. kimi: decidability YES on the same hardest cases; reachability
NO on one class — `REPRO_BLOCKED`'s exclusive domain was empty as written — repaired here by the named-source test.

**The leak, first (Duho 14:31: strip consequence, not just content).** codex from the packet alone: the lane has an
expectation; an unreproduced result is consequential; a favourable audit sample is possible. kimi from the packet
alone: the conclusion rides on `rests_on`; `DERIVED_ONLY` is the clean pole of a graded order; the corpus is cosmology;
the lane has an expectation; a comparison exists. **Applied:** C0's "refute this lane's own expectation" → "every
declared condition"; C6's "consequential and invisible" → "every claim in the arithmetic group"; the "favourable
sample" rationale, the `rests_on` severity order, the "interpretation reads `rests_on`" sentence, the retired-class
note and the origin-dispute rationale all moved into `SEAT-REDACT` spans; every "pattern-blind" in seat-visible text →
"independent"; the packet header no longer says what was removed; "Tori" leaves every seat-visible clause; the
builder's forbidden list gains the custody-chain names, the engine names, `R3D`, and the consequence words, each
asserted by the builder. **Kept, and why it cannot leak:** the wording rule "unreproduced from the stated inputs, not
error" constrains how a seat writes a negative, not whether it finds one; any census implies failures are possible.
**Accepted, and why:** the Planck-2018-only `STANDARD` list tells a seat the corpus is cosmology; so do the sources it
reads; that is content the seat must have, not consequence.

**Applied from both lists (substantive):** §4 total precedence with exactly-one filing (codex's chronological order;
kimi's differed only on the denominator dispute's place); `CENSUS_AUDIT_FAILED` extended to a seal failure (kimi);
every control `PASS|FAIL|NOT_RUN` and `NOT_RUN` spelled once (codex); C0 by two independent seats in the operative
text — the sentence §10.2 said was replaced at V8 and was not (both); C1/C2 machine-validated by the pinned script
(codex); `origin` classified by both seats, reason-code precedence for co-applicable codes, `MEASURED` added (kimi Q2;
codex Q2); referential integrity, acyclicity and "DERIVED needs parents" asserted by the script (kimi 5); disputed roots
carried as a pair (kimi 7); C6 sample formula bounded by `R` and the seed serialised (kimi 8, codex); stated-precision
rule (kimi 11); the two-receipt seal, P before limb A (both — §10.2 said this was applied at V8; it was not); C4
labelled procedural, not enforced, and the dispatch copy's contents listed before launch (codex, kimi obs 5); the
provenance script named, delivered and pinned, the dispatch script's absolute path stated, the corpus pinned by
manifest (both, codex).

**Escalated, the principal's:** codex asks to rename `REPRO_EXACT` to `REPRO_WITHIN_STATED_PRECISION` (kimi: the name
is cosmetic; the missing "report both numbers" is repaired here). A class rename is a redefinition — as with
`DYM_NO_*` in R3D — and is Duho's.

**Recorded, not a design change:** the pinned corpus is 89 enumerable texts, 106,676 non-blank lines. §6's
"2–3 seat-days" for limb B was written before the corpus was pinned and is an estimate, not a rule; the principal
should know the scale before ordering a run.

**Four items §10.2 recorded as "applied" at V8 were not in the operative text at V10** — the C0 assignment, the seal
timing, the three-valued tokens, the study-level precedence. That is the describe-versus-compute law failing in this
lane's own record, and it is stated here rather than absorbed.

**V11 has NOT had its own C0 or gate. R3C2 is NOT frozen and NOT run.**

R3C2_PREREG_V11_READY_FOR_C0""","§10.5")
miss=[(t,s.count(o)) for o,n,t in E if s.count(o)!=1]
if miss: print("DRY-RUN MISSES:",miss); sys.exit(1)
for o,n,t in E: s=s.replace(o,n); print("  -",t)
io.open(p,'w',encoding='utf-8').write(s); print("V11 written")
