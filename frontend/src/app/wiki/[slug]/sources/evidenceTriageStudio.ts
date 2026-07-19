import type { CrossPagePaperFootprintResponse, CrossPagePaperTone } from "./crossPagePaperFootprint";

export type EvidenceTriageLane = "needs_adjudication" | "needs_source" | "ready_to_review";
export type EvidenceTriageLaneFilter = EvidenceTriageLane | "all";

export const EVIDENCE_TRIAGE_PAGE_SIZE = 6;

export interface EvidenceTriageLaneInput {
  tone?: CrossPagePaperTone | string | null;
  trustLevel?: string | null;
  votesDisagree?: number | null;
  status?: string | null;
  flagged?: boolean | null;
  sourceTier?: string | null;
  hasPaper?: boolean | null;
}

export interface EvidenceTriageSourceLike {
  id?: number | null;
  source_tier?: string | null;
  claim_id?: number | null;
  trust_level_snapshot?: string | null;
  evidence_count_snapshot?: number | null;
  representative_arxiv_id?: string | null;
  attribution?: string | null;
  flagged?: boolean | null;
  reason?: string | null;
}

export interface EvidenceTriageCitationLike {
  evidence_id?: number | null;
  author_year_key?: string | null;
  title?: string | null;
  arxiv_id?: string | null;
  url?: string | null;
}

export interface EvidenceTriageStudioInput {
  sources?: EvidenceTriageSourceLike[] | null;
  citations?: EvidenceTriageCitationLike[] | null;
  crossPageFootprints?: Array<CrossPagePaperFootprintResponse | null | undefined> | null;
  pageSlug?: string | null;
  pageTitle?: string | null;
}

export interface EvidenceTriageStudioItem {
  id: string;
  lane: EvidenceTriageLane;
  laneLabel: string;
  actionLabel: string;
  paperLabel: string;
  pageTitle: string;
  claimLabel: string;
  claimText: string;
  href: string;
  tone: CrossPagePaperTone;
  trustLevel: string;
  votesSummary: string;
  reasonText: string;
  priorityScore: number;
}

export interface EvidenceTriageStudioDeck {
  hasTriageSignal: boolean;
  summary: string;
  scopeCaveat: string;
  laneCounts: Record<EvidenceTriageLane, number>;
  items: EvidenceTriageStudioItem[];
}

export interface EvidenceTriageQueueViewOptions {
  laneFilter?: EvidenceTriageLaneFilter;
  page?: number;
  pageSize?: number;
}

export interface EvidenceTriageQueueView {
  laneFilter: EvidenceTriageLaneFilter;
  laneLabel: string;
  totalCount: number;
  filteredCount: number;
  hiddenByFilterCount: number;
  pageSize: number;
  currentPage: number;
  pageCount: number;
  visibleItems: EvidenceTriageStudioItem[];
  hasOverflow: boolean;
  overflowDisclosure: string;
  emptyFilterMessage: string;
}

const LANE_LABELS: Record<EvidenceTriageLane, string> = {
  needs_adjudication: "Needs adjudication",
  needs_source: "Needs source",
  ready_to_review: "Ready to review",
};

const ACTION_LABELS: Record<EvidenceTriageLane, string> = {
  needs_adjudication: "Adjudicate counter-pressure",
  needs_source: "Find stronger source",
  ready_to_review: "Synthesis readiness check",
};

const LANE_RANK: Record<EvidenceTriageLane, number> = {
  needs_adjudication: 0,
  needs_source: 1,
  ready_to_review: 2,
};

function cleanText(value?: string | number | null): string {
  return String(value ?? "").replace(/\s+/g, " ").trim();
}

function numberValue(value: unknown): number {
  const n = Number(value ?? 0);
  return Number.isFinite(n) ? n : 0;
}

function paperLabel(response: CrossPagePaperFootprintResponse): string {
  const explicit = cleanText(response.paper?.author_year_key);
  if (explicit) return explicit;
  const year = cleanText(response.paper?.year);
  const title = cleanText(response.paper?.title);
  const arxivId = cleanText(response.paper?.arxiv_id);
  if (year) {
    const authors = response.paper?.authors;
    const first = Array.isArray(authors) ? cleanText(authors[0]) : cleanText(authors).split(/[;,]/)[0];
    const last = cleanText(first).split(/\s+/).filter(Boolean).pop() || "Paper";
    return `${last}${year}`;
  }
  return title || arxivId || "Paper footprint";
}

function normalizeTone(value?: string | null): CrossPagePaperTone {
  const text = cleanText(value).toLowerCase();
  if (/counter|contradict|oppose|against|refut|weak/.test(text)) return "counter";
  if (/support|agree|for|confirm|entail|strengthen/.test(text)) return "support";
  return "neutral";
}

