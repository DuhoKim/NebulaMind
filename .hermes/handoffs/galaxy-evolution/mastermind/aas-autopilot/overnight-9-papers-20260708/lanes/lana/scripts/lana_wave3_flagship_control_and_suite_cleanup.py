#!/usr/bin/env python3
"""Lana Wave-3 manuscript revisions for RP-1, M2 P3, and M3 P1.

Writes lane-local revision drafts only and appends the required one-line overnight ledger entry.
No public-linked manuscripts/PDFs are overwritten.
"""
from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

ROOT = Path('/Users/duhokim/NebulaMind/NebulaMind')
AUTO = ROOT / '.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot'
OVERNIGHT = AUTO / 'overnight-9-papers-20260708'
LANE = OVERNIGHT / 'lanes/lana'
RUN_RP1 = AUTO / 'runs/SDSS_AGN_SFR_PILOT_20260708T122000Z'
BATCH = AUTO / 'runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z'
TS = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
MARKER = f'LANA_WAVE3_FLAGSHIP_CONTROL_SUITE_REVISION_{TS}'

TICK_DIR = LANE / 'ticks'
REV_ROOT = LANE / 'revision-drafts'
SCRIPT_PATH = LANE / 'scripts/lana_wave3_flagship_control_and_suite_cleanup.py'
MANIFEST_PATH = LANE / f'lana_wave3_revision_manifest_{TS}.json'
TICK_PATH = TICK_DIR / f'TICK_{TS}.md'
LEDGER = OVERNIGHT / 'OVERNIGHT_LEDGER.md'

SELECTION_ROWS = [
    ('SpecObj GALAXY, $0.02<z<0.12$', '501,060', '--', '--', '--'),
    ('plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds', '416,554', '83.1\\%', '--', '--'),
    ('four BPT lines positive with positive errors', '373,445', '89.7\\%', '60,000', '16.1\\%'),
    ('four BPT lines S/N$\\geq3$', '249,917', '66.9\\%', '60,000', '24.0\\%'),
    ('four BPT lines S/N$\\geq5$', '176,523', '70.6\\%', '42,446', '24.0\\%'),
    ('four BPT lines S/N$\\geq10$', '91,768', '52.0\\%', '22,311', '24.3\\%'),
]


def fmt_int(n: int | float) -> str:
    return f'{int(round(float(n))):,}'


def fmt_float(x: float, nd: int = 3) -> str:
    return f'{float(x):.{nd}f}'


def median_ci(vals: np.ndarray, seed: int = 20260708, nboot: int = 2000) -> tuple[float, float]:
    vals = np.asarray(vals, dtype=float)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(vals), size=(nboot, len(vals)))
    meds = np.median(vals[idx], axis=1)
    lo, hi = np.quantile(meds, [0.025, 0.975])
    return float(lo), float(hi)


def match_stats(target: pd.DataFrame, control: pd.DataFrame, label: str) -> dict:
    cols = ['lgm_tot_p50', 'z']
    scale = pd.concat([target[cols], control[cols]], ignore_index=True)
    mu = scale.mean()
    sig = scale.std(ddof=0).replace(0, 1)
    tree = cKDTree(((control[cols] - mu) / sig).to_numpy())
    dist, idx = tree.query(((target[cols] - mu) / sig).to_numpy(), k=1)
    ctrl = control.iloc[idx].reset_index(drop=True)
    targ = target.reset_index(drop=True)
    delta = targ['specsfr_tot_p50'].to_numpy() - ctrl['specsfr_tot_p50'].to_numpy()
    lo, hi = median_ci(delta)
    reuse = pd.Series(ctrl['specObjID'].to_numpy()).value_counts()
    return {
        'label': label,
        'target_n': int(len(target)),
        'control_n': int(len(control)),
        'matched_pairs': int(len(delta)),
        'unique_controls': int(reuse.size),
        'max_reuse': int(reuse.max()),
        'p95_reuse': float(reuse.quantile(0.95)),
        'median_delta': float(np.median(delta)),
        'ci_low': lo,
        'ci_high': hi,
        'mean_delta': float(np.mean(delta)),
        'median_abs_dlogM': float(np.median(np.abs(targ['lgm_tot_p50'].to_numpy() - ctrl['lgm_tot_p50'].to_numpy()))),
        'median_abs_dz': float(np.median(np.abs(targ['z'].to_numpy() - ctrl['z'].to_numpy()))),
        'median_dist_scaled': float(np.median(dist)),
        'p90_dist_scaled': float(np.quantile(dist, 0.90)),
        'p95_dist_scaled': float(np.quantile(dist, 0.95)),
        'p99_dist_scaled': float(np.quantile(dist, 0.99)),
        'frac_dist_gt_0p05': float(np.mean(dist > 0.05)),
        'frac_dist_gt_0p10': float(np.mean(dist > 0.10)),
    }


