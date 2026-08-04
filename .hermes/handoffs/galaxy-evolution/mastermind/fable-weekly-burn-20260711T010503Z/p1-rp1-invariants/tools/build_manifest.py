#!/usr/bin/env python3
"""Build INVARIANT_MANIFEST.json from the cycle-5 snapshot and cross-check cycles 6/7.

Part of FABLE_BURN_P1 (marker HWAO_FABLE_BURN_P1_BRIEF_20260711T010503Z).
Reads ONLY from p1-rp1-invariants/sources-snapshot/; writes ONLY into p1-rp1-invariants/.
"""
import json, re, hashlib, sys
from pathlib import Path

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p1-rp1-invariants")
SNAP = ROOT / "sources-snapshot"
CAND = SNAP / "candidates"
FLAG_REL = "flagship_rp1/aastex/rp1_flagship_polished.tex"
SUPP_REL = "supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex"

def read_lines(cycle, rel):
    return (CAND / f"cycle_{cycle}_package" / rel).read_text().split("\n")

def num_pattern(s):
    return re.compile(r"(?<![\d.,])" + re.escape(s) + r"(?![\d.,])")

def find_hits(lines, mode, s):
    """Return list of (1-based line, count-in-line)."""
    hits = []
    if mode == "sub":
        for i, ln in enumerate(lines):
            c = ln.count(s)
            if c:
                hits.append((i + 1, c))
    else:
        pat = num_pattern(s)
        for i, ln in enumerate(lines):
            c = len(pat.findall(ln))
            if c:
                hits.append((i + 1, c))
    return hits

# ---------------------------------------------------------------- scalar spec
# (id, doc, kind, mode, string, context, extra-dict-or-None)
S = []
def add(doc, id_, kind, mode, s, ctx, **extra):
    S.append(dict(id=id_, doc=doc, kind=kind, mode=mode, s=s, ctx=ctx, extra=extra or {}))

F, P = "flagship", "supplement"

add(F, "FLG-60000", "count", "sub", "60,000", "fixed 60,000-galaxy optical-emission-line cache / 60,000-row cache / 60,000-galaxy subset")
add(F, "FLG-8146", "count", "sub", "8,146", "matched pairs; broad optical BPT-selected targets; 8,146 of 8,146 matched")
add(F, "FLG-8146-BRACED", "count", "sub", "8{,}146", "N=8{,}146 pairs (figure caption LaTeX form)")
add(F, "FLG-MEDIAN-OFFSET", "point_estimate", "sub", "-1.309", "median Delta log sSFR (target minus matched control), dex",
    artifact_full_precision=-1.3088869999999995, artifact_field="matched_delta_log_sSFR_median_dex")
add(F, "FLG-CI95", "ci_interval", "sub", "[-1.334,-1.283]", "bootstrap 95% confidence interval on the median offset, dex",
    components=["-1.334", "-1.283"],
    artifact_full_precision=[-1.3341385500000003, -1.2821399375],
    artifact_field="matched_delta_log_sSFR_median_ci95_bootstrap",
    rounding_anomaly=True,
    note="AUDIT-CANONICAL STRING. Upper bound -1.283 does NOT equal nearest-rounding of the raw artifact value -1.2821399375 (nearest = -1.282). Carry -1.283 verbatim; do not re-derive. See RCA_NUMERIC_DRIFT.md.")
add(F, "FLG-CI-LEVEL", "percent", "sub", r"95\%", "bootstrap confidence level (95%)")
add(F, "FLG-PARENT", "count", "sub", "249,917", "strict four-line S/N>=3 eligible parent count")
add(F, "FLG-COVERAGE", "percent", "sub", r"24.0\%", "cache coverage of strict parent (selection-context diagnostic)")
add(F, "FLG-ZRANGE", "redshift_range", "sub", "0.02<z<0.12", "sample redshift restriction")
add(F, "FLG-KPC", "physical_range", "sub", "1.2--6.5", "kpc subtended by the 3-arcsec fiber over the redshift interval")
add(F, "FLG-FIBER", "aperture", "sub", "3-arcsec", "SDSS fiber aperture")
add(F, "FLG-SNCUT", "threshold", "sub", r"S/N$\geq3$", "four-line signal-to-noise cut")
add(F, "FLG-SF", "count", "sub", "39,553", "star-forming galaxies in the analysis denominator",
    artifact_full_precision=39553, artifact_field="bpt_counts.star-forming")
