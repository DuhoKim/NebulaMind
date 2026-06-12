"use client";

import { usePathname } from "next/navigation";

const VIEWS = [
  { label: "List", href: "/wiki" },
  { label: "Cards", href: "/explore/cards" },
  { label: "Graph", href: "/explore/graph" },
  { label: "Q&A", href: "/explore/qa" },
];

export function WikiViewToggle() {
  const pathname = usePathname();

  return (
    <div
      style={{
        display: "inline-flex",
        gap: 0,
        border: "1px solid #334155",
        borderRadius: "6px",
        overflow: "hidden",
        fontSize: "0.8rem",
      }}
    >
      {VIEWS.map((v) => {
        const isActive = v.href === "/wiki" ? pathname === "/wiki" : pathname.startsWith(v.href);
        return (
          <a
            key={v.href}
            href={v.href}
            style={{
              padding: "5px 14px",
              textDecoration: "none",
              fontWeight: 500,
              background: isActive ? "#1e293b" : "transparent",
              color: isActive ? "#f8fafc" : "#64748b",
              borderRight: "1px solid #334155",
              transition: "all 0.15s",
            }}
          >
            {v.label}
          </a>
        );
      })}
    </div>
  );
}
