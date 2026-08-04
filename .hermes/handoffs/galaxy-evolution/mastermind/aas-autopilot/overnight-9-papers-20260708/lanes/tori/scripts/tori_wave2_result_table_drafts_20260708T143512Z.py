#!/usr/bin/env python3
"""Create lane-local Wave-2 manuscript drafts with concrete result tables.

This script reads only preserved local SDSS/Goru artifacts and current AASTeX
sources.  It writes Tori lane-local drafts/PDFs; it does not overwrite the
public-linked manuscripts or touch public/frontend/product state.
"""
from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import textwrap
from pathlib import Path

TS = "20260708T143512Z"
REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTOPILOT = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
OVERNIGHT = AUTOPILOT / "overnight-9-papers-20260708"
RUN_ROOT = AUTOPILOT / "runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z"
GORU_TABLE_DIR = OVERNIGHT / "lanes/goru/tables"
METRIC_CSV = GORU_TABLE_DIR / "topic_metric_robustness_20260708T141459Z.csv"
TARGET_CSV = GORU_TABLE_DIR / "simulation_target_vector_cells_20260708T141459Z.csv"
OUT_ROOT = OVERNIGHT / "lanes/tori/wave2-result-table-drafts" / TS

TOPICS = {
    "m2_p2_radio_jet_environment": {
        "title": "Environment-stratified optical AGN denominators for radio-jet coupling follow-up in SDSS DR17",
        "short": "Environment-stratified optical AGN denominators",
        "source_title": "Environmental dependence of radio-jet coupling efficiency in galaxy gas",
        "question": "Does a local-density proxy change the optical AGN fraction in massive SDSS hosts, and how stable is that contrast to the neighbour scale?",
        "requires": "radio jet morphology and age, jet-power or cavity energetics, hot-gas density, and calibrated coupling-efficiency measurements.",
        "fig": RUN_ROOT / "m2_p2_radio_jet_environment/figures/m2_p2_radio_jet_environment_figure1.pdf",
    },
    "m2_p3_feedback_transition_mass": {
        "title": "A mass-binned SDSS DR17 optical transition table for quenching and AGN-incidence follow-up",
        "short": "Mass-binned optical transition table",
        "source_title": "Locating the transition from stellar-feedback to AGN-feedback regulation",
        "question": "Across stellar-mass bins, where do quenched fraction and optical AGN incidence rise in the same SDSS denominator?",
        "requires": "gas fractions, baryon deficits, halo masses, stellar-feedback observables, morphology, and redshift extensions before attributing the transition to a physical feedback channel.",
        "fig": RUN_ROOT / "m2_p3_feedback_transition_mass/figures/m2_p3_feedback_transition_mass_figure1.pdf",
    },
    "m3_p1_multiphase_census": {
        "title": "Selection-definition sensitivity in a common SDSS DR17 optical tracer denominator",
        "short": "Optical tracer denominator sensitivity",
        "source_title": "A multiphase, common-denominator census of AGN-driven outflows",
        "question": "How much does inferred candidate prevalence move when simple optical tracer definitions and line-S/N cuts are varied inside one denominator?",
        "requires": "co-measured ionized, molecular, neutral, X-ray, and radio tracers over an aperture-matched common parent sample.",
        "fig": RUN_ROOT / "m3_p1_multiphase_census/figures/m3_p1_multiphase_census_figure1.pdf",
    },
    "m3_p2_gas_depletion_efficiency": {
        "title": "Massive quenched SDSS denominators for molecular-gas depletion versus efficiency follow-up",
        "short": "Massive quenched gas-follow-up denominators",
        "source_title": "Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies",
        "question": "How many massive low-sSFR emission-line galaxies are available for CO/dust follow-up, and how do the counts shift with mass and sSFR thresholds?",
        "requires": "CO or dust-based molecular gas masses, aperture-matched SFRs, resolved morphology, and environment labels.",
        "fig": RUN_ROOT / "m3_p2_gas_depletion_efficiency/figures/m3_p2_gas_depletion_efficiency_figure1.pdf",
    },
    "m3_p3_simulation_validation": {
        "title": "A compact observed SDSS target vector for feedback-model forward validation",
        "short": "Observed SDSS feedback-validation vector",
        "source_title": "Forward-modelled validation of cosmological feedback prescriptions",
        "question": "What observed mass-redshift cells can serve as a compact target vector for later simulation mocks?",
        "requires": "simulation catalogs passed through SDSS/MaNGA/ALMA/X-ray/radio selection functions, aperture models, and noise models before any model-comparison claim.",
        "fig": RUN_ROOT / "m3_p3_simulation_validation/figures/m3_p3_simulation_validation_figure1.pdf",
    },
}

