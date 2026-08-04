import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot")
BASE = ROOT / "dr-revised-20260714"
ROUND1 = BASE / "round1"
ROUND2 = BASE / "round2"
RECEIPTS = ROUND2 / "receipts"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: expected one replacement anchor, found {text.count(old)}")
    return text.replace(old, new, 1)


def invariant_lines_preserved(source: str, revised: str, required_lines: list[str]) -> bool:
    source_lines = source.splitlines()
    revised_lines = revised.splitlines()
    for line in required_lines:
        if source_lines.count(line) != 1 or revised_lines.count(line) != 1:
            return False
    return True


PAPER1_INVARIANTS = [
    "All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\\% of that strict parent. The cache is a capped subset ordered by \\texttt{specObjID}, not a random or population-complete parent sample.",
    "SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\\\",
    "plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\\\",
    "plus galSpecLine join & 416,554 & -- & 0.831 \\\\",
    "four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\\\",
    "four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\\\",
    "four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\\\",
    "four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\\\",
    "The four-line requirement is strongly selection dependent. In the public counts, S/N$\\geq3$ keeps 33.6\\% of the $-12<\\log {\\rm sSFR}<-11$ parent bin but 94.9\\% of the $-10<\\log {\\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.",
    "Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.",
    "BPT classes are computed from H$\\alpha$, H$\\beta$, [O~III]$\\lambda5007$, and [N~II]$\\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \\citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. The cached analysis table contains 39,553 star-forming galaxies, 12,234 intermediate/composite objects, 8,146 broad optical AGN, and 67 unclassified objects.",
    "\\item Broad BPT optical AGN vs. star-forming controls at S/N$\\geq3$: $N=8,146$ matched pairs, median $\\Delta\\log {\\rm sSFR}=-1.309$ dex with 95\\% bootstrap interval $[-1.334,-1.283]$ dex.",
    "\\item Moderate mass-redshift caliper $|\\Delta\\log M_\\star|\\leq0.05$, $|\\Delta z|\\leq0.002$: $N=7,867$ retained pairs (96.6\\% target coverage), median offset -1.318 dex.",
    "\\item A deterministic no-replacement diagnostic uses $N=7,419$ pairs and gives median offset -1.446 dex, but with visibly poorer mass balance; it is a stress test, not the preferred estimator.",
    "\\item Raising the line-S/N threshold to 10 leaves $N=1,530$ matched pairs and reduces the median offset to -0.744 dex, showing sensitivity to the emission-line selection function.",
    "\\item A narrower [N II] Seyfert-like proxy gives $N=2,114$ pairs and median offset -0.763 dex, reinforcing that subclass definitions change the effect size.",
]

PAPER2_INVARIANTS = [
    PAPER1_INVARIANTS[0],
    *PAPER1_INVARIANTS[1:10],
    "\\item The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy.",
    "\\item The high-density quartile has quenched fraction 0.230 (3,456/15,000); the low-density quartile has 0.181 (2,710/15,000).",
    "\\item The bootstrap high-minus-low quenched-fraction interval is [0.041, 0.059].",
    "\\item A linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004.",
]


