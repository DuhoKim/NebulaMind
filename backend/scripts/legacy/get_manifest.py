import json

with open("/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/candidate_grounded_atom_backfill_20260528T135038Z/validator_ready_rows.jsonl") as f:
    for line in f:
        r = json.loads(line.strip())
        print(list(r.keys()))
        break