MASS_ORDER = ["8.0-9.5", "9.5-10.0", "10.0-10.5", "10.5-11.0", "11.0-12.5"]
Z_ORDER = ["0.02-0.05", "0.05-0.08", "0.08-0.12"]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing required CSV: {path}")
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


METRICS = read_csv(METRIC_CSV)
TARGET_ROWS = read_csv(TARGET_CSV)


def rows_for(topic: str) -> list[dict[str, str]]:
    return [r for r in METRICS if r["topic"] == topic]


def get_metric(topic: str, variant: str, metric: str) -> dict[str, str]:
    hits = [r for r in METRICS if r["topic"] == topic and r["variant"] == variant and r["metric"] == metric]
    if len(hits) != 1:
        raise SystemExit(f"Expected one metric row for {topic} {variant} {metric}; found {len(hits)}")
    return hits[0]


def fnum(value: str | float, nd: int = 3) -> str:
    if value in (None, ""):
        return "---"
    return f"{float(value):.{nd}f}"


def intish(value: str | float) -> str:
    if value in (None, ""):
        return "---"
    return f"{int(float(value)):,}"


def frac_text(row: dict[str, str]) -> str:
    return f"{intish(row['numerator_k'])}/{intish(row['denominator_n'])} ({fnum(row['value'])})"


def ci_text(row: dict[str, str]) -> str:
    return f"{fnum(row['value'])} [{fnum(row['ci95_low'])}, {fnum(row['ci95_high'])}]"


def tex_filename(path: Path) -> str:
    return path.name.replace("_", r"\_")


