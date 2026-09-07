import re, pathlib
base = pathlib.Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828")
both = re.sub(r"\s+", " ", (base/"R3C2_D1_D7_CANDIDATE_CLAUSES_20260906.md").read_text() + "\n" + (base/"R3C2_BATCH_PREPARATION_UNADOPTED_20260906.md").read_text())
new = ["lists the intended repairs by topic","For eligible imports the intended status, origin and value agree","Whether the quotation cites THAT value is seat judgement","Revision 2 added controls for these cases","then require a run record supporting enumeration before ledger exposure","A PASS accompanied by satisfactory dispatch and release evidence","implements the clause's stages","Batch 1 is light but not the lightest","The pinned partition implementation deterministically computes these bytes","Whole-text ownership preserves a claim's local context","sections 1 and 3 require equivalent evidence access","Per-claim outcomes and classes use the operative rules explicitly accepted","the difference between a census that could not run","Blocks a first run on the evidence of the limb-B death finding"]
old = ["every accepted repair is in this revision","They assign the same classification","caught by the second seat","all repaired above and in the kit","rest on an audit whose enumeration was produced","The audit's PASS then rests on an independent enumeration","as the clause states","Batch 1, the lightest","must get the same bytes","§2's arithmetic is per claim","which §1 and §3 supply","exactly as V23 states","a census that can run and one that cannot","no seat completes"]
print("NEW (want 1 each):")
for f in new: print(f"  {both.count(f)}  {f}")
print("OLD (want 0 each):")
for f in old: print(f"  {both.count(f)}  {f}")
