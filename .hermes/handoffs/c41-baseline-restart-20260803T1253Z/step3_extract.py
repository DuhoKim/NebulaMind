#!/usr/bin/env python3
import json
import os
import re
import sys
import hashlib
from pathlib import Path

# Adjust sys.path to allow importing nm_fulltext_layer
repo_root = Path(__file__).resolve().parents[3]
sys.path.append(str(repo_root))

from tools import nm_fulltext_layer
import step1_filter

LANE_DIR = Path(__file__).resolve().parent
MANIFEST_PATH = LANE_DIR / "STEP2_FULLTEXT_MANIFEST.json"
SPAN_TABLE_PATH = LANE_DIR / "SPAN_TABLE.jsonl"
SUMMARY_PATH = LANE_DIR / "STEP3_SUMMARY.json"
REPORT_PATH = LANE_DIR / "GORU_STEP3_REPORT.md"

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def extract_sentences_with_offsets(text):
    # A simple sentence splitter that keeps track of offsets
    pattern = re.compile(r'\S.*?(?:[.!?](?=\s|$)|\Z)', re.DOTALL)
    sentences = []
    for match in pattern.finditer(text):
        sentences.append({
            'text': match.group().strip(),
            'start': match.start(),
            'end': match.end()
        })
    return sentences

def estimate_page(char_offset, total_chars, total_pages=15):
    # A rough heuristic for PDF page numbers
    if total_chars == 0: return 1
    return min(total_pages, int((char_offset / total_chars) * total_pages) + 1)

def detect_zone(text_before, current_offset, sentence_text):
    window = text_before[max(0, current_offset - 5000):current_offset]
    
    last_double_newline = window.rfind('\n\n')
    block_start = window[last_double_newline:].lstrip() if last_double_newline != -1 else window.lstrip()
    
    caption_pat = r'^(?:Figure|Fig\.|Table|Extended Data)\s*\d'
    if re.match(caption_pat, block_start, re.IGNORECASE) or re.match(caption_pat, sentence_text, re.IGNORECASE) or block_start.startswith("[TABLE]"):
        return 'caption'

    brackets = len(re.findall(r'\[\d+(?:\s*,\s*\d+)*\]', sentence_text))
    years = len(re.findall(r'\b(?:19|20)\d{2}\b', sentence_text))
    if brackets >= 3 or years >= 3:
        return 'references'

    lines = window.split('\n')
    is_after_references = False
    last_heading = 'unknown'
    for line in reversed(lines):
        line_s = line.strip()
        if len(line_s) < 100 and len(line_s) > 3:
            hl = line_s.lower()
            if hl in ['references', 'bibliography']:
                is_after_references = True
                break
            if any(x in hl for x in ['result', 'finding', 'conclusion', 'abstract']):
                last_heading = 'finding'
                break
            break

    if is_after_references:
        return 'references'

    finding_verbs = re.compile(r'\b(show|shows|find|finds|found|suggest|suggests|demonstrate|demonstrates|conclude|concludes|reveal|reveals)\b', re.IGNORECASE)
    if last_heading == 'finding' and finding_verbs.search(sentence_text):
        return 'finding'

    return 'unknown'

