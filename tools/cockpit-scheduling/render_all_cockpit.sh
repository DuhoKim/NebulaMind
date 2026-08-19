#!/bin/zsh
# One full cockpit render pass (usage monitor + all four page renderers).
# Safe to run any time; single-writer discipline means ONLY the scheduled job
# or the OPS coordinator should invoke it, not both habitually.
export PATH=/opt/homebrew/bin:$PATH
cd /Users/duhokim/NebulaMind/NebulaMind
LOG=/Users/duhokim/HermesOps/cockpit/render.log
{
  echo "--- pass $(date '+%Y-%m-%d %H:%M:%S %Z') ---"
  python3 tools/live_provider_usage_monitor.py 2>&1 | tail -1
  python3 tools/render_ge_autopilot_dashboard_v2.py 2>&1 | tail -1
  python3 tools/render_spin_parity_status.py 2>&1
  python3 tools/render_bhu_lane2_status.py 2>&1
  python3 tools/render_cockpit_index.py 2>&1 | tail -1
} >> "$LOG" 2>&1