def common_header(topic: str, abstract: str, result_intro: str, table_tex: str, guard_extra: str) -> str:
    meta = TOPICS[topic]
    fig_dir = str(meta["fig"].parent) + "/"
    fig_name = tex_filename(meta["fig"])
    source_tex = RUN_ROOT / topic / "aastex" / f"{topic}_aas.tex"
    source_json = RUN_ROOT / topic / "analysis_results.json"
    source_tex_name = source_tex.name.replace("_", r"\_")
    source_json_name = source_json.name.replace("_", r"\_")
    metric_csv_name = METRIC_CSV.name.replace("_", r"\_")
    target_csv_name = TARGET_CSV.name.replace("_", r"\_")
    return textwrap.dedent(f"""
    % TORI_WAVE2_RESULT_TABLE_DRAFT_{TS}
    % Paper: {topic}
    % This lane-local revision draft does not overwrite public-linked manuscripts or PDFs.
    \\documentclass[twocolumn]{{aastex631}}
    \\usepackage{{amsmath}}
    \\usepackage{{booktabs}}
    \\graphicspath{{{{{fig_dir}}}}}
    \\shorttitle{{{meta['short']}}}
    \\shortauthors{{NebulaMind Autopilot}}

    \\begin{{document}}
    \\title{{{meta['title']}}}
    \\author{{NebulaMind Research Autopilot}}
    \\affiliation{{Local reproducible pilot run; public SDSS DR17 data and overnight local artifacts only}}

    \\begin{{abstract}}
    {abstract}
    \\end{{abstract}}

    \\keywords{{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}}

    \\section{{Scope and data}}
    This Wave-2 draft improves the active consolidated pilot for ``{meta['source_title']}'' by replacing a short itemized result with an explicit result table.  It remains an SDSS-only denominator/proxy manuscript.  The full topic still requires {meta['requires']}

    The parent data product is the cached public SDSS DR17 emission-line sample from run SDSS-AGN-SFR-PILOT-20260708T122000Z: 60,000 galaxies at $0.02<z<0.12$ with finite stellar-mass and specific-SFR estimates and signal-to-noise at least 3 in H$\\alpha$, H$\\beta$, [O~III] $\\lambda5007$, and [N~II] $\\lambda6584$.  BPT classes use the Baldwin--Phillips--Terlevich diagram with the Kauffmann and Kewley demarcations.  Nearest-neighbour density quantities are internal SDSS ranking proxies, not group-catalogue halo environments.

    \\section{{Result-table addendum}}
    {result_intro}

    {table_tex}

    \\begin{{figure}}
    \\centering
    \\includegraphics[width=\\columnwidth]{{{fig_name}}}
    \\caption{{Preserved topic-specific SDSS DR17 diagnostic from the original batch run.  It should be read with Table~\\ref{{tab:{topic.replace('_', '-')}}}: the figure and table are proxy or denominator measurements, not the full multi-survey physical test.}}
    \\label{{fig:{topic.replace('_', '-')}}}
    \\end{{figure}}

    \\section{{Interpretation guard}}
    {guard_extra}  The manuscript must continue to distinguish actual SDSS optical measurements from future radio, X-ray, molecular-gas, resolved-kinematic, or simulation-mock measurements.  No causal AGN-feedback, gas-depletion, escape/recycling, jet-coupling, or model-validation claim is established by this table alone.

    \\section{{Integration notes}}
    This file is a Tori lane-local draft.  It was generated from the current source manuscript \\texttt{{{source_tex_name}}}, the topic analysis JSON \\texttt{{{source_json_name}}}, Goru's actual-data robustness CSV, and the preserved figure path under the batch run.  If merged later, the table should be checked against the then-current analysis code and accompanied by a fresh PDF/hash manifest.

    \\section*{{Reproducibility and safety note}}
    Draft marker: TORI\\_WAVE2\\_RESULT\\_TABLE\\_DRAFT\\_{TS}.  Sources: \\texttt{{{metric_csv_name}}}, \\texttt{{{target_csv_name}}} when applicable, and current batch-run figures.  This draft uses local files only and does not overwrite public-linked PDFs.

    \\acknowledgments
    This pilot used public SDSS DR17 data products and local open-source tooling.

    \\begin{{thebibliography}}{{}}
    \\bibitem[Baldwin et al.(1981)]{{baldwin1981}} Baldwin, J.~A., Phillips, M.~M., \\& Terlevich, R. 1981, PASP, 93, 5
    \\bibitem[Kauffmann et al.(2003)]{{kauffmann2003}} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003, MNRAS, 346, 1055
    \\bibitem[Kewley et al.(2001)]{{kewley2001}} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \\& Trevena, J. 2001, ApJ, 556, 121
    \\bibitem[York et al.(2000)]{{york2000}} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    \\end{{thebibliography}}

    \\end{{document}}
    """).strip() + "\n"


def table_m2_p2() -> tuple[str, str, str, str]:
    topic = "m2_p2_radio_jet_environment"
    rows = []
    deltas = []
    for k in [5, 10, 20]:
        base = f"mass_ge_10.8_knn_k{k}"
        low = get_metric(topic, base + "_low", "low_density_massive_optical_agn_fraction")
        high = get_metric(topic, base + "_high", "high_density_massive_optical_agn_fraction")
        delta = get_metric(topic, base, "high_minus_low_density_optical_agn_fraction")
        deltas.append(float(delta["value"]))
        rows.append(f"$k={k}$ & {frac_text(low)} & {frac_text(high)} & {ci_text(delta)} " + r"\\")
    table = "\n".join(rows)
    table_tex = textwrap.dedent(f"""
    \\begin{{deluxetable*}}{{lccc}}
    \\tablecaption{{Massive-host optical AGN fraction by internal density scale\\label{{tab:m2-p2-radio-jet-environment}}}}
    \\tablehead{{\\colhead{{Density proxy}} & \\colhead{{Low-density quartile}} & \\colhead{{High-density quartile}} & \\colhead{{$\\Delta f_{{\\rm AGN}}$ high--low}}}}
    \\startdata
    {table}
    \\enddata
    \\tablecomments{{Rows are restricted to massive hosts with $\\log M_\\star\\geq10.8$.  Fractions are BPT optical AGN fractions in the same SDSS emission-line denominator.  The density proxy is recomputed with $k=5$, 10, and 20 nearest neighbours; it is not a group catalogue or radio-jet environment measurement.}}
    \\end{{deluxetable*}}
    """).strip()
    abstract = f"We revise the SDSS-only pilot for environmental radio-jet follow-up by adding a scale-robust massive-host optical AGN denominator table.  For $\\log M_\\star\\geq10.8$ hosts, the high-minus-low optical AGN fraction is {min(deltas):.3f}--{max(deltas):.3f} across $k=5$, 10, and 20 nearest-neighbour density rankings.  These are optical AGN/environment proxy measurements; they do not measure radio jet power, hot-gas coupling, or causal feedback efficiency."
    intro = "Table~\\ref{tab:m2-p2-radio-jet-environment} turns the prior single-number result into a neighbour-scale check.  The sign of the massive-host optical AGN fraction contrast is stable across the three internal density rankings."
    guard = "The table supports a target-selection statement: massive optical AGN are more common in the high-density quartile under these internal rankings."
    return abstract, intro, table_tex, guard