export function normalizeTriageLane(input: EvidenceTriageLaneInput): EvidenceTriageLane {
  const tone = normalizeTone(input.tone);
  const trust = cleanText(input.trustLevel).toLowerCase();
  const votesDisagree = numberValue(input.votesDisagree);
  const sourceTier = cleanText(input.sourceTier).toLowerCase();

  if (tone === "counter" || /challenged|debated|disputed|contested/.test(trust) || votesDisagree > 0) {
    return "needs_adjudication";
  }
  if (input.flagged || sourceTier === "ai_estimate" || input.hasPaper === false || tone === "neutral" || /unverified|unknown/.test(trust)) {
    return "needs_source";
  }
  if (tone === "support" && /accepted|consensus|verified/.test(trust) && votesDisagree === 0) {
    return "ready_to_review";
  }
  return "needs_source";
}

function reasonText(parts: Array<string | null | undefined>): string {
  const cleaned = parts.map(cleanText).filter(Boolean);
  return cleaned.length ? cleaned.join(" · ") : "Needs human review before readiness decisions.";
}

function itemPriority(lane: EvidenceTriageLane, tone: CrossPagePaperTone, trustLevel: string, votesDisagree: number): number {
  return (
    (lane === "needs_adjudication" ? 100 : lane === "needs_source" ? 50 : 10) +
    (tone === "counter" ? 30 : 0) +
    (/challenged/i.test(trustLevel) ? 20 : /debated/i.test(trustLevel) ? 12 : 0) +
    votesDisagree * 4
  );
}

function votesSummary(agree: number, disagree: number): string {
  if (agree === 0 && disagree === 0) return "No votes yet";
  return `${agree.toLocaleString()} agree · ${disagree.toLocaleString()} disagree`;
}

export function buildEvidenceTriageStudioDeck(input: EvidenceTriageStudioInput): EvidenceTriageStudioDeck {
  const laneCounts: Record<EvidenceTriageLane, number> = {
    needs_adjudication: 0,
    needs_source: 0,
    ready_to_review: 0,
  };
  const citationByArxiv = new Map<string, EvidenceTriageCitationLike>();
  for (const citation of input.citations || []) {
    const arxivId = cleanText(citation?.arxiv_id).replace(/^arXiv:/i, "");
    if (arxivId && !citationByArxiv.has(arxivId)) citationByArxiv.set(arxivId, citation);
  }

  const items: EvidenceTriageStudioItem[] = [];
  for (const footprint of input.crossPageFootprints || []) {
    if (!footprint || footprint.schema_version !== "cross_page_paper_footprint.v1") continue;
    const label = paperLabel(footprint);
    const arxivId = cleanText(footprint.paper?.arxiv_id).replace(/^arXiv:/i, "");
    const citation = arxivId ? citationByArxiv.get(arxivId) : undefined;
    for (const page of footprint.pages || []) {
      for (const claim of page.claims || []) {
        const tone = normalizeTone(claim.tone || claim.stance);
        const trustLevel = cleanText(claim.trust_level) || "unverified";
        const votesAgree = numberValue(claim.votes_agree);
        const votesDisagree = numberValue(claim.votes_disagree);
        const lane = normalizeTriageLane({ tone, trustLevel, votesDisagree, hasPaper: Boolean(citation || arxivId) });
        const reason = reasonText([
          tone === "counter" ? "counter-pressure" : null,
          /challenged|debated|disputed/i.test(trustLevel) ? `trust: ${trustLevel}` : null,
          votesDisagree > 0 ? `${votesDisagree.toLocaleString()} disagree votes` : null,
          citation || arxivId ? null : "paper metadata missing",
        ]);
        const claimId = numberValue(claim.claim_id);
        items.push({
          id: `paper:${arxivId || label}:claim:${claimId}:evidence:${numberValue(claim.evidence_id)}`,
          lane,
          laneLabel: LANE_LABELS[lane],
          actionLabel: ACTION_LABELS[lane],
          paperLabel: label,
          pageTitle: cleanText(page.title) || cleanText(page.slug) || "Wiki page",
          claimLabel: claimId ? `claim #${claimId}` : "claim",
          claimText: cleanText(claim.claim_text) || "Untitled claim",
          href: cleanText(claim.href) || `/wiki/${cleanText(page.slug)}#claim-${claimId}`,
          tone,
          trustLevel,
          votesSummary: votesSummary(votesAgree, votesDisagree),
          reasonText: reason,
          priorityScore: itemPriority(lane, tone, trustLevel, votesDisagree),
        });
        laneCounts[lane] += 1;
      }
    }
  }

  for (const source of input.sources || []) {
    const sourceTier = cleanText(source.source_tier);
    if (!source.flagged && sourceTier !== "ai_estimate") continue;
    const trustLevel = cleanText(source.trust_level_snapshot) || "unverified";
    const lane = normalizeTriageLane({ sourceTier, flagged: source.flagged, trustLevel, hasPaper: Boolean(source.representative_arxiv_id) });
    const claimId = numberValue(source.claim_id);
    const reason = reasonText([
      source.reason,
      sourceTier === "ai_estimate" ? "AI estimate needs paper-backed source" : null,
      source.flagged ? "flagged source record" : null,
    ]);
    items.push({
      id: `source:${numberValue(source.id) || items.length}`,
      lane,
      laneLabel: LANE_LABELS[lane],
      actionLabel: ACTION_LABELS[lane],
      paperLabel: cleanText(source.representative_arxiv_id) || "Source gap",
      pageTitle: cleanText(input.pageTitle) || cleanText(input.pageSlug) || "Current page",
      claimLabel: claimId ? `claim #${claimId}` : "source gap",
      claimText: cleanText(source.attribution) || reason,
      href: claimId && input.pageSlug ? `/wiki/${input.pageSlug}#claim-${claimId}` : `/wiki/${cleanText(input.pageSlug)}`,
      tone: "neutral",
      trustLevel,
      votesSummary: cleanText(source.evidence_count_snapshot) ? `${source.evidence_count_snapshot} evidence records` : "No paper-backed count",
      reasonText: reason,
      priorityScore: itemPriority(lane, "neutral", trustLevel, 0) + 8,
    });
    laneCounts[lane] += 1;
  }

  items.sort((a, b) => LANE_RANK[a.lane] - LANE_RANK[b.lane] || b.priorityScore - a.priorityScore || a.pageTitle.localeCompare(b.pageTitle) || a.claimLabel.localeCompare(b.claimLabel));

  const summary = items.length
    ? `${laneCounts.needs_adjudication.toLocaleString()} adjudication · ${laneCounts.needs_source.toLocaleString()} source gaps · ${laneCounts.ready_to_review.toLocaleString()} synthesis-ready`
    : "No evidence triage signals are available yet.";

  return {
    hasTriageSignal: items.length > 0,
    summary,
    scopeCaveat: "Evidence triage is a review queue, not a final verdict. No labels are written from this surface.",
    laneCounts,
    items,
  };
}

