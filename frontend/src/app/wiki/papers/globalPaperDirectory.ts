export type GlobalPaperTriageStatus = "needs_adjudication" | "needs_source" | "ready_to_review";

export interface GlobalPaperDirectoryPaper {
  evidence_id?: number | null;
  arxiv_id?: string | null;
  doi?: string | null;
  url?: string | null;
  title?: string | null;
  authors?: string[] | string | null;
  year?: number | string | null;
  summary?: string | null;
  author_year_key?: string | null;
}

export interface GlobalPaperDirectoryPage {
  page_id?: number | null;
  slug: string;
  title: string;
  href?: string | null;
  claim_count?: number | null;
  evidence_count?: number | null;
  support_count?: number | null;
  counter_count?: number | null;
  neutral_count?: number | null;
}

export interface GlobalPaperDirectoryPayloadItem {
  paper: GlobalPaperDirectoryPaper;
  page_count?: number | null;
  claim_count?: number | null;
  evidence_count?: number | null;
  tone_counts?: Record<string, number> | null;
  trust_counts?: Record<string, number> | null;
  triage_status?: GlobalPaperTriageStatus | string | null;
  impact_label?: string | null;
  pages?: GlobalPaperDirectoryPage[] | null;
}

export interface GlobalPaperDirectoryPayload {
  schema_version: "global_paper_directory.v1" | string;
  query?: string | null;
  limit?: number | null;
  total_papers?: number | null;
  result_count?: number | null;
  scope?: { label?: string | null; caveat?: string | null } | null;
  items?: GlobalPaperDirectoryPayloadItem[] | null;
}

export interface GlobalPaperDirectoryItem {
  id: string;
  paperLabel: string;
  title: string;
  summary: string;
  arxivId: string | null;
  externalHref: string | null;
  footprintHref: string;
  status: GlobalPaperTriageStatus;
  statusLabel: string;
  pageCount: number;
  claimCount: number;
  evidenceCount: number;
  counterCount: number;
  supportCount: number;
  neutralCount: number;
  impactLabel: string;
  accessibleSummary: string;
  pages: Array<GlobalPaperDirectoryPage & { href: string; claim_count: number; counter_count: number }>;
}

export interface GlobalPaperDirectoryDeck {
  hasResults: boolean;
  query: string;
  paperCount: number;
  totalPapers: number;
  resultCount: number;
  counterCount: number;
  summary: string;
  scopeCaveat: string;
  emptyMessage: string;
  truncationDisclosure: string | null;
  items: GlobalPaperDirectoryItem[];
}

function cleanText(value?: string | number | null): string {
  return String(value ?? "").replace(/\s+/g, " ").trim();
}

function numberValue(value: unknown): number {
  const n = Number(value ?? 0);
  return Number.isFinite(n) ? n : 0;
}

function plural(count: number, singular: string, pluralForm = `${singular}s`): string {
  return `${count.toLocaleString()} ${count === 1 ? singular : pluralForm}`;
}

function firstAuthor(authors?: string[] | string | null): string {
  if (!authors) return "Paper";
  const list = Array.isArray(authors) ? authors : String(authors).split(/[;,]/);
  const first = cleanText(list[0]);
  if (!first) return "Paper";
  const parts = first.split(/\s+/).filter(Boolean);
  return parts[parts.length - 1] || first;
}

function paperLabel(paper: GlobalPaperDirectoryPaper): string {
  const explicit = cleanText(paper.author_year_key);
  if (explicit) return explicit;
  const title = cleanText(paper.title);
  const arxivId = cleanText(paper.arxiv_id);
  const year = cleanText(paper.year);
  if (year) return `${firstAuthor(paper.authors)}${year}`;
  return title || arxivId || "Indexed paper";
}

function statusLabel(status: GlobalPaperTriageStatus): string {
  if (status === "needs_adjudication") return "Needs adjudication";
  if (status === "needs_source") return "Needs source";
  return "Ready to review";
}

export function normalizeGlobalPaperTriageStatus(input: { counterCount?: number; trustCounts?: Record<string, number> | null; hasStableIdentifier?: boolean | null; status?: string | null }): GlobalPaperTriageStatus {
  const explicit = cleanText(input.status).toLowerCase();
  if (explicit === "needs_adjudication" || explicit === "needs_source" || explicit === "ready_to_review") return explicit;
  const trustCounts = input.trustCounts || {};
  if (numberValue(input.counterCount) > 0) return "needs_adjudication";
  if (["challenged", "debated", "disputed", "contested"].some((level) => numberValue(trustCounts[level]) > 0)) return "needs_adjudication";
  if (input.hasStableIdentifier === false || numberValue(trustCounts.unverified) > 0) return "needs_source";
  return "ready_to_review";
}

