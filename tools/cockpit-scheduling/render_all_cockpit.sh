#!/bin/zsh
# One full cockpit render pass (usage monitor + all four page renderers).
# Safe to run any time; single-writer discipline means ONLY the scheduled job
# or the OPS coordinator should invoke it, not both habitually.
export PATH=/opt/homebrew/bin:$PATH
cd /Users/duhokim/NebulaMind/NebulaMind
LOG=/Users/duhokim/HermesOps/cockpit/render.log
{
  echo "--- pass $(date '+%Y-%m-%d %H:%M:%S %Z') ---"
  # The agy card only updates when the monitor SENDS /usage to an idle pane; a
  # passive scan just re-reads yesterday's panel (it sat 26 h stale on 08-20).
  # Refresh by slash when the card is older than 2 h, otherwise stay hands-off.
  if python3 - <<'AGE'
import json, sys, datetime, re
try:
    c = json.load(open('frontend/public/agent-reports/stable-cockpit-canonical.json'))
    g = [x for x in c['provider_usage_gauges'] if 'agy' in x.get('provider', '')][0]
    m = re.search(r'20\d{2}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', g.get('source_label') or '')
    age = (datetime.datetime.utcnow() - datetime.datetime.strptime(m.group(0), '%Y-%m-%dT%H:%M:%SZ')).total_seconds()
    sys.exit(0 if age > 7200 else 1)
except Exception:
    sys.exit(0)
AGE
  then
    python3 tools/live_provider_usage_monitor.py --refresh-slash 2>&1 | tail -1
  else
    python3 tools/live_provider_usage_monitor.py 2>&1 | tail -1
  fi
  python3 tools/render_ge_autopilot_dashboard_v2.py 2>&1 | tail -1
  python3 tools/render_spin_parity_status.py 2>&1
  python3 tools/render_bhu_lane2_status.py 2>&1
  python3 tools/render_cockpit_index.py 2>&1 | tail -1
} >> "$LOG" 2>&1
