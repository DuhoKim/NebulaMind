#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path('/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution')
METHODS = {
    'M1': 'packet-gated-paper-to-wiki-reconciliation',
    'M2': 'source-first-paper-adjudication',
    'M3': 'debate-map-to-wiki-rebuild',
}
HTML_FORBIDDEN = re.compile(r'<\s*script\b|\bfetch\s*\(|XMLHttpRequest|WebSocket\s*\(|\son[a-z]+\s*=|<\s*form\b', re.I)
CASUAL = re.compile(r'\b(casual|cute|fun|blog|storytelling|big question|maybe|probably|simple|easy|interestingly|what studies already show)\b', re.I)
PRIOR_HEAD = re.compile(r'(Prior evidence and constraints|Prior evidence|What prior studies establish|Prior studies and constraints|Previous studies|What studies already show)', re.I)
NEXT_FIELD = re.compile(r'\n(?:\*\*|- \*\*)?(Remaining uncertainty|What remains unknown|Data and measurement plan|Survey/data plan|Analysis and decision criterion|Analysis/test|Expected result|Limitations|Caveats|Provenance)\b', re.I)


def split_cards(md: str):
    headings = list(re.finditer(r'(?m)^##\s+(.+)$', md))
    cards = []
    for idx, m in enumerate(headings):
        title = m.group(1).strip()
        if re.search(r'^(Scope|Methods appendix|Methods note)', title, re.I):
            continue
        start = m.end()
        end = headings[idx + 1].start() if idx + 1 < len(headings) else len(md)
        cards.append((title, md[start:end]))
    return cards


def prior_section(card: str):
    # Markdown variants: bold paragraph, bullet bold field, or heading text.
    patterns = [
        r'\*\*(Prior evidence and constraints|Prior evidence|What prior studies establish|Prior studies and constraints|Previous studies|What studies already show)\.?:?\*\*(.*?)(?=\n\*\*|\n###|\n##|\n- \*\*(?:Remaining uncertainty|What remains unknown|Data and measurement plan|Survey/data plan|Analysis and decision criterion|Analysis/test|Expected result|Limitations|Caveats|Provenance)|\Z)',
        r'-\s+\*\*(Prior evidence and constraints|Prior evidence|What prior studies establish|Prior studies and constraints|Previous studies|What studies already show):\*\*(.*?)(?=\n- \*\*|\n##|\Z)',
    ]
    for pat in patterns:
        m = re.search(pat, card, re.S | re.I)
        if m:
            return m.group(1), m.group(2).strip()
    return None, ''


def md_links(text: str):
    return re.findall(r'\[[^\]]+\]\(([^)]+)\)', text)


def statement_count(text: str):
    bullets = [ln for ln in text.splitlines() if ln.strip().startswith('-') and re.search(r'[A-Za-z]', ln)]
    if bullets:
        return len(bullets)
    # Split paragraph sentences; ignore parenthetical fragments.
    sents = [s for s in re.split(r'(?<=[.!?])\s+', re.sub(r'\s+', ' ', text).strip()) if len(s) > 30]
    return max(1, len(sents)) if text.strip() else 0


def resolve_link(link: str, base_file: Path):
    if link.startswith('#'):
        return True, 'fragment-only'
    parsed = urlparse(link)
    if parsed.scheme in ('http', 'https'):
        try:
            req = urllib.request.Request(link, headers={'User-Agent': 'Hermes verifier'}, method='GET')
            with urllib.request.urlopen(req, timeout=15) as r:
                return 200 <= r.status < 400, f'http {r.status}'
        except Exception as e:
            return False, f'http error {e!r}'
    path_part = parsed.path
    target = (base_file.parent / unquote(path_part)).resolve()
    if not target.exists():
        return False, f'missing local {target}'
    if parsed.fragment and target.suffix.lower() in ('.html', '.md'):
        text = target.read_text(errors='ignore')
        frag = re.escape(parsed.fragment)
        has = bool(re.search(r'id=["\']' + frag + r'["\']|\{#' + frag + r'\}|^#+\s+.*' + frag, text, re.M))
        # Markdown source anchors may not have explicit HTML ids; file existence is still useful but warn.
        return True, 'local file exists' + (', anchor seen' if has else ', anchor not explicit')
    return True, 'local file exists'


def verify_method(mid: str, slug: str):
    d = ROOT / slug / 'research-topics-from-wiki-20260708T090359Z'
    mdp = d / 'research-topics-from-wiki-20260708T090359Z.md'
    htmlp = d / 'research-topics-from-wiki-20260708T090359Z.html'
    mapp = d / 'research-topic-map-20260708T090359Z.json'
    md = mdp.read_text(errors='ignore')
    html = htmlp.read_text(errors='ignore')
    data = json.loads(mapp.read_text())
    cards = split_cards(md)
    card_reports = []
    ok = True
    for title, body in cards:
        head, sec = prior_section(body)
        links = md_links(sec)
        stmt_n = statement_count(sec)
        link_results = [resolve_link(link, mdp) for link in links]
        card_ok = bool(sec) and len(links) >= stmt_n and all(r[0] for r in link_results)
        casual_hits = sorted(set(m.group(0).lower() for m in CASUAL.finditer(title + '\n' + body)))
        # Allow legacy phrase only if used nowhere in the prior heading; this pass should move to formal heading.
        if head and re.search(r'What studies already show', head, re.I):
            casual_hits.append('legacy prior heading')
        if casual_hits:
            card_ok = False
        if not card_ok:
            ok = False
        card_reports.append({
            'title': title,
            'prior_heading': head,
            'statements': stmt_n,
            'links': len(links),
            'link_results': link_results,
            'casual_hits': casual_hits,
            'ok': card_ok,
        })
    product_claim = html.count('<!--claim:')
    product_cite = html.count('<!--cite:')
    static_hits = len(HTML_FORBIDDEN.findall(html))
    if static_hits or product_claim or product_cite:
        ok = False
    expected = data.get('proposal_count') or len(data.get('proposals', []))
    if expected != len(cards) or not (5 <= len(cards) <= 8):
        ok = False
    return {
        'method': mid,
        'ok': ok,
        'cards_seen': len(cards),
        'json_proposal_count': expected,
        'static_hits': static_hits,
        'product_claim_comments': product_claim,
        'product_cite_comments': product_cite,
        'cards': card_reports,
    }


def main():
    reports = [verify_method(mid, slug) for mid, slug in METHODS.items()]
    print(json.dumps(reports, indent=2))
    if not all(r['ok'] for r in reports):
        sys.exit(1)

if __name__ == '__main__':
    main()
