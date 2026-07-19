export type CrossPagePaperTone = "support" | "counter" | "neutral";

export interface CrossPagePaperClaim {
  claim_id: number;
  claim_text: string;
  section?: string | null;
  trust_level?: string | null;
  evidence_id?: number | null;
  stance?: string | null;
  status?: string | null;
  tone?: CrossPagePaperTone | string | null;
  href?: string | null;
  votes_agree?: number | null;
  votes_disagree?: number | null;
}

export interface CrossPagePaperPage {
  page_id?: number | null;
  slug: string;
  title: string;
  claim_count?: number | null;
  evidence_count?: number | null;
  support_count?: number | null;
  counter_count?: number | null;
  neutral_count?: number | null;
  claims?: CrossPagePaperClaim[] | null;
}

export interface CrossPagePaperFootprintResponse {
  schema_version: "cross_page_paper_footprint.v1" | string;
  paper: {
    evidence_id?: number | null;
    arxiv_id?: string | null;
    doi?: string | null;
    url?: string | null;
    title?: string | null;
    authors?: string[] | string | null;
    year?: number | string | null;
    summary?: string | null;
    author_year_key?: string | null;
  };
  page_count?: number | null;
  claim_count?: number | null;
  evidence_count?: number | null;
  tone_counts?: Record<string, number> | null;
  trust_counts?: Record<string, number> | null;
  scope?: {
    label?: string | null;
    caveat?: string | null;
  } | null;
  pages?: CrossPagePaperPage[] | null;
}

export interface CrossPagePaperFootprintItem {
  paperLabel: string;
  title: string;
  arxivId: string | null;
  externalHref: string | null;
  pageCount: number;
  claimCount: number;
  evidenceCount: number;
  counterCount: number;
  supportCount: number;
  neutralCount: number;
  impactLabel: string;
  pages: Array<CrossPagePaperPage & { claims: CrossPagePaperClaim[] }>;
  scopeCaveat: string;
}

export interface CrossPagePaperFootprintDeck {
  hasCrossPageFootprint: boolean;
  paperCount: number;
  pageCount: number;
  claimCount: number;
  counterCount: number;
  supportCount: number;
  neutralCount: number;
  summary: string;
  scopeCaveat: string;
  items: CrossPagePaperFootprintItem[];
}

function cleanText(value?: string | number | null): string {
  return String(value ?? "").replace(/\s+/g, " ").trim();
}

function numberValue(value: unknown): number {
  const n = Number(value ?? 0);
  return Number.isFinite(n) ? n : 0;
}

function pluralCount(count: number, singular: string, plural = `${singular}s`): string {
  return `${count.toLocaleString()} ${count === 1 ? singular : plural}`;
}

function firstAuthor(authors?: string[] | string | null): string {
  if (!authors) return "Paper";
  const list = Array.isArray(authors) ? authors : String(authors).split(/[;,]/);
  const first = cleanText(list[0]);
  if (!first) return "Paper";
  const parts = first.split(/\s+/);
  return parts[parts.length - 1] || first;
}

export function normalizePaperFootprintTone(stance?: string | null): CrossPagePaperTone {
  const value = cleanText(stance).toLowerCase();
  if (/counter|contradict|oppose|against|refut|weak/.test(value)) return "counter";
  if (/support|agree|for|confirm|entail|strengthen/.test(value)) return "support";
  return "neutral";
}

function paperLabel(response: CrossPagePaperFootprintResponse): string {
  const explicit = cleanText(response.paper?.author_year_key);
  if (explicit) return explicit;
  const year = cleanText(response.paper?.year);
  const arxivId = cleanText(response.paper?.arxiv_id);
  return year ? `${firstAuthor(response.paper?.authors)}${year}` : cleanText(response.paper?.title) || arxivId || "Paper footprint";
}

function impactLabel(pageCount: number, claimCount: number, counterCount: number): string {
  return `${pluralCount(pageCount, "page")} · ${pluralCount(claimCount, "claim")} · ${counterCount.toLocaleString()} countering`;
}

export function buildCrossPagePaperFootprintDeck(
  responses: Array<CrossPagePaperFootprintResponse | null | undefined>,
): CrossPagePaperFootprintDeck {
  const items = responses
    .filter((response): response is CrossPagePaperFootprintResponse => Boolean(response && response.schema_version === "cross_page_paper_footprint.v1"))
    .map((response) => {
      const pages = (response.pages || [])
        .map((page) => ({ ...page, claims: Array.isArray(page.claims) ? page.claims : [] }))
        .sort((a, b) => numberValue(b.counter_count) - numberValue(a.counter_count) || numberValue(b.claim_count) - numberValue(a.claim_count) || cleanText(a.title).localeCompare(cleanText(b.title)));
      const toneCounts = response.tone_counts || {};
      const pageCount = numberValue(response.page_count || pages.length);
      const claimCount = numberValue(response.claim_count || pages.reduce((sum, page) => sum + numberValue(page.claim_count), 0));
      const evidenceCount = numberValue(response.evidence_count);
      const counterCount = numberValue(toneCounts.counter || pages.reduce((sum, page) => sum + numberValue(page.counter_count), 0));
      const supportCount = numberValue(toneCounts.support || pages.reduce((sum, page) => sum + numberValue(page.support_count), 0));
      const neutralCount = numberValue(toneCounts.neutral || pages.reduce((sum, page) => sum + numberValue(page.neutral_count), 0));
      const scopeCaveat = cleanText(response.scope?.caveat) || "Across indexed wiki evidence rows; this is not a final verdict about which claim is correct.";
      return {
        paperLabel: paperLabel(response),
        title: cleanText(response.paper?.title) || "Untitled paper",
        arxivId: cleanText(response.paper?.arxiv_id) || null,
        externalHref: cleanText(response.paper?.url) || (cleanText(response.paper?.arxiv_id) ? `https://arxiv.org/abs/${cleanText(response.paper?.arxiv_id)}` : null),
        pageCount,
        claimCount,
        evidenceCount,
        counterCount,
        supportCount,
        neutralCount,
        impactLabel: impactLabel(pageCount, claimCount, counterCount),
        pages,
        scopeCaveat,
      } satisfies CrossPagePaperFootprintItem;
    })
    .sort((a, b) => b.counterCount - a.counterCount || b.pageCount - a.pageCount || b.claimCount - a.claimCount || a.paperLabel.localeCompare(b.paperLabel));

  const pageCount = items.reduce((sum, item) => sum + item.pageCount, 0);
  const claimCount = items.reduce((sum, item) => sum + item.claimCount, 0);
  const counterCount = items.reduce((sum, item) => sum + item.counterCount, 0);
  const supportCount = items.reduce((sum, item) => sum + item.supportCount, 0);
  const neutralCount = items.reduce((sum, item) => sum + item.neutralCount, 0);
  const scopeCaveat = items[0]?.scopeCaveat || "Across indexed wiki evidence rows; this is not a final verdict about which claim is correct.";

  return {
    hasCrossPageFootprint: items.length > 0,
    paperCount: items.length,
    pageCount,
    claimCount,
    counterCount,
    supportCount,
    neutralCount,
    scopeCaveat,
    summary: items.length > 0
      ? `${pluralCount(items.length, "paper")} mapped across ${pluralCount(pageCount, "page")} and ${pluralCount(claimCount, "claim")}; this is not a final verdict.`
      : "No cross-page paper footprint is available for this page yet.",
    items,
  };
}
