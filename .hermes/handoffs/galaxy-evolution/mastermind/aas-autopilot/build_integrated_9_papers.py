#!/usr/bin/env python3
"""Build local-only integrated AASTeX drafts for the nine active Galaxy Evolution papers.

This script deliberately does not touch public pages, live roots, product DB/API,
deploy/restart, git, cron, billing/OAuth, or external submission. It reads the
existing public-data pilot artifacts and overnight lane outputs, then writes a
new local integration run with revised manuscript sources and copied figures.
"""

from __future__ import annotations

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTO = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
RUN_ID = "INTEGRATED_9_PAPERS_20260709T012051Z"
OUT = AUTO / "integration-runs" / RUN_ID

RP1_RUN = AUTO / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z"
BATCH_RUN = AUTO / "runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z"
OVERNIGHT = AUTO / "overnight-9-papers-20260708"

SELECTION_JSON = OVERNIGHT / "lanes/tori/selection-function-attrition/20260708T155514Z/selection_function_attrition_summary_20260708T155514Z.json"
REP_JSON = OVERNIGHT / "lanes/tori/cached-public-representativeness/20260708T220242Z/cached_public_representativeness_summary_20260708T220242Z.json"
GORU_MATCH_JSON = OVERNIGHT / "lanes/goru/artifacts/goru_matching_control_robustness_20260708T205859Z.json"
GORU_BPT_JSON = OVERNIGHT / "lanes/goru/artifacts/goru_stratified_bpt_robustness_20260708T162615Z.json"
GORU_REG_JSON = OVERNIGHT / "lanes/goru/artifacts/goru_regression_bin_sensitivity_20260708T183643Z.json"
BATCH_MANIFEST = BATCH_RUN / "ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text())


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def clean_text(s: Any) -> str:
    text = str(s)
    repl = {
        "—": "--",
        "–": "-",
        "−": "-",
        "“": "\"",
        "”": "\"",
        "‘": "'",
        "’": "'",
        "≈": "about",
        "≥": ">=",
        "≤": "<=",
        "λ": "lambda",
        "α": "alpha",
        "β": "beta",
    }
    for k, v in repl.items():
        text = text.replace(k, v)
    return text


def tex_escape(s: Any) -> str:
    text = clean_text(s)
    out = []
    for ch in text:
        if ch == "\\":
            out.append(r"\textbackslash{}")
        elif ch == "&":
            out.append(r"\&")
        elif ch == "%":
            out.append(r"\%")
        elif ch == "$":
            out.append(r"\$")
        elif ch == "#":
            out.append(r"\#")
        elif ch == "_":
            out.append(r"\_")
        elif ch == "{":
            out.append(r"\{")
        elif ch == "}":
            out.append(r"\}")
        elif ch == "~":
            out.append(r"\textasciitilde{}")
        elif ch == "^":
            out.append(r"\textasciicircum{}")
        else:
            out.append(ch)
    return "".join(out)


def fmt(x: Any, nd: int = 3) -> str:
    if x is None:
        return "--"
    if isinstance(x, int):
        return f"{x:,}"
    if isinstance(x, float):
        return f"{x:.{nd}f}"
    return tex_escape(x)


def pct(x: float, nd: int = 1) -> str:
    return f"{100.0 * x:.{nd}f}"


def copy_if_exists(src: Path, dst: Path) -> dict[str, Any]:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not src.exists():
        return {"source": str(src), "dest": str(dst), "exists": False}
    shutil.copy2(src, dst)
    return {"source": str(src), "dest": str(dst), "exists": True, "bytes": dst.stat().st_size, "sha256": sha256(dst)}


def itemize(lines: list[str]) -> str:
    return "\\begin{itemize}\n" + "\n".join(f"\\item {line}" for line in lines) + "\n\\end{itemize}\n"