add(F, "FLG-COMP", "count", "sub", "12,234", "intermediate/composite galaxies in the denominator",
    artifact_full_precision=12234, artifact_field="bpt_counts.intermediate")
add(F, "FLG-UNCLASS", "count", "num", "67", "unclassified objects retained in denominator counts",
    artifact_full_precision=67, artifact_field="bpt_counts.unclassified")
add(F, "FLG-COVERAGE-PCT", "percent", "sub", r"100\%", "target coverage (8,146 of 8,146 targets matched)")
add(F, "FLG-SEP-LOGM", "dex", "sub", "0.0045", "median absolute matching separation in log M*",
    artifact_full_precision=0.0044599999999999085, artifact_field="match_abs_delta_logM_median")
add(F, "FLG-SEP-Z", "other", "sub", "0.00021", "median absolute matching separation in redshift",
    artifact_full_precision=0.00021079499999999973, artifact_field="match_abs_delta_z_median")
add(F, "FLG-OIII", "wavelength_identifier", "sub", r"\lambda5007", "[O III] 5007 emission line")
add(F, "FLG-NII", "wavelength_identifier", "sub", r"\lambda6584", "[N II] 6584 emission line")
add(F, "FLG-RUNID", "run_identifier", "sub", r"SDSS\_AGN\_SFR\_PILOT\_20260708T122000Z", "custody run family for the flagship result")
add(F, "FLG-DR17", "release_identifier", "sub", "DR17", "SDSS data release 17")

add(P, "SUP-60000", "count", "sub", "60,000", "shared 60,000-galaxy / 60,000-row selection-limited cache")
add(P, "SUP-8146", "count", "sub", "8,146", "flagship matched-pair file row count")
add(P, "SUP-PARENT", "count", "sub", "249,917", "strict four-line S/N>=3 parent count")
add(P, "SUP-COVERAGE", "percent", "sub", r"24.0\%", "contextual cache coverage of strict parent")
add(P, "SUP-SNCUT-A", "threshold", "sub", r"S/N$\geq3$", "four-line S/N cut (abstract / shared-limitations form)")
add(P, "SUP-SNCUT-B", "threshold", "sub", r"S/N$\geq$3", "S/N cut (mass-bin subsection spacing variant)")
add(P, "SUP-ZRANGE", "redshift_range", "sub", "0.02<z<0.12", "sample redshift restriction")
add(P, "SUP-FCOLL", "aperture", "sub", "55-arcsec", "SDSS fiber-collision angular limit")
add(P, "SUP-FIBER", "aperture", "sub", "3-arcsec", "SDSS fiber aperture")
add(P, "SUP-NEIGHBOR-ORD", "method_parameter", "sub", "10th", "10th-neighbor projected rank index")
add(P, "SUP-ENV-HI", "fraction", "sub", "0.230", "high-index-quartile low-sSFR emission-line fraction")
add(P, "SUP-ENV-HI-RATIO", "fraction", "sub", "3,456/15,000", "high-index quartile count ratio")
add(P, "SUP-ENV-LO", "fraction", "sub", "0.181", "low-index-quartile low-sSFR emission-line fraction")
add(P, "SUP-ENV-LO-RATIO", "fraction", "sub", "2,710/15,000", "low-index quartile count ratio")
add(P, "SUP-ENV-CI", "ci_interval", "sub", "[0.041, 0.059]", "bootstrap high-minus-low interval (environment baseline)")
add(P, "SUP-ENV-COEF", "point_estimate", "sub", "0.032 +/- 0.004", "high-index linear-probability coefficient at fixed mass/redshift")
add(P, "SUP-ENV-PP", "percent", "num", "3.2", "approximate percentage-point increase in low-sSFR incidence")
add(P, "SUP-15000", "count", "sub", "15,000", "galaxies per neighbor-index quartile")
add(P, "SUP-MASSCUT", "threshold", "num", "10.8", "massive-subset cut log M* >= 10.8")
add(P, "SUP-MASSIVE-N", "count", "sub", "9,298", "massive emission-line galaxies (log M* >= 10.8)")
add(P, "SUP-MASSIVE-LOWSSFR-N", "count", "sub", "5,695", "low-sSFR objects within the massive subset")
add(P, "SUP-BPT-FRAC-MASSIVE", "fraction", "sub", "0.430", "broad optical BPT-selected fraction in the massive subset (also appears as a sim-vector cell value)")
add(P, "SUP-BPT-FRAC-MASSIVE-LOWSSFR", "fraction", "sub", "0.607", "broad optical BPT-selected fraction among massive low-sSFR objects")
add(P, "SUP-HIEXC-N", "count", "sub", "4,440", "high-excitation broad optical BPT-selected candidates")
add(P, "SUP-HIEXC-FRAC", "fraction", "sub", "0.074", "high-excitation candidate fraction of 60,000")
add(P, "SUP-HIEXC-SSFR", "dex", "sub", "-11.53", "median log sSFR of high-excitation subset")
add(P, "SUP-FULL-SSFR", "dex", "sub", "-10.14", "median log sSFR of full denominator")
add(P, "SUP-JET-HI", "fraction", "sub", "0.509", "high-index-quartile broad optical BPT-selected fraction (massive hosts)")
add(P, "SUP-JET-LO", "fraction", "sub", "0.367", "low-index-quartile broad optical BPT-selected fraction (massive hosts)")
add(P, "SUP-JET-CI", "ci_interval", "sub", "[0.112, 0.170]", "bootstrap high-minus-low interval (radio-jet environment baseline)")
add(P, "SUP-MASSBIN-INT", "range", "sub", "[11.0,12.5]", "first stellar-mass bin with low-sSFR fraction above 0.5")
add(P, "SUP-MASSBIN-DASH", "range", "sub", "11.0--12.5", "11.0--12.5 stellar-mass bin (prose and table rows)")
add(P, "SUP-BPT-PEAK", "fraction", "sub", "0.520", "broad optical BPT-selected incidence peak in the 11.0--12.5 bin (also the upper end of the 0.003-0.520 span)")
add(P, "SUP-HALF", "threshold", "num", "0.5", "low-sSFR fraction threshold defining the transition bin")
add(P, "SUP-TRACER-LO", "fraction", "sub", "0.136", "narrowest tracer prevalence")
add(P, "SUP-TRACER-HI", "fraction", "sub", "0.418", "widest tracer prevalence")
add(P, "SUP-TRACER-RATIO", "ratio", "num", "3.1", "widest-to-narrowest prevalence ratio")
add(P, "SUP-GAS-N", "count", "sub", "6,729", "massive low-sSFR gas-depletion denominator")
add(P, "SUP-GAS-BPT", "fraction", "sub", "0.549", "broad optical BPT-selected fraction of gas-depletion denominator")
add(P, "SUP-GAS-LHA", "luminosity", "sub", "40.061", "median log L_Halpha proxy (erg/s)")
add(P, "SUP-GAS-DEX", "dex", "num", "0.66", "H-alpha proxy offset vs massive star-forming galaxies, dex")
add(P, "SUP-SPAN-QUENCH", "range", "sub", "0.005-0.729", "low-sSFR fraction span across mass bins (artifact-anchored)",
    artifact_full_precision=[0.005283204324855633, 0.7292338209769402],
    artifact_field="m3_p3 quenched_fraction_range",
    note="Anchored to the m3_p3 artifact result bullet 'Across mass bins ... span 0.005-0.729'. Cycle 6 replaced this with a table-derived span 0.001-0.856; see RCA.")