def build_paper1() -> dict:
    paper_id = "paper_01"
    source_path = ROUND1 / f"{paper_id}_r1.tex"
    review_path = ROUND1 / "dr-review-packets" / f"{paper_id}_round1_review_dr_packet.md"
    output_path = ROUND2 / f"{paper_id}_r2.tex"
    source = source_path.read_text()
    revised = source

    revised = replace_once(
        revised,
        "before interpreting the topic-specific measurement.",
        "before evaluating the fidelity and selection dependence of the topic-specific measurement.",
        f"{paper_id} abstract",
    )
    revised = replace_once(
        revised,
        "The large negative offset is robust within the optical emission-line subset but remains selection- and subclass-dependent.",
        "The negative catalog offset persists across the baseline matching diagnostics but changes substantially with the emission-line signal-to-noise threshold and optical subclass definition; it is therefore a selection-conditional association, not uniform physical quenching.",
        f"{paper_id} figure caption",
    )
    old_section = r"""\section{Deep Research literature integration: aperture and classification limits}\label{sec:dr-r1}
Fixed-aperture spectroscopy does not by itself establish a global star-formation state. Empirical SDSS aperture-correction work and spatially resolved MaNGA profiles show why central and galaxy-wide star-formation diagnostics must be distinguished \citep{duartepuertas2017,belfiore2018}. These studies therefore sharpen, rather than relax, the existing boundary: the matched catalog-sSFR offset remains an association inside the selected optical denominator and cannot be read as a measurement of galaxy-wide quenching.

The broad BPT branch also mixes excitation sources. Equivalent-width information such as the WHAN framework can separate weak accretion candidates from systems whose low-ionization emission is compatible with retired stellar populations \citep{cidfernandes2011}. A later physical analysis should therefore add aperture fraction, resolved structure, and equivalent-width controls before interpreting the optical subclasses; none of those missing observables is supplied by the present SDSS-only pilot.
"""
    new_section = r"""\section{Deep Research literature integration: aperture, classification, and estimator limits}\label{sec:dr-r1}
Fixed-aperture spectroscopy does not by itself establish a global star-formation state. Empirical SDSS aperture-correction work, CALIFA-based aperture tests, and spatially resolved MaNGA profiles show why central and galaxy-wide stellar-population and star-formation diagnostics must be distinguished \citep{duartepuertas2017,zibetti2026,belfiore2018}. The 3-arcsec SDSS fibre samples a central, morphology-dependent region rather than an invariant fraction of each galaxy. These studies therefore sharpen, rather than relax, the existing boundary: the matched catalog-sSFR offset remains an association inside the selected optical denominator and cannot be read as a measurement of galaxy-wide quenching.

The broad BPT branch also mixes excitation sources. Equivalent-width information such as the WHAN framework can separate weak accretion candidates from systems whose low-ionization emission is compatible with retired stellar populations \citep{cidfernandes2011}. Strong-line SFR work in AGN-ionized regions likewise requires explicit separation of AGN and H~II-region contributions before an optical line luminosity is interpreted as star formation \citep{demellos2024}. A later physical analysis should therefore add aperture fraction, resolved structure, equivalent-width controls, and excitation decomposition before interpreting the optical subclasses; none of those missing observables is supplied by the present SDSS-only pilot.

A spatially resolved MaNGA comparison using young stellar populations rather than standard emission-line SFR proxies reports higher nuclear recent star formation in its AGN hosts than in matched controls \citep{gatto2025}. The different sample and estimator do not determine the physical explanation for this draft's catalog offset. They do show that the sign and magnitude are not estimator-independent, so the present result cannot distinguish genuine host-wide suppression from aperture, excitation, population, or catalog-model systematics.
"""
    revised = replace_once(revised, old_section, new_section, f"{paper_id} review section")
    revised = replace_once(
        revised,
        "The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.",
        "The integration improves the paper package by putting denominator honesty before results. For RP-1, the catalog assigns lower sSFR to broad optical BPT AGN hosts than to mass--redshift matched star-forming controls inside this capped, four-line-selected subset. The offset is strongly selection-, subclass-, aperture-, and estimator-dependent; without resolved star-formation and excitation controls it is not evidence that AGN activity caused host-wide quenching. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.",
        f"{paper_id} conclusion",
    )
    bibitems = r"""
\bibitem[Zibetti et al.(2026)]{zibetti2026} Zibetti, S., Pratesi, J., Gallazzi, A.~R., et al. 2026, A\&A, 708, A13
\bibitem[de Mellos et al.(2024)]{demellos2024} de Mellos, M.~S.~Z., Riffel, R.~A., Schimoia, J.~S., et al. 2024, MNRAS, 535, 123
\bibitem[Gatto et al.(2025)]{gatto2025} Gatto, L., Storchi-Bergmann, T., Riffel, R.~A., et al. 2025, MNRAS, 539, 3229
"""
    revised = replace_once(revised, "\\end{thebibliography}", bibitems + "\\end{thebibliography}", f"{paper_id} bibliography")

    if not invariant_lines_preserved(source, revised, PAPER1_INVARIANTS):
        raise RuntimeError(f"{paper_id}: one or more measured invariant lines changed")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(revised)

    selected = [
        {"citation_key": "zibetti2026", "citation": "Zibetti et al. (2026), A&A, 708, A13", "identifier": "DOI:10.1051/0004-6361/202557018; arXiv:2508.19462", "role": "interpretation-caveat", "claim_boundary": "central-fibre stellar-population measurements require aperture-aware interpretation; no claim that the present offset is wholly an aperture artifact"},
        {"citation_key": "demellos2024", "citation": "de Mellos et al. (2024), MNRAS, 535, 123", "identifier": "DOI:10.1093/mnras/stae2352; arXiv:2410.06297", "role": "method-support", "claim_boundary": "AGN/H II excitation separation is required for strong-line SFR use; no recalculation of the SDSS catalog values"},
        {"citation_key": "gatto2025", "citation": "Gatto et al. (2025), MNRAS, 539, 3229", "identifier": "DOI:10.1093/mnras/staf669", "role": "contradiction", "claim_boundary": "different MaNGA sample/estimator demonstrates estimator dependence; it does not prove the SDSS offset is an artifact"},
    ]
    skipped = [
        {"source": "Mattolini et al. (2025)", "reason": "not required after the existing mass-model and aperture boundaries; review-specific systematic numbers were not independently settled locally"},
        {"source": "Pulatova et al. (2025)", "reason": "the advisory packet both proposed and later explicitly skipped this source; no new kinematic-decomposition claim was needed"},
        {"source": "Wild et al. (2025)", "reason": "far-infrared discussion is outside the optical-only data boundary and was explicitly marked SKIP"},
        {"source": "advisory 'catalog-derived illusion' wording", "reason": "overstated causality; replaced with estimator-dependence language consistent with the actual data"},
    ]
    return write_receipt(paper_id, source_path, review_path, output_path, selected, skipped, ["abstract framing", "matched-offset figure caption", "DR literature section", "conclusion", "bibliography"], PAPER1_INVARIANTS)


