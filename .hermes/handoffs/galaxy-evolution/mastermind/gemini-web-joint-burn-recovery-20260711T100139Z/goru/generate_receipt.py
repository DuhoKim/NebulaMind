import os
import hashlib
from datetime import datetime, timezone

packet_root = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-joint-burn-recovery-20260711T100139Z"
goru_dir = os.path.join(packet_root, "goru")

start_utc = "2026-07-11T10:08:52Z"
end_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

inputs = [
    "DIRECTION.md",
    "MANIFEST.json",
    "prompts/C1.md",
    "WAVE_LEDGER.md",
    "weekend prompts glob: requests/REQ_*_WEEKEND_BURN_PROMPT.md",
    "valid reports base: gemini-web-rampage-20260711T052300Z",
    "valid reports ext: gemini-web-rampage-extension-20260711T064115Z"
]

outputs = [
    "goru/TOPIC_DEDUPE.md",
    "goru/PROMPT_SCHEMA_CHECK.md",
    "goru/EXPECTED_MARKERS.json"
]

def hash_file(path):
    if not os.path.exists(path): return "missing", 0
    with open(path, "rb") as f:
        data = f.read()
        return hashlib.sha256(data).hexdigest(), len(data)

output_stats = {}
for out in outputs:
    h, b = hash_file(os.path.join(packet_root, out))
    output_stats[out] = {"sha256": h, "bytes": b}

# Parse schema check verdict
with open(os.path.join(goru_dir, "PROMPT_SCHEMA_CHECK.md"), "r") as f:
    schema_content = f.read()
    schema_pass = "Verdict: PASS" in schema_content

# Parse dedupe counts
covered = 0
not_covered = 0
unparseable = 0
with open(os.path.join(goru_dir, "TOPIC_DEDUPE.md"), "r") as f:
    dedupe_content = f.read()
    for line in dedupe_content.split("\n"):
        if "- COVERED_BY_VALID_REPORT:" in line: covered = int(line.split(":")[-1].strip())
        if "- NOT_COVERED:" in line: not_covered = int(line.split(":")[-1].strip())
        if "- UNPARSEABLE:" in line: unparseable = int(line.split(":")[-1].strip())

final_verdict = "PASS" if schema_pass else "BLOCKED"

receipt_path = os.path.join(goru_dir, "GORU_PREFLIGHT_RECEIPT.md")
with open(receipt_path, "w", encoding="utf-8") as f:
    f.write("# GORU PREFLIGHT RECEIPT\n\n")
    f.write(f"- Start UTC: {start_utc}\n")
    f.write(f"- End UTC: {end_utc}\n")
    f.write(f"- Model/Tool: Antigravity Local Helper (Goru)\n\n")
    f.write("## Input Roots\n")
    for inp in inputs:
        f.write(f"- {inp}\n")
    f.write("\n## Output Hashes and Byte Counts\n")
    for out, stats in output_stats.items():
        f.write(f"- {out}: {stats['bytes']} bytes, SHA-256: {stats['sha256']}\n")
    f.write("\n## Verdict Counts\n")
    f.write(f"- COVERED_BY_VALID_REPORT: {covered}\n")
    f.write(f"- NOT_COVERED: {not_covered}\n")
    f.write(f"- UNPARSEABLE: {unparseable}\n")
    f.write(f"- PROMPT SCHEMA: {'PASS' if schema_pass else 'FAIL'}\n\n")
    f.write("## Safety Attestation\n")
    f.write("No Chrome, System Events, browser automation, Playwright, cookies, profiles, login, CAPTCHA, or network-to-Google were used. Operations were strictly local read-only on inputs and write-only to goru/ directory.\n\n")
    f.write(f"## Final Verdict\n")
    f.write(final_verdict + "\n")