def main():
    with open(MANIFEST_PATH, 'r') as f:
        manifest = json.load(f)
        
    records = manifest.get('records', [])
    
    # Load axis lexicons from step1_filter
    axis_patterns = step1_filter.AXIS_PATTERNS
    strict_terms = step1_filter.STRICT_TERMS
    
    quant_comp_pattern = re.compile(r'\d|%|dex|σ|higher|lower|consistent|rules out|cannot explain|' + '|'.join(re.escape(t) for t in strict_terms), re.IGNORECASE)
    
    all_spans = []
    summary = {
        'protocol_version': 'C41_STEP3_V3',
        'records_processed': 0,
        'spans_extracted': 0,
        'zone_histogram': {},
        'axis_tag_histogram': {},
        'no_span_records': [],
        'failed_records': 0
    }
    
    pdf_noisy_count = 0
    
    for record in records:
        summary['records_processed'] += 1
        identity = record.get('identity', {}).get('key', 'unknown')
        cache_path = record.get('cache_path')
        if not cache_path:
            summary['no_span_records'].append({'identity': identity, 'reason': 'extraction_failed'})
            summary['failed_records'] += 1
            continue
            
        full_cache_path = repo_root / cache_path
        if not full_cache_path.exists():
            summary['no_span_records'].append({'identity': identity, 'reason': 'extraction_failed'})
            summary['failed_records'] += 1
            continue
            
        text = ""
        is_pdf = cache_path.endswith('.pdf')
        
        try:
            with open(full_cache_path, 'rb') as f:
                data = f.read()
            if is_pdf:
                text = nm_fulltext_layer.extract_text(data)
            else:
                html_text = data.decode('utf-8', errors='replace')
                prose, tables = nm_fulltext_layer.extract_html_structured(html_text)
                text = prose + "\n" + "\n".join(tables)
        except Exception as e:
            print(f"Error extracting {cache_path}: {e}")
            summary['no_span_records'].append({'identity': identity, 'reason': 'extraction_failed'})
            summary['failed_records'] += 1
            continue
            
        if not text.strip():
            summary['no_span_records'].append({'identity': identity, 'reason': 'extraction_failed'})
            summary['failed_records'] += 1
            continue
            
        sentences = extract_sentences_with_offsets(text)
        total_chars = len(text)
        
        flags = []
        if is_pdf:
            # simple noisy text heuristic (many unrecognized chars or lack of spaces)
            if len(re.findall(r'[^\w\s]', text)) / max(1, len(text)) > 0.2:
                flags.append('pdf_text_noisy')
                pdf_noisy_count += 1
                
        record_spans = []
        seen_span_ids = set()
        for i, s in enumerate(sentences):
            s_text = s['text']
            
            # Check axis hits
            hit_axes = []
            for axis, patterns in axis_patterns.items():
                for pat in patterns:
                    if pat.search(s_text):
                        hit_axes.append(axis)
                        break
                        
            if not hit_axes:
                continue
                
            # Check quant/comp signal
            if not quant_comp_pattern.search(s_text):
                continue
                
            # Valid span!
            # Window = sentence ± one neighbor, quote capped at 600 chars.
            start_idx = max(0, i - 1)
            end_idx = min(len(sentences) - 1, i + 1)
            
            a = start_idx
            b = end_idx
            
            full_span_chars = sentences[b]['end'] - sentences[a]['start']
            truncated = False
            
            if full_span_chars > 600:
                truncated = True
                if a < i and (sentences[i]['end'] - sentences[a]['start']) <= 600:
                    b = i
                elif b > i and (sentences[b]['end'] - sentences[i]['start']) <= 600:
                    a = i
                else:
                    a = i
                    b = i
            
            char_range = [sentences[a]['start'], sentences[b]['end']]
            window_text = text[char_range[0]:char_range[1]]
            
            if len(window_text) > 600:
                window_text = window_text[:600]
                char_range[1] = char_range[0] + 600
                truncated = True
                
            zone = detect_zone(text, s['start'], s_text)
            page = estimate_page(s['start'], total_chars) if is_pdf else None
            
            span_id = f"{identity}_{char_range[0]}_{char_range[1]}"
            # Ensure deterministic, remove spaces if any in identity
            span_id = span_id.replace(" ", "_")
            
            if span_id in seen_span_ids:
                continue
            seen_span_ids.add(span_id)
            
            trigger_terms = list(set(quant_comp_pattern.findall(s_text)))
            
            span = {
                'span_id': span_id,
                'record_identity': identity,
                'quote': window_text,
                'char_range': char_range,
                'page_estimate': page,
                'zone': zone,
                'axis_tags': hit_axes,
                'trigger_terms': trigger_terms,
                'extraction_flags': flags,
                'truncated': truncated,
                'full_span_chars': full_span_chars
            }
            record_spans.append(span)
            
            # Update summary stats
            summary['spans_extracted'] += 1
            summary['zone_histogram'][zone] = summary['zone_histogram'].get(zone, 0) + 1
            for a in hit_axes:
                summary['axis_tag_histogram'][a] = summary['axis_tag_histogram'].get(a, 0) + 1
                
        if not record_spans:
            summary['no_span_records'].append({'identity': identity, 'reason': 'no_axis_sentence'})
            # Ensure we emit a row for zero spans as requested
            all_spans.append({'span_id': f"{identity}_no_span", 'record_identity': identity, 'type': 'no_span_record', 'reason': 'no_axis_sentence'})
        else:
            all_spans.extend(record_spans)
            
    # Check failure rate
    if summary['failed_records'] / max(1, summary['records_processed']) > 0.2:
        print("Failure rate > 20%. Stopping.")
        sys.exit(1)
        
    summary['input_manifest'] = {
        'STEP2_FULLTEXT_MANIFEST.json': sha256_file(MANIFEST_PATH),
        'step3_extract.py': sha256_file(Path(__file__).resolve())
    }
    
    with open(SPAN_TABLE_PATH, 'w') as f:
        for span in all_spans:
            f.write(json.dumps(span) + '\n')
            
    with open(SUMMARY_PATH, 'w') as f:
        json.dump(summary, f, indent=2)
        
    report = f"""# GORU STEP 3 REPORT

## Summary
- Records Processed: {summary['records_processed']}
- Spans Extracted: {summary['spans_extracted']}
- Failed Records: {summary['failed_records']}
- Noisy PDFs: {pdf_noisy_count}

## Zone Histogram
{json.dumps(summary['zone_histogram'], indent=2)}

## Axis Tag Histogram
{json.dumps(summary['axis_tag_histogram'], indent=2)}

## Anomalies / Notes
- The extraction completed successfully within the acceptable failure threshold.
- No network access was used, texts were processed locally.

## Safety Boundary Statement
No network access was attempted. Outputs were written strictly to the lane directory. The cache and previous artifacts were left unmodified. No semantic guessing was performed for rhetorical zones.

## Repair round (V3)
- Implemented strict zone heuristics by design change rather than tuning.
- 'finding' is now exclusively applied when there is BOTH a result-verb signal AND proximity to a results/conclusions/abstract heading.
- Upgraded caption detection to explicitly match 'Figure/Fig./Table/Extended Data'.
- Implemented robust 'references' detection based on citation-dense lines and bibliography headings.
- All other uncertain zone classes (method, background, interpretation) have been set to 'unknown' wholesale to avoid false claims.
- Eliminated duplicate span_ids by checking and skipping identical IDs per record.
- Regenerated SPAN_TABLE.jsonl and STEP3_SUMMARY.json as C41_STEP3_V3.

GORU_STEP3_V3_COMPLETE_20260804
"""
    with open(REPORT_PATH, 'w') as f:
        f.write(report)
        
if __name__ == "__main__":
    main()
