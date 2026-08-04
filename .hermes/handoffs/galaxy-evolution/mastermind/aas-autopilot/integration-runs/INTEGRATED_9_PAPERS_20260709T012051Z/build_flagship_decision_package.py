#!/usr/bin/env python3
"""Build the local flagship decision package.

Outputs:
- polished RP-1 flagship AASTeX draft/PDF source tree
- combined supplementary denominator/proxy atlas for the other eight active drafts
- package manifest before compile/audit

Safety: local files under the handoff tree only. No public/live/wiki/DB/deploy/git/external submission side effects.
"""

from __future__ import annotations

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BASE = Path("/Users/duhokim/NebulaMind/NebulaMind")
RUN = BASE / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z"
OUT_ID = "RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z"
OUT = RUN / "decision-package" / OUT_ID


def read_json(path: Path) -> Any:
    return json.loads(path.read_text())


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def clean_text(x: Any) -> str:
    s = str(x)
    replacements = {
        "—": "--",
        "–": "-",
        "−": "-",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "≈": "about",
        "≥": ">=",
        "≤": "<=",
        "α": "alpha",
        "β": "beta",
        "λ": "lambda",
    }
    for a, b in replacements.items():
        s = s.replace(a, b)
    return s


def tex_escape(x: Any) -> str:
    s = clean_text(x)
    out: list[str] = []
    for ch in s:
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
    if x is None or x == "":
        return "--"
    if isinstance(x, int):
        return f"{x:,}"
    if isinstance(x, float):
        return f"{x:.{nd}f}"
    return tex_escape(x)


def pct(x: float, nd: int = 1) -> str:
    return f"{100*x:.{nd}f}"


def copy(src: Path, dst: Path) -> dict[str, Any]:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return {"source": str(src), "dest": str(dst), "bytes": dst.stat().st_size, "sha256": sha256(dst)}


def itemize(lines: list[str]) -> str:
    return "\\begin{itemize}\n" + "\n".join(f"\\item {line}" for line in lines) + "\n\\end{itemize}\n"


def selection_table(selection: dict[str, Any]) -> str:
    rows = []
    for rec in selection["stage_counts"]:
        cached = rec.get("cached_sample_count_at_matching_stage") or "--"
        rows.append(
            f"{tex_escape(rec['stage_label'])} & {fmt(rec['sdss_dr17_count'])} & {fmt(cached)} & {fmt(rec.get('retention_vs_spectro_z_parent'), 3)} " + r"\\"
        )
    return "\n".join(rows)


def common_bibliography(extra: str = "") -> str:
    return r"""
\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
""" + extra + "\\end{thebibliography}\n"