def build_paper2() -> dict:
    paper_id = "paper_02"
    source_path = ROUND1 / f"{paper_id}_r1.tex"
    review_path = ROUND1 / "dr-review-packets" / f"{paper_id}_round1_review_dr_packet.md"
    output_path = ROUND2 / f"{paper_id}_r2.tex"
    source = source_path.read_text()
    revised = source

    revised = replace_once(
        revised,
        "\\end{itemize}\n\n\n\\begin{figure}",
        "\\end{itemize}\n\nHere, ``quenched fraction'' is an operational catalog fraction within the four-line-capable emission-line denominator. It excludes many classically passive, line-weak systems and must not be interpreted as the total quenched fraction of the low-redshift galaxy population.\n\n\\begin{figure}",
        f"{paper_id} operational definition",
    )
    old_section = r"""\section{Deep Research literature integration: density-proxy limits}\label{sec:dr-r1}
Projected neighbour ranks are useful empirical environment coordinates, but their physical interpretation depends on spectroscopic completeness and projection. SDSS light-cone work documents that fibre assignment can remove close angular pairs, so a nearest-neighbour statistic in a spectroscopic sample must not be treated as an unbiased reconstruction of the densest environments \citep{dongpaez2024}. This caveat applies to the proxy, not to the unchanged high-minus-low comparison reported above.

Separating ram pressure, starvation, and preprocessing requires more than a projected rank. Group/cluster studies use central--satellite classification and projected phase space to connect galaxy location to an infall history \citep{oxland2024}. Those quantities are absent here. The present result therefore remains a mass-adjusted association within the emission-line denominator and is a target-selection input for a later halo- and phase-space-resolved analysis.
"""
    new_section = r"""\section{Deep Research literature integration: density-proxy limits}\label{sec:dr-r1}
Projected neighbour ranks are useful empirical environment coordinates, but their physical interpretation depends on spectroscopic completeness and projection. SDSS light-cone work documents that fibre assignment can remove close angular pairs, so a nearest-neighbour statistic in a spectroscopic sample must not be treated as an unbiased reconstruction of the densest environments \citep{dongpaez2024}. Because incompleteness can change which galaxies occupy each rank, the high-minus-low result is a comparison between observable spectroscopic density quartiles, not between unbiased absolute physical-density bins.

The physical scale represented by a fixed neighbour rank also changes with catalog sparsity. The published correction to the SDSS--simulation comparison notes that nearest-neighbour ranks are not automatically like-for-like between a mass-incomplete observed catalog and a complete simulated catalog \citep{goubert2024,goubert2024corr}. A scalar rank is additionally blind to whether a galaxy lies in a sheet, filament, or node \citep{nandi2025}. These limitations do not establish the direction or size of any bias in the measured quartile contrast, and no lower-limit claim is made here.

Local density can remain a useful first-order empirical coordinate when mass is controlled, even though it is not a complete physical environment model \citep{okane2024}. Separating ram pressure, starvation, preprocessing, and infall stage requires central--satellite classification and projected phase space rather than a static rank alone \citep{oxland2024,sampaio2024}. Those quantities are absent here. The present result therefore remains a mass-adjusted association within the emission-line denominator and is a target-selection input for a later halo- and phase-space-resolved analysis.
"""
    revised = replace_once(revised, old_section, new_section, f"{paper_id} review section")
    revised = replace_once(
        revised,
        "The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.",
        "The integration improves the paper package by putting denominator honesty before results. For this environmental-proxy draft, the high- and low-density quartiles are relative ranks inside a sparse, four-line-selected spectroscopic denominator. Their mass-adjusted difference is an association for target design, not a total-population quenched fraction, an absolute density calibration, or evidence for a particular environmental mechanism.",
        f"{paper_id} conclusion",
    )
    revised = replace_once(
        revised,
        "\\bibitem[Goubert et al.(2024)]{goubert2024} Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \\& Maiolino, R. 2024, arXiv:2401.12953",
        "\\bibitem[Goubert et al.(2024a)]{goubert2024} Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \\& Maiolino, R. 2024a, MNRAS, 528, 4891",
        f"{paper_id} original Goubert bibliography",
    )
    bibitems = r"""
\bibitem[Goubert et al.(2024b)]{goubert2024corr} Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2024b, MNRAS, 532, 3556
\bibitem[Nandi \& Pandey(2025)]{nandi2025} Nandi, A., \& Pandey, B. 2025, arXiv e-prints, arXiv:2507.18614
\bibitem[O'Kane et al.(2024)]{okane2024} O'Kane, C.~J., Kuchner, U., Gray, M.~E., \& Aragón-Salamanca, A. 2024, MNRAS, 534, 1682
\bibitem[Sampaio et al.(2024)]{sampaio2024} Sampaio, V.~M., de Carvalho, R.~R., Aragón-Salamanca, A., et al. 2024, MNRAS, 532, 982
"""
    revised = replace_once(revised, "\\end{thebibliography}", bibitems + "\\end{thebibliography}", f"{paper_id} bibliography")

    if not invariant_lines_preserved(source, revised, PAPER2_INVARIANTS):
        raise RuntimeError(f"{paper_id}: one or more measured invariant lines changed")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(revised)

    selected = [
        {"citation_key": "goubert2024corr", "citation": "Goubert et al. (2024), MNRAS, 532, 3556", "identifier": "DOI:10.1093/mnras/stae1667", "role": "interpretation-caveat", "claim_boundary": "neighbour-rank scale differs between incomplete observations and complete simulations; no lower-limit claim"},
        {"citation_key": "nandi2025", "citation": "Nandi & Pandey (2025), arXiv:2507.18614", "identifier": "arXiv:2507.18614", "role": "interpretation-caveat", "claim_boundary": "scalar density is topologically incomplete; the preprint is not used for a quantitative correction"},
        {"citation_key": "okane2024", "citation": "O'Kane et al. (2024), MNRAS, 534, 1682", "identifier": "DOI:10.1093/mnras/stae2142", "role": "method-support", "claim_boundary": "local density is a useful first-order coordinate after matching, not a complete environment model"},
        {"citation_key": "sampaio2024", "citation": "Sampaio et al. (2024), MNRAS, 532, 982", "identifier": "DOI:10.1093/mnras/stae1533", "role": "future-data-motivation", "claim_boundary": "projected phase space is required for infall-stage interpretation; no mechanism inferred here"},
    ]
    skipped = [
        {"source": "Atalebe (2026)", "reason": "non-peer-reviewed preprint and unnecessary speculative terminology; structural confounding is already acknowledged without this source"},
        {"source": "Montaguth et al. (2025)", "reason": "identifier details were inconsistent across the advisory narrative and captured packet; omitted rather than silently repaired"},
        {"source": "advisory lower-limit interpretation", "reason": "the sign and size of fibre-collision bias are not established by this local analysis, so no lower-limit claim was added"},
        {"source": "specific ram-pressure/starvation causal narrative", "reason": "missing phase-space and halo data; explicitly held as future work"},
    ]
    return write_receipt(paper_id, source_path, review_path, output_path, selected, skipped, ["operational quenched-fraction definition", "DR density-proxy section", "conclusion", "Goubert bibliography correction", "new bibliography entries"], PAPER2_INVARIANTS)


