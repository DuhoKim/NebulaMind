import re

with open('../PREREG_SUCCESSOR_DRAFT_V27_20260827.md', 'r') as f:
    v27_content = f.read()

with open('GENERATED_TRACE.md', 'r') as f:
    trace_content = f.read()

# Replace the title
new_content = v27_content.replace(
    '# PREREGISTRATION DRAFT V27 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT',
    '# PREREGISTRATION DRAFT V28 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT'
)

# Extract the part before Section 10 and after Section 10's trace table notes
sec10_start = new_content.find('## §10 Gate plan and repair trace\n')
if sec10_start == -1:
    print("Could not find section 10")
    exit(1)

next_sec_start = new_content.find('\nNext: both referee seats on this text', sec10_start)
if next_sec_start == -1:
    print("Could not find the end of section 10")
    exit(1)

new_sec10_text = """## §10 Gate plan and repair trace

The checker contract is as follows:
- in-band coverage is the §10 table, scoped to the table itself, stopping at the subject's predecessor;
- the current transition is mapped in the sidecar `gates/FINDINGS_MAP.md` and is checked there;
- V1→V15 are exempt by a named rule in the checker, not by silence.

Each written row must carry its own result digest — not any digest found elsewhere.

""" + trace_content.strip() + "\n"

new_content = new_content[:sec10_start] + new_sec10_text + new_content[next_sec_start:]

with open('../PREREG_SUCCESSOR_DRAFT_V28_20260827.md', 'w') as f:
    f.write(new_content)

print("Done writing V28.")
