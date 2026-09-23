#!/usr/bin/env python3
"""Record Duho's V138 chat signature — two-step, recompute before recording (standing rule).
usage: record_v138_signature.py --digest <64hex as stated in chat> --utc 2026-09-23T12:34:00Z --relay-file <Blanc's verbatim relay .md>
Refuses unless: the stated digest equals the CURRENT plain sha256 of the draft with both lines blank; the relay file exists and
contains the digest. Then fills the two lines, recomputes the filled-file digest, writes V138_AMENDMENT_RECORD_20260923.md, and
prints both digests. Never re-signs, never edits a filled file."""
import argparse, hashlib, pathlib, datetime, re, subprocess
S=pathlib.Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824')
D=S/'PREREG_SUCCESSOR_DRAFT_V138_20260923.md'
def sha(b): return hashlib.sha256(b).hexdigest()
ap=argparse.ArgumentParser(); ap.add_argument('--digest',required=True); ap.add_argument('--utc',required=True); ap.add_argument('--relay-file',required=True); a=ap.parse_args()
t=D.read_text()
assert t.endswith('SIGNATURE UTC: \nDUHO SIGNATURE: \n') or t.rstrip('\n').endswith('SIGNATURE UTC: \nDUHO SIGNATURE: '), 'REFUSED: signature lines are not blank — already filled?'
cur=sha(D.read_bytes())
if cur!=a.digest.lower(): raise SystemExit(f'REFUSED: stated digest {a.digest[:16]}… != current blank-line digest {cur[:16]}… — a mismatch is not a signature')
relay=pathlib.Path(a.relay_file).read_text()
if a.digest.lower()[:16] not in relay.lower(): raise SystemExit('REFUSED: relay file does not contain the stated digest')
if not re.fullmatch(r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ',a.utc): raise SystemExit('REFUSED: --utc must be like 2026-09-23T12:34:00Z')
filled=t.replace('SIGNATURE UTC: \nDUHO SIGNATURE: ',f'SIGNATURE UTC: {a.utc}\nDUHO SIGNATURE: {a.digest.lower()} at {a.utc} (chat signature via Blanc relay; V136 preamble mechanism carried into V138)')
D.write_text(filled); fd=sha(D.read_bytes())
kst=subprocess.run(['date','+%Y-%m-%d %H:%M:%S %Z'],capture_output=True,text=True).stdout.strip()
(S/'V138_AMENDMENT_RECORD_20260923.md').write_text(f"""# V138 AMENDMENT RECORD — SIGNED {a.utc}

**Signed.** Duho, in the chat channel under the §17-style convention, relayed verbatim by Blanc ({pathlib.Path(a.relay_file).name}, sha256 `{sha(pathlib.Path(a.relay_file).read_bytes())[:16]}…`), recorded by Hwao at {kst}.

**Digest signed:** `{a.digest.lower()}` — the sha256 of `PREREG_SUCCESSOR_DRAFT_V138_20260923.md` with `SIGNATURE UTC:` and `DUHO SIGNATURE:` blank; recomputed from disk immediately before filling and found equal.

**Signature lines now filled** (this changes the file's digest, as with V135–V137):
```
SIGNATURE UTC: {a.utc}
DUHO SIGNATURE: {a.digest.lower()} at {a.utc} (chat signature via Blanc relay; V136 preamble mechanism carried into V138)
```
Digest of the signed-and-filled file: `{fd}` (goes into V139's §10 row).

**Predecessor:** V137-H (amendment-signed 2026-09-03T13:20:00Z, `700fd0d2…`; filled `bf46e62a…`). P0's ssh-signed V134 manifest is untouched (`d1be4a3b…`, 30/30 OK at referee time).

**Referee:** agy `V138-REFEREE-V2` — SIGNABLE, COUNT 0, ACCESS PROVEN on `{a.digest.lower()[:16]}…` (round 1 NOT-SIGNABLE, F1 FATAL path repaired, CLOSED in round 2). Change record: `V138_RESTART_RECORD_20260923.md`.

**What is signed:** the restart amendment — Tier A with the 2026-09-10 exposure disclosed and archived (§6.4, §6.2); BS-3 re-pinned to the R2 reader (§6.6) with BS-7p/BS-4 re-run before BS-6; the repeatability acceptance criterion stated before the replay (primary exact equality; fallback decisions-equal + |Δz| ≤ 1e-12 only on a recorded FAILED primary; second FAIL = STOP; EA-3 imported only under an admissibility receipt); BS-RG readability slot (§6.5) with the positive control before any Tier A read and f_R entering only as a_eff with Stage P/C re-run at a_eff (expected to FAIL at ~8%); BS-3g edge (a). Choices 2–6 RULED-20260923-DECISIONPAGE; q2m RULED-20260923-CHAT.

**What is NOT decided:** the three committee checkers (provisioning data). **What now starts, needing no human decision:** the two post-signature runs of `SPIN_RESTART_READINESS_20260923/hwao/V138_SIGNABLE.md` §6 (replay Run A; positive control Run B).
""")
print(f'FILLED. blank-line digest {a.digest.lower()}  filled-file digest {fd}  record V138_AMENDMENT_RECORD_20260923.md')
