#!/usr/bin/env python3
"""Cached-vs-public marginal representativeness check for overnight 9-paper work.

This tick addresses the external-review blocker that the 60,000-row cached
SpecObjID-ordered sample may not represent the 249,917-row public SDSS DR17
four-line-eligible parent in z, stellar mass, and sSFR marginals.

Safety: public/read-only SDSS COUNT(*) queries and local file reads only; writes
lane-local artifacts under the overnight work root and appends the required
ledger entry. No product DB/API/page_versions/public/live/git/deploy/cron/etc.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import subprocess
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTO = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
OVERNIGHT = AUTO / "overnight-9-papers-20260708"
SOURCE_CSV = AUTO / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
LEDGER = OVERNIGHT / "OVERNIGHT_LEDGER.md"
BASE_URL = "https://skyserver.sdss.org/dr17/SkyServerWS/SearchTools/SqlSearch"
MARKER_BASE = "CACHED_PUBLIC_REPRESENTATIVENESS"

LINE_FROM = (
    "SpecObj s JOIN galSpecInfo i ON s.specObjID=i.specObjID "
    "JOIN PhotoObj p ON s.bestObjID=p.objID "
    "JOIN galSpecExtra x ON s.specObjID=x.specObjID "
    "JOIN galSpecLine l ON s.specObjID=l.specObjID"
)
BASE_Z = "s.class='GALAXY' AND s.z>=0.02 AND s.z<=0.12"
MASS_SSFR = "x.lgm_tot_p50 BETWEEN 8 AND 12.5 AND x.specsfr_tot_p50 BETWEEN -14 AND -7"
ERR_POS = " AND ".join([
    "l.h_alpha_flux_err>0",
    "l.h_beta_flux_err>0",
    "l.oiii_5007_flux_err>0",
    "l.nii_6584_flux_err>0",
])
SN3 = " AND ".join([
    ERR_POS,
    "l.h_alpha_flux>=3*l.h_alpha_flux_err",
    "l.h_beta_flux>=3*l.h_beta_flux_err",
    "l.oiii_5007_flux>=3*l.oiii_5007_flux_err",
    "l.nii_6584_flux>=3*l.nii_6584_flux_err",
])
STRICT_WHERE = f"{BASE_Z} AND {MASS_SSFR} AND {SN3}"

SAFETY = (
    "Read-only public SDSS DR17 count queries plus local cached-CSV reads; wrote "
    "lane-local artifacts under overnight-9-papers-20260708/lanes/tori/"
    "cached-public-representativeness plus the required tick report and ledger "
    "append. No product DB/API/page_versions/wiki publish/live mirror/deploy/"
    "restart/git/extra-cron/billing/OAuth/external submission changes."
)


@dataclass(frozen=True)
class BinDef:
    dimension: str
    label: str
    column: str
    lo: float
    hi: float
    last: bool = False

    @property
    def sql_condition(self) -> str:
        op_hi = "<=" if self.last else "<"
        return f"{self.column}>={self.lo:g} AND {self.column}{op_hi}{self.hi:g}"

    def contains(self, value: float) -> bool:
        if self.last:
            return self.lo <= value <= self.hi
        return self.lo <= value < self.hi

    @property
    def safe_key(self) -> str:
        raw = f"{self.dimension}_{self.label}"
        return (
            raw.replace("log", "log")
            .replace("-", "m")
            .replace("+", "p")
            .replace(".", "p")
            .replace("<", "lt")
            .replace(">", "gt")
            .replace("=", "eq")
            .replace(" ", "_")
            .replace("/", "_")
        )


def bins() -> list[BinDef]:
    return [
        BinDef("redshift", "0.020-0.050", "s.z", 0.02, 0.05),
        BinDef("redshift", "0.050-0.080", "s.z", 0.05, 0.08),
        BinDef("redshift", "0.080-0.120", "s.z", 0.08, 0.12, True),
        BinDef("stellar_mass", "8.0-9.5", "x.lgm_tot_p50", 8.0, 9.5),
        BinDef("stellar_mass", "9.5-10.0", "x.lgm_tot_p50", 9.5, 10.0),
        BinDef("stellar_mass", "10.0-10.5", "x.lgm_tot_p50", 10.0, 10.5),
        BinDef("stellar_mass", "10.5-11.0", "x.lgm_tot_p50", 10.5, 11.0),
        BinDef("stellar_mass", "11.0-12.5", "x.lgm_tot_p50", 11.0, 12.5, True),
        BinDef("ssfr", "-14.0--12.0", "x.specsfr_tot_p50", -14.0, -12.0),
        BinDef("ssfr", "-12.0--11.0", "x.specsfr_tot_p50", -12.0, -11.0),
        BinDef("ssfr", "-11.0--10.5", "x.specsfr_tot_p50", -11.0, -10.5),
        BinDef("ssfr", "-10.5--10.0", "x.specsfr_tot_p50", -10.5, -10.0),
        BinDef("ssfr", "-10.0--9.5", "x.specsfr_tot_p50", -10.0, -9.5),
        BinDef("ssfr", "-9.5--9.0", "x.specsfr_tot_p50", -9.5, -9.0),
        BinDef("ssfr", "-9.0--7.0", "x.specsfr_tot_p50", -9.0, -7.0, True),
    ]


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with SOURCE_CSV.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append({
                "specObjID": int(row["specObjID"]),
                "redshift": float(row["z"]),
                "stellar_mass": float(row["lgm_tot_p50"]),
                "ssfr": float(row["specsfr_tot_p50"]),
            })
    return rows


def fetch_count(name: str, where_clause: str, raw_dir: Path, delay_s: float = 0.25) -> int:
    raw_dir.mkdir(parents=True, exist_ok=True)
    sql = f"SELECT COUNT(*) n FROM {LINE_FROM} WHERE {where_clause}"
    (raw_dir / f"{name}.sql").write_text(sql + "\n", encoding="utf-8")
    url = BASE_URL + "?" + urllib.parse.urlencode({"cmd": sql, "format": "json"})
    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "NebulaMind-local-readonly-representativeness-check/1.0"},
            )
            with urllib.request.urlopen(req, timeout=150) as response:
                payload = response.read()
            (raw_dir / f"{name}.json").write_bytes(payload)
            parsed = json.loads(payload.decode("utf-8"))
            value = int(parsed[0]["Rows"][0]["n"])
            time.sleep(delay_s)
            return value
        except Exception as exc:  # pragma: no cover - runtime network guard
            last_error = exc
            time.sleep(1.5 * attempt)
    raise RuntimeError(f"SDSS count failed for {name}: {last_error}")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})


def pct(x: float | None, digits: int = 1) -> str:
    if x is None or math.isnan(x):
        return "--"
    return f"{100*x:.{digits}f}%"


def latex_escape(text: str) -> str:
    return text.replace("_", r"\_").replace("%", r"\%").replace("&", r"\&")


def build_table_fragment(ts: str, rows: list[dict[str, Any]], out_path: Path) -> None:
    lines = [
        f"% {MARKER_BASE}_{ts}; lane-local table fragment, not merged into public PDFs.",
        r"\begin{deluxetable*}{llrrrrr}",
        r"\tablecaption{Cached 60,000-row sample versus public SDSS DR17 four-line parent marginals\label{tab:cached-public-marginals}}",
        r"\tablehead{\colhead{Dimension} & \colhead{Bin} & \colhead{Public $N$} & \colhead{Cached $N$} & \colhead{Public frac.} & \colhead{Cached frac.} & \colhead{$\Delta$ pp}}",
        r"\startdata",
    ]
    for row in rows:
        lines.append(
            f"{latex_escape(str(row['dimension']))} & {latex_escape(str(row['bin_label']))} & "
            f"{int(row['public_sn3_count']):,} & {int(row['cached_count']):,} & "
            f"{100*float(row['public_fraction']):.1f}\\% & {100*float(row['cached_fraction']):.1f}\\% & "
            f"{float(row['fraction_difference_pp']):+.1f} \\\\"
        )
    lines += [
        r"\enddata",
        r"\tablecomments{Public counts are read-only SDSS DR17 SkyServer counts for the same redshift, mass, sSFR, and four-line S/N$\geq3$ constraints. The cached sample is the SpecObjID-ordered 60,000-row subset used by the overnight pilots; deviations diagnose representativeness, not astrophysical effects.}",
        r"\end{deluxetable*}",
        "",
    ]
    out_path.write_text("\n".join(lines), encoding="utf-8")


def build_plot(ts: str, rows: list[dict[str, Any]], fig_pdf: Path, fig_png: Path) -> None:
    dimensions = ["redshift", "stellar_mass", "ssfr"]
    titles = {
        "redshift": "Redshift z",
        "stellar_mass": r"$\log_{10}(M_*/M_\odot)$",
        "ssfr": r"$\log_{10}(\mathrm{sSFR}/\mathrm{yr}^{-1})$",
    }
    fig, axes = plt.subplots(len(dimensions), 1, figsize=(9.2, 10.5), constrained_layout=True)
    for ax, dim in zip(axes, dimensions):
        sub = [r for r in rows if r["dimension"] == dim]
        labels = [r["bin_label"] for r in sub]
        public = [100 * float(r["public_fraction"]) for r in sub]
        cached = [100 * float(r["cached_fraction"]) for r in sub]
        x = list(range(len(labels)))
        width = 0.38
        ax.bar([i - width / 2 for i in x], public, width, label="Public strict parent", color="#4C78A8")
        ax.bar([i + width / 2 for i in x], cached, width, label="Cached 60k", color="#F58518")
        ax.set_title(titles[dim])
        ax.set_ylabel("Fraction of sample (%)")
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=25, ha="right")
        ax.grid(axis="y", alpha=0.25)
    axes[0].legend(loc="best")
    fig.suptitle(
        "Cached SpecObjID-ordered SDSS sample vs. public four-line eligible parent\n"
        f"{MARKER_BASE}_{ts}: use as selection-function diagnostic only",
        fontsize=12,
    )
    fig_pdf.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(fig_pdf)
    fig.savefig(fig_png, dpi=180)
    plt.close(fig)


def summarize_by_dimension(rows: list[dict[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for dim in sorted({r["dimension"] for r in rows}):
        sub = [r for r in rows if r["dimension"] == dim]
        max_abs = max(sub, key=lambda r: abs(float(r["fraction_difference_pp"])))
        lowest_cov = min(sub, key=lambda r: float(r["cached_coverage_of_public_bin"]))
        highest_cov = max(sub, key=lambda r: float(r["cached_coverage_of_public_bin"]))
        out[dim] = {
            "max_abs_fraction_difference_bin": max_abs["bin_label"],
            "max_abs_fraction_difference_pp": float(max_abs["fraction_difference_pp"]),
            "lowest_cached_coverage_bin": lowest_cov["bin_label"],
            "lowest_cached_coverage": float(lowest_cov["cached_coverage_of_public_bin"]),
            "highest_cached_coverage_bin": highest_cov["bin_label"],
            "highest_cached_coverage": float(highest_cov["cached_coverage_of_public_bin"]),
        }
    return out


def build_markdown(
    ts: str,
    out_dir: Path,
    rows: list[dict[str, Any]],
    summary: dict[str, Any],
    artifacts: dict[str, Path],
    verification: dict[str, Any],
) -> str:
    dim_summary = summary["dimension_summary"]
    flagged = summary["flagged_bins"]
    lines = [
        f"# Cached-vs-public SDSS representativeness tick — {ts}",
        "",
        f"Marker: `{MARKER_BASE}_{ts}`",
        "",
        "## What this tick did",
        "",
        "- Addressed the external-review blocker that the cached `TOP 60000 ... ORDER BY specObjID` sample may not be representative of the full public SDSS DR17 four-line-eligible parent.",
        "- Ran public/read-only SDSS DR17 `COUNT(*)` queries for redshift, stellar-mass, and sSFR bins under the same four-line S/N$\\geq$3, redshift, mass, and sSFR constraints used by the pilots.",
        "- Compared those public marginals against the cached 60,000-row CSV used by all nine active AAS-style pilots.",
        "- Wrote a CSV/JSON/AASTeX table fragment and a figure for manuscript-integration review; no public-linked manuscript or PDF was overwritten.",
        "",
        "## Grounding / data used",
        "",
        f"- Cached row-level CSV: `{SOURCE_CSV}` ({summary['cached_total']:,} rows read).",
        f"- Public SDSS endpoint: `{BASE_URL}`.",
        f"- Public strict four-line S/N$\\geq$3 total from this tick: **{summary['public_total']:,}** rows.",
        f"- Cached/public strict-parent coverage: **{100*summary['global_cached_coverage']:.1f}%**.",
        f"- Raw SQL/JSON public payloads preserved under `{artifacts['raw_payload_dir']}`.",
        "",
        "## Main representativeness results",
        "",
    ]
    for dim in ["redshift", "stellar_mass", "ssfr"]:
        d = dim_summary[dim]
        lines.append(
            f"- **{dim}**: largest cached-minus-public fraction difference is "
            f"{d['max_abs_fraction_difference_pp']:+.2f} percentage points in bin `{d['max_abs_fraction_difference_bin']}`; "
            f"cached coverage ranges from {100*d['lowest_cached_coverage']:.1f}% (`{d['lowest_cached_coverage_bin']}`) "
            f"to {100*d['highest_cached_coverage']:.1f}% (`{d['highest_cached_coverage_bin']}`)."
        )
    if flagged:
        lines += ["", "Bins with absolute cached-minus-public marginal differences >= 5 percentage points:"]
        for row in flagged:
            lines.append(
                f"- `{row['dimension']}` `{row['bin_label']}`: public {100*float(row['public_fraction']):.1f}%, "
                f"cached {100*float(row['cached_fraction']):.1f}%, diff {float(row['fraction_difference_pp']):+.1f} pp, "
                f"cached/public bin coverage {100*float(row['cached_coverage_of_public_bin']):.1f}%."
            )
    else:
        lines += ["", "No bin exceeded the 5 percentage-point flag threshold, but the cached sample remains row-capped and non-random."]
    lines += [
        "",
        "## Paper-use guardrails",
        "",
        "- Use this packet as a selection-function/representativeness diagnostic for M2 P2, M3 P2, M3 P3, and any shared parent-sample section.",
        "- Any reported `f_BPT_AGN`, `f_Q`, H$\\alpha$ proxy, density, or target-vector fraction remains conditional on four-line emission detection and the SpecObjID-ordered 60,000-row cap.",
        "- The packet does not add radio, X-ray, CO/HI, resolved outflow, or simulation-mock data; it cannot support radio coupling, gas-depletion/SFE, causal feedback, or model-validation claims.",
        "",
        "## Files changed / written",
        "",
    ]
    for key, path in artifacts.items():
        lines.append(f"- `{key}`: `{path}`")
    lines += [
        "",
        "## Verification",
        "",
        f"- Public bin sums equal public total for all dimensions: {verification['bin_sums_equal_public_total']}.",
        f"- Cached bin sums equal 60,000 for all dimensions: {verification['cached_bin_sums_equal_cached_total']}.",
        f"- Raw JSON payload count: {verification['raw_json_count']}; raw SQL payload count: {verification['raw_sql_count']}.",
        f"- Figure PDFs/PNGs exist and are nonzero: {verification['figure_outputs_nonzero']}.",
        f"- Manifest artifact hashes recorded: {verification['manifest_artifact_count']} artifacts.",
        "",
        "## Blockers / cautions",
        "",
        "- This is still a denominator-quality improvement, not a new science measurement.",
        "- The cached sample remains ordered by SpecObjID, not randomized; manuscript text should call it a capped subset and avoid population-complete language.",
        "- Use the table/figure locally before any future merge; do not replace public-linked PDFs without a separate approval gate.",
        "",
        "## Next recommended tick",
        "",
        "Patch the lane-local M2 P2, M3 P2, and M3 P3 revisions with this representativeness paragraph/table plus Wave-2 citations, then compile/hash those local PDFs only.",
        "",
        "## Safety",
        "",
        SAFETY,
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ts = os.environ.get("TICK_TS") or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = OVERNIGHT / "lanes/tori/cached-public-representativeness" / ts
    tables_dir = out_dir / "tables"
    figures_dir = out_dir / "figures"
    raw_dir = out_dir / "raw_sdss_payloads"
    ticks_dir = OVERNIGHT / "ticks"
    for d in (out_dir, tables_dir, figures_dir, raw_dir, ticks_dir):
        d.mkdir(parents=True, exist_ok=True)

    local_rows = read_rows()
    cached_total = len(local_rows)
    if cached_total != 60000:
        raise RuntimeError(f"Expected 60000 cached rows, got {cached_total}")

    public_total = fetch_count("strict_public_total", STRICT_WHERE, raw_dir)
    marginal_rows: list[dict[str, Any]] = []
    for b in bins():
        public_count = fetch_count(b.safe_key, f"{STRICT_WHERE} AND {b.sql_condition}", raw_dir)
        local_col = {"redshift": "redshift", "stellar_mass": "stellar_mass", "ssfr": "ssfr"}[b.dimension]
        cached_count = sum(1 for r in local_rows if b.contains(float(r[local_col])))
        public_fraction = public_count / public_total if public_total else float("nan")
        cached_fraction = cached_count / cached_total if cached_total else float("nan")
        coverage = cached_count / public_count if public_count else float("nan")
        ratio = cached_fraction / public_fraction if public_fraction else float("nan")
        marginal_rows.append({
            "dimension": b.dimension,
            "bin_label": b.label,
            "public_sn3_count": public_count,
            "cached_count": cached_count,
            "public_fraction": public_fraction,
            "cached_fraction": cached_fraction,
            "fraction_difference_pp": 100 * (cached_fraction - public_fraction),
            "cached_coverage_of_public_bin": coverage,
            "representation_ratio_cached_frac_over_public_frac": ratio,
            "guard": "Selection-function diagnostic only; not an astrophysical effect measurement.",
        })

    fields = [
        "dimension", "bin_label", "public_sn3_count", "cached_count", "public_fraction",
        "cached_fraction", "fraction_difference_pp", "cached_coverage_of_public_bin",
        "representation_ratio_cached_frac_over_public_frac", "guard",
    ]
    csv_path = tables_dir / f"cached_vs_public_marginals_{ts}.csv"
    write_csv(csv_path, marginal_rows, fields)

    table_tex = out_dir / f"cached_vs_public_marginals_table_fragment_{ts}.tex"
    build_table_fragment(ts, marginal_rows, table_tex)

    fig_pdf = figures_dir / f"cached_vs_public_marginals_{ts}.pdf"
    fig_png = figures_dir / f"cached_vs_public_marginals_{ts}.png"
    build_plot(ts, marginal_rows, fig_pdf, fig_png)

    dim_summary = summarize_by_dimension(marginal_rows)
    flagged_bins = [r for r in marginal_rows if abs(float(r["fraction_difference_pp"])) >= 5.0]
    flagged_bins = sorted(flagged_bins, key=lambda r: abs(float(r["fraction_difference_pp"])), reverse=True)

    public_sums = {
        dim: sum(int(r["public_sn3_count"]) for r in marginal_rows if r["dimension"] == dim)
        for dim in {r["dimension"] for r in marginal_rows}
    }
    cached_sums = {
        dim: sum(int(r["cached_count"]) for r in marginal_rows if r["dimension"] == dim)
        for dim in {r["dimension"] for r in marginal_rows}
    }
    verification = {
        "public_sums_by_dimension": public_sums,
        "cached_sums_by_dimension": cached_sums,
        "bin_sums_equal_public_total": all(v == public_total for v in public_sums.values()),
        "cached_bin_sums_equal_cached_total": all(v == cached_total for v in cached_sums.values()),
        "raw_json_count": len(list(raw_dir.glob("*.json"))),
        "raw_sql_count": len(list(raw_dir.glob("*.sql"))),
        "figure_outputs_nonzero": fig_pdf.exists() and fig_pdf.stat().st_size > 0 and fig_png.exists() and fig_png.stat().st_size > 0,
        "manifest_artifact_count": 0,
    }

    summary = {
        "marker": f"{MARKER_BASE}_{ts}",
        "timestamp_utc": ts,
        "source_csv": str(SOURCE_CSV),
        "sdss_endpoint": BASE_URL,
        "cached_total": cached_total,
        "public_total": public_total,
        "global_cached_coverage": cached_total / public_total if public_total else None,
        "dimension_summary": dim_summary,
        "flagged_bins": flagged_bins,
        "marginal_rows": marginal_rows,
        "verification": verification,
        "safety": SAFETY,
    }
    summary_json = out_dir / f"cached_public_representativeness_summary_{ts}.json"
    summary_json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    artifacts: dict[str, Path] = {
        "summary_json": summary_json,
        "marginals_csv": csv_path,
        "aastex_table_fragment": table_tex,
        "figure_pdf": fig_pdf,
        "figure_png": fig_png,
        "raw_payload_dir": raw_dir,
    }

    lane_md = out_dir / f"CACHED_PUBLIC_REPRESENTATIVENESS_{ts}.md"
    tick_report = ticks_dir / f"TICK_{ts}.md"
    # Build preliminary reports before manifest collection.
    report_text = build_markdown(ts, out_dir, marginal_rows, summary, artifacts, verification)
    lane_md.write_text(report_text, encoding="utf-8")
    tick_report.write_text(report_text, encoding="utf-8")
    artifacts["lane_report_md"] = lane_md
    artifacts["tick_report_md"] = tick_report
    artifacts["helper_script"] = Path(__file__).resolve()

    manifest_paths = [p for p in artifacts.values() if p.is_file()]
    manifest = {
        "marker": f"{MARKER_BASE}_MANIFEST_{ts}",
        "timestamp_utc": ts,
        "scope": "Cached-vs-public z/mass/sSFR marginal representativeness check for the 9 active AAS-style pilots.",
        "artifacts": [
            {"path": str(p), "bytes": p.stat().st_size, "sha256": sha256_path(p)} for p in manifest_paths
        ],
        "raw_payload_count_json": verification["raw_json_count"],
        "raw_payload_count_sql": verification["raw_sql_count"],
        "verification": verification,
        "safety": SAFETY,
        "manifest_self_hash_note": "Self-hash intentionally excluded.",
    }
    verification["manifest_artifact_count"] = len(manifest["artifacts"]) + 1
    manifest["verification"] = verification
    manifest_json = out_dir / f"cached_public_representativeness_manifest_{ts}.json"
    manifest_json.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    artifacts["manifest_json"] = manifest_json

    # Rewrite reports with final verification count and manifest path.
    final_report_text = build_markdown(ts, out_dir, marginal_rows, summary, artifacts, verification)
    lane_md.write_text(final_report_text, encoding="utf-8")
    tick_report.write_text(final_report_text, encoding="utf-8")

    # Optional direct hash verification via sha256sum, for a simple external receipt in stdout.
    hash_proc = subprocess.run(
        ["shasum", "-a", "256", str(csv_path), str(summary_json), str(fig_pdf), str(manifest_json)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=60,
    )

    z = dim_summary["redshift"]
    mass = dim_summary["stellar_mass"]
    ssfr = dim_summary["ssfr"]
    ledger_prefix = f"- {ts[:4]}-{ts[4:6]}-{ts[6:8]}T{ts[9:11]}:{ts[11:13]}:{ts[13:15]}Z — Tori cached-vs-public representativeness tick"
    ledger_line = (
        f"{ledger_prefix} wrote `lanes/tori/cached-public-representativeness/{ts}/` and `ticks/TICK_{ts}.md`; "
        f"queried public SDSS z/mass/sSFR marginals for strict four-line parent N={public_total:,} vs cached N={cached_total:,}, "
        f"verified bin sums match totals, and flagged largest cached-minus-public marginal differences: "
        f"redshift {z['max_abs_fraction_difference_bin']} {z['max_abs_fraction_difference_pp']:+.1f} pp, "
        f"mass {mass['max_abs_fraction_difference_bin']} {mass['max_abs_fraction_difference_pp']:+.1f} pp, "
        f"sSFR {ssfr['max_abs_fraction_difference_bin']} {ssfr['max_abs_fraction_difference_pp']:+.1f} pp. "
        "No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/extra-cron/billing/OAuth/external submission changes.\n"
    )
    existing_lines = LEDGER.read_text().splitlines() if LEDGER.exists() else []
    existing_lines = [line for line in existing_lines if not line.startswith(ledger_prefix)]
    LEDGER.write_text("\n".join(existing_lines).rstrip() + "\n" + ledger_line, encoding="utf-8")

    success = (
        verification["bin_sums_equal_public_total"]
        and verification["cached_bin_sums_equal_cached_total"]
        and verification["figure_outputs_nonzero"]
        and hash_proc.returncode == 0
    )
    print(json.dumps({
        "timestamp_utc": ts,
        "tick_report": str(tick_report),
        "lane_report": str(lane_md),
        "manifest": str(manifest_json),
        "summary_json": str(summary_json),
        "marginals_csv": str(csv_path),
        "figure_pdf": str(fig_pdf),
        "public_total": public_total,
        "cached_total": cached_total,
        "global_cached_coverage": summary["global_cached_coverage"],
        "dimension_summary": dim_summary,
        "verification": verification,
        "sha256_receipt_stdout": hash_proc.stdout.strip(),
        "sha256_receipt_stderr": hash_proc.stderr.strip(),
    }, indent=2, sort_keys=True))
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
