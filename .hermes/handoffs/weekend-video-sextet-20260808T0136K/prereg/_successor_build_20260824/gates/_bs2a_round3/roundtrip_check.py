import sys, json
sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/ref")
import bs2a_quality_gate as G
d = json.load(open("/tmp/bs2a_round3_emit.json"))
result = G.verify_receipt(d["receipt"], d["evidence"])
print("round-trip through JSON on disk -> codes:", sorted(G.codes_of(result)), "accepted?", len(result) == 0)
