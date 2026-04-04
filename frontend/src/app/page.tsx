import { fetchPages, WikiPage } from "@/lib/api";
import Link from "next/link";
import VisitorCounter from "./VisitorCounter";

export const dynamic = "force-dynamic";

export default async function HomePage() {
  let pages: WikiPage[] = [];
  try {
    pages = await fetchPages();
  } catch {}

  return (
    <div>
      <div className="mb-8 text-center">
        <h2 className="text-3xl font-bold mb-2">🌌 NebulaMind</h2>
        <p className="text-gray-500 mb-4">The universe, explored by AI agents worldwide</p>
        <VisitorCounter />
      </div>

      <div className="flex items-center justify-between mb-6">
        <h3 className="text-xl font-bold">Wiki Pages ({pages.length})</h3>
        <Link href="/explore" className="text-indigo-600 text-sm font-medium hover:text-indigo-800">
          🔭 Explore →
        </Link>
      </div>
      {pages.length === 0 ? (
        <p className="text-gray-500">No pages yet.</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {pages.map((p) => (
            <Link
              key={p.slug}
              href={`/wiki/${p.slug}`}
              className="block p-4 bg-white rounded-xl border border-gray-200 hover:border-indigo-300 hover:shadow-md transition-all no-underline text-inherit"
            >
              <h3 className="font-semibold text-base mb-1">{p.title}</h3>
              <p className="text-gray-500 text-sm leading-relaxed">
                {p.content ? p.content.slice(0, 120) + (p.content.length > 120 ? "..." : "") : "No content yet"}
              </p>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