add(P, "SUP-SPAN-BPT", "range", "sub", "0.003-0.520", "broad optical BPT-selected fraction span across mass bins (artifact-anchored)",
    artifact_full_precision=[0.0027030347708563705, 0.5202082816761716],
    artifact_field="m3_p3 agn_fraction_range",
    note="Anchored to the m3_p3 artifact result bullet. Cycle 6 replaced this with a table-derived span 0.001-0.610; see RCA.")
add(P, "SUP-CELLS", "count", "num", "15", "mass-redshift cells in the simulation target vector")
add(P, "SUP-CELL-MIN", "threshold", "num", "50", "minimum cell occupancy n >= 50")
add(P, "SUP-60K", "count", "sub", "60k", "shorthand for the 60,000-galaxy sample (atlas summary row)")
add(P, "SUP-RUNID-TOPICS", "run_identifier", "sub", r"SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z", "custody run family for the eight topic artifacts")
add(P, "SUP-RUNID-PILOT", "run_identifier", "sub", r"SDSS\_AGN\_SFR\_PILOT\_20260708T122000Z", "custody run family for the flagship result")
add(P, "SUP-SHA-RESULTS", "sha256", "sub", "668ad7a67290600ff5028ae587d32ef239a09bd8627a480539f37e1927d659df", "SHA-256 of flagship analysis_results.json (provenance tablecomments)")
add(P, "SUP-SHA-PAIRS", "sha256", "sub", "4ea53af867cccccb2b68b81557ff84fe90ec3f13e0512ffbdc977fa7216996fd", "SHA-256 of matched_agn_sf_pairs.csv (provenance tablecomments)")
add(P, "SUP-DR17", "release_identifier", "sub", "DR17", "SDSS data release 17")