def shared_selection_section(selection: dict[str, Any], represent: dict[str, Any]) -> str:
    stage = selection["stage_counts"]
    rows = []
    for rec in stage:
        label = rec["stage_label"]
        public = rec["sdss_dr17_count"]
        cached = rec.get("cached_sample_count_at_matching_stage") or "--"
        retention = rec.get("retention_vs_spectro_z_parent")
        rows.append(f"{tex_escape(label)} & {fmt(public)} & {fmt(cached)} & {fmt(retention, 3)} " + r"\\")
    red = represent["dimension_summary"]["redshift"]
    mass = represent["dimension_summary"]["stellar_mass"]
    ssfr = represent["dimension_summary"]["ssfr"]
    return rf"""
\section{{Shared parent sample and selection function}}\label{{sec:shared-selection}}
All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: {fmt(selection['cached_rows'])} rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains {fmt(selection['strict_sdss_sn_ge_3_total'])} rows, so the cached table covers {pct(selection['cached_coverage_of_strict_sdss_sn_ge_3'])}\% of that strict parent. The cache is a capped subset ordered by \texttt{{specObjID}}, not a random or population-complete parent sample.

\begin{{deluxetable*}}{{lrrr}}
\tabletypesize{{\scriptsize}}
\tablecaption{{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{{tab:selection-cascade}}}}
\tablehead{{\colhead{{Selection stage}} & \colhead{{Public DR17 rows}} & \colhead{{Cached rows}} & \colhead{{Retention vs. spectro-z parent}}}}
\startdata
{chr(10).join(rows)}
\enddata
\tablecomments{{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}}
\end{{deluxetable*}}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps {pct(selection['ssfr_low_bin_reference']['sn_ge_3_retention_vs_parent'], 1)}\% of the $-12<\log {{\rm sSFR}}<-11$ parent bin but {pct(selection['ssfr_star_forming_bin_reference']['sn_ge_3_retention_vs_parent'], 1)}\% of the $-10<\log {{\rm sSFR}}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.

Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were {fmt(red['max_abs_fraction_difference_pp'], 2)} percentage points in redshift, {fmt(mass['max_abs_fraction_difference_pp'], 2)} percentage points in stellar mass, and {fmt(ssfr['max_abs_fraction_difference_pp'], 2)} percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
"""


def bibliography(topic_slug: str) -> str:
    common = r"""
\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
"""
    extra: dict[str, str] = {
        "m1_rp1_sdss_agn_sfr": r"""
\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
""",
        "m1_rp2_environment_quenching": r"""
\bibitem[Baldry et al.(2006)]{baldry2006} Baldry, I.~K., Balogh, M.~L., Bower, R.~G., et al. 2006, MNRAS, 373, 469
\bibitem[Goubert et al.(2024)]{goubert2024} Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2024, arXiv:2401.12953
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
""",
        "m1_rp3_maintenance_heating": r"""
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, arXiv:2403.17145
\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[McNamara \& Nulsen(2012)]{mcnamara2012} McNamara, B.~R., \& Nulsen, P.~E.~J. 2012, New J. Phys., 14, 055023
""",
        "m2_p1_outflow_escape_recycling": r"""
\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
""",
        "m2_p2_radio_jet_environment": r"""
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, arXiv:2403.17145
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Santoro et al.(2020)]{santoro2020} Santoro, F., Tadhunter, C., Baron, D., Morganti, R., \& Holt, J. 2020, A\&A, 644, A54
""",
        "m2_p3_feedback_transition_mass": r"""
\bibitem[Baldry et al.(2004)]{baldry2004} Baldry, I.~K., Glazebrook, K., Brinkmann, J., et al. 2004, ApJ, 600, 681
\bibitem[Bluck et al.(2023)]{bluck2023} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108
\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Peng et al.(2012)]{peng2012} Peng, Y.-j., Lilly, S.~J., Renzini, A., \& Carollo, M. 2012, ApJ, 757, 4
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
""",
        "m3_p1_multiphase_census": r"""
\bibitem[Bae \& Woo(2018)]{bae2018} Bae, H.-J., \& Woo, J.-H. 2018, ApJ, 853, 185
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Feruglio et al.(2015)]{feruglio2015} Feruglio, C., Fiore, F., Carniani, S., et al. 2015, A\&A, 583, A99
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Rupke(2018)]{rupke2018} Rupke, D.~S.~N. 2018, Galaxies, 6, 138
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Woo et al.(2016)]{woo2016} Woo, J.-H., Bae, H.-J., Son, D., \& Karouzos, M. 2016, ApJ, 817, 108
""",
        "m3_p2_gas_depletion_efficiency": r"""
\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
\bibitem[Saintonge et al.(2011a)]{coldgass1} Saintonge, A., Kauffmann, G., Kramer, C., et al. 2011a, MNRAS, 415, 32
\bibitem[Saintonge et al.(2011b)]{coldgass2} Saintonge, A., Kauffmann, G., Wang, J., et al. 2011b, MNRAS, 415, 61
\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
""",
        "m3_p3_simulation_validation": r"""
\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
\bibitem[Donnari et al.(2021)]{donnari2021} Donnari, M., Pillepich, A., Nelson, D., et al. 2021, MNRAS, 506, 4760
\bibitem[Dubrois et al.(2013)]{dubois2013} Dubois, Y., Gavazzi, R., Peirani, S., \& Silk, J. 2013, MNRAS, 433, 3297
\bibitem[Dubrois et al.(2016)]{dubois2016} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, MNRAS, 463, 3948
\bibitem[Nanni et al.(2023)]{imanga2023} Nanni, L., Thomas, D., Trayford, J., et al. 2023, MNRAS, 518, 2605
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
""",
    }
    return common + extra.get(topic_slug, "") + "\\end{thebibliography}\n"