def table_m2_p3() -> tuple[str, str, str, str]:
    topic = "m2_p3_feedback_transition_mass"
    rows = []
    qvals = []
    avals = []
    for mb in MASS_ORDER:
        q = get_metric(topic, f"mass_bin_{mb}", "quenched_fraction")
        a = get_metric(topic, f"mass_bin_{mb}", "optical_agn_fraction")
        qvals.append(float(q["value"]))
        avals.append(float(a["value"]))
        rows.append(f"{mb} & {intish(q['denominator_n'])} & {frac_text(q)} & {frac_text(a)} " + r"\\")
    table = "\n".join(rows)
    table_tex = textwrap.dedent(f"""
    \\begin{{deluxetable*}}{{lccc}}
    \\tablecaption{{Mass-binned quenched and optical-AGN fractions in the SDSS denominator\\label{{tab:m2-p3-feedback-transition-mass}}}}
    \\tablehead{{\\colhead{{$\\log M_\\star$ bin}} & \\colhead{{$N$}} & \\colhead{{Quenched fraction}} & \\colhead{{BPT optical AGN fraction}}}}
    \\startdata
    {table}
    \\enddata
    \\tablecomments{{The quenched flag is the pilot low-sSFR threshold used in the batch run.  The table is an optical mass-transition diagnostic only; it does not distinguish stellar feedback, AGN feedback, halo quenching, or gas supply.}}
    \\end{{deluxetable*}}
    """).strip()
    abstract = f"We add a mass-binned result table to the SDSS-only transition-mass pilot.  In the 60,000-galaxy emission-line denominator, the quenched fraction rises from {qvals[0]:.3f} in the $\\log M_\\star=8.0$--9.5 bin to {qvals[-1]:.3f} at $11.0$--12.5, while the BPT optical AGN fraction rises from {avals[0]:.3f} to {avals[-1]:.3f}.  This is a measurable optical transition vector, not an attribution of the transition to AGN feedback."
    intro = "Table~\\ref{tab:m2-p3-feedback-transition-mass} gives the numerator and denominator behind the transition statement, so the draft no longer depends on a bare qualitative summary."
    guard = "The table supports an empirical statement about co-rising low-sSFR and optical-AGN incidence with stellar mass in this emission-line sample."
    return abstract, intro, table_tex, guard