TABLE_ROWS = {
    F: [(57, "preferred matched-control result row (Table 1)")],
    P: (
        [(n, "custody provenance-map row (Table 1)") for n in range(39, 47)]
        + [(n, "atlas summary row (Table 2)") for n in range(59, 67)]
        + [(n, "simulation target-vector row (Table 4)") for n in range(176, 191)]
    ),
}

DOC_REL = {F: FLAG_REL, P: SUPP_REL}

# ---------------------------------------------------------------- build
c5 = {d: read_lines("05", DOC_REL[d]) for d in (F, P)}
c6 = {d: read_lines("06", DOC_REL[d]) for d in (F, P)}
c7 = {d: read_lines("07", DOC_REL[d]) for d in (F, P)}

entries, problems = [], []
for spec in S:
    doc = spec["doc"]
    hits = find_hits(c5[doc], spec["mode"], spec["s"])
    if not hits:
        problems.append(f"NOT FOUND in cycle 5 {doc}: {spec['id']} {spec['s']!r}")
        continue
    e = {
        "id": spec["id"],
        "file": DOC_REL[doc],
        "line": hits[0][0],
        "exact_string": spec["s"],
        "kind": spec["kind"],
        "allowed_context": spec["ctx"],
        "match_mode": "substring" if spec["mode"] == "sub" else "numeric_token",
        "lines": [h[0] for h in hits],
        "occurrences_expected": sum(c for _, c in hits),
    }
    e.update(spec["extra"])
    entries.append(e)

for doc, rows in TABLE_ROWS.items():
    for lineno, ctx in rows:
        text = c5[doc][lineno - 1]
        if "&" not in text:
            problems.append(f"ROW {doc}:{lineno} does not look like a table row: {text[:60]!r}")
            continue
        entries.append({
            "id": f"{'FLG' if doc == F else 'SUP'}-ROW-{lineno:03d}",
            "file": DOC_REL[doc],
            "line": lineno,
            "exact_string": text,
            "kind": "table_row",
            "allowed_context": ctx,
            "match_mode": "substring",
            "lines": [lineno],
            "occurrences_expected": 1,
        })

# ---------------------------------------------------------------- cross-check 6/7
def count_all(lines, mode, s):
    return sum(c for _, c in find_hits(lines, mode, s))

drift_report = []
for e in entries:
    doc = F if e["file"] == FLAG_REL else P
    mode = "sub" if e["match_mode"] == "substring" else "num"
    n5 = e["occurrences_expected"]
    n6 = count_all(c6[doc], mode, e["exact_string"])
    n7 = count_all(c7[doc], mode, e["exact_string"])
    if n6 != n5 or n7 != n5:
        drift_report.append({"id": e["id"], "file": e["file"], "line": e["line"],
                             "exact_string": e["exact_string"][:90],
                             "count_c5": n5, "count_c6": n6, "count_c7": n7})

VARIANTS = ["[-1.334,-1.282]", "-1.282", "-1.283", "2.831", "2.830",
            "0.001-0.856", "0.001-0.610", "0.005-0.729", "0.003-0.520",
            "Across the displayed table", "Across mass bins",
            "4,239", "2,731", "1,508"]
variant_scan = {}
for doc in (F, P):
    for cyc, lines in (("c5", c5[doc]), ("c6", c6[doc]), ("c7", c7[doc])):
        for v in VARIANTS:
            n = count_all(lines, "sub", v)
            if n:
                variant_scan.setdefault(v, {}).setdefault(doc, {})[cyc] = n

# new numeric tokens in c6/c7 (bib lines excluded)
tok = re.compile(r"\d[\d,]*(?:\.\d+)?")
def tokens(lines):
    out = set()
    for ln in lines:
        if ln.lstrip().startswith(r"\bibitem"):
            continue
        out.update(tok.findall(ln))
    return out
new_tokens = {}
for doc in (F, P):
    base = tokens(c5[doc])
    for cyc, lines in (("c6", c6[doc]), ("c7", c7[doc])):
        new = sorted(tokens(lines) - base)
        if new:
            new_tokens[f"{doc}-{cyc}"] = new

# ---------------------------------------------------------------- snapshot hashes
snapshot_sha = {}
for p in sorted(SNAP.rglob("*")):
    if p.is_file():
        snapshot_sha[str(p.relative_to(SNAP))] = hashlib.sha256(p.read_bytes()).hexdigest()