def flagship_tex(selection: dict[str, Any], represent: dict[str, Any], rp1: dict[str, Any], gmatch: dict[str, Any], gbpt: dict[str, Any]) -> str:
    base = gmatch["key_results"]["rp1_baseline_bpt_agn_sn3_nearest_replacement"]
    cal = gmatch["key_results"]["rp1_mass_z_moderate_caliper"]
    norepl = gmatch["key_results"]["rp1_greedy_without_replacement"]
    sn10 = gbpt["matched_bpt_agn_sn10"]
    sey = gbpt["matched_nii_seyfert_like_proxy_sn3"]
    rows = [
        ("Broad BPT AGN, S/N$\\geq3$, nearest SF control with replacement", base["matched_pairs"], base["median_delta_log_sSFR"], base.get("median_delta_ci95_low"), base.get("median_delta_ci95_high"), "Preferred association estimate"),
        ("Moderate mass--redshift caliper", cal["matched_pairs"], cal["median_delta_log_sSFR"], None, None, "96.6% target coverage"),
        ("Greedy no-replacement stress test", norepl["matched_pairs"], norepl["median_delta_log_sSFR"], None, None, "Poorer balance; diagnostic only"),
        ("Broad BPT AGN, S/N$\\geq10$", sn10["matched_pairs"], sn10["median_delta_log_sSFR_target_minus_control"], None, None, "Line-S/N sensitivity"),
        ("N II Seyfert-like proxy, S/N$\\geq3$", sey["matched_pairs"], sey["median_delta_log_sSFR_target_minus_control"], None, None, "Subclass sensitivity"),
    ]
    robust_rows = []
    for label, n, val, lo, hi, note in rows:
        ci = f"[{fmt(lo)},{fmt(hi)}]" if lo is not None and hi is not None else "--"
        robust_rows.append(f"{label} & {fmt(n)} & {fmt(val)} & {ci} & {tex_escape(note)} " + r"\\")
    red = represent["dimension_summary"]["redshift"]
    mass = represent["dimension_summary"]["stellar_mass"]
    ssfr = represent["dimension_summary"]["ssfr"]
    return rf"""\documentclass[twocolumn]{{aastex631}}
\usepackage{{amsmath}}
\usepackage{{booktabs}}
\shorttitle{{Selection-aware SDSS optical AGN/sSFR pilot}}
\shortauthors{{NebulaMind local decision package}}
\begin{{document}}

\title{{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Pilot}}
\author{{NebulaMind Research Autopilot}}
\affiliation{{Local reproducible decision package; public SDSS DR17 data only}}

\begin{{abstract}}
We present a local, selection-aware SDSS DR17 pilot measuring the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of {fmt(selection['strict_sdss_sn_ge_3_total'])} galaxies. Broad BPT optical AGN hosts are matched to star-forming controls in stellar mass and redshift. The preferred matched comparison yields {fmt(base['matched_pairs'])} pairs and a median $\Delta\log {{\rm sSFR}}$ of {fmt(base['median_delta_log_sSFR'])} dex, with a bootstrap interval of [{fmt(base.get('median_delta_ci95_low'))},{fmt(base.get('median_delta_ci95_high'))}] dex. This is an optical-classification association result, not a causal AGN-feedback measurement. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude, so subclass and selection-function treatment must precede any physical interpretation.
\end{{abstract}}

\keywords{{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}}

\section{{Question and claim boundary}}
This polished local draft is the flagship output from the nine-paper Galaxy Evolution integration. It asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT optical AGN hosts have lower catalog sSFR than mass--redshift matched star-forming controls? The answer is yes for the cached denominator analyzed here. The result does not establish causal AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.

The claim boundary is part of the result. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and LINER-like ionization can contaminate broad low-ionization classes \citep{{stasinska2008,stasinska2015}}. Therefore the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.

\section{{Data and shared selection}}
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{{york2000,sdssdr17,brinchmann2004}}. The cached analysis table is capped at {fmt(selection['cached_rows'])} rows and ordered by \texttt{{specObjID}}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains {fmt(selection['strict_sdss_sn_ge_3_total'])} rows, so the cache covers {pct(selection['cached_coverage_of_strict_sdss_sn_ge_3'])}\% of that strict parent.

\begin{{deluxetable*}}{{lrrr}}
\tabletypesize{{\scriptsize}}
\tablecaption{{Selection cascade for the flagship denominator.\label{{tab:selection}}}}
\tablehead{{\colhead{{Selection stage}} & \colhead{{Public DR17 rows}} & \colhead{{Cached rows}} & \colhead{{Retention vs. spectro-z parent}}}}
\startdata
{selection_table(selection)}
\enddata
\tablecomments{{Counts are read-only public SDSS DR17 count queries plus the local cached CSV. Cached rows are shown only where the cache applies.}}
\end{{deluxetable*}}

The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps {pct(selection['ssfr_low_bin_reference']['sn_ge_3_retention_vs_parent'], 1)}\% of the $-12<\log {{\rm sSFR}}<-11$ parent bin but {pct(selection['ssfr_star_forming_bin_reference']['sn_ge_3_retention_vs_parent'], 1)}\% of the $-10<\log {{\rm sSFR}}<-9.5$ bin. Cached-versus-public marginal checks show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are {fmt(red['max_abs_fraction_difference_pp'],2)}, {fmt(mass['max_abs_fraction_difference_pp'],2)}, and {fmt(ssfr['max_abs_fraction_difference_pp'],2)} percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.

\section{{Classification and matching}}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}}. The cached denominator contains {fmt(rp1['bpt_counts']['star-forming'])} star-forming galaxies, {fmt(rp1['bpt_counts']['intermediate'])} intermediate/composite galaxies, {fmt(rp1['bpt_counts']['agn'])} broad optical AGN, and {fmt(rp1['bpt_counts']['unclassified'])} unclassified objects. Each broad optical AGN host is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.

\begin{{figure*}}
\centering
\includegraphics[width=0.72\textwidth]{{../figures/fig-bpt.pdf}}
\caption{{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}}
\label{{fig:bpt}}
\end{{figure*}}

\section{{Matched-control result}}
The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the optical AGN hosts relative to star-forming controls.

\begin{{deluxetable*}}{{lrrrr}}
\tabletypesize{{\scriptsize}}
\tablecaption{{Robustness ladder for matched catalog-sSFR offsets.\label{{tab:robust}}}}
\tablehead{{\colhead{{Variant}} & \colhead{{$N$ pairs}} & \colhead{{Median $\Delta\log {{\rm sSFR}}$}} & \colhead{{95\% interval}} & \colhead{{Interpretation}}}}
\startdata
{chr(10).join(robust_rows)}
\enddata
\tablecomments{{$\Delta\log {{\rm sSFR}}$ is target minus matched star-forming control. All values are conditional on the optical emission-line denominator.}}
\end{{deluxetable*}}

\begin{{figure*}}
\centering
\includegraphics[width=0.86\textwidth]{{../figures/fig-matched-offsets.pdf}}
\caption{{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT AGN hosts minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions.}}
\label{{fig:offsets}}
\end{{figure*}}

\section{{Interpretation}}
The flagship result is a useful SDSS short-paper result because it is directly measured, reproducible, and falsifiable inside the stated denominator. The median offset is large and survives a moderate mass--redshift caliper. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude to roughly half the preferred broad-BPT estimate. That sensitivity means the safest wording is: broad optical BPT AGN classification is associated with lower catalog sSFR in this capped SDSS emission-line sample. Claims about causal quenching require additional data: morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

\section{{Conclusion}}
RP-1 should be the flagship paper from the current local package. It should be polished further as a concise, selection-aware association paper. The other eight active topics should be packaged as a supplementary denominator/proxy atlas, not as independent causal feedback papers, because their original claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables not present in the current SDSS-only analysis.

\section{{Local reproducibility}}
This PDF was generated by local decision package \texttt{{{tex_escape(OUT_ID)}}}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.

{common_bibliography()}
\end{{document}}
"""