function matchesQuery(item: GlobalPaperDirectoryPayloadItem, query: string): boolean {
  if (!query) return true;
  const haystack = [
    item.paper?.author_year_key,
    item.paper?.title,
    item.paper?.arxiv_id,
    item.paper?.doi,
    item.paper?.summary,
    Array.isArray(item.paper?.authors) ? item.paper?.authors?.join(" ") : item.paper?.authors,
    ...(item.pages || []).flatMap((page) => [page.title, page.slug]),
  ].map(cleanText).join(" ").toLowerCase();
  return haystack.includes(query.toLowerCase());
}

export function buildGlobalPaperDirectoryDeck(payload: GlobalPaperDirectoryPayload | null | undefined, queryOverride = ""): GlobalPaperDirectoryDeck {
  const query = cleanText(queryOverride || payload?.query || "");
  const scopeCaveat = cleanText(payload?.scope?.caveat) || "Across indexed wiki evidence rows; directory/search, not a final verdict. No labels are written.";
  const rawItems = payload?.schema_version === "global_paper_directory.v1" && Array.isArray(payload.items) ? payload.items : [];
  const items = rawItems
    .filter((item) => item && item.paper && matchesQuery(item, query))
    .map((item) => {
      const toneCounts = item.tone_counts || {};
      const trustCounts = item.trust_counts || {};
      const pageCount = numberValue(item.page_count || item.pages?.length);
      const claimCount = numberValue(item.claim_count);
      const evidenceCount = numberValue(item.evidence_count);
      const counterCount = numberValue(toneCounts.counter);
      const supportCount = numberValue(toneCounts.support);
      const neutralCount = numberValue(toneCounts.neutral);
      const paper = item.paper || {};
      const label = paperLabel(paper);
      const arxivId = cleanText(paper.arxiv_id) || null;
      const externalHref = cleanText(paper.url) || (arxivId ? `https://arxiv.org/abs/${arxivId}` : null);
      const pages = (item.pages || []).map((page) => ({
        ...page,
        href: cleanText(page.href) || `/wiki/${cleanText(page.slug)}`,
        claim_count: numberValue(page.claim_count),
        counter_count: numberValue(page.counter_count),
      })).sort((a, b) => b.counter_count - a.counter_count || b.claim_count - a.claim_count || cleanText(a.title).localeCompare(cleanText(b.title)));
      const status = normalizeGlobalPaperTriageStatus({
        status: item.triage_status,
        counterCount,
        trustCounts,
        hasStableIdentifier: Boolean(arxivId || cleanText(paper.doi) || externalHref),
      });
      const footprintHref = pages[0]?.slug ? `/wiki/${pages[0].slug}/sources` : "/wiki";
      const impactLabel = cleanText(item.impact_label) || `${plural(pageCount, "page")} · ${plural(claimCount, "claim")} · ${counterCount.toLocaleString()} countering`;
      const title = cleanText(paper.title) || label;
      const accessibleSummary = `${label}: ${statusLabel(status)}; ${pageCount} pages, ${claimCount} claims, ${counterCount} countering. Open footprint context.`;
      return {
        id: arxivId || cleanText(paper.doi) || String(paper.evidence_id || label),
        paperLabel: label,
        title,
        summary: cleanText(paper.summary),
        arxivId,
        externalHref,
        footprintHref,
        status,
        statusLabel: statusLabel(status),
        pageCount,
        claimCount,
        evidenceCount,
        counterCount,
        supportCount,
        neutralCount,
        impactLabel,
        accessibleSummary,
        pages,
      } satisfies GlobalPaperDirectoryItem;
    })
    .sort((a, b) => {
      const rank = { needs_adjudication: 0, needs_source: 1, ready_to_review: 2 } as Record<GlobalPaperTriageStatus, number>;
      return rank[a.status] - rank[b.status] || b.counterCount - a.counterCount || b.pageCount - a.pageCount || b.claimCount - a.claimCount || a.paperLabel.localeCompare(b.paperLabel);
    });

  const counterCount = items.reduce((sum, item) => sum + item.counterCount, 0);
  const totalPapers = query ? items.length : numberValue(payload?.total_papers || items.length);
  const resultCount = items.length;
  const payloadTotal = numberValue(payload?.total_papers);
  const hasServerTruncation = payloadTotal > resultCount && !query;
  const hasSearchTruncation = payloadTotal > resultCount && Boolean(query) && cleanText(payload?.query) === query;
  const truncationDisclosure = hasServerTruncation || hasSearchTruncation
    ? `Showing ${resultCount.toLocaleString()} of ${payloadTotal.toLocaleString()} indexed papers. Refine search to narrow the directory.`
    : null;
  const summary = resultCount > 0
    ? `${plural(resultCount, "paper")} ${query ? `matching “${query}”` : "indexed"} · ${plural(items.reduce((sum, item) => sum + item.pageCount, 0), "page touch", "page touches")} · ${counterCount.toLocaleString()} countering`
    : query ? `No indexed papers match “${query}”.` : "No indexed papers are available yet.";

  return {
    hasResults: resultCount > 0,
    query,
    paperCount: items.length,
    totalPapers,
    resultCount,
    counterCount,
    summary,
    scopeCaveat,
    emptyMessage: summary,
    truncationDisclosure,
    items,
  };
}