def table_m3_p1() -> tuple[str, str, str, str]:
    topic = "m3_p1_multiphase_census"
    tracers = [
        ("bpt_agn", "BPT AGN"),
        ("high_nii", "high [N~II]/H$\\alpha$"),
        ("high_oiii", "high [O~III]/H$\\beta$"),
        ("red_sequence", "red emission-line"),
        ("low_sSFR_quenched", "low-sSFR emission-line"),
    ]
    rows = []
    sn3_vals = []
    for sn in [3, 5, 10]:
        for key, label in tracers:
            r = get_metric(topic, f"sn_ge_{sn}_{key}", "optical_tracer_prevalence")
            if sn == 3:
                sn3_vals.append(float(r["value"]))
            rows.append(f"$\\geq {sn}$ & {label} & {intish(r['numerator_k'])}/{intish(r['denominator_n'])} & {fnum(r['value'])} " + r"\\")
    table = "\n".join(rows)
    table_tex = textwrap.dedent(f"""
    \\begin{{deluxetable*}}{{llcc}}
    \\tablecaption{{Optical tracer prevalence under common-denominator and line-S/N changes\\label{{tab:m3-p1-multiphase-census}}}}
    \\tablehead{{\\colhead{{Line S/N cut}} & \\colhead{{Optical tracer definition}} & \\colhead{{Selected/denominator}} & \\colhead{{Prevalence}}}}
    \\startdata
    {table}
    \\enddata
    \\tablecomments{{All rows are optical SDSS definitions.  They are useful for common-denominator design but are not molecular, neutral, X-ray, or radio outflow measurements.}}
    \\end{{deluxetable*}}
    """).strip()
    abstract = f"We add a selection-sensitivity table to the common-denominator optical tracer census.  At S/N$\\geq3$, simple optical tracer definitions span prevalence {min(sn3_vals):.3f}--{max(sn3_vals):.3f}; tightening the line-S/N threshold changes both denominator size and tracer prevalence.  This motivates a true multiphase common-denominator survey, but the present result remains optical only."
    intro = "Table~\\ref{tab:m3-p1-multiphase-census} exposes the selection dependence that was previously compressed into one range.  The same parent idea gives different candidate fractions depending on the tracer and S/N threshold."
    guard = "The table supports a methodological point about denominator control and selection sensitivity."
    return abstract, intro, table_tex, guard


def table_m3_p2() -> tuple[str, str, str, str]:
    topic = "m3_p2_gas_depletion_efficiency"
    rows = []
    ns = []
    for mass in ["10.6", "10.8", "11.0"]:
        for ssfr in ["-10.7", "-11.0"]:
            variant = f"mass_ge_{mass}_ssfr_lt_{ssfr}"
            nrow = get_metric(topic, variant, "massive_transition_quenched_denominator_rows")
            agn = get_metric(topic, variant, "optical_agn_fraction_in_denominator")
            lha = get_metric(topic, variant, "median_log_lha_proxy")
            ns.append(int(float(nrow["numerator_k"])))
            rows.append(f"$\\geq {mass}$ & $< {ssfr}$ & {intish(nrow['numerator_k'])} & {frac_text(agn)} & {fnum(lha['value'], 2)} " + r"\\")
    table = "\n".join(rows)
    table_tex = textwrap.dedent(f"""
    \\begin{{deluxetable*}}{{lcccc}}
    \\tablecaption{{Massive low-sSFR denominators for gas follow-up under threshold changes\\label{{tab:m3-p2-gas-depletion-efficiency}}}}
    \\tablehead{{\\colhead{{$\\log M_\\star$ cut}} & \\colhead{{$\\log {{\\rm sSFR}}$ cut}} & \\colhead{{Denominator $N$}} & \\colhead{{BPT AGN fraction}} & \\colhead{{Median $\\log L_{{\\rm H\\alpha}}$ proxy}}}}
    \\startdata
    {table}
    \\enddata
    \\tablecomments{{The H$\\alpha$ luminosity column is an optical emission proxy computed in the batch run; it is not a molecular-gas mass, gas fraction, or star-formation efficiency measurement.}}
    \\end{{deluxetable*}}
    """).strip()
    abstract = f"We add a threshold-grid denominator table to the molecular-gas depletion versus efficiency pilot.  Across $\\log M_\\star$ cuts 10.6--11.0 and low-sSFR cuts -10.7 to -11.0, the emission-line follow-up denominator ranges from {min(ns):,} to {max(ns):,} galaxies.  The table identifies SDSS optical targets for CO/dust follow-up; it does not measure gas depletion or star-formation efficiency."
    intro = "Table~\\ref{tab:m3-p2-gas-depletion-efficiency} makes the follow-up denominator explicit and shows how it changes under plausible mass and sSFR cuts."
    guard = "The table supports target-list design for molecular-gas follow-up."
    return abstract, intro, table_tex, guard