def supplement_tex(selection: dict[str, Any], proxy_papers: list[dict[str, Any]]) -> str:
    sections = []
    for idx, p in enumerate(proxy_papers, 1):
        data = p["data"]
        bullets = [tex_escape(x) for x in data.get("result_bullets", [])]
        sections.append(rf"""
\subsection{{{tex_escape(p['title'])}}}
\textbf{{Measured SDSS question.}} {tex_escape(data.get('pilot_question', 'Bounded SDSS denominator/proxy question.'))}

\textbf{{Result summary.}}
{itemize(bullets)}

\textbf{{Missing observables for the full proposal.}} {tex_escape(data.get('full_proposal_requires', 'additional non-SDSS data'))}

\textbf{{Interpretation guard.}} {tex_escape(data.get('interpretation_guard', 'Guarded SDSS-only proxy or denominator.'))}

\begin{{figure}}
\centering
\includegraphics[width=\columnwidth]{{../figures/{p['fig_name']}}}
\caption{{SDSS optical denominator/proxy diagnostic for {tex_escape(p['slug'])}. This is a follow-up target definition or baseline, not a physical-feedback proof.}}
\label{{fig:{p['label']}}}
\end{{figure}}
""")
    return rf"""\documentclass[twocolumn]{{aastex631}}
\usepackage{{amsmath}}
\usepackage{{booktabs}}
\shorttitle{{SDSS denominator/proxy atlas}}
\shortauthors{{NebulaMind local decision package}}
\begin{{document}}

\title{{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up}}
\author{{NebulaMind Research Autopilot}}
\affiliation{{Local reproducible decision package; public SDSS DR17 data only}}

\begin{{abstract}}
This supplement packages the eight non-flagship Galaxy Evolution drafts as denominator/proxy notes rather than standalone physical-feedback papers. All notes share the same capped 60,000-row SDSS DR17 optical emission-line cache and the same selection-function caveats. The atlas preserves useful follow-up targets--environment proxies, optical AGN denominators, transition-mass vectors, tracer-threshold censuses, gas-follow-up denominators, and simulation target vectors--while explicitly refusing claims that require radio, X-ray, molecular/neutral gas, resolved outflow, halo/group, or simulation-mock data not analyzed here.
\end{{abstract}}

\keywords{{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}}

\section{{Purpose}}
The companion flagship paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are different: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. Keeping them in one supplement prevents overclaiming and gives future work a clean checklist of what must be added.

\section{{Shared denominator}}
The atlas uses the same cached public-data backbone as the flagship: {fmt(selection['cached_rows'])} cached rows from a strict public four-line S/N$\geq3$ parent of {fmt(selection['strict_sdss_sn_ge_3_total'])} rows, i.e. {pct(selection['cached_coverage_of_strict_sdss_sn_ge_3'])}\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped/non-random, so all counts and fractions are conditional denominators rather than population-complete measurements.

\begin{{deluxetable*}}{{lrrr}}
\tabletypesize{{\scriptsize}}
\tablecaption{{Selection cascade shared by the atlas.\label{{tab:supp-selection}}}}
\tablehead{{\colhead{{Selection stage}} & \colhead{{Public DR17 rows}} & \colhead{{Cached rows}} & \colhead{{Retention vs. spectro-z parent}}}}
\startdata
{selection_table(selection)}
\enddata
\end{{deluxetable*}}

\section{{Atlas notes}}
{chr(10).join(sections)}

\section{{Package decision}}
These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the flagship result. They are not suitable as eight standalone causal feedback papers in their current SDSS-only form.

\section{{Local reproducibility}}
This PDF was generated by local decision package \texttt{{{tex_escape(OUT_ID)}}}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.

{common_bibliography()}
\end{{document}}
"""


