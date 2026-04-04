"use client";

import { usePathname } from "next/navigation";
import Link from "next/link";

const TABS = [
  { label: "Cards", href: "/explore/cards" },
  { label: "Q&A", href: "/explore/qa" },
  { label: "Chat", href: "/explore/chat" },
  { label: "Graph", href: "/explore/graph" },
];

export default function ExploreLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();

  return (
    <div>
      <nav
        style={{
          display: "flex",
          gap: "0.25rem",
          borderBottom: "2px solid #e5e7eb",
          marginBottom: "1.5rem",
          paddingBottom: 0,
        }}
      >
        {TABS.map((tab) => {
          const active = pathname.startsWith(tab.href);
          return (
            <Link
              key={tab.href}
              href={tab.href}
              style={{
                padding: "0.5rem 1rem",
                textDecoration: "none",
                fontWeight: active ? 600 : 400,
                color: active ? "#4f46e5" : "#6b7280",
                borderBottom: active ? "2px solid #4f46e5" : "2px solid transparent",
                marginBottom: "-2px",
                fontSize: "0.9rem",
              }}
            >
              {tab.label}
            </Link>
          );
        })}
      </nav>
      {children}
    </div>
  );
}
