# Lana co-author contribution to *The Baseline*

Task: `THE_BASELINE_QUARTET_PRIMITIVE_WRITE_20260703T0738Z` · Lane: Lana (methods/pipeline co-author) · Status: proposed text below, docs-only.
This is my drop-in section for the canonical plan; Hermes integrates. No target files edited. No DB/SQL/deploy/git/secrets.

---

## PROPOSED SECTION — "The Distillation Pipeline: Lanes, Gates, and Method Bindings"

### The primitive, stated as two invariants

> **Papers → claim/status ledger → research-status/debate map → prose → derived claims/evidence/trust.**

1. **Ledger-primary.** The claim/status ledger is the single source of truth. Prose is a *rendering* of the ledger, never the other way round. Every prose sentence binds to ≥1 ledger entry; a sentence that binds to nothing does not ship.
2. **Modality ≤ certainty.** A sentence's *modality* — its verb strength, quantifier, and scope — may never exceed the *certainty* of the ledger entries it renders. "Can, in ~46%" may not be rendered as "does, universally." This is the enforceable form of the whole doctrine.

Everything below operationalizes these two lines.

### The modality ↔ certainty ladder (the enforceable rule)

Each ledger entry carries a certainty tier (GRADE-style; see Lane 5). Prose may only use a modality at or below its entry's tier:

| Ledger certainty tier | Max prose modality | Example rendering |
|---|---|---|
| **Established** (multi-source, consistent, direct; review + observation backbone) | Declarative, general | "AGN feedback heats the circumgalactic gas of massive galaxies." |
| **Widely supported** | Declarative + scope | "commonly drives outflows in massive galaxies" |
| **Emerging / sample-limited** | Modal + quantified scope | "can expel gas, observed in a substantial fraction (~46% of massive z~2 systems)" |
| **Debated / mixed** | Two-sided, attributed | "X reports central-property control; Y finds halo-mass dominance; unresolved" |
| **Contradicted / model-dependent** | Bounded or negative | "not established"; "in simulations only" |
| **No-info / single abstract** | Not renderable | excluded from prose; may appear only as a named open question |

Worked check: claim **2299** (expels) is *emerging* → modality capped at "can, ~46%"; claim **2924** (heats) is *widely supported* → "commonly heats … with scope." The ladder resolves both without ad-hoc argument.

### Pipeline lanes and gates (each gate is a hard pass/fail before advancing)

| Lane | Does | Method binding (see methods survey) | Produces | **Gate to advance** |
|---|---|---|---|---|
| **L0 Ingest & structure** | PDF/HTML → structured sections | GROBID / S2ORC; SciSpaCy; section-aware parse | structured full text | **G0:** full text present; abstract tagged *not* a findings source |
| **L1 Balanced select** | pool → 20–40 shortlist | submodular coverage + MMR over category × stance × epistemic-type × scope | shortlist + PRISMA flow counts | **G1:** category quotas met; every debate axis two-sided; sim share ≤ cap |
| **L2 Sentence & scope extract** | pull findings sentences + scope | argumentative/rhetorical zoning; scope/fraction extraction | scoped candidate sentences | **G2:** each candidate is a result-zone sentence with explicit scope (N, z, mass, fraction) |
| **L3 Claim decompose → ledger** | atomize + scope-qualify; **write the ledger** | claim decomposition; FActScore-style atomicity | **claim/status ledger entries** | **G3:** no non-atomic or unscoped claim enters the ledger (the 2299 fix, enforced) |
| **L4 Verify & stance** | link claim↔source via rationale | SciFact (SUPPORTS/REFUTES/NO-INFO + rationale); SciNLI contradiction | rationale-grounded links | **G4:** every link has a findings-level rationale sentence; zero topical-keyword links |
| **L5 Status/debate map** | aggregate to certainty + debate | GRADE dimensions; consensus-meter; explicit debate axes | per-claim certainty tier + debate map | **G5:** certainty tier assigned from dimensions (not a targeted scalar); counter-evidence retained |
| **L6 Prose render** | ledger + map → prose | STORM perspective outline; OpenScholar grounded generation | reader-facing prose | **G6:** every sentence binds ≥1 ledger entry; modality ≤ its tier (ladder above) |
| **L7 Derive & reconcile** | emit claims/evidence/trust as derived | reconcile back to ledger | derived claims/evidence/trust | **G7:** derived artifacts match ledger; trust = GRADE-derived, never targeted |

### Invariants that must hold at every gate

- **No orphan sentences** — each prose sentence → ≥1 ledger entry (G6).
- **No modality overflow** — sentence modality ≤ its entries' certainty tier (G6, ladder).
- **No topical links** — every claim↔source link carries a findings-level rationale sentence (G4).
- **No filtered counter-evidence** — contradictions are content, retained through L5 (G1, G5).
- **No scalar targeting** — trust is *derived* from GRADE dimensions; it is never an objective to optimize (G5, G7).
- **Reproducible flow** — L0–L1 emit PRISMA-style found→deduped→screened→included counts (G1).

### Why this is safe by construction

Because the ledger is primary and prose is a bounded rendering, the failure modes we hit repeatedly — over-broad sentences (2299), topical/abstract "evidence" (row 30631), a marginal scalar standing in for real certainty (0.324), a fabricated refute setting status (2557) — are each caught at a specific gate (G3, G4, G5, G4) *before* prose exists. Prose can no longer outrun the evidence, because modality is capped at certainty by rule, not by editorial judgment.

---

LANA_BASELINE_COAUTHOR_DONE_20260703T0738Z