def main() -> None:
    manifest = read_json(RUN / "INTEGRATION_MANIFEST_PRECOMPILE.json")
    selection = read_json(Path(manifest["source_artifacts"]["selection_json"]))
    represent = read_json(Path(manifest["source_artifacts"]["representativeness_json"]))
    gmatch = read_json(Path(manifest["source_artifacts"]["goru_matching_json"]))
    gbpt = read_json(Path(manifest["source_artifacts"]["goru_bpt_json"]))
    OUT.mkdir(parents=True, exist_ok=True)

    flagship = next(p for p in manifest["papers"] if p["slug"] == "m1_rp1_sdss_agn_sfr")
    rp1 = read_json(Path(flagship["source_results_json"]))

    flag_dir = OUT / "flagship_rp1"
    flag_aas = flag_dir / "aastex"
    flag_fig = flag_dir / "figures"
    flag_aas.mkdir(parents=True, exist_ok=True)
    flag_fig.mkdir(parents=True, exist_ok=True)
    fig_copies = []
    fig_copies.append(copy(Path(flagship["figures"][0]["dest"]), flag_fig / "fig-bpt.pdf"))
    fig_copies.append(copy(Path(flagship["figures"][1]["dest"]), flag_fig / "fig-matched-offsets.pdf"))
    flag_tex = flag_aas / "rp1_flagship_polished.tex"
    flag_tex.write_text(flagship_tex(selection, represent, rp1, gmatch, gbpt))

    supp_dir = OUT / "supplementary_denominator_atlas"
    supp_aas = supp_dir / "aastex"
    supp_fig = supp_dir / "figures"
    supp_aas.mkdir(parents=True, exist_ok=True)
    supp_fig.mkdir(parents=True, exist_ok=True)
    proxy_papers = []
    for i, p in enumerate([x for x in manifest["papers"] if x["slug"] != "m1_rp1_sdss_agn_sfr"], 1):
        fig_name = f"topic-{i:02d}.pdf"
        fcopy = copy(Path(p["figures"][0]["dest"]), supp_fig / fig_name)
        proxy_papers.append({
            "slug": p["slug"],
            "title": p["title"],
            "status": p["status"],
            "data": read_json(Path(p["source_results_json"])),
            "fig_name": fig_name,
            "label": p["slug"].replace("_", "-"),
            "figure": fcopy,
        })
    supp_tex = supp_aas / "supplementary_denominator_atlas.tex"
    supp_tex.write_text(supplement_tex(selection, proxy_papers))

    package = {
        "package_id": OUT_ID,
        "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "decision": "one polished RP-1 flagship draft plus one supplementary denominator/proxy atlas for the other eight",
        "source_integration_run": str(RUN),
        "flagship": {
            "slug": flagship["slug"],
            "tex": str(flag_tex),
            "expected_pdf": str(flag_aas / "rp1_flagship_polished.pdf"),
            "figures": fig_copies,
        },
        "supplement": {
            "tex": str(supp_tex),
            "expected_pdf": str(supp_aas / "supplementary_denominator_atlas.pdf"),
            "topics": [{k: v for k, v in pp.items() if k not in {"data"}} for pp in proxy_papers],
        },
        "safety": "local-only files under handoff tree; no public/live/wiki/DB/deploy/git/cron/billing/OAuth/external submission changes",
    }
    (OUT / "PACKAGE_MANIFEST_PRECOMPILE.json").write_text(json.dumps(package, indent=2, sort_keys=True))
    (OUT / "README.md").write_text(
        f"# {OUT_ID}\n\n"
        "Decision package: one polished RP-1 flagship draft plus one supplementary denominator/proxy atlas.\n\n"
        "Compile with Tectonic from each aastex directory, then run package audit.\n"
    )
    print(json.dumps({"package_id": OUT_ID, "out": str(OUT), "flagship_tex": str(flag_tex), "supplement_tex": str(supp_tex)}, indent=2))


if __name__ == "__main__":
    main()
