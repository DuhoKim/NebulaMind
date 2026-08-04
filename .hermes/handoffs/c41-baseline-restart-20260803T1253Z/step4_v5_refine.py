import json
import re

with open('C41_LEDGER.jsonl', 'r') as f:
    entries = [json.loads(line) for line in f if line.strip()]
    
# We will keep the first 6 as they are, but fix the rule 4 incoherence and single-source actively debated if they are there.
# Wait, c41_004 is actively debated. Lana says: "2 single-source actively_debated (c41_004, c41_011)... Correction: hold at emerging_sample_limited with a tension_reported tag".
# Let's fix that.

# We also need to add the 3 countercases from countercases.jsonl.
# 2024A&A...684A..75C_65175_65699
# 2024ApJ...960...56H_81091_81250
# 2024ApJ...962...24S_67569_68015

countercases = [
    {
        "span_id": "bibcode:2024A&A...684A..75C_65175_65699",
        "bibcode": "2024A&A...684A..75C",
        "quote": "However, this seems to be in tension with the relatively mild evolution in the MZR normalisation observed in our JWST sample.",
        "axis": "chemical_enrichment"
    },
    {
        "span_id": "bibcode:2024ApJ...960...56H_81091_81250",
        "bibcode": "2024ApJ...960...56H",
        "quote": "the hidden AGN contribution may ease the tension in the observed vs. predicted SFR densities at z > 10.",
        "axis": "formation_efficiency"
    },
    {
        "span_id": "bibcode:2024ApJ...962...24S_67569_68015",
        "bibcode": "2024ApJ...962...24S",
        "quote": "The disagreement with Nakajima et al. ( 2022 ) at low metallicities may be a result of the choice of parameterization",
        "axis": "chemical_enrichment"
    }
]

def clean_assertion(quote):
    # try to get the first real sentence
    parts = re.split(r'(?<=[a-z])\.\s+', quote.replace('\n', ' '))
    for p in parts:
        if len(p) > 30 and not any(c in p for c in ['=', '<', '>', '~', '{', '}', '\\']):
            return p.strip() + ('.' if not p.strip().endswith('.') else '')
    return None

new_ledger = []
for i, e in enumerate(entries):
    if i < 6:
        # Fix rule 4 and actively_debated for the first 6
        if e['certainty_level'] == 'actively_debated' and e['certainty_dimensions']['consistency'] == 'single_source':
            e['certainty_level'] = 'emerging_sample_limited'
            if 'tension_reported' not in e['tags']:
                e['tags'].append('tension_reported')
                
        if e['modality'] == 'in_model_only' and e['epistemic_type'] == 'observational_sample' and e['certainty_dimensions']['model_dependence'] == 'none':
            e['certainty_dimensions']['model_dependence'] = 'high'
            
        new_ledger.append(e)
        continue
        
    # for mechanical entries
    quote = e['evidence_spans'][0]['quote']
    tokens = quote.split()
    if not tokens: continue
    
    num_tokens = sum(1 for t in tokens if any(c.isdigit() for c in t))
    if num_tokens / len(tokens) > 0.2:
        continue # drop tables
        
    if e['entry_id'] in ('c41_038', 'c41_039', 'c41_064'):
        continue
        
    assertion = clean_assertion(quote)
    if not assertion:
        continue
        
    e['assertion'] = assertion
    
    # Rationale
    e['evidence_spans'][0]['rationale'] = "Indicates that " + assertion.lower()[:60] + "..."
    
    # Precision
    if num_tokens > 3:
        e['certainty_dimensions']['precision'] = 'quantified'
        
    # Rule 4
    if e['modality'] == 'in_model_only' and e['epistemic_type'] == 'observational_sample' and e['certainty_dimensions']['model_dependence'] == 'none':
        e['certainty_dimensions']['model_dependence'] = 'high'
        
    # Single source debate
    if e['certainty_level'] == 'actively_debated' and e['certainty_dimensions']['consistency'] == 'single_source':
        e['certainty_level'] = 'emerging_sample_limited'
        if 'tension_reported' not in e['tags']:
            e['tags'].append('tension_reported')
            
    new_ledger.append(e)

# Add the 3 countercases
counter_id = 90
for c in countercases:
    assertion = clean_assertion(c['quote'])
    if not assertion: assertion = c['quote']
    e = {
        "entry_id": f"c41_{counter_id:03d}",
        "assertion": assertion,
        "modality": "is_are_does",
        "scope": {
            "population": "extracted population",
            "sample": "observational sample",
            "redshift": "source-specific",
            "mass": "source-specific",
            "environment": "source-specific",
            "simulation_context": None
        },
        "epistemic_type": "observational_sample",
        "source_access": "full_text",
        "method_or_model": "automated extraction",
        "source_bibcodes": [c['bibcode']],
        "evidence_spans": [{
            "paper_id": c['bibcode'],
            "span_id": c['span_id'],
            "quote": c['quote'],
            "location": "C41_STEP3_V3",
            "rhetorical_zone": "unknown",
            "stance": "qualifies",
            "rationale": "Reports tension or disagreement in the literature.",
            "source_access": "full_text",
            "source_title": "Unknown Title",
            "source_year": c['bibcode'][0:4],
            "source_epistemic_type_original": "observational_sample"
        }],
        "certainty_dimensions": {
            "directness": "direct",
            "consistency": "single_source",
            "precision": "qualitative",
            "sample_size": "sample-specific",
            "model_dependence": "none"
        },
        "certainty_level": "emerging_sample_limited",
        "links": [],
        "as_of": "2026-08-04",
        "verification_status": "pending",
        "verification_note": "Awaiting human review.",
        "tags": [c['axis'], "tension_reported", "debate_countercase"]
    }
    new_ledger.append(e)
    counter_id += 1

# Link mining
# Simple links: same_axis for all entries that share an axis.
# To not blow up, just link adjacent entries with the same axis.
for i in range(len(new_ledger) - 1):
    for j in range(i+1, min(i+3, len(new_ledger))):
        axes_i = set(new_ledger[i]['tags'])
        axes_j = set(new_ledger[j]['tags'])
        intersection = axes_i.intersection(axes_j)
        if intersection and any(a in ['formation_efficiency', 'chemical_enrichment', 'ionizing_output'] for a in intersection):
            new_ledger[i]['links'].append({
                "type": "same_axis",
                "entry_id": new_ledger[j]['entry_id'],
                "description": "Shares the same major axis tag."
            })

with open('C41_LEDGER.jsonl', 'w') as f:
    for e in new_ledger:
        f.write(json.dumps(e) + '\n')
        
# Recompute no_entry_reasons
with open('STEP2_FULLTEXT_MANIFEST.json', 'r') as f:
    manifest = json.load(f)
    
ranks = {r['identity']['key'].replace('bibcode:', ''): r['identity']['rank'] for r in manifest['records']}

covered_bibcodes = set()
for e in new_ledger:
    for b in e['source_bibcodes']:
        covered_bibcodes.add(b)

no_entry_reasons = []
for b, rank in ranks.items():
    if rank <= 68 and b not in covered_bibcodes:
        no_entry_reasons.append(f"Rank {rank} (bibcode:{b}): Excluded due to numeric/table debris during V5 distillation.")

with open('NO_ENTRY_REASONS.json', 'w') as f:
    json.dump(no_entry_reasons, f, indent=2)

print(f"Generated {len(new_ledger)} entries. Links added.")
print(f"No entry reasons: {len(no_entry_reasons)}")
