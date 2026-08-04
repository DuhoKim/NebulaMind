import json
import sys

def main():
    with open('C41_LEDGER.jsonl', 'r') as f:
        ledger = [json.loads(line) for line in f if line.strip()]

    patch = {}
    with open('VERIFICATION_STATUS_PATCH.jsonl', 'r') as f:
        for line in f:
            if not line.strip(): continue
            d = json.loads(line)
            patch[d['entry_id']] = d

    nits = {
        "c41_007": "nit: full abstract sentence w/ exact numbers; conservative modality kept",
        "c41_016": "nit: CEERS-1019/GN-z11 named; bound span truncates before them (present later in paragraph)",
        "c41_019": "nit: \"fainter\" for \"northernmost, weaker (COSMOS24108-b)\" \u2014 direction correct",
        "c41_024": "nit: \"all elements\" is source's own phrase (covers Ne/S/Cl/Ar) \u2014 carry as source-level overstatement",
        "c41_031": "nit: span ends before tension's object; fulltext confirms O/Fe \u2014 qualifies-on-span/supports-on-fulltext",
        "c41_042": "nit: span omits paper's own selection caveat; agree-inside/disagree-outside pair \u2192 mixed",
        "c41_053": "nit: \"preference\" slightly stronger than source's \"suggestive of\"",
        "c41_079": "nit: sufficiency conditional preserved (\"if high enough\"); commonly_probably borderline-acceptable"
    }

    for e in ledger:
        eid = e['entry_id']
        
        # Apply verification status
        if eid in patch:
            p = patch[eid]
            e['verification_status'] = 'validated'
            if p.get('note'):
                e['verification_note'] = p['note']
            else:
                e['verification_note'] = "" # Clear previous pending notes

        # Fix zone-field mismatches
        if eid in ["c41_004", "c41_005"]:
            e['evidence_spans'][0]['rhetorical_zone'] = "unknown"
            # Apply rule 7 stance constraint if needed
            if e['epistemic_type'] in ['observational_sample', 'single_case'] and e['evidence_spans'][0]['stance'] == 'supports':
                e['evidence_spans'][0]['stance'] = 'qualifies'

        # Add binding_note to the 8 nit entries
        if eid in nits:
            e['binding_note'] = nits[eid]

    assert len(ledger) == 80, f"Expected 80 rows, got {len(ledger)}"

    with open('C41_LEDGER.jsonl', 'w') as f:
        for e in ledger:
            f.write(json.dumps(e) + '\n')

    # Update receipt version
    with open('STEP4_VALIDATION_RECEIPT.json', 'r') as f:
        receipt = json.load(f)
        
    receipt['entries_count'] = 80
    receipt['version'] = 'V8'
    
    with open('STEP4_VALIDATION_RECEIPT.json', 'w') as f:
        json.dump(receipt, f, indent=2)

    print("V8 Applied successfully.")

if __name__ == '__main__':
    main()