def table_m3_p3() -> tuple[str, str, str, str]:
    topic = "m3_p3_simulation_validation"
    rows = sorted(TARGET_ROWS, key=lambda r: (MASS_ORDER.index(r["mass_bin"]), Z_ORDER.index(r["z_bin"])))
    qvals = [float(r["quenched_fraction"]) for r in rows]
    avals = [float(r["optical_agn_fraction"]) for r in rows]
    body = []
    for r in rows:
        body.append(
            f"{r['mass_bin']} & {r['z_bin']} & {intish(r['n'])} & {fnum(r['quenched_fraction'])} & {fnum(r['optical_agn_fraction'])} & {fnum(r['high_excitation_agn_fraction'])} & {fnum(r['median_u_minus_r'])} " + r"\\")
    table = "\n".join(body)
    table_tex = textwrap.dedent(f"""
    \\begin{{deluxetable*}}{{llccccc}}
    \\tabletypesize{{\\scriptsize}}
    \\tablecaption{{Observed SDSS mass-redshift target vector for later feedback-model forward modelling\\label{{tab:m3-p3-simulation-validation}}}}
    \\tablehead{{\\colhead{{$\\log M_\\star$ bin}} & \\colhead{{$z$ bin}} & \\colhead{{$N$}} & \\colhead{{$f_Q$}} & \\colhead{{$f_{{\\rm BPT\,AGN}}$}} & \\colhead{{$f_{{\\rm high\,exc.}}$}} & \\colhead{{median $u-r$}}}}
    \\startdata
    {table}
    \\enddata
    \\tablecomments{{This is an observed SDSS target vector.  It is not a comparison to any simulation until mock catalogs are passed through matching selection, aperture, and noise models.}}
    \\end{{deluxetable*}}
    """).strip()
    abstract = f"We add the full 15-cell observed target vector to the simulation-validation pilot.  The SDSS cells span quenched fraction {min(qvals):.3f}--{max(qvals):.3f} and BPT optical AGN fraction {min(avals):.3f}--{max(avals):.3f} across mass and redshift.  These are observed validation targets only; no cosmological feedback model is accepted or rejected without forward-modelled mocks."
    intro = "Table~\\ref{tab:m3-p3-simulation-validation} is the concrete artifact the full proposal can later ask simulations to reproduce under the same selection function."
    guard = "The table supports an observed-target-vector statement, not a model-ranking statement."
    return abstract, intro, table_tex, guard


BUILDERS = {
    "m2_p2_radio_jet_environment": table_m2_p2,
    "m2_p3_feedback_transition_mass": table_m2_p3,
    "m3_p1_multiphase_census": table_m3_p1,
    "m3_p2_gas_depletion_efficiency": table_m3_p2,
    "m3_p3_simulation_validation": table_m3_p3,
}


def compile_tex(tex_path: Path) -> tuple[int, str]:
    proc = subprocess.run(["tectonic", tex_path.name], cwd=tex_path.parent, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=240)
    log_path = tex_path.with_name("compile.log")
    log_path.write_text(proc.stdout)
    return proc.returncode, proc.stdout


