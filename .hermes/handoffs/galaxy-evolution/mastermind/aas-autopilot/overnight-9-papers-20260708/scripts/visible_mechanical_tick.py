#!/usr/bin/env python3
# pyright: reportAttributeAccessIssue=false
import hashlib
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

try:
    import pandas as pd
except Exception:
    pd = None

LANE = sys.argv[1] if len(sys.argv) > 1 else "unknown"
REPO = Path('/Users/duhokim/NebulaMind/NebulaMind')
AUTO = REPO/'.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot'
WORK = AUTO/'overnight-9-papers-20260708'
RUN1 = AUTO/'runs/SDSS_AGN_SFR_PILOT_20260708T122000Z'
RUN8 = AUTO/'runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z'
LEDGER = WORK/'OVERNIGHT_LEDGER.md'

now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
print(f"# Visible {LANE} lane tick — {now}\n")
print(f"Lane: `{LANE}`")
print(f"Work root: `{WORK}`\n")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def find_primary_pdfs():
    pdfs = []
    p = RUN1/'aastex/sdss_agn_sfr_pilot_aas.pdf'
    if p.exists():
        pdfs.append(p)
    manifest = RUN8/'ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json'
    if manifest.exists():
        data = json.loads(manifest.read_text())
        if isinstance(data, dict):
            items = data.get('papers') or data.get('entries') or data.get('manifest') or []
        else:
            items = data
        for item in items:
            if isinstance(item, dict):
                for key in ('pdf', 'pdf_path', 'aas_pdf'):
                    val = item.get(key)
                    if val:
                        pp = Path(val)
                        if not pp.is_absolute():
                            pp = (RUN8/pp).resolve()
                        if pp.exists():
                            pdfs.append(pp)
                        break
    # fallback
    if len(pdfs) < 9:
        for pp in RUN8.glob('*/aastex/*.pdf'):
            if pp not in pdfs:
                pdfs.append(pp)
    return sorted(set(pdfs), key=lambda x: str(x))

if LANE == 'goru':
    print("## Mechanical SDSS/data inventory\n")
    csvs = list(RUN1.glob('data/*.csv')) + list(RUN8.glob('**/*.csv'))
    print(f"CSV files found: {len(csvs)}")
    for c in sorted(csvs)[:20]:
        print(f"- `{c.relative_to(AUTO)}` size={c.stat().st_size}")
    if pd is None:
        print("\nPandas unavailable; row-level robustness not run in this tick.")
    else:
        sample = None
        for cand in [RUN1/'data/analysis_sample.csv', RUN1/'data/sdss_dr17_sample.csv', RUN1/'data/raw_sample.csv'] + sorted(RUN8.glob('**/*analysis*.csv')):
            if cand.exists():
                sample = cand
                break
        if sample:
            df = pd.read_csv(sample)
            print(f"\nPrimary sample: `{sample.relative_to(AUTO)}`")
            print(f"Rows: {len(df):,}; columns: {len(df.columns):,}")
            for col in ['bpt_class', 'class', 'z', 'logmass', 'logsfr', 'logsSFR', 'log_ssfr']:
                if col in df.columns:
                    if col in ['bpt_class', 'class']:
                        print(f"\n{col} counts:")
                        for k, v in Counter(df[col].astype(str)).most_common(12):
                            print(f"- {k}: {v:,}")
                    else:
                        s = pd.to_numeric(df[col], errors='coerce')
                        finite = int(s.count())
                        print(f"- {col}: finite={finite:,}, min={float(s.min()):.4g}, median={float(s.median()):.4g}, max={float(s.max()):.4g}")
        else:
            print("\nNo primary sample CSV located.")
    print("\nNext useful Goru pass: generate paper-specific denominator/attrition tables for any manuscript still lacking them.")

elif LANE == 'kun':
    print("## Reproducibility and artifact integrity\n")
    pdfs = find_primary_pdfs()
    print(f"Primary PDFs found: {len(pdfs)}")
    for p in pdfs[:20]:
        head = p.read_bytes()[:4]
        print(f"- `{p.relative_to(AUTO)}` bytes={p.stat().st_size:,} starts_pdf={head == b'%PDF'} sha256={sha256(p)[:16]}…")
    logs = sorted(list(RUN1.glob('**/compile.log')) + list(RUN8.glob('**/compile.log')) + list((WORK/'lanes').glob('**/compile.log')))
    fatal = []
    for log in logs:
        text = log.read_text(errors='replace')
        bad = any(x in text.lower() for x in ['fatal error', '! emergency stop', 'failed to compile'])
        if bad:
            fatal.append(log)
    print(f"\nCompile logs checked: {len(logs)}; fatal markers: {len(fatal)}")
    for log in fatal[:20]:
        print(f"- fatal marker: `{log}`")
    print("\nNext useful Kun pass: verify any new lane-local revision PDFs and record a consolidated repro manifest.")

elif LANE == 'tori':
    print("## Integration/receipt monitor\n")
    lane_files = sorted((WORK/'lanes').glob('**/*.md'), key=lambda p: p.stat().st_mtime, reverse=True)
    print(f"Lane markdown reports found: {len(lane_files)}")
    for p in lane_files[:18]:
        try:
            rel = p.relative_to(WORK)
        except Exception:
            rel = p
        print(f"- `{rel}` mtime={datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec='seconds')}")
    if LEDGER.exists():
        lines = LEDGER.read_text().splitlines()
        print("\nLatest ledger entries:")
        for line in lines[-10:]:
            print(line)
    print("\nNext useful Tori pass: synthesize lane outputs and identify which revised drafts are ready for morning integration.")

else:
    print("Unknown mechanical lane; no action.")