def topic_future_citation_sentence(slug: str) -> str:
    m = {
        "m1_rp1_sdss_agn_sfr": "Low-redshift AGN--star-formation context motivates the test, but retired/LINER-like ionization sources require caution before interpreting broad BPT-AGN labels as accretion-powered feedback signatures \\citep{lamassa2013,stasinska2008,stasinska2015}.",
        "m1_rp2_environment_quenching": "Mass and environment are known separable axes in low-redshift galaxy evolution, but a real environmental-quenching analysis requires group/halo and central-satellite information beyond this nearest-neighbour proxy \\citep{peng2010,baldry2006,wetzel2013,goubert2024}.",
        "m1_rp3_maintenance_heating": "Radio-mode and hot-atmosphere studies define the future calorimetric observables--jet power, cavities, cooling luminosity, and group gas--that are absent from this optical denominator \\citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}.",
        "m2_p1_outflow_escape_recycling": "Wind and outflow literature specifies the missing kinematic, geometric, molecular, and multiphase measurements; these sources motivate follow-up and do not turn line-ratio selection into an escape/recycling measurement \\citep{veilleux2005,cicone2014,fiore2017,carniani2017,fabian2012}.",
        "m2_p2_radio_jet_environment": "The radio/X-ray/group literature motivates environment-stratified follow-up, but the present result is only an optical BPT-AGN fraction versus an internal density proxy \\citep{best2005,santoro2020,mcnamara2007,eckert2024}.",
        "m2_p3_feedback_transition_mass": "Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition \\citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.",
        "m3_p1_multiphase_census": "A real multiphase census needs independent ionized, neutral, molecular, and energetic outflow observables; the present SDSS thresholds are an optical denominator only \\citep{veilleux2005,rupke2018,cicone2014,fiore2017,feruglio2015,woo2016,bae2018}.",
        "m3_p2_gas_depletion_efficiency": "Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs; optical H$\\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \\citep{coldgass1,coldgass2,xcoldgass2017,xgass2018}.",
        "m3_p3_simulation_validation": "Simulation suites and mock-observation methods define the future comparison problem; no simulation mock has been forward-modelled or ranked in this pilot \\citep{tng2019,eagle2015,simba2019,imanga2023,donnari2021,dubois2013,dubois2016}.",
    }
    return m[slug]


