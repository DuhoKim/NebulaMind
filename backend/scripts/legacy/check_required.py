import json
with open("/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/retrieval_filter_v2_ship_20260527T050600Z/element_candidate_pairs.jsonl") as f:
    r = json.loads(f.readline())
    print("required" in r, r.get("required"))