manifest = {
    "marker": "FABLE_BURN_P1_INVARIANT_MANIFEST_20260711T010503Z",
    "generated_utc": sys.argv[1] if len(sys.argv) > 1 else "unknown",
    "generated_by": "Fable burn lane A (P1), pane %184, brief HWAO_FABLE_BURN_P1_BRIEF_20260711T010503Z",
    "base_package": "candidates/cycle_05_package",
    "base_package_abs": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_05_package",
    "base_files": {"flagship": FLAG_REL, "supplement": SUPP_REL},
    "audit_reference": {
        "cycle_05_audit": "candidates/cycle_05_package/CYCLE_05_tables_figures_AUDIT.json",
        "cycle_05_numeric_invariants_missing": [],
        "note": "Cycle 5 is the last package with empty integrity_blockers; its strings are the audit-canonical carry targets.",
    },
    "check_rule": (
        "A candidate rewrite of a base file PASSES this manifest iff, for every entry with that file: "
        "(1) the candidate contains exact_string at least occurrences_expected times "
        "(substring match for match_mode=substring; for match_mode=numeric_token, match exact_string only where "
        "not adjacent to another digit, comma or dot); and "
        "(2) no near-miss variant of a ci_interval / point_estimate / fraction / table_row entry appears "
        "(same context, different digits). Line numbers are cycle-5 anchors for humans; matching is line-independent. "
        "Numbers are carried character-for-character from the base package; any intentional numeric change must be "
        "declared out-of-band and this manifest regenerated."
    ),
    "exclusions": [
        "citation metadata: years, volumes, pages, DOIs, ADS bibcodes, arXiv ids in \\bibitem entries and inline citation years like 'Kauffmann et al. (2003)' - bibliography churn is tracked separately, not as numeric invariants",
        "LaTeX layout dimensions (0.72/0.86\\textwidth, column specs) and document class version (aastex631)",
        "document-structure cross-references ('Supplement Sections 5.1 and 5.7', figure/table numbers)",
        "digits inside catalog/quantity/file identifiers (R90/R50, petroR50/petroR90, lgm_tot_p50, specsfr_tot_p50, galSpecExtra, fig-bpt.pdf, topic-01..08.pdf, m1_rp2..m3_p3 artifact codes) - carried implicitly by table_row and run_identifier entries where they matter",
        "spelled-out numbers ('four-line', 'eight entries', 'two variables') - not numerals; treated as prose",
    ],
    "known_rounding_anomalies": [
        {
            "entry": "FLG-CI95",
            "canonical": "[-1.334,-1.283]",
            "artifact_nearest_rounding": "[-1.334,-1.282]",
            "explanation": "Raw bootstrap CI is [-1.3341385500000003, -1.2821399375]; nearest 3-dp rounding of the upper bound is -1.282. The audit invariant list and cycle-5 text carry -1.283. Rewriters that re-derive from the artifact emit -1.282 and fail the audit.",
        },
        {
            "entry": "SUP-ROW-188",
            "canonical": "... & 2.830 \\\\",
            "artifact_nearest_rounding": "2.831",
            "explanation": "Raw median_u_minus_r for the (11.0-12.5, 0.02-0.05) cell is 2.83066; nearest 3-dp rounding is 2.831. Cycle-5 carries 2.830 (truncation); every other cell in the table is nearest-rounded.",
        },
    ],
    "entry_count": len(entries),
    "entries": entries,
    "snapshot_sha256": snapshot_sha,
}

out = ROOT / "INVARIANT_MANIFEST.json"
out.write_text(json.dumps(manifest, indent=2) + "\n")

print(f"entries: {len(entries)}  (scalars {len(S) - len(problems)}, rows {sum(len(v) for v in TABLE_ROWS.values())})")
print(f"manifest written: {out} ({out.stat().st_size} bytes)")
if problems:
    print("\nPROBLEMS:")
    for p in problems:
        print(" ", p)
print("\n=== entries whose occurrence counts change in cycle 6/7 ===")
for d in drift_report:
    print(f"  {d['id']:<22} c5={d['count_c5']} c6={d['count_c6']} c7={d['count_c7']}  {d['exact_string']!r}")
print("\n=== variant scan (occurrences per doc/cycle) ===")
for v, docs in variant_scan.items():
    print(f"  {v!r}: {docs}")
print("\n=== new numeric tokens in c6/c7 (bib lines excluded) ===")
for k, v in new_tokens.items():
    print(f"  {k}: {v}")