def rp1_results_section(rp1: dict[str, Any], goru_match: dict[str, Any], goru_bpt: dict[str, Any]) -> str:
    baseline = goru_match["key_results"]["rp1_baseline_bpt_agn_sn3_nearest_replacement"]
    cal = goru_match["key_results"]["rp1_mass_z_moderate_caliper"]
    norepl = goru_match["key_results"]["rp1_greedy_without_replacement"]
    sn10 = goru_bpt["matched_bpt_agn_sn10"]
    sey = goru_bpt["matched_nii_seyfert_like_proxy_sn3"]
    lines = [
        f"Broad BPT optical AGN vs. star-forming controls at S/N$\\geq3$: $N={fmt(baseline['matched_pairs'])}$ matched pairs, median $\\Delta\\log {{\\rm sSFR}}={fmt(baseline['median_delta_log_sSFR'])}$ dex with 95\\% bootstrap interval $[{fmt(baseline['median_delta_ci95_low'])},{fmt(baseline['median_delta_ci95_high'])}]$ dex.",
        f"Moderate mass-redshift caliper $|\\Delta\\log M_\\star|\\leq0.05$, $|\\Delta z|\\leq0.002$: $N={fmt(cal['matched_pairs'])}$ retained pairs ({pct(cal['target_coverage_fraction'])}\\% target coverage), median offset {fmt(cal['median_delta_log_sSFR'])} dex.",
        f"A deterministic no-replacement diagnostic uses $N={fmt(norepl['matched_pairs'])}$ pairs and gives median offset {fmt(norepl['median_delta_log_sSFR'])} dex, but with visibly poorer mass balance; it is a stress test, not the preferred estimator.",
        f"Raising the line-S/N threshold to 10 leaves $N={fmt(sn10['matched_pairs'])}$ matched pairs and reduces the median offset to {fmt(sn10['median_delta_log_sSFR_target_minus_control'])} dex, showing sensitivity to the emission-line selection function.",
        f"A narrower [N II] Seyfert-like proxy gives $N={fmt(sey['matched_pairs'])}$ pairs and median offset {fmt(sey['median_delta_log_sSFR_target_minus_control'])} dex, reinforcing that subclass definitions change the effect size.",
    ]
    return rf"""
\section{{Flagship integrated result: optical AGN and catalog sSFR}}\label{{sec:rp1-result}}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \citep{{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}}. The cached analysis table contains {fmt(rp1['bpt_counts']['star-forming'])} star-forming galaxies, {fmt(rp1['bpt_counts']['intermediate'])} intermediate/composite objects, {fmt(rp1['bpt_counts']['agn'])} broad optical AGN, and {fmt(rp1['bpt_counts']['unclassified'])} unclassified objects.

The preferred estimator matches every broad optical AGN host to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. This is an association design; controls are not matched in morphology, halo mass, gas mass, aperture scale, AGN luminosity, or duty-cycle phase.

{itemize(lines)}

\begin{{figure*}}
\centering
\includegraphics[width=0.73\textwidth]{{../figures/fig-bpt.pdf}}
\caption{{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used by the flagship RP-1 integration. This figure verifies the measured line-ratio denominator and broad optical classification; it does not by itself identify causal AGN feedback.}}
\label{{fig:bpt}}
\end{{figure*}}

\begin{{figure*}}
\centering
\includegraphics[width=0.86\textwidth]{{../figures/fig-matched-offsets.pdf}}
\caption{{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset is robust within the optical emission-line subset but remains selection- and subclass-dependent.}}
\label{{fig:offsets}}
\end{{figure*}}
"""


def proxy_results_section(spec: dict[str, Any], data: dict[str, Any]) -> str:
    bullets = [tex_escape(b) for b in data.get("result_bullets", [])]
    req = tex_escape(data.get("full_proposal_requires", "additional survey data"))
    guard = tex_escape(data.get("interpretation_guard", "SDSS-only proxy/denominator pilot."))
    question = tex_escape(data.get("pilot_question", "Bounded SDSS pilot question."))
    return rf"""
\section{{Topic-specific optical denominator or proxy result}}\label{{sec:topic-result}}
The consolidated proposal question is: {question} The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.

{itemize(bullets)}

\begin{{figure}}
\centering
\includegraphics[width=\columnwidth]{{../figures/fig-topic.pdf}}
\caption{{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for {tex_escape(spec['card_label'])}. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}}
\label{{fig:topic}}
\end{{figure}}

\section{{Interpretation and missing observables}}\label{{sec:missing}}
{guard} The full proposal requires: {req}

{topic_future_citation_sentence(spec['slug'])}
"""


