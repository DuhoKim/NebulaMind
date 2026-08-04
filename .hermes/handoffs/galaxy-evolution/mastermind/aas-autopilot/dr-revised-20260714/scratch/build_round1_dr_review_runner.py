from pathlib import Path

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/browser-concurrency/studio-simultaneous-web-viability-test-20260714T034720Z/scratch/dr_batch_9_reference_runner.py")
DEST = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/browser-concurrency/studio-simultaneous-web-viability-test-20260714T034720Z/scratch/dr_manuscript_round1_review_runner.py")
ROOT = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714/round1"

text = SOURCE.read_text()
replacements = [
    ('BATCH_ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-research-lane-9-20260714")', f'BATCH_ROOT = Path("{ROOT}")'),
    ('PROMPT_DIR = BATCH_ROOT / "prompts"', 'PROMPT_DIR = BATCH_ROOT / "dr-review-prompts"'),
    ('PACKET_DIR = BATCH_ROOT / "packets"', 'PACKET_DIR = BATCH_ROOT / "dr-review-packets"'),
    ('STATE_PATH = PACKET_DIR / "DR_RESEARCH_BATCH_9_STATE.json"', 'STATE_PATH = PACKET_DIR / "ROUND1_DR_REVIEW_STATE.json"'),
    ('SUMMARY_PATH = PACKET_DIR / "DR_RESEARCH_BATCH_9_FINAL_SUMMARY_VERIFIED.md"', 'SUMMARY_PATH = PACKET_DIR / "ROUND1_DR_REVIEW_FINAL_SUMMARY.md"'),
    ('HOLD_SUMMARY_PATH = PACKET_DIR / "DR_RESEARCH_BATCH_9_HOLD_SUMMARY.md"', 'HOLD_SUMMARY_PATH = PACKET_DIR / "ROUND1_DR_REVIEW_HOLD_SUMMARY.md"'),
    ('HWAO_TARGET = "hwao-pilot-gemini-resume:0.0"', 'HWAO_TARGET = "garu-agy-viability:0.0"'),
    ('"batch_id": "DR_RESEARCH_BATCH_9_REFERENCE_20260714"', '"batch_id": "DR_MANUSCRIPT_REVIEW_ROUND1_20260715"'),
    ('f"tori-goru-dr9-{paper_id}-submit"', 'f"goru-dr-review-r1-{paper_id}-submit"'),
    ('f"tori-goru-dr9-{paper_id}-plan"', 'f"goru-dr-review-r1-{paper_id}-plan"'),
    ('f"tori-goru-dr9-{paper_id}-start"', 'f"goru-dr-review-r1-{paper_id}-start"'),
    ('f"tori-goru-dr9-{paper_id}-monitor"', 'f"goru-dr-review-r1-{paper_id}-monitor"'),
    ('f"tori-goru-dr9-{paper_id}-delete"', 'f"goru-dr-review-r1-{paper_id}-delete"'),
    ('f"tori-goru-dr9-{spec[\'paper_id\']}-recover"', 'f"goru-dr-review-r1-{spec[\'paper_id\']}-recover"'),
    ('str(LEDGER_PATH), "tori", etype', 'str(LEDGER_PATH), "goru", etype'),
    ('dr9_', 'dr_review_r1_'),
    ('DR9', 'DR-REVIEW-R1'),
    ('Hwao/local validators', 'Tori/WonE validators'),
    ('no .tex/DB/autopilot-lane/auto-apply/deploy/git/publish/cron/account/secret mutation.', 'no .tex/DB/autopilot-lane/auto-apply/deploy/git/publish/cron/account-setting/secret mutation; exact-owned conversation cleanup occurs only after verified save.'),
    ('No DB, API, wiki, trust, autopilot-lane, deploy, git, publish, cron, billing, account, credential, or secret mutation is authorized or performed.', 'No DB, API, wiki, trust, autopilot-lane, deploy, git, publish, cron, billing, account-setting, credential, secret, bulk-history, or unrelated-conversation mutation is authorized or performed. Exact-owned conversation cleanup is authorized only after verified packet save.'),
    ('No `.tex`, DB, autopilot-lane, auto-apply, deploy, git, publish, cron, billing, account, credential, or secret mutation was authorized or performed by this runner.', 'No `.tex`, DB, autopilot-lane, auto-apply, deploy, git, publish, cron, billing, account-setting, credential, secret, bulk-history, or unrelated-conversation mutation was authorized or performed. Exact-owned conversation cleanup occurred only after verified packet save.'),
    ('for attempt in range(8):', 'for attempt in range(24):'),
    ('deadline = time.monotonic() + 45', 'deadline = time.monotonic() + 120'),
    (
        '            if target_matches(path, page) and snapshot["research"] and snapshot["stop"]:\n                accepted = True; break',
        '            in_progress_text = " ".join(item["text"] for item in snapshot["messages"])\n            in_progress_signal = snapshot["research"] or "While I\\\'m researching" in in_progress_text or "Researching " in in_progress_text or "Creating visuals for the report" in in_progress_text\n            if target_matches(path, page) and snapshot["stop"] and in_progress_signal:\n                accepted = True; break',
    ),
]
for old, new in replacements:
    if old not in text:
        raise RuntimeError(f"source replacement anchor missing: {old}")
    text = text.replace(old, new)
DEST.write_text(text)
print(DEST)
