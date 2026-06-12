#!/bin/bash
LOG=/tmp/security_scan.log
echo "=== Security Scan $(date) ===" | tee -a "$LOG"

cd ~/NebulaMind/NebulaMind/backend && source .venv/bin/activate

echo "=== pip-audit ===" | tee -a "$LOG"
pip-audit 2>&1 | tee -a "$LOG"
PIP_EXIT=${PIPESTATUS[0]}

echo "=== bandit ===" | tee -a "$LOG"
bandit -r app/ -ll -q 2>&1 | tee -a "$LOG"
BANDIT_EXIT=${PIPESTATUS[0]}

cd ~/NebulaMind/NebulaMind/frontend
echo "=== npm audit ===" | tee -a "$LOG"
npm audit 2>&1 | tee -a "$LOG"
NPM_EXIT=${PIPESTATUS[0]}

# Notify on HIGH/CRITICAL findings
if [ "$PIP_EXIT" -ne 0 ] || [ "$BANDIT_EXIT" -ne 0 ] || [ "$NPM_EXIT" -ne 0 ]; then
    MSG="[SECURITY] Scan found issues (pip-audit=$PIP_EXIT bandit=$BANDIT_EXIT npm=$NPM_EXIT) — check $LOG"
    echo "$MSG" | tee -a "$LOG"
    # Discord notification if webhook is configured
    WEBHOOK=$(grep NM_DISCORD_WEBHOOK_URL ~/NebulaMind/NebulaMind/backend/.env 2>/dev/null | cut -d= -f2-)
    if [ -n "$WEBHOOK" ]; then
        curl -s -X POST "$WEBHOOK" -H "Content-Type: application/json" \
            -d "{\"content\":\"$MSG\"}" > /dev/null
    fi
fi

echo "=== Done $(date) ===" | tee -a "$LOG"