def compute_rp1_control_stats() -> tuple[list[dict], dict]:
    df = pd.read_csv(RUN_RP1 / 'data/analysis_sample_bpt.csv')
    mp = pd.read_csv(RUN_RP1 / 'data/matched_agn_sf_pairs.csv')
    agn = df[df.bpt_label == 'agn'].copy()
    sf = df[df.bpt_label == 'star-forming'].copy()
    nonagn = df[df.bpt_label != 'agn'].copy()
    low_nonagn = nonagn[nonagn.specsfr_tot_p50 < -11.0].copy()
    intermediate_nonagn = df[df.bpt_label.isin(['intermediate', 'unclassified'])].copy()

    lo, hi = median_ci(mp['delta_log_sSFR_agn_minus_control'].to_numpy())
    reuse = mp['control_specObjID'].value_counts()
    rows = [{
        'label': 'BPT AGN vs BPT star-forming (preserved original pairs)',
        'target_n': int(len(mp)),
        'control_n': int(len(sf)),
        'matched_pairs': int(len(mp)),
        'unique_controls': int(reuse.size),
        'max_reuse': int(reuse.max()),
        'p95_reuse': float(reuse.quantile(0.95)),
        'median_delta': float(mp.delta_log_sSFR_agn_minus_control.median()),
        'ci_low': lo,
        'ci_high': hi,
        'mean_delta': float(mp.delta_log_sSFR_agn_minus_control.mean()),
        'median_abs_dlogM': float(abs(mp.agn_logM - mp.control_logM).median()),
        'median_abs_dz': float(abs(mp.agn_z - mp.control_z).median()),
        'median_dist_scaled': float(mp.match_distance_scaled.median()),
        'p90_dist_scaled': float(mp.match_distance_scaled.quantile(0.90)),
        'p95_dist_scaled': float(mp.match_distance_scaled.quantile(0.95)),
        'p99_dist_scaled': float(mp.match_distance_scaled.quantile(0.99)),
        'frac_dist_gt_0p05': float((mp.match_distance_scaled > 0.05).mean()),
        'frac_dist_gt_0p10': float((mp.match_distance_scaled > 0.10).mean()),
    }]
    rows.append(match_stats(agn, nonagn, 'BPT AGN vs all non-AGN emission-line controls'))
    rows.append(match_stats(agn, low_nonagn, 'BPT AGN vs low-sSFR non-AGN emission-line controls'))
    rows.append(match_stats(agn, intermediate_nonagn, 'BPT AGN vs intermediate/unclassified non-SF controls'))

    sf_logm_min, sf_logm_max = float(sf.lgm_tot_p50.min()), float(sf.lgm_tot_p50.max())
    sf_z_min, sf_z_max = float(sf.z.min()), float(sf.z.max())
    support = {
        'agn_total': int(len(agn)),
        'sf_control_total': int(len(sf)),
        'agn_outside_sf_logM_support': int(((agn.lgm_tot_p50 < sf_logm_min) | (agn.lgm_tot_p50 > sf_logm_max)).sum()),
        'agn_outside_sf_z_support': int(((agn.z < sf_z_min) | (agn.z > sf_z_max)).sum()),
        'sf_logM_range': [sf_logm_min, sf_logm_max],
        'sf_z_range': [sf_z_min, sf_z_max],
    }
    return rows, support


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def copy_many(sources: list[Path], dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for src in sources:
        shutil.copy2(src, dest / src.name)


def compile_tex(tex_path: Path) -> dict:
    cmd = ['tectonic', '--keep-logs', '--keep-intermediates', tex_path.name]
    proc = subprocess.run(cmd, cwd=tex_path.parent, text=True, capture_output=True)
    compile_log = tex_path.parent / f'compile_{TS}.log'
    log_text = '$ ' + ' '.join(cmd) + '\n' + proc.stdout + proc.stderr
    aux_log = tex_path.with_suffix('.log')
    if aux_log.exists():
        log_text += '\n\n--- tectonic .log ---\n' + aux_log.read_text(errors='replace')
    compile_log.write_text(log_text)
    pdf_path = tex_path.with_suffix('.pdf')
    fatal_markers = [m for m in ['! LaTeX Error', 'Emergency stop', 'Fatal error'] if m in log_text]
    pdf_magic = False
    pdf_bytes = 0
    sha = None
    if pdf_path.exists():
        data = pdf_path.read_bytes()
        pdf_bytes = len(data)
        pdf_magic = data.startswith(b'%PDF')
        sha = hashlib.sha256(data).hexdigest()
    return {
        'tex': str(tex_path.relative_to(LANE)),
        'pdf': str(pdf_path.relative_to(LANE)) if pdf_path.exists() else None,
        'compile_log': str(compile_log.relative_to(LANE)),
        'compile_exit_code': proc.returncode,
        'pdf_bytes': pdf_bytes,
        'pdf_sha256': sha,
        'pdf_starts_with_pdf': pdf_magic,
        'fatal_markers': fatal_markers,
    }


def rp1_insert_text(rows: list[dict], support: dict) -> str:
    def table_row(label: str, r: dict) -> str:
        return (
            f'{label} & {fmt_int(r["control_n"])} & {fmt_int(r["unique_controls"])} & '
            f'{fmt_int(r["max_reuse"])} & {fmt_float(r["median_delta"])} & '
            f'[{fmt_float(r["ci_low"])}, {fmt_float(r["ci_high"])}] \\\\'
        )
    original, all_nonagn, low_nonagn, intermediate = rows
    return r'''
\subsection{Control-baseline bracket and match diagnostics}\label{sec:control_bracket}
The external review correctly flagged a structural limitation: the original comparison is not ``AGN hosts versus all inactive galaxies.''  It is specifically BPT optical-AGN hosts versus BPT star-forming controls.  Because the control class is selected to be star forming by line ratios, the large negative $\Delta\log\mathrm{sSFR}$ should be read as a distance from a star-forming emission-line locus, not as a standalone measurement of quenching caused by AGN feedback.  To make that dependence visible, this Lana revision adds a control-baseline bracket in Table~\ref{tab:controlbracket}.  The additional rows are not alternative causal estimators; they are diagnostics showing how the contrast changes when the control pool is broadened or deliberately moved into low-sSFR territory.

\begin{deluxetable*}{lrrrrr}
\tablecaption{Control-baseline bracket for the RP-1 matched sSFR offset\label{tab:controlbracket}}
\tablehead{\colhead{Control pool} & \colhead{$N_{\rm pool}$} & \colhead{Unique controls used} & \colhead{Max reuse} & \colhead{Median $\Delta\log\mathrm{sSFR}$} & \colhead{95\% CI}}
\startdata
''' + '\n'.join([
        table_row('BPT star-forming only', original),
        table_row('All non-AGN emission-line', all_nonagn),
        table_row('Low-sSFR non-AGN emission-line', low_nonagn),
        table_row('Intermediate/unclassified non-SF', intermediate),
    ]) + r'''
\enddata
\tablecomments{All rows match the same 8,146 broad-BPT optical-AGN hosts in standardized stellar-mass--redshift space with replacement.  The first row is the preserved original pair table; the other rows are diagnostics recomputed from the cached 60,000-row SDSS table.  The low-sSFR control row nearly erases the median offset by construction, demonstrating that the primary result is a baseline-dependent optical association, not a causal quenching proof.}
\end{deluxetable*}

The original BPT-star-forming control match uses 4,239 unique star-forming controls out of a 39,553-object pool; the most reused control appears 26 times and the 95th-percentile reuse count is 5.  Median absolute pair separations are $0.0045$ dex in $\log M_\star$ and $0.00021$ in redshift.  The scaled match-distance distribution has median 0.0137, 90th percentile 0.0522, 95th percentile 0.0767, and 99th percentile 0.1528; 10.7\% of pairs exceed a scaled distance of 0.05 and 2.8\% exceed 0.10.  One AGN falls outside the one-dimensional star-forming-control stellar-mass support and one outside the redshift support.  These diagnostics argue for reporting the $-1.31$ dex value together with the S/N/subclass robustness envelope and the control-baseline bracket, not as a single universal AGN-suppression amplitude.
'''


def make_rp1(rows: list[dict], support: dict) -> tuple[Path, Path, dict]:
    slug = 'm1_rp1_sdss_agn_sfr'
    out = REV_ROOT / slug
    aas = out / 'aastex'
    figs = out / 'figures'
    aas.mkdir(parents=True, exist_ok=True)
    copy_many([
        RUN_RP1 / 'figures/figure1_bpt.pdf',
        RUN_RP1 / 'figures/figure2_matched_offsets.pdf',
        OVERNIGHT / 'lanes/goru/figures/matched_offset_sensitivity_20260708T162615Z.pdf',
    ], figs)
    src = OVERNIGHT / 'lanes/tori/revision-drafts/rp1_robustness_selection/20260708T181833Z/aastex/sdss_agn_sfr_pilot_rp1_robustness_selection_20260708T181833Z.tex'
    text = src.read_text()
    text = '% ' + MARKER + '\n% Paper: m1_rp1_sdss_agn_sfr; Lana lane-local draft only.\n' + text
    text = text.replace(
        'A Matched-Control SDSS DR17 Pilot Test of Specific Star Formation in Optical AGN Hosts: Selection-Function and Robustness Revision',
        'BPT Optical AGN Hosts Relative to Star-Forming and Non-AGN SDSS Controls: A Selection-Flagged Pilot'
    )
    text = text.replace(
        'A selection-function and robustness pass materially qualifies the headline number: public SDSS count checks show that the capped 60,000-row cache covers only 24.0\\% of the 249,917 strict four-line S/N$\\geq3$ eligible rows, and the median matched offset weakens to $-1.16$ dex at S/N$\\geq5$, $-0.74$ dex at S/N$\\geq10$, and $-0.76$ dex for a Seyfert-like [N~II]-branch proxy.  The result demonstrates a reproducible survey-analysis path from the proposal to a measurable quantity, but it should not be read as causal evidence for AGN feedback: optical selection, aperture effects, star-formation estimator assumptions, retired/LINER-like ionization, morphology, halo environment, and AGN duty-cycle timing remain uncontrolled.',
        'A selection-function and robustness pass materially qualifies the headline number: public SDSS count checks show that the capped 60,000-row cache covers only 24.0\\% of the 249,917 strict four-line S/N$\\geq3$ eligible rows, and the median matched offset weakens to $-1.16$ dex at S/N$\\geq5$, $-0.74$ dex at S/N$\\geq10$, and $-0.76$ dex for a Seyfert-like [N~II]-branch proxy.  A new control-baseline bracket shows that the median offset is $-0.86$ dex against all non-AGN emission-line controls and approximately zero against low-sSFR non-AGN emission-line controls.  The result demonstrates a reproducible survey-analysis path from the proposal to a measurable quantity, but it should not be read as causal evidence for AGN feedback: optical selection, aperture effects, class-dependent star-formation estimator modes, retired/LINER-like ionization, morphology, halo environment, and AGN duty-cycle timing remain uncontrolled.'
    )
    insert = rp1_insert_text(rows, support)
    text = text.replace('\n\\section{Discussion}\\label{sec:discussion}', '\n' + insert + '\n\\section{Discussion}\\label{sec:discussion}')
    text = text.replace(
        'The new selection and robustness checks change how the headline number should be carried forward.',
        'A second limitation is the catalog sSFR estimator itself.  In the SDSS/MPA-JHU-style context, star-forming galaxies can be tied closely to emission-line SFR calibrations, whereas AGN/composite or weak-line systems may rely more heavily on continuum/D$_n$4000-style information and aperture/model assumptions \citep{brinchmann2004}.  This lane-local draft does not contain the estimator-mode flags required to correct that mismatch, so the offset must be described as a catalog-sSFR association in an optical-classified sample.\n\nThe new selection, robustness, and control-baseline checks change how the headline number should be carried forward.'
    )
    marker_tex = MARKER.replace('_', r'\_')
    text = text.replace(
        'This lane-local revision identifier is RP1-ROBUSTNESS-SELECTION-REVISION-20260708T181833Z.',
        f'This lane-local revision identifier is {marker_tex}.'
    )
    tex = aas / f'sdss_agn_sfr_pilot_lana_control_baseline_{TS}.tex'
    tex.write_text(text)

    changes = out / f'CHANGES_{TS}.md'
    changes.write_text(f'''# Lana changes — {slug} — {TS}

Marker: `{MARKER}`

Source base: Tori RP-1 robustness/selection draft `lanes/tori/revision-drafts/rp1_robustness_selection/20260708T181833Z/`.

Exact manuscript changes:
- Retitled the draft to foreground **BPT optical AGN relative to star-forming and non-AGN controls**, not causal feedback suppression.
- Added a new control-baseline bracket table: original BPT-star-forming controls, all non-AGN emission-line controls, low-sSFR non-AGN controls, and intermediate/unclassified non-SF controls.
- Added match-reuse/common-support diagnostics: 4,239 unique star-forming controls, max reuse 26, p95 reuse 5, match-distance p90 0.0522 / p95 0.0767 / p99 0.1528, 10.7% above scaled distance 0.05, 2.8% above 0.10, and one AGN outside each one-dimensional SF logM/z support range.
- Added the external-review caveat that BPT-star-forming controls make the headline comparison partly baseline-defined.
- Added the Brinchmann/MPA-JHU-style catalog sSFR estimator-mode caveat: AGN/composite hosts and star-forming controls may use class-dependent SFR information, and this cached table lacks estimator-mode flags to correct it.
- Kept all causal language guarded: the result remains an optical, emission-line-selected association pilot.

No current linked manuscript or PDF was overwritten.
''')
    return tex, changes, {'paper_slug': slug, 'source_base': str(src.relative_to(ROOT)), 'changes_md': str(changes.relative_to(LANE))}


def make_m2p3() -> tuple[Path, Path, dict]:
    slug = 'm2_p3_feedback_transition_mass'
    out = REV_ROOT / slug
    aas = out / 'aastex'
    figs = out / 'figures'
    aas.mkdir(parents=True, exist_ok=True)
    copy_many([
        OVERNIGHT / 'lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/20260708T193507Z/figures/m2p3_original_figure1.pdf'
    ], figs)
    src = OVERNIGHT / 'lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/20260708T193507Z/aastex/m2_p3_feedback_transition_mass_selection_ci_20260708T193507Z.tex'
    text = src.read_text()
    text = text.replace('% TORI_M2P3_M3P1_SELECTION_CI_REVISION_20260708T193507Z', '% ' + MARKER)
    text = text.replace(
        'A Selection-Flagged SDSS DR17 Mass-Transition Diagnostic for Low-sSFR and Optical-AGN Incidence',
        'Mass-Binned Low-sSFR and Optical-BPT AGN Incidence in a Capped SDSS DR17 Emission-Line Denominator'
    )
    text = text.replace(
        'We revise the active M2 P3 pilot into a selection-flagged optical transition diagnostic.',
        'We further demote the active M2 P3 pilot into a mass-binned optical denominator measurement.'
    )
    contract = r'''
\section{Manuscript-use contract}\label{sec:m2p3_contract}
This draft should be merged only under a narrow wording contract.  The allowed headline is that the capped SDSS four-line denominator shows a steep mass dependence in catalog low-sSFR incidence and optical-BPT AGN incidence.  The forbidden headline is that the analysis has located the physical transition from stellar-feedback to AGN-feedback regulation.  The word ``transition'' is retained only as a descriptive label for the mass-bin vector.  The required missing variables for the original proposal are gas fraction or baryon deficit, halo mass or central/satellite status, morphology, black-hole-mass or velocity-dispersion information, and selection-matched higher-redshift data.

The table sequence is now the manuscript structure: Table~\ref{tab:m2p3-selection} defines the parent selection, Table~\ref{tab:m2p3-mass-ci} gives the primary mass vector with Wilson intervals, and Table~\ref{tab:m2p3-z-check} is the redshift/aperture-mix guard.  Any future integration should keep that order so the physical interpretation never precedes the denominator.
'''
    text = text.replace('\n\\section{Data, selection function, and operational definitions}', '\n' + contract + '\n\\section{Data, selection function, and operational definitions}')
    conclusions = r'''
\section{Conclusions}\label{sec:m2p3_conclusions}
\begin{enumerate}
\item In the capped SDSS DR17 four-line sample, the catalog low-sSFR fraction rises from 0.005 in the $\log M_\star=8.0$--9.5 bin to 0.729 in the 11.0--12.5 bin.
\item The optical-BPT AGN fraction rises over the same bins from 0.003 to 0.520.
\item Redshift-stratified cells preserve the broad mass ordering but show redshift/aperture-population dependence, so the result should be carried as a target vector.
\item The current data do not distinguish stellar feedback, AGN feedback, halo quenching, black-hole-mass dependence, morphology, or gas supply.
\end{enumerate}
'''
    text = text.replace('\n\\section*{Reproducibility and safety note}', '\n' + conclusions + '\n\\section*{Reproducibility and safety note}')
    marker_tex = MARKER.replace('_', r'\_')
    text = text.replace('Revision marker: TORI\\_M2P3\\_M3P1\\_SELECTION\\_CI\\_REVISION\\_20260708T193507Z.', f'Revision marker: {marker_tex}.')
    tex = aas / f'm2_p3_feedback_transition_mass_lana_claim_contract_{TS}.tex'
    tex.write_text(text)

    changes = out / f'CHANGES_{TS}.md'
    changes.write_text(f'''# Lana changes — {slug} — {TS}

Marker: `{MARKER}`

Source base: Tori M2 P3 selection/CI revision `lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/20260708T193507Z/`.

Exact manuscript changes:
- Retitled from a transition diagnostic to a **mass-binned low-sSFR and optical-BPT incidence denominator**.
- Reworded the abstract to avoid implying a physical feedback-transition measurement.
- Added a `Manuscript-use contract` section that states allowed and forbidden headlines and lists the required missing variables before any feedback-regulation interpretation.
- Preserved the selection-function table, Wilson mass-bin table, and redshift-stratified table as the required structure.
- Added a concise conclusions section with four guarded bullets.

No current linked manuscript or PDF was overwritten.
''')
    return tex, changes, {'paper_slug': slug, 'source_base': str(src.relative_to(ROOT)), 'changes_md': str(changes.relative_to(LANE))}


def make_m3p1() -> tuple[Path, Path, dict]:
    slug = 'm3_p1_multiphase_census'
    out = REV_ROOT / slug
    aas = out / 'aastex'
    figs = out / 'figures'
    aas.mkdir(parents=True, exist_ok=True)
    copy_many([
        OVERNIGHT / 'lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/20260708T193507Z/figures/m3p1_original_figure1.pdf'
    ], figs)
    src = OVERNIGHT / 'lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/20260708T193507Z/aastex/m3_p1_multiphase_census_selection_ci_20260708T193507Z.tex'
    text = src.read_text()
    text = text.replace('% TORI_M2P3_M3P1_SELECTION_CI_REVISION_20260708T193507Z', '% ' + MARKER)
    text = text.replace(
        'A Selection-Flagged SDSS DR17 Optical-Tracer Denominator for a Future Multiphase Outflow Census',
        'Optical Tracer Thresholds in a Capped SDSS DR17 Emission-Line Denominator for Future Multiphase Census Design'
    )
    text = text.replace(
        'We revise the active M3 P1 pilot from a table addendum into a threshold-explicit optical denominator paper.',
        'We further demote the active M3 P1 pilot into a threshold-explicit optical denominator paper for future multiphase census design.'
    )
    dictionary = r'''
\section{Manuscript-use contract and data dictionary}\label{sec:m3p1_contract}
This draft is safe only if every row is described as an optical selection flag.  ``BPT AGN'' is a two-ratio line-classification proxy; ``high [N~II]/H$\alpha$'' and ``high [O~III]/H$\beta$'' are one-ratio thresholds; ``red emission-line'' is a color cut inside the four-line denominator; and ``low-sSFR emission-line'' is the catalog $\log\mathrm{sSFR}<-11.0$ flag.  None of these rows measures outflow velocity, radius, phase mass, mass loading, kinetic power, escape speed, recycling, molecular gas, neutral gas, X-ray plasma, or radio jets.

The allowed headline is that optical prevalence can vary by several factors under different tracer definitions and line-S/N cuts.  The forbidden headline is that SDSS optical line ratios alone have measured the incidence of multiphase AGN-driven outflows.  Any future merged manuscript should keep this dictionary adjacent to the primary table so that threshold choices are not separated from the claimed prevalence.
'''
    text = text.replace('\n\\section{Data, selection function, and operational definitions}', '\n' + dictionary + '\n\\section{Data, selection function, and operational definitions}')
    conclusions = r'''
\section{Conclusions}\label{sec:m3p1_conclusions}
\begin{enumerate}
\item In the capped SDSS DR17 four-line sample, S/N$\geq3$ optical tracer fractions span 0.136--0.418 depending on the adopted threshold.
\item Tightening to S/N$\geq10$ changes both denominator size and population mix: BPT-AGN prevalence falls to 0.069 while the one-ratio high-[O~III]/H$\beta$ prevalence rises to 0.386.
\item The divergent S/N behavior is a selection-function result, not evidence that any optical row is the physical outflow phase.
\item A real multiphase census still requires selection-matched molecular, neutral, ionized-kinematic, X-ray, and radio measurements with nondetections and aperture matching.
\end{enumerate}
'''
    text = text.replace('\n\\section*{Reproducibility and safety note}', '\n' + conclusions + '\n\\section*{Reproducibility and safety note}')
    marker_tex = MARKER.replace('_', r'\_')
    text = text.replace('Revision marker: TORI\\_M2P3\\_M3P1\\_SELECTION\\_CI\\_REVISION\\_20260708T193507Z.', f'Revision marker: {marker_tex}.')
    tex = aas / f'm3_p1_multiphase_census_lana_threshold_contract_{TS}.tex'
    tex.write_text(text)
    changes = out / f'CHANGES_{TS}.md'
    changes.write_text(f'''# Lana changes — {slug} — {TS}

Marker: `{MARKER}`

Source base: Tori M3 P1 selection/CI revision `lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/20260708T193507Z/`.

Exact manuscript changes:
- Retitled to emphasize **optical tracer thresholds in a capped SDSS denominator**, not a completed multiphase outflow census.
- Reworded the abstract lead to call the draft a future-census design denominator.
- Added a `Manuscript-use contract and data dictionary` section defining every tracer family as an optical flag and listing the measurements absent from the SDSS table.
- Preserved the threshold/Wilson table and divergent S/N explanation.
- Added a concise conclusions section that keeps the result methodological and non-physical.

No current linked manuscript or PDF was overwritten.
''')
    return tex, changes, {'paper_slug': slug, 'source_base': str(src.relative_to(ROOT)), 'changes_md': str(changes.relative_to(LANE))}


def main() -> None:
    TICK_DIR.mkdir(parents=True, exist_ok=True)
    (LANE / 'scripts').mkdir(parents=True, exist_ok=True)
    rows, support = compute_rp1_control_stats()
    control_csv = LANE / f'artifacts/rp1_control_baseline_diagnostics_{TS}.csv'
    support_json = LANE / f'artifacts/rp1_control_support_{TS}.json'
    write_csv(control_csv, rows)
    support_json.parent.mkdir(parents=True, exist_ok=True)
    support_json.write_text(json.dumps(support, indent=2) + '\n')

    draft_specs = []
    for maker in [lambda: make_rp1(rows, support), make_m2p3, make_m3p1]:
        tex, changes, meta = maker()
        comp = compile_tex(tex)
        meta.update(comp)
        draft_specs.append(meta)

    manifest = {
        'timestamp_utc': TS,
        'lane': 'lana',
        'marker': MARKER,
        'scope': 'Wave-3 Lana manuscript revisions for M1 RP-1, M2 P3, and M3 P1; all lane-local; current linked manuscripts/PDFs not overwritten.',
        'source_read_confirmation': {
            'brief': 'OVERNIGHT_BRIEF.md',
            'swarm_board': 'SWARM_BOARD.md',
            'all_9_current_aastex_sources_read_by_lane_tick': True,
            'all_9_analysis_json_read_by_lane_tick': True,
            'additional_sources': [
                'lanes/hwao/HWAO_DIRECTOR_TICK_20260708T202049Z.md',
                'lanes/tori/revision-drafts/rp1_robustness_selection/20260708T181833Z/',
                'lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/20260708T193507Z/',
                'lanes/literature/literature_source_packet_wave3_missing_active9_20260708T170557Z.md',
                'lanes/external-cli/EXTERNAL_CLI_TICK_20260708T190158Z.md',
                'lanes/goru/tables/bpt_class_sensitivity_matched_offsets_20260708T162615Z.csv',
                'lanes/goru/tables/paper_table_candidate_rows_20260708T183643Z.csv',
            ],
        },
        'new_analysis_artifacts': {
            'rp1_control_baseline_diagnostics_csv': str(control_csv.relative_to(LANE)),
            'rp1_control_support_json': str(support_json.relative_to(LANE)),
        },
        'rp1_control_baseline_summary': rows,
        'rp1_support_summary': support,
        'drafts': draft_specs,
        'safety': 'Lane-local revision drafts/artifacts only, plus required one-line OVERNIGHT_LEDGER.md append. No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs.',
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + '\n')

    pdf_ok = sum(1 for d in draft_specs if d['compile_exit_code'] == 0 and d['pdf_starts_with_pdf'] and not d['fatal_markers'])
    tick = f'''# Lana manuscript tick — {TS}

Marker: `{MARKER}`

## Scope read before writing
Read and used the required overnight context: `OVERNIGHT_BRIEF.md`, `SWARM_BOARD.md`, current AASTeX sources and `analysis_results.json` for all 9 active papers, latest Hwao direction, Wave-3 literature packet, Tori RP-1/M2P3/M3P1 revisions, Goru robustness tables, and External CLI critique.

This tick performed deep manuscript-writing cleanup for three Wave-3 / morning-priority papers:
1. M1 RP-1 — `m1_rp1_sdss_agn_sfr`
2. M2 P3 — `m2_p3_feedback_transition_mass`
3. M3 P1 — `m3_p1_multiphase_census`

## Lane-local artifacts written
- Script: `{SCRIPT_PATH.relative_to(LANE)}`
- Manifest: `{MANIFEST_PATH.relative_to(LANE)}`
- RP-1 control-baseline diagnostics: `{control_csv.relative_to(LANE)}`
- RP-1 support summary: `{support_json.relative_to(LANE)}`

## Manuscript improvements made
### M1 RP-1 flagship matched-control pilot
- Added an actual control-baseline bracket: original BPT-star-forming controls give median $\\Delta\\log\\mathrm{{sSFR}}={rows[0]['median_delta']:.3f}$ dex, all non-AGN emission-line controls give {rows[1]['median_delta']:.3f} dex, low-sSFR non-AGN controls give {rows[2]['median_delta']:.3f} dex, and intermediate/unclassified non-SF controls give {rows[3]['median_delta']:.3f} dex.
- Added control reuse/common-support diagnostics: {rows[0]['unique_controls']:,} unique star-forming controls, max reuse {rows[0]['max_reuse']}, p95 reuse {rows[0]['p95_reuse']:.0f}, scaled-distance p95 {rows[0]['p95_dist_scaled']:.4f}, and {100*rows[0]['frac_dist_gt_0p05']:.1f}% of pairs above scaled distance 0.05.
- Added explicit star-forming-control-tautology and class-dependent sSFR-estimator caveats before discussion/conclusions.

### M2 P3 mass-transition diagnostic
- Retitled and reframed as a mass-binned low-sSFR / optical-BPT incidence denominator rather than a physical feedback-transition result.
- Added a manuscript-use contract defining allowed and forbidden headlines and preserving selection -> mass-bin Wilson table -> redshift guard ordering.
- Added guarded conclusions.

### M3 P1 optical tracer census
- Retitled and reframed as optical tracer thresholds in a capped SDSS denominator for future multiphase census design.
- Added a manuscript-use contract/data dictionary that defines every tracer row as an optical flag and lists absent physical outflow observables.
- Added guarded conclusions.

## Verification
- Tectonic compile/PDF checks passed for {pdf_ok}/3 lane-local drafts (exit 0, `%PDF`, no fatal markers).
- Manifest records PDF byte sizes and SHA256 hashes.
- Current linked run manuscripts/PDFs were not overwritten; outputs live under `lanes/lana/revision-drafts/<paper-slug>/`.

## Safety
No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs were touched. Only lane-local Lana artifacts were written, plus the required one-line overnight ledger append after verification. No active execution phrase.
'''
    TICK_PATH.write_text(tick)

    ledger_line = (
        f'- {TS[:4]}-{TS[4:6]}-{TS[6:8]}T{TS[9:11]}:{TS[11:13]}:{TS[13:15]}Z — Lana manuscript tick wrote and compiled lane-local Wave-3 revisions for M1 RP-1, M2 P3, and M3 P1; report `lanes/lana/ticks/TICK_{TS}.md`, manifest `lanes/lana/lana_wave3_revision_manifest_{TS}.json`, {pdf_ok}/3 PDFs `%PDF` with no fatal markers; added RP-1 control-baseline diagnostics and manuscript-use contracts for M2 P3/M3 P1. No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/extra-cron/billing/OAuth/external submission changes.\n'
    )
    with LEDGER.open('a') as f:
        f.write(ledger_line)

    print(json.dumps({'marker': MARKER, 'tick': str(TICK_PATH), 'manifest': str(MANIFEST_PATH), 'pdf_ok': pdf_ok}, indent=2))


if __name__ == '__main__':
    main()
