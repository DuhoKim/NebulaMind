HOLD_CAPTION_CORPUS_LEDGER_GAPS_AND_RESIDUAL_GARBLES

Signed: Hermes Agent adversarial gate — engine OpenAI GPT-5.6-sol (openai-codex route).

## Verdict basis

Two independent mandatory claims fail:

1. Four broad `.pre-whisper1` caption mutations have real, retained before/after bytes but no caption-repair event in the 70-line ledger. They are also not classified by evidence kind. This is an edit-without-event HOLD under check 1.
2. The 223-caption corpus still contains many context-confirmed garbles. `GemIIni`, `Blonk`/`Blunk`, `CUN`/`CUNS`, `Goryu`, `Huao`, and others alone refute “zero unidentified garbles.” This is a HOLD under check 4.

The anchor checks, deliberate-mention check, sampled backup chains, and aggressive-short-pattern overcorrection attack otherwise held as detailed below.

## 1. LEDGER-VS-MUTATION COMPLETENESS — HOLD

### Corpus and ledger census

- Root `*.txt`: 225 files; excluding only `latest.txt` and `latest_transcript.txt` gives the brief’s 223-caption population.
- Ledger: 70 valid JSONL events: 16 `caption_corrected`, 4 `caption_glossary_pass`, 42 `publish`, and 8 other custody/publication events.
- `_caption_backup_20260822`: 102 backup files covering 72 distinct captions.
- Every one of the 102 backup files differs from the next stage or current caption.
- Event-backed backup groups reconcile exactly by filename: event 62 = 1 `.pre-retranscribe`; 63 = 11 `.pre-glossary`; 64 = 6 `.pre-glossary2`; 65 = 36 `.pre-glossary3`; 66 = 2 `.pre-source-anchored`; 67 = 40 `.pre-glossary4`; 70 = 2 `.pre-round5`.

### Blocking finding F1 — four unledgered whole-caption changes

The four `.pre-whisper1` backups each isolate a real mutation, but no ledger event contains `pre-whisper1`, names the broad rewrite, or records its before/after pairs:

- `20260811T201833-gemini-dr-verdict.txt.pre-whisper1` → the next `.pre-glossary` stage: examples include `feckened universes` → `Fecund Universes`, `cayon` → `kaon`, and the newly introduced `Gemini` → `GemIIni`; 36 non-equal token opcodes.
- `20260811T215531-spin-split.txt.pre-whisper1` → the next `.pre-glossary2` stage: examples include `Amisotropy` → `Anisotropy`, `quadruple` → `quadrupole`, `galaxy zulane` → `Galaxy Zoo lane`, and `Kun` → `Kuhn`; 24 non-equal token opcodes.
- `20260812T112909-spike-two.txt.pre-whisper1` → the next `.pre-glossary` stage: examples include `resumpling` → `resampling`, `Longdo's` → `Longo's`, `Youi` → `Yui`, and deletion of the whole sentence `Gauru touched no survey label.`; 39 non-equal token opcodes.
- `why-method-only-20260810T1440.txt.pre-whisper1` → current: examples include `lame` → `lane`, `lintot` → `Lintot`, `GANELIZER` → `GANalyzer`, and `DIPOL` → `Dipole`; 22 non-equal token opcodes.

Ledger events 63–67 do record later narrow glossary/source passes on some of these captions, but those later events have their own later backups and declared mappings. They cannot retroactively ledger the preceding wholesale `.pre-whisper1` mutations. `why-method-only-20260810T1440` is not named by any caption-repair event at all.

This also breaks the claim that every repair has an evidence-kind classification: the unledgered rewrites have no ledger authority/class field.

### Required changed-caption sample (13 captions)

Each row compares the named backup to the next stage, not blindly to a later multi-round current file.