def write_receipt(paper_id: str, source_path: Path, review_path: Path, output_path: Path, selected: list[dict], skipped: list[dict], changes: list[str], invariants: list[str]) -> dict:
    receipt = {
        "paper_id": paper_id,
        "round": 2,
        "writer": "Tori",
        "source_round1_tex": str(source_path),
        "source_round1_tex_sha256": sha(source_path),
        "source_round1_dr_review": str(review_path),
        "source_round1_dr_review_sha256": sha(review_path),
        "output_tex": str(output_path),
        "output_tex_sha256": sha(output_path),
        "measured_invariant_line_count": len(invariants),
        "measured_invariants_preserved_exact": invariant_lines_preserved(source_path.read_text(), output_path.read_text(), invariants),
        "analysis_measurements_recomputed": False,
        "review_feedback_applied": changes,
        "added_or_corrected_sources": selected,
        "skipped_review_sources_or_claims": skipped,
        "association_not_causal": True,
        "real_data_only": True,
        "drafts_only": True,
        "local_only": True,
        "browser_or_account_touched": False,
        "broker_touched": False,
        "publish_commit_git_performed": False,
        "generated_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    receipt_path = RECEIPTS / f"{paper_id}_sources.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
    note = (
        f"# {paper_id} round-2 revision\n\n"
        f"- Writer: Tori\n"
        f"- Input round-1 SHA-256: `{receipt['source_round1_tex_sha256']}`\n"
        f"- DR review SHA-256: `{receipt['source_round1_dr_review_sha256']}`\n"
        f"- Output: `{output_path}`\n"
        f"- Output SHA-256: `{receipt['output_tex_sha256']}`\n"
        f"- Exact measured invariant lines checked: {len(invariants)}; preserved: `{receipt['measured_invariants_preserved_exact']}`.\n"
        f"- Applied: {', '.join(changes)}.\n"
        f"- Added/corrected source keys: `{', '.join(row['citation_key'] for row in selected)}`.\n"
        f"- Skipped review sources/claims: {len(skipped)} with reasons in the JSON receipt.\n"
        "- No measured value was recomputed or replaced; the edits tighten claim boundaries and add review-grounded context only.\n"
        "- Local draft only: no browser, account, Deep Research, broker, DB, wiki, deploy, publish, commit, or git action.\n"
    )
    (RECEIPTS / f"{paper_id}_revision.md").write_text(note)
    return {"paper_id": paper_id, "output": str(output_path), "sha256": receipt["output_tex_sha256"], "selected_sources": len(selected), "skipped": len(skipped)}


def main() -> None:
    generated = [build_paper1(), build_paper2()]
    print(json.dumps({"status": "TORI_ACCOUNT_SAFE_ROUND2_01_02_COMPLETE", "generated": generated}, sort_keys=True))


if __name__ == "__main__":
    main()