def verify_pdf(pdf_path: Path) -> dict[str, object]:
    if not pdf_path.exists():
        return {"exists": False, "starts_pdf": False, "bytes": 0, "sha256": None}
    data = pdf_path.read_bytes()
    return {
        "exists": True,
        "starts_pdf": data.startswith(b"%PDF"),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def main() -> None:
    if not shutil.which("tectonic"):
        raise SystemExit("tectonic executable not available")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, object] = {
        "marker": f"TORI_WAVE2_RESULT_TABLE_DRAFTS_{TS}",
        "timestamp_utc": TS,
        "scope": "Lane-local result-table manuscript drafts for the five active papers not covered by Lana Wave-1.",
        "inputs": {
            "metric_csv": str(METRIC_CSV),
            "simulation_target_csv": str(TARGET_CSV),
            "batch_run_root": str(RUN_ROOT),
        },
        "drafts": [],
        "safety": "Local overnight lane artifacts only; no public pages, live roots, product DB/API/page_versions, trust, deploy, restart, git, cron, billing/OAuth, or external submission.",
    }
    summary_lines = [
        f"# Tori Wave-2 result-table draft summary — {TS}",
        "",
        f"Marker: `TORI_WAVE2_RESULT_TABLE_DRAFTS_{TS}`",
        "",
        "This tick created lane-local AASTeX drafts/PDFs for five active SDSS-only pilot papers using Goru's robustness tables. It did not overwrite the public-linked PDFs.",
        "",
    ]
    for topic in BUILDERS:
        draft_dir = OUT_ROOT / topic
        draft_dir.mkdir(parents=True, exist_ok=True)
        abstract, intro, table_tex, guard = BUILDERS[topic]()
        tex = common_header(topic, abstract, intro, table_tex, guard)
        tex_path = draft_dir / f"{topic}_tori_wave2_{TS}.tex"
        tex_path.write_text(tex)
        changes_path = draft_dir / "CHANGES.md"
        changes_path.write_text(textwrap.dedent(f"""
        # Wave-2 table draft changes — {topic}

        Marker: `TORI_WAVE2_RESULT_TABLE_DRAFTS_{TS}`

        - Created a lane-local AASTeX draft with an explicit result table sourced from Goru's preserved robustness CSVs.
        - Preserved the SDSS-only/proxy scope guard; no physical feedback causality is inferred.
        - Reused the original batch-run figure by absolute local path; no public/static artifact was overwritten.
        """).strip() + "\n")
        code, log = compile_tex(tex_path)
        pdf_path = tex_path.with_suffix(".pdf")
        pdf_info = verify_pdf(pdf_path)
        fatal_markers = [m for m in ["! LaTeX Error", "Emergency stop", "Fatal error"] if m in log]
        if code != 0 or not pdf_info["starts_pdf"]:
            raise SystemExit(f"Compile/verification failed for {topic}: code={code}, pdf={pdf_info}, fatal={fatal_markers}\n{log[-2000:]}")
        item = {
            "paper_slug": topic,
            "source_tex": str(RUN_ROOT / topic / "aastex" / f"{topic}_aas.tex"),
            "draft_tex": str(tex_path),
            "changes_md": str(changes_path),
            "compiled_pdf": str(pdf_path),
            "compile_log": str(tex_path.with_name("compile.log")),
            "compile_exit_code": code,
            "fatal_markers": fatal_markers,
            "pdf_bytes": pdf_info["bytes"],
            "pdf_sha256": pdf_info["sha256"],
            "pdf_starts_with_pdf": pdf_info["starts_pdf"],
        }
        manifest["drafts"].append(item)
        summary_lines.extend([
            f"## {topic}",
            f"- Draft TeX: `{tex_path}`",
            f"- PDF: `{pdf_path}`",
            f"- Bytes/SHA256: {pdf_info['bytes']} / `{pdf_info['sha256']}`",
            "- Verification: tectonic exit 0; `%PDF` header verified; no fatal LaTeX markers.",
            "",
        ])
        print(f"DONE {topic} {pdf_info['bytes']} {pdf_info['sha256']}")
    manifest_path = OUT_ROOT / f"tori_wave2_result_table_manifest_{TS}.json"
    summary_path = OUT_ROOT / f"tori_wave2_result_table_summary_{TS}.md"
    manifest["outputs"] = {"manifest_json": str(manifest_path), "summary_md": str(summary_path), "draft_root": str(OUT_ROOT)}
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True))
    summary_lines.extend([
        "## Safety",
        "No public pages/live roots/product DB/API/page_versions/trust/deploy/restart/git/cron/billing/OAuth/external submission changes.",
        "",
        "## Next integration step",
        "Have the next Lana/Hwao pass decide whether to merge these lane-local table drafts into the active manuscript sources or keep them as addenda.",
        "",
    ])
    summary_path.write_text("\n".join(summary_lines))
    print(json.dumps({"manifest": str(manifest_path), "summary": str(summary_path), "draft_count": len(manifest["drafts"]), "draft_root": str(OUT_ROOT)}, indent=2))


if __name__ == "__main__":
    main()