| Caption / backup stage | Isolated real diff | Ledger coverage |
|---|---|---|
| `20260820T173007-hwao-report.txt.corrupt-20260821` | three split integers → `2,047`, `60,308`, `208,407` | event 47 |
| `20260820T231235-hwao-report.txt.corrupt-20260821` | three false decimal phrases → full-precision values | event 48 |
| `20260814T160157-variance-pass.txt.corrupt2-20260822` | `800 and 32,000` → `832,000` | event 57 |
| `20260811T211421-tori-fresh-verdict.txt.pre-retranscribe` | whole re-transcription, including restored 12,449-byte/123-line clause | event 62 |
| `20260811T201833-gemini-dr-verdict.txt.pre-whisper1` | broad re-transcription; includes `Gemini` → `GemIIni` | **NO EVENT — HOLD** |
| `20260812T112909-spike-two.txt.pre-whisper1` | broad re-transcription and one sentence deletion | **NO EVENT — HOLD** |
| `20260811T154757-where-and-what.txt.pre-glossary` | four `mital`/`Mital` forms → Mittal | event 63 |
| `20260811T225150-spin-priorart.txt.pre-glossary2` | `Coons` → `Kun's` | event 64 |
| `20260811T143640-kunpass-external.txt.pre-glossary3` | `Koon` → `Kun` | event 65; later distinct `.pre-glossary4` chain covers event 67 |
| `20260811T234955-spin-converge.txt.pre-source-anchored` | `cardi`, `Gia, zoo and pen`, `anti-satripy`, `free access` repaired | event 66; later distinct `.pre-glossary4` covers event 67 |
| `20260811T195847-all-verdicts.txt.pre-glossary4` | `Coon`/`Coon's` → Kun/Kun's | event 67 |
| `20260812T141231-rowcount.txt.pre-round5` | `for Baidam` → `verbatim`; `set-in-all` → `sentinel` | event 70; earlier stages separately chained to 65 and 67 |
| `20260812T004123-overnight-converged.txt.pre-round5` | `Knight's` → `night's` | event 70; earlier `.pre-glossary4` separately covers event 67 |

### Failed attack — no phantom caption-repair event found

Every caption-repair ledger event corresponds to real bytes:

- All 13 legacy numeric/integer events 47–60 have their declared old literal in the named `.corrupt*` original and the declared new literal in current; the old literal is absent after repair.
- Event 62 has a real whole-caption diff.
- Every file named by events 63–67 and 70 has a real isolated stage diff; no event file lacks its corresponding backup.
- Isolated token-opcode totals are exact: event 63 = 15, event 64 = 6, event 65 = 57, event 67 = 79. Event 67’s ledger `count: 79` is therefore real, not asserted.

Non-blocking record discrepancy: `CAPTION_WORDS_20260822.md` lines 86–89 says round four found `Coon ×31`, `Gore ×12`, `Tory ×17`, and `UE ×17`. The isolated `.pre-glossary4` stage actually contains 23 Coon-family, 7 Gore-family, 14 Tory-family, and 12 UE-family replacements (56 short-pattern changes). The ledger’s overall 79 remains correct because the other 23 changes are parity/word/name repairs.

## 2. EVIDENCE-CLASS HONESTY — sampled anchors hold

I opened the cited authored documents, not the repair record alone. Eight repair claims were checked (minimum required: five):

| Repair | Claimed class | Opened anchor and observed text | Result |
|---|---|---|---|
| `cardi` → `party` | SOURCE | `reviews/LANA_SPIN_ANISOTROPY_ENTRY_ASSESSMENT_20260811.md` lines 201–208: “it is one party to the dispute” | holds |
| `Gia, zoo and pen` → `Jia, Zhu & Pen` | SOURCE | same source, lines 206–208: “Jia, Zhu & Pen 2023” | holds |
| `anti-satripy` → `anisotropy` | SOURCE | same source, line 207: “no anisotropy analysis at all” | holds |
| `free access integer scans` → `free-axis integer scans` | SOURCE | same source, line 206: “free-axis integer scans” | holds |
| `F shorty` → `Afshordi` | SOURCE | `reviews/GORU_BHU_INDEPENDENT_LITERATURE_VERDICT_20260811.md` line 11: “Afshordi, Pourhasan, Mann 2014” | holds |
| `multipulse` → `multipole` | SOURCE/technical phrase | same source, line 13: “specific low-ℓ power suppression”; ℓ is the multipole index. The source uses notation rather than spelling the word. | holds, with notation disclosure |
| `for Baidam` → `verbatim` | IDIOM | `prereg/DR11_STEP1_WHAT_CHANGED_20260816.md` line 66: “frozen cuts verbatim”; `prereg/DR10_1_RETAINED_DECISION_20260817.md` line 51: “frozen cuts carried verbatim” | holds |
| `set-in-all` → `sentinel` | SOURCE | `paper/RECORD_SPIN_PROGRAM_20260812.md` lines 251–253: “Photo-z −99 sentinel” | holds |