def manuscript(spec: dict[str, Any], data: dict[str, Any], selection: dict[str, Any], represent: dict[str, Any], goru_match: dict[str, Any], goru_bpt: dict[str, Any]) -> str:
    slug = spec["slug"]
    title = spec["integrated_title"]
    short = spec["short_title"]
    is_flagship = slug == "m1_rp1_sdss_agn_sfr"
    status = "flagship short-paper draft" if is_flagship else "guarded SDSS optical proxy/denominator draft"
    abstract_main = spec["abstract"]
    scope = spec["scope"]
    if is_flagship:
        result_section = rp1_results_section(data, goru_match, goru_bpt)
    else:
        result_section = proxy_results_section(spec, data)
    return rf"""\documentclass[twocolumn]{{aastex631}}
\usepackage{{amsmath}}
\usepackage{{booktabs}}
\shorttitle{{{tex_escape(short)}}}
\shortauthors{{NebulaMind local integration}}
\begin{{document}}

\title{{{tex_escape(title)}}}
\author{{NebulaMind Research Autopilot}}
\affiliation{{Local reproducible integration run; public SDSS DR17 data only}}

\begin{{abstract}}
{abstract_main} This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a {tex_escape(status)}. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{{abstract}}

\keywords{{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}}

\section{{Purpose and claim contract}}\label{{sec:purpose}}
{scope}

The claim contract is intentionally conservative. Quantities measured here are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. Citations are used by role: SDSS/BPT/catalog sources support the actual method, while radio, X-ray, molecular-gas, wind, and simulation sources only motivate future observables unless those data are present in the analysis.

{shared_selection_section(selection, represent)}

\section{{Measurements}}\label{{sec:measurements}}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{{sdssdr17,brinchmann2004,york2000}}.

{result_section}

\section{{Reproducibility and safety}}\label{{sec:repro}}
This manuscript was generated by local integration run \texttt{{{tex_escape(RUN_ID)}}}. Inputs are the original RP-1 SDSS query/run directory, the eight-topic SDSS remaining-topic manifest, the overnight shared selection-function packet, the cached-versus-public representativeness packet, Goru robustness outputs, and literature/source placement packets. The output is a local draft PDF and manifest entry only. No public-linked PDF was replaced.

\section{{Conclusion}}\label{{sec:conclusion}}
The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.

{bibliography(slug)}
\end{{document}}
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    selection = read_json(SELECTION_JSON)
    represent = read_json(REP_JSON)
    goru_match = read_json(GORU_MATCH_JSON)
    goru_bpt = read_json(GORU_BPT_JSON)
    _ = read_json(GORU_REG_JSON)  # read to validate availability; topic JSONs carry current result bullets.
    rp1 = read_json(RP1_RUN / "analysis_results.json")
    batch_manifest = read_json(BATCH_MANIFEST)

    topic_specs: list[dict[str, Any]] = [
        {
            "slug": "m1_rp1_sdss_agn_sfr",
            "card_label": "M1 RP-1",
            "short_title": "SDSS optical AGN/sSFR matched-control pilot",
            "integrated_title": "Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot",
            "abstract": "We integrate the strongest Galaxy Evolution pilot into a selection-aware short-paper draft: a matched-control comparison of catalog specific star formation in broad BPT optical AGN hosts and star-forming controls in SDSS DR17.",
            "scope": "This is the flagship local integration draft. It tests an optical-classification-associated catalog-sSFR offset, not causal AGN feedback, gas depletion, or halo maintenance heating.",
            "figures": [
                (RP1_RUN / "figures/figure1_bpt.pdf", "fig-bpt.pdf"),
                (RP1_RUN / "figures/figure2_matched_offsets.pdf", "fig-matched-offsets.pdf"),
            ],
            "data": rp1,
        }
    ]

    for topic in batch_manifest["topics"]:
        result_json = Path(topic["pdf"]).parents[1] / "analysis_results.json"
        data = read_json(result_json)
        topic_specs.append(
            {
                "slug": topic["slug"],
                "card_label": f"{topic['method']} {topic['card_id']}",
                "short_title": topic["short_title"],
                "integrated_title": topic["short_title"] + ": selection-aware SDSS optical proxy integration",
                "abstract": f"We integrate the active proposal '{tex_escape(topic['title'])}' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper.",
                "scope": f"This draft preserves the active proposal title, '{tex_escape(topic['title'])}', but narrows the supported claim to the cached SDSS optical measurement named in the results. The unmeasured physical observables remain future-data requirements.",
                "figures": [(Path(topic["figure_pdf"]), "fig-topic.pdf")],
                "data": data,
            }
        )

    manifest: dict[str, Any] = {
        "run_id": RUN_ID,
        "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "scope": "local-only integrated AASTeX manuscripts; no public/live replacement",
        "source_artifacts": {
            "rp1_run": str(RP1_RUN),
            "batch_manifest": str(BATCH_MANIFEST),
            "selection_json": str(SELECTION_JSON),
            "representativeness_json": str(REP_JSON),
            "goru_matching_json": str(GORU_MATCH_JSON),
            "goru_bpt_json": str(GORU_BPT_JSON),
            "goru_regression_json": str(GORU_REG_JSON),
        },
        "shared_counts": {
            "cached_rows": selection["cached_rows"],
            "strict_public_sn_ge_3_total": selection["strict_sdss_sn_ge_3_total"],
            "cached_coverage": selection["cached_coverage_of_strict_sdss_sn_ge_3"],
            "bpt_counts": rp1["bpt_counts"],
            "sn_threshold_counts": goru_match["sn_threshold_counts"],
        },
        "papers": [],
    }

    for i, spec in enumerate(topic_specs, start=1):
        paper_dir = OUT / f"{i:02d}_{spec['slug']}"
        aas_dir = paper_dir / "aastex"
        fig_dir = paper_dir / "figures"
        data_dir = paper_dir / "data"
        aas_dir.mkdir(parents=True, exist_ok=True)
        fig_dir.mkdir(parents=True, exist_ok=True)
        data_dir.mkdir(parents=True, exist_ok=True)

        copied = []
        for src, name in spec["figures"]:
            copied.append(copy_if_exists(Path(src), fig_dir / name))

        tex = manuscript(spec, spec["data"], selection, represent, goru_match, goru_bpt)
        tex_path = aas_dir / f"{spec['slug']}_integrated.tex"
        tex_path.write_text(tex)
        result_path = data_dir / "source_analysis_results.json"
        result_path.write_text(json.dumps(spec["data"], indent=2, sort_keys=True))

        manifest["papers"].append(
            {
                "index": i,
                "slug": spec["slug"],
                "status": "flagship short-paper draft" if spec["slug"] == "m1_rp1_sdss_agn_sfr" else "guarded proxy/denominator draft",
                "tex": str(tex_path),
                "expected_pdf": str(aas_dir / f"{spec['slug']}_integrated.pdf"),
                "figures": copied,
                "source_results_json": str(result_path),
                "title": spec["integrated_title"],
            }
        )

    (OUT / "INTEGRATION_MANIFEST_PRECOMPILE.json").write_text(json.dumps(manifest, indent=2, sort_keys=True))
    (OUT / "README.md").write_text(
        "# Integrated 9-paper local run\n\n"
        f"Run ID: `{RUN_ID}`\n\n"
        "This directory contains local-only integrated AASTeX manuscript sources for the nine active Galaxy Evolution paper drafts. "
        "It does not replace public-linked PDFs and does not touch live/static roots. Compile with Tectonic from each `aastex/` directory, then run the local audit.\n"
    )
    print(json.dumps({"run_id": RUN_ID, "out": str(OUT), "papers": len(manifest["papers"]), "manifest": str(OUT / "INTEGRATION_MANIFEST_PRECOMPILE.json")}, indent=2))


if __name__ == "__main__":
    main()
