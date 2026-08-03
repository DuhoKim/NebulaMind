Implemented the local-only weekend sprint orchestrator and tests.

Changed:
- [run_weekend_journal_sprint.py](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/run_weekend_journal_sprint.py)
- [tests/test_weekend_journal_sprint.py](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/tests/test_weekend_journal_sprint.py)
- [BUILD_RECEIPT.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/BUILD_RECEIPT.md)

Also generated safe preflight state files:
- `PREFLIGHT.json`
- `SPRINT_STATUS.json`

Verification passed:
- `PYTHONPYCACHEPREFIX=/tmp/weekend_pycache python3 -m py_compile run_weekend_journal_sprint.py tests/test_weekend_journal_sprint.py`
- `PYTHONPYCACHEPREFIX=/tmp/weekend_pycache python3 -m unittest tests/test_weekend_journal_sprint.py`
- `PYTHONPYCACHEPREFIX=/tmp/weekend_pycache python3 run_weekend_journal_sprint.py --preflight --duration-seconds 172800 --max-cycles 24 --slot-seconds 7200`

No provider calls or 48-hour run were launched.