`the night's decider` is classified correctly, not laundered into a source claim. Ledger event 70 says exactly: `night's: CONTEXT-STRONG, NOT SOURCE-ANCHORED`; `CAPTION_WORDS_20260822.md` lines 120–124 repeats that it is context-strong, not source-anchored; Hwao’s candidate note lines 51–57 calls it a medium-confidence phrasing reconstruction with no frozen phrase.

## 3. MENTION PRESERVATION — holds

`20260822T142239-tori-report.txt` still contains the deliberate quotation exactly:

> It read "brownly and rose-owned" for Brown and Rho, and "cayon condensation" for kaon condensation.

Corpus-wide counts are two occurrences apiece: once in the caption and once in its `.spoken.txt` companion. Both are mention/use-correct. None of the three forms was substituted away, and the caption is not listed in any glossary/substitution event. This attack failed.

## 4. THE ZERO CLAIM, INDEPENDENTLY ATTACKED — HOLD

### Method

I did not rerun the repairers’ known-form scans. I tokenized all 223 root captions, checked tokens against macOS `/usr/share/dict/words`, applied only mechanical inflection/possessive/hyphen normalization, then attacked:

- OOV tokens close to the known crew/author/term list;
- malformed merged tokens in otherwise grammatical sentences;
- capitalized/voice/name tokens whose nearby caption context identifies the intended referent;
- the outputs produced between each `.pre-whisper1` backup and the next stage.

The lexical pass produced 429 raw OOV types. Ordinary acronyms, valid technical terms, names, and transparent compounds were rejected rather than called garbles. Every promoted candidate family is listed below with context. The first rows alone are confirmed non-word/name garbles and settle the HOLD.

### Context-confirmed residual name/term garbles

| Candidate (corpus hits) | Context evidence | Assessment |
|---|---|---|
| `Blonk` / `Blunk` (4) | `20260819T190426-blanc-report.txt`: “Blonk here”; three other `*-blanc-report`/Blanc voice captions say “Blunk here” | **confirmed Blanc garble** |
| `GemIIni` / `GemIIni's` (5) | `20260811T201833-gemini-dr-verdict.txt`: “GemIIni's deep research finished” | **confirmed Gemini garble; introduced by unledgered whisper-1 rewrite** |
| `CUN` / `CUN's` / `CUNS` (16) | `kunpass-20260811T1425.txt`: “CUN passed it”; `lana-repair`: “CUN's exact wording” | **confirmed Kun garble** |
| `Garu` / `Goryu` (5) | `catchup`: “numbers to Goryu that Goryu never supplied”; `torirelease`: “Garu effects artifact” | **confirmed Goru garble** |
| `Huao` (2) | corrected-voice reports: “Huao speaks as shimmer” | **confirmed Hwao garble** |
| `Mattal` / `Mittle` (5) | “Mattal used”; “Mittle not bite self-binding” in Mittal/Singal method captions | **confirmed Mittal garble** |
| `Torrey` (2) | `gemini-dr-verdict`: “once Torrey verifies it” | **confirmed Tori garble** |
| `Mova` (1) | Blanc voice report: “Tori is Mova”; the same voice series and ledger identify Tori’s voice as Nova | **confirmed Nova garble** |
| `Koya` (4) plus `Quaya`/`Quia`/`Kuea`/`Klaya` (9) | “binding Koya and Catwise”; “Quaya is the Gaia Unwise Quasar Catalog”; “Kuea version 0.1.0” | **confirmed Quaia garble family** |
| `Abgari` / `Abgari-style` (2) | “Abgari's ecliptic leakage”; local authored source names Abghari | **confirmed Abghari garble** |
| `Seacrest` (3) | “Seacrest et al. on Catwise”; local authored sources consistently say Secrest | **confirmed real-surname substitution; floor-caveat class** |
| `Poplaski's` / `Poplowski's` / `Poploski's` (4) | torsion-cosmology contexts; authored records use Poplawski | **confirmed Poplawski garble** |
| `Dimnakova` (1) | “dimnakova style vacuum bubble work” | **confirmed Dymnikova garble** |
| `Fralev` (1) | “Fralev, Markov, and Mucanov” | **confirmed Frolov garble** |
| `Mucanov` / `McConov` (2) | same BHU author list | author-name garble candidate; intended local spelling is not consistently preserved |
| `Ganilizer` / `Gannalizer's` (2) | “deterministic ganilizer”; “Gannalizer's strict geometric tracing” | **confirmed Ganalyzer garble** |
| `Longvos` (1) | “coverage near Longvos axis” | **confirmed Longo's garble** |
| `Lindtok` / `Linta` (2) | “Lindtok 2011 and Land 2008”; “Linta and land are procedural” | **confirmed Lintott garble** |
| `Singdong` / `Singdahl's` / `Singdala` (4) | “Singdahl's magnitude cuts”; “middle versus Singdala” | **confirmed Singal garble** |
| `Geazhu and Penn` (1) | `spin-priorart`: “Geazhu and Penn 2023 built CE ResNet”; authored source says Jia, Zhu & Pen | **confirmed missed source-anchor garble** |
| `Pathary` (1) | “Pathary is original 1972 paper” | **confirmed Pathria garble** |
| `NoiLab` (1) | “NoiLab Astro Data Lab endpoint” | **confirmed NOIRLab garble** |
| `Olama` (1) | “model loaded in Olama” | **confirmed Ollama garble** |
| `Pandock` / `Pandox` / possessives (7) | “Pandox markdown reader”; “replaced it with pandock” | **confirmed Pandoc garble** |
| `Panstars` (1) | “PanStars offers anonymous FITS cutouts” | Pan-STARRS term candidate; orthographic rather than semantic risk |
| `Eason` (2) | BHU author context “Eason and Brandenburger”; local repair record names Easson | author-name candidate |
| `Arreza` (1) | “Phil Cox and Arreza, in the Philosophical Transactions…” | unresolved proper-name candidate; source name not established in this gate |
| `Lefsky` (1) | “For Lefsky and colleagues state they agree…” | unresolved proper-name candidate |