export function buildEvidenceTriageQueueView(deck: EvidenceTriageStudioDeck, options: EvidenceTriageQueueViewOptions = {}): EvidenceTriageQueueView {
  const laneFilter: EvidenceTriageLaneFilter = options.laneFilter || "all";
  const laneLabel = laneFilter === "all" ? "All lanes" : LANE_LABELS[laneFilter];
  const pageSize = Math.max(1, Math.floor(numberValue(options.pageSize || EVIDENCE_TRIAGE_PAGE_SIZE)));
  const totalCount = deck.items.length;
  const filteredItems = laneFilter === "all" ? deck.items : deck.items.filter((item) => item.lane === laneFilter);
  const filteredCount = filteredItems.length;
  const hiddenByFilterCount = totalCount - filteredCount;
  const pageCount = Math.max(1, Math.ceil(filteredCount / pageSize));
  const requestedPage = Math.max(0, Math.floor(numberValue(options.page)));
  const currentPage = Math.min(requestedPage, pageCount - 1);
  const startIndex = filteredCount ? currentPage * pageSize : 0;
  const endIndex = Math.min(filteredCount, startIndex + pageSize);
  const visibleItems = filteredItems.slice(startIndex, endIndex);
  const showingText = filteredCount
    ? `Showing ${startIndex + 1}-${endIndex} of ${filteredCount} triage items${laneFilter === "all" ? "" : ` in ${laneLabel}`}.`
    : `No triage rows match ${laneLabel}.`;
  const laterPages = filteredCount > endIndex ? ` ${filteredCount - endIndex} more on later pages.` : "";
  const filterText = hiddenByFilterCount > 0 ? ` ${hiddenByFilterCount} hidden by the active lane filter.` : "";
  const overflowDisclosure = `${showingText}${laterPages}${filterText} Queue is paginated for review safety; no labels are written.`;

  return {
    laneFilter,
    laneLabel,
    totalCount,
    filteredCount,
    hiddenByFilterCount,
    pageSize,
    currentPage,
    pageCount,
    visibleItems,
    hasOverflow: filteredCount > pageSize || hiddenByFilterCount > 0,
    overflowDisclosure,
    emptyFilterMessage: totalCount
      ? `No triage rows match ${laneLabel}. Clear the lane filter to review all queued signals.`
      : "No evidence triage signals are available yet.",
  };
}