### Context-confirmed malformed/OOV garbles

| Candidate | Context evidence | Assessment |
|---|---|---|
| `atticked` | “dead code atticked, 346 stale files swept” | malformed; intended word unresolved |
| `clob` | “several codecs clob per model … named fields” | malformed/abbreviation candidate; intended phrase unresolved |
| `Conheld` | “Conheld version 2” | likely merged “Kun held”; confirmed malformed |
| `Consverte` | “Consverte has been sitting on disks…” | likely “Kun's verdict”; confirmed malformed |
| `contigate` | “for Lana to freeze and contigate” | confirmed malformed; intended phrase unresolved |
| `condating` | “Lana writing it and condating it” | confirmed malformed |
| `conjates` + `redrass` | “until Lana redrass from her record set and conjates it” | two confirmed malformed tokens |
| `crawn` | “Crawn rather than watchers” | confirmed `cron` garble |
| `difked` | “difked the 2 storyboards” | confirmed `diffed` garble |
| `gation` | “swallowed in a gation” | confirmed malformed; intended word unresolved |
| `heelpicks` | “Heelpicks templates at N64” | confirmed HEALPix garble |
| `Kunenguru` | “Lana Kunenguru are working … in parallel” | confirmed merged “Kun and Goru” garble |
| `non-afforetative` / `non-authorative` | “artifact is marked non-afforetative”; “my non-authorative artifact” | confirmed non-authoritative garbles |
| `rediriving` / `reduriving` / `redurizing` / `rederevation` / `redirived` | “does not reduce to rediriving”; “a rederevation”; “her redirived decision band” | confirmed rederive/rederivation garble family |
| `slawless` | “he called it slawless” | malformed; likely “flawless” |
| `Smallins` | “Smallins' 92 paper” | confirmed Smolin's garble |
| `Torxian` | “Torxian derived work” | confirmed torsion garble |
| `verusai` | “On the verusai markers, 13 became 11” | malformed; intended term unresolved |
| `Westerday` (2) | “Everything else from Westerday stands” | confirmed yesterday garble |
| `zulane` | “the galaxy zulane” | confirmed Zoo-lane garble |
| `kint` | “created on the 8th kint of December” | confirmed malformed date phrase |
| `asseine` | “detect the asseine branch because a frame convention is … relabeling” | likely axis/sign phrase; confirmed malformed |
| `concard` | “The moonshot concard, fresh live meter” | likely “Kun card”; confirmed malformed |
| `cre-registration` | “the cre-registration has to be tight” | confirmed pre-registration garble |
| `curratus` / `curradius` | “a curratus correction to the standard cosmological metric”; “metric containing the curradius” | confirmed curvature-family garbles |
| `D-doop` | “the moonshot D-doop” | likely dedupe; malformed candidate |
| `Fesk` | “technical words … things like Fesk, and MZR anchor” | likely FESC lane garble; acronym candidate |
| `gnall` | “correction to the kinematic gnall” | confirmed kinematic-null garble |
| `mael` | “the kinematic mael statement” | malformed; likely model/null phrase |
| `Nodo` | “a Nodo record 8060755” | confirmed Zenodo garble |
| `relabling` | “Relabling it as one…” | confirmed relabeling garble |
| `reshone` | “a sample was reshone mirrored” | malformed; intended word unresolved |
| `salantin` | “heart lap, Salantin heavens, shrinkage…” | malformed phrase candidate; intended technical term unresolved |
| `supram` / `hyper-superim` | “Hyper supram cam”; “Hyper-superim cam” | confirmed Hyper Suprime-Cam garbles |
| `Tantan` | “Tantan Projection World Coordinate System” | confirmed TAN-projection garble |
| `Waikun` | “Waikun called the dominant systematic…” | confirmed merged “why Kun”/Kun garble |
| `mocksweets` (2) | “published mocksweets”; “are the mocksweets released…” | confirmed mock-suites garble |
| `Fitzrow` | “whether the Fitzrow order convention silently flips it” | confirmed FITS-row garble |

### Borderline/real-word candidates covered by the record’s floor caveat

These are findings, not independent HOLD triggers, because they are real surnames/acronyms/compounds even though context strongly points elsewhere:

- `Kuhn`/`Kohn`/`Kahn` (29 hits): e.g. “Kuhn blocked Lana's first repair”; crew context points to Kun, but each surface form is a real surname or valid name.
- `UI`/`UI's`/`UIs` (3): e.g. “Ui is re-measuring the sorter”; context points to Yui, but UI is a real acronym.
- `unmeared` and de-/un-mirror spelling variants (10): e.g. “main unmeared columns”; likely unmirrored, but some de-mirror compounds may be intentional technical coinages.
- `skyrun` (4): e.g. “No empirical skyrun yet”; could be an intentional compound for “sky run.”
- `flaggate` (2): e.g. “mandatory quality flaggate”; could be a fused local term for “flag gate.”

Deliberate mentions were rejected rather than counted as residual uses: `brownly`, `rose-owned`, `cayon`, `cardi`, `shorty`, and `Baidam` occur in later captions that explicitly quote the old garble and name its repair.

## 5. REVERSIBILITY — sampled chains hold; ledger gap remains separate

Six repaired captions were stage-compared (minimum required: five):

1. `20260811T154757-where-and-what`: `.pre-glossary` → current changes only four Mital spellings, matching event 63.
2. `20260811T225150-spin-priorart`: `.pre-glossary2` → current changes only `Coons` → `Kun's`, matching event 64.
3. `20260811T143640-kunpass-external`: `.pre-glossary3` → `.pre-glossary4` is only `Koon` → `Kun` (event 65); `.pre-glossary4` → current is only two Tory→Tori plus Coon→Kun (event 67).
4. `20260811T234955-spin-converge`: `.pre-source-anchored` → `.pre-glossary4` is exactly the five source repairs in that caption (event 66); `.pre-glossary4` → current is only Coon→Kun (event 67).
5. `20260812T141231-rowcount`: `.pre-glossary3` → `.pre-glossary4` is Gora→Goru (event 65); `.pre-glossary4` → `.pre-round5` is two gores→Goru's plus UE's→Yui's (event 67); `.pre-round5` → current is verbatim/sentinel (event 70).
6. `20260812T004123-overnight-converged`: `.pre-glossary4` → `.pre-round5` is two Gore's→Goru's (event 67); `.pre-round5` → current is Knight's→night's (event 70).

Backup custody facts across all 102 files:

- 102 unique paths and 102 unique SHA-256 values.
- Every backup differs from its next stage/current target.
- For all 102 files, filesystem birth time and mtime differ by at most 0.00034 seconds; none shows a later rewrite timestamp.
- Multi-round sample mtimes are monotonic and use distinct suffixes/hashes (e.g. rowcount `.pre-glossary3` 20:18 → `.pre-glossary4` 20:28 → `.pre-round5` 20:58).

No sampled backup was overwritten in place; later rounds created a new, explicitly chained backup. The four `.pre-whisper1` originals also exist and are reversible at the byte level, but their mutations are not reversible *through the ledger* because F1 has no event.

## 6. OVERCORRECTION SWEEP — attack failed on the actual round-four bytes

I isolated event 67 as `.pre-glossary4` → next stage/current and enumerated every one of its 79 token opcodes. There were no hidden substring merges. The aggressive short-pattern population was 56 changes:

- Coon family: 23 (`Coon` 15, `Coon's` 7, lowercase `coon` 1)
- Gore family: 7 (`Gore's` 5, `gores` 2)
- Tory family: 14 (`Tory` 11, `Tory's` 3)
- UE family: 12 (`UE` 6, `UE's` 5, `Ue` 1)

All 56 original contexts were inspected. None plausibly used the ordinary English/political/biological meaning:

- Tory examples all perform Tori’s lane actions: “dispatched Tory,” “Tory holds the evidence,” “Tory bound the route.”
- Coon examples all perform Kun’s gate actions or take Kun possessives: “Coon regates,” “Coon's requirements,” “Coon found…”.
- Gore examples all take Goru’s review/cut ownership: “Gore's independent sweep,” “Gore's frozen cuts,” “gores still omits.”
- UE examples all take Yui’s work/possessives: “UE is rebuilding,” “UE's measured retention,” “UE has it.”

Current-corpus embedded-token check found zero non-exact tokens containing `Yui` or `Goru`; the event-67 diff inventory contains no replacement other than the 22 declared mapping families. The pre-existing `Waikun`, `Kunenguru`, `kung`, and `Kungate's` are residual-garble candidates, not round-four merges.

## UNVERIFIED-AT-GATE

- No audio was replayed and no fresh ASR was run. This gate attacks text custody, source anchors, lexical residue, and backup chains only.
- The 429 raw OOV types were mechanically screened, but not every ordinary acronym, inflection, proper noun, or scientific coinage was opened against audio. Only candidates promoted by broken context/name proximity are listed above. Because multiple confirmed residual garbles already refute zero, deeper audio adjudication cannot change this verdict.
- No served HTML/page rebuild was inspected; the brief scoped the caption corpus, ledger, backups, and repair records.
- Historical immutability before each backup’s current filesystem birth time cannot be proven from present bytes alone. Present metadata shows no later overwrite of any backup.

## Evidence and custody ledger

Content-read inputs:

- all 223 root captions by local token/diff scripts; individual context reads include every candidate quoted above;
- `queue_ledger.jsonl` (all 70 JSON events parsed);
- all 102 `_caption_backup_20260822` files plus all 13 root `.txt.corrupt*` originals;
- `CAPTION_CORRUPTION_20260821.md`, `CAPTION_WORDS_20260822.md`, `HWAO_CANDIDATES_ROUND5_20260822.md`;
- source anchors: `LANA_SPIN_ANISOTROPY_ENTRY_ASSESSMENT_20260811.md`, `GORU_BHU_INDEPENDENT_LITERATURE_VERDICT_20260811.md`, `RECORD_SPIN_PROGRAM_20260812.md`, `DR11_STEP1_WHAT_CHANGED_20260816.md`, `DR10_1_RETAINED_DECISION_20260817.md`;
- the gate kickoff and the deliberate-mention caption.

Local-only analyses: JSON parse/count reconciliation; stage-aware `difflib` token opcodes; literal before/after checks; SHA-256 and filesystem birth/mtime checks; `/usr/share/dict/words` lexical census; contextual near-name/term review. One analysis wrapper invocation failed on a local Python quoting syntax error before accessing or mutating target files; it had no side effect.

No network calls were made. No caption, ledger, backup, repair record, source anchor, or served page was edited.